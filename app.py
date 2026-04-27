from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from werkzeug.utils import secure_filename
from datetime import timedelta
from excel_loader import load_excel_to_db
from workshop_loader import load_workshops_to_db
# 1. إعداد التطبيق
app = Flask(__name__)

# 2. إعداد مجلد الرفع
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'kfmc_2026_smart_portal'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# --- إعدادات قاعدة البيانات (SQLite) ---
base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'kfmc.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class CourseRegistration(db.Model):
    __tablename__ = 'course_registrations'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    national_id = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=True) # للبرامج القصيرة
    workshop_id = db.Column(db.Integer, db.ForeignKey('applied_workshops.id'), nullable=True) # للحلقات
    registration_date = db.Column(db.DateTime, default=datetime.utcnow)

class Applicant(db.Model):
    __tablename__ = 'applicants'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    national_id = db.Column(db.String(10), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    university = db.Column(db.String(255), nullable=False)
    major = db.Column(db.String(100), nullable=False)
    graduation_year = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(255), nullable=False)

    university_letter = db.Column(db.String(255))
    status = db.Column(db.String(50), default='استقبال الطلب')

    interview_date = db.Column(db.String(100))
    assigned_facility = db.Column(db.String(255))
    interview_location = db.Column(db.String(255))

    attendance_logs = db.relationship('Attendance', backref='trainee', lazy=True)
    evaluation_score = db.relationship('Evaluation', backref='trainee', uselist=False)

class Attendance(db.Model):
    __tablename__ = 'attendance'
    id = db.Column(db.Integer, primary_key=True)
    applicant_id = db.Column(db.Integer, db.ForeignKey('applicants.id'), nullable=False)
    date = db.Column(db.String(20), default=datetime.now().strftime('%Y-%m-%d'))
    check_in = db.Column(db.String(20)) 
    check_out = db.Column(db.String(20)) 
    status = db.Column(db.String(50)) 
    notes = db.Column(db.Text)

class Evaluation(db.Model):
    __tablename__ = 'evaluations'
    id = db.Column(db.Integer, primary_key=True)
    applicant_id = db.Column(db.Integer, db.ForeignKey('applicants.id'), nullable=False)
    score = db.Column(db.Integer) 
    performance_notes = db.Column(db.Text) 
    evaluator_name = db.Column(db.String(100)) 

class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    branch = db.Column(db.String(100))
    category = db.Column(db.String(100))
    course_code = db.Column(db.String(50))
    title = db.Column(db.String(255))
    start_date_h = db.Column(db.String(50))
    start_date_m = db.Column(db.Date)
    duration = db.Column(db.String(50))
    target_group = db.Column(db.String(100))
    location = db.Column(db.String(100))

class AppliedWorkshop(db.Model):
    __tablename__ = 'applied_workshops'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    duration = db.Column(db.String(50))
    riyadh_dates = db.Column(db.Text)
    jeddah_dates = db.Column(db.Text)
    dammam_dates = db.Column(db.Text)
    abha_dates = db.Column(db.Text)

class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    sender_name = db.Column(db.String(255), nullable=False)
    sender_email = db.Column(db.String(255), nullable=False)
    subject = db.Column(db.String(255))
    content = db.Column(db.Text, nullable=False)
    sent_date = db.Column(db.DateTime, default=datetime.utcnow)

class AdminUser(db.Model):
    __tablename__ = 'admin_users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), default='viewer')

class ClearanceRequest(db.Model):
    __tablename__ = 'clearance_requests'
    id = db.Column(db.Integer, primary_key=True)
    applicant_id = db.Column(db.Integer, db.ForeignKey('applicants.id'), nullable=True)
    admin_name = db.Column(db.String(100))
    employee_no = db.Column(db.String(50))
    nationality = db.Column(db.String(50))
    name_ar = db.Column(db.String(255))
    name_en = db.Column(db.String(255))
    national_id = db.Column(db.String(10))
    mobile = db.Column(db.String(15))
    attachment = db.Column(db.String(255)) 
    request_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(50), default='Pending')

# --- المسارات (Routes) ---
@app.before_request
def setup_once():
    if not hasattr(app, 'db_initialized'):
        db.create_all()
        load_excel_to_db('programs.xlsx')
        load_workshops_to_db('workshops.xlsx')
        app.db_initialized = True
@app.route('/')
def index(): return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email_input = request.form.get('username')
        password_input = request.form.get('password')
        if email_input == "admin" and password_input == "kfmc2026":
            session.update({'logged_in': True, 'user_name': "المشرف العام", 'role': 'admin'})
            return jsonify({"status": "success"})
        admin = AdminUser.query.filter_by(email=email_input, password=password_input).first()
        if admin:
            session.update({'logged_in': True, 'user_name': admin.name, 'role': admin.role})
            return jsonify({"status": "success"})
        return jsonify({"status": "error", "message": "خطأ في البيانات"}), 401
    return render_template('Login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():         
    if not session.get('logged_in'): 
        return redirect(url_for('login'))

    all_applicants = Applicant.query.all()
    all_messages = Message.query.order_by(Message.sent_date.desc()).all()
    pending_count = Applicant.query.filter(
        Applicant.status.in_(['استقبال الطلب', 'قيد المراجعة' ,'مقابلة شخصية'])
    ).count()

    # 👇 هذا الجديد (يجلب تسجيلات البرامج القصيرة)
    course_registrations = CourseRegistration.query.order_by(
        CourseRegistration.registration_date.desc()
    ).all()

    return render_template(
        'Dashboard.html',
        applicants=all_applicants,
        messages=all_messages,
        pending_count=pending_count,
        course_registrations=course_registrations
    )

@app.route('/steps')
def registration_steps():
    return render_template('RegistrationSteps.html')

@app.route('/apply', methods=['GET', 'POST'])
def apply():
    if request.method == 'POST':
        try:
            file = request.files.get('university_letter')
            filename = None
            if file and file.filename != '':
                filename = secure_filename(f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{file.filename}")
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            new_app = Applicant(
                full_name=request.form.get('full_name'),
                national_id=request.form.get('national_id'),
                phone=request.form.get('phone'),
                university=request.form.get('university'),
                major=request.form.get('major'),
                graduation_year=request.form.get('graduation_year'),
                email=request.form.get('email'),
                university_letter=filename,
                status='استقبال الطلب'
            )
            db.session.add(new_app)
            db.session.commit()
            return jsonify({"status": "success", "message": "تم استلام طلبك بنجاح"})
        except Exception as e:
            db.session.rollback()
            return jsonify({"status": "error", "message": "رقم الهوية مسجل مسبقاً"}), 400
    return render_template('Apply.html')

@app.route('/get_registration_details/<int:id>')
def get_registration_details(id):
    if not session.get('logged_in'):
        return jsonify({"status": "error"}), 403

    reg = db.session.get(CourseRegistration, id)
    if not reg:
        return jsonify({"status": "error"}), 404

    return jsonify({
        "full_name": reg.full_name,
        "national_id": reg.national_id,
        "email": reg.email,
        "date": reg.registration_date.strftime('%Y-%m-%d %H:%M')
    })

@app.route('/delete_registration', methods=['POST'])
def delete_registration():
    if not session.get('logged_in') or session.get('role') == 'viewer':
        return jsonify({"status": "error"}), 403

    data = request.get_json()
    reg = db.session.get(CourseRegistration, data['id'])

    if not reg:
        return jsonify({"status": "error"}), 404

    db.session.delete(reg)
    db.session.commit()

    return jsonify({"status": "success"})

@app.route('/get_applicant_details/<int:id>')
def get_applicant_details(id):
    if not session.get('logged_in'): return jsonify({"status": "error"}), 403
    
    app_obj = db.session.get(Applicant, id)
    if not app_obj: return jsonify({"status": "error", "message": "غير موجود"}), 404
    
    # 1. جلب البرامج القصيرة (Short Programs)
    short_progs = db.session.query(Course.title).join(
        CourseRegistration, Course.id == CourseRegistration.course_id
    ).filter(CourseRegistration.national_id == app_obj.national_id).all()
    
    # 2. جلب الحلقات التطبيقية (Applied Workshops)
    workshops = db.session.query(AppliedWorkshop.title).join(
        CourseRegistration, AppliedWorkshop.id == CourseRegistration.workshop_id
    ).filter(CourseRegistration.national_id == app_obj.national_id).all()

    return jsonify({
        "full_name": app_obj.full_name, 
        "national_id": app_obj.national_id,
        "phone": app_obj.phone, 
        "university": app_obj.university,
        "major": app_obj.major, 
        "graduation_year": app_obj.graduation_year,
        "email": app_obj.email,
        "status": app_obj.status,
        "interview_date": app_obj.interview_date,
        "assigned_facility": app_obj.assigned_facility,
        "university_letter": app_obj.university_letter,
        
        # إرسال القوائم منفصلة للمعاينة
        "short_programs": [p[0] for p in short_progs],
        "applied_workshops": [w[0] for w in workshops]
    })

@app.route('/programs')
def programs():
    today = datetime.today().date()
    smart_courses = Course.query.filter(Course.start_date_m >= today).order_by(Course.start_date_m.asc()).limit(20).all()
    return render_template('ShortPrograms.html', courses=smart_courses)

@app.route('/available')
def available():
    workshops = AppliedWorkshop.query.all()
    expanded_courses = []
    for ws in workshops:
        # خريطة المدن المتاحة في قاعدة البيانات
        city_map = [
            {'name': 'الرياض', 'data': ws.riyadh_dates}, 
            {'name': 'جدة', 'data': ws.jeddah_dates},
            {'name': 'الدمام', 'data': ws.dammam_dates},
            {'name': 'أبها', 'data': ws.abha_dates}
        ]
        for city in city_map:
            if city['data'] and str(city['data']).strip() != "":
                expanded_courses.append({
                    'id': ws.id, # إضافة الـ ID لربطه بالـ Modal
                    'title': ws.title, 
                    'duration': ws.duration, 
                    'location': city['name'], 
                    'date_details': city['data']
                })
    return render_template('avalable.html', courses=expanded_courses)

@app.route('/track', methods=['GET', 'POST'])
def track():
    applicant = None
    clearance = None
    if request.method == 'POST':
        national_id = request.form.get('national_id')
        applicant = Applicant.query.filter_by(national_id=national_id).first()
        clearance = ClearanceRequest.query.filter_by(national_id=national_id)\
            .order_by(ClearanceRequest.request_date.desc()).first()
    return render_template('Track.html', applicant=applicant, clearance=clearance)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        try:
            new_msg = Message(sender_name=request.form.get('name'), sender_email=request.form.get('email'), subject=request.form.get('subject'), content=request.form.get('message'))
            db.session.add(new_msg); db.session.commit()
            return jsonify({"status": "success", "message": "Message sent"})
        except:
            db.session.rollback(); return jsonify({"status": "error"}), 500
    return render_template('ContactUs.html')

@app.route('/settings')
def settings():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    try:
        admins = AdminUser.query.all()
    except Exception as e:
        print("ERROR in settings:", e)
        admins = []

    return render_template('settings.html', admins=admins)

@app.route('/update_full_status', methods=['POST'])
def update_full_status():
    if session.get('role') == 'viewer': return jsonify({"status": "error", "message": "صلاحية مرفوضة"}), 403
    data = request.json
    applicant = db.session.get(Applicant, data['id'])
    applicant.status = data['status']
    if data['status'] == 'مقابلة شخصية':
        applicant.interview_date = data.get('date')
        applicant.interview_location = data.get('location')
    elif data['status'] == 'مقبول':
        facility = data.get('facility')
        if not facility:
            return jsonify({"status": "error", "message": "يجب تحديد المنشأة للمتدرب المقبول"}), 400
        applicant.assigned_facility = facility
    db.session.commit()
    return jsonify({"status": "success"})

@app.route('/attendance')
def attendance():
    if not session.get('logged_in'): return redirect(url_for('login'))
    today_dt = datetime.now()
    today_str = today_dt.strftime('%Y-%m-%d')
    week_dates = [(today_dt - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(7)]
    week_dates.reverse() 
    trainees = Applicant.query.filter_by(status='مقبول').all()
    attendance_data = []
    weekly_report = []
    for trainee in trainees:
        record = Attendance.query.filter_by(applicant_id=trainee.id, date=today_str).first()
        attendance_data.append({
            "id": trainee.id, "full_name": trainee.full_name, "assigned_facility": trainee.assigned_facility,
            "check_in": record.check_in if record else None, "check_out": record.check_out if record else None,
            "status": record.status if record else None
        })
        days_status = []
        for d in week_dates:
            rec = Attendance.query.filter_by(applicant_id=trainee.id, date=d).first()
            days_status.append(rec.status if rec else "غائب")
        weekly_report.append({"name": trainee.full_name, "days": days_status})
    return render_template('Attendance.html', trainees=attendance_data, weekly_report=weekly_report, week_dates=week_dates, datetime=datetime)

@app.route('/submit_attendance', methods=['POST'])
def submit_attendance():
    if not session.get('logged_in') or session.get('role') == 'viewer': return jsonify({"status": "error"}), 403
    data = request.get_json()
    trainee_id = data['id']
    status_type = data['type']
    time_now = data['time']
    date_today = data['date']
    note_content = data.get('note', '')
    record = Attendance.query.filter_by(applicant_id=trainee_id, date=date_today).first()
    if not record:
        record = Attendance(applicant_id=trainee_id, date=date_today)
    if status_type in ['حاضر', 'تأخير بعذر', 'تأخير بدون عذر', 'مهمة عمل']:
        record.check_in = time_now
    elif status_type in ['انصراف', 'استئذان']:
        record.check_out = time_now
    record.status = status_type
    record.notes = note_content
    db.session.add(record); db.session.commit()
    return jsonify({'status': 'success'})

@app.route('/submit_evaluation', methods=['POST'])
def submit_evaluation():
    if not session.get('logged_in') or session.get('role') == 'viewer': return jsonify({"status": "error"}), 403
    data = request.json
    existing_eval = Evaluation.query.filter_by(applicant_id=data['applicant_id']).first()
    if existing_eval:
        existing_eval.score = data['score']
        existing_eval.performance_notes = data['notes']
        existing_eval.evaluator_name = session.get('user_name')
    else:
        new_eval = Evaluation(applicant_id=data['applicant_id'], score=data['score'], performance_notes=data['notes'], evaluator_name=session.get('user_name'))
        db.session.add(new_eval)
    db.session.commit()
    return jsonify({"status": "success"})

@app.route('/clearance')
def trainee_clearance():
    return render_template('Clearance.html', datetime=datetime)

@app.route('/admin/clearance')
def admin_clearance():
    if not session.get('logged_in'): return redirect(url_for('login'))
    requests = ClearanceRequest.query.order_by(ClearanceRequest.request_date.desc().nullslast()).all()
    return render_template('Clearance_Admin.html', requests=requests)

@app.route('/get_clearance_details/<int:id>')
def get_clearance_details(id):
    if not session.get('logged_in'):
        return jsonify({"status": "error"}), 403

    clearance = db.session.get(ClearanceRequest, id)

    if not clearance:
        return jsonify({"status": "error", "message": "غير موجود"}), 404

    return jsonify({
        "name_ar": clearance.name_ar,
        "name_en": clearance.name_en,
        "admin_name": clearance.admin_name,
        "employee_no": clearance.employee_no,
        "national_id": clearance.national_id,
        "nationality": clearance.nationality,
        "mobile": clearance.mobile,
        "attachment": clearance.attachment,
        "status": clearance.status,
        "date": clearance.request_date.strftime('%Y-%m-%d')
    })
@app.route('/update_clearance_status', methods=['POST'])
def update_clearance_status():
    if not session.get('logged_in') or session.get('role') == 'viewer':
        return jsonify({"status": "error", "message": "غير مصرح"}), 403

    data = request.get_json()
    request_id = data.get('id')

    clearance = db.session.get(ClearanceRequest, request_id)

    if not clearance:
        return jsonify({"status": "error", "message": "الطلب غير موجود"}), 404

    # 👇 هنا نحدد الحالة مباشرة
    clearance.status = "Approved"

    db.session.commit()

    return jsonify({"status": "success"})

@app.route('/submit_clearance', methods=['POST'])
def submit_clearance():
    try:
        file = request.files.get('attachment')
        filename = None
        if file and file.filename != '':
            filename = secure_filename(f"CLR_{datetime.now().strftime('%Y%m%d%H%M%S')}_{file.filename}")
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        national_id = request.form.get('national_id')
        applicant = Applicant.query.filter_by(national_id=national_id).first()
        new_req = ClearanceRequest(
            applicant_id=applicant.id if applicant else None, admin_name=request.form.get('admin_name'),
            employee_no=request.form.get('employee_no'), nationality=request.form.get('nationality'),
            name_ar=request.form.get('name_ar'), name_en=request.form.get('name_en'),
            national_id=national_id, mobile=request.form.get('mobile'), attachment=filename
        )
        db.session.add(new_req); db.session.commit()
        return jsonify({"status": "success", "message": "تم إرسال طلب إخلاء الطرف بنجاح"})
    except Exception as e:
        db.session.rollback(); return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/add_admin', methods=['POST'])
def add_admin():
    if not session.get('logged_in') or session.get('role') == 'viewer': return jsonify({"status": "error"}), 403
    try:
        new_admin = AdminUser(name=request.form.get('admin_name'), email=request.form.get('admin_email'), password=request.form.get('admin_pass'), role=request.form.get('admin_role'))
        db.session.add(new_admin); db.session.commit()
        return jsonify({"status": "success", "message": "تم الإضافة"})
    except:
        db.session.rollback(); return jsonify({"status": "error", "message": "مسجل مسبقاً"}), 400

@app.route('/evaluation')
def evaluation():
    if not session.get('logged_in'): return redirect(url_for('login'))
    trainees = Applicant.query.filter_by(status='مقبول').all()
    data = []
    for trainee in trainees:
        eval_record = Evaluation.query.filter_by(applicant_id=trainee.id).first()
        data.append({"id": trainee.id, "full_name": trainee.full_name, "assigned_facility": trainee.assigned_facility, "major": trainee.major, "score": eval_record.score if eval_record else None, "notes": eval_record.performance_notes if eval_record else None})
    return render_template('Evaluation.html', trainees=data)

@app.route('/register_course', methods=['POST'])
def register_course():
    data = request.json
    try:
        new_reg = CourseRegistration(
            full_name=data.get('full_name'),
            national_id=data.get('national_id'),
            email=data.get('email'),
            course_id=data.get('course_id'),    
            workshop_id=data.get('workshop_id') 
        )
        db.session.add(new_reg); db.session.commit()
        return jsonify({"status": "success", "message": "تم التسجيل بنجاح"})
    except Exception as e:
        print(f"CRITICAL ERROR: {str(e)}")
        db.session.rollback(); return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
