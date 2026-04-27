// translator.js - المحرك العالمي لبوابة التميز الرقمية
const dictionary = {
    // --- القائمة العلوية والجانبية (Navbar & Sidebar) ---
    "الرئيسية": "Home",
    "خطوات التسجيل": "Steps",
    "البرامج القصيرة": "Short Programs",
    "الحلقات التطبيقية": "Applied Workshops",
    "متابعة الطلب": "Follow up",
    "إخلاء الطرف": "Clearance",
    "تواصل معنا": "Contact Us",
    "دخول الموظفين": "Staff Login",
    "الداشبورد": "Dashboard",
    "الحضور والانصراف": "Attendance",
    "تقييم المتدربين": "Evaluation",
    "الإعدادات": "Settings",
    "تسجيل الخروج": "Logout",
    "لوحة الإدارة": "Admin Panel",

    // --- صفحة تسجيل الدخول (Login) ---
    "تسجيل دخول الإدارة": "Admin Login",
    "مرحباً بك مجدداً، يرجى إدخال بياناتك للوصول": "Welcome back, please enter your credentials to access",
    "اسم المستخدم أو البريد": "Username or Email",
    "كلمة المرور": "Password",
    "دخول النظام": "System Login",
    "جاري التحقق...": "Verifying...",
    "تم الدخول بنجاح!": "Login Successful!",
    "جاري تحويلك إلى لوحة الإدارة...": "Redirecting to Admin Panel...",
    "فشل تسجيل الدخول": "Login Failed",
    "خطأ تقني": "Technical Error",
    "فشل الاتصال بالخادم، يرجى التأكد من تشغيل ملف app.py": "Server connection failed, please ensure app.py is running",
    "العودة للرئيسية": "Back to Home Page",

    // --- الصفحة الرئيسية (Index) ---
    "منصة التدريب التعاوني الموحدة":" Cooperative Training ",
    "بوابتك نحو التميز المهني في مدينة الملك فهد الطبية ومرافق التجمع الصحي الثاني": "Your gateway to professional excellence at KFMC and Second Health Cluster facilities",
    "قدم طلب انضمام": "Apply Now",
    "فرص تدريبية متنوعة": "Diverse Training Opportunities",
    "تشمل التخصصات الطبية، التقنية، والإدارية.": "Includes medical, technical, and administrative specialties.",
    "متابعة فورية": "Instant Tracking",
    "استعلم عن حالة طلبك في أي وقت برقم الهوية.": "Check your application status anytime using your National ID.",
    "قبول إلكتروني": "Electronic Admission",
    "إجراءات ميسرة تبدأ من التسجيل وحتى مباشرة التدريب.": "Smooth procedures from registration to training commencement.",
    "جميع الحقوق محفوظة لـ التجمع الصحي الثاني - مدينة الملك فهد الطبية ©": "All rights reserved to Second Health Cluster - KFMC ©",
    "الشروط والأحكام": "Terms & Conditions",
    "الدعم الفني": "Technical Support",

    // --- صفحة التقديم (Apply) ---
    "بوابة التميز الرقمية": "Digital Excellence Portal",
    "انضم إلينا في رحلة تطوير مهاراتك داخل أحد أكبر التجمعات الصحية في المملكة.": "Join us on a journey to develop your skills within one of the largest health clusters in the Kingdom.",
    "العودة إلى الرئيسية": "Back to Home",
    "طلب انضمام جديد": "New Application Request",
    "أدخل بياناتك بدقة لضمان سرعة معالجة الطلب": "Enter your data accurately to ensure fast processing",
    "الاسم الكامل": "Full Name",
    "رقم الهوية": "National ID",
    "رقم الجوال": "Mobile Number",
    "اسم الجامعة": "University Name",
    "التخصص": "Major",
    "سنة التخرج": "Graduation Year",
    "البريد الإلكتروني": "Email Address",
    "ارفاق خطاب الجامعة": "Attach University Letter",
    "إرسال الطلب الآن": "Submit Application Now",
    "اختر التخصص": "Select Major",
    "تقنية معلومات": "IT",
    "تمريض": "Nursing",
    "إدارة صحية": "Health Administration",

    // --- صفحة التتبع (Track) ---
    "استعلام عن حالة الطلب": "Application Status Inquiry",
    "أدخل رقم الهوية الوطنية لمتابعة مراحل تدريبك": "Enter National ID to track your training stages",
    "استعلام الآن": "Search Now",
    "عزيزي": "Dear",
    "تهانينا! تم قبولك نهائياً وتوجيه خطابك للمنشأة التالية:": "Congratulations! You have been accepted and your letter is directed to:",
    "مقر التدريب:": "Training Location:",
    "نرجو منك التوجه للمقر المذكور أعلاه للمباشرة.": "Please proceed to the mentioned location for commencement.",
    "لقد تم ترشيحك للمرحلة الثانية:": "You have been nominated for the second stage:",
    "المقابلة الشخصية": "Personal Interview",
    "موعدك هو:": "Your appointment is:",
    "المكان: مدينة الملك فهد الطبية - إدارة التدريب.": "Location: KFMC - Training Administration.",
    "نعتذر منك، لم يتم قبول طلبك لهذه الفترة نظراً للاكتفاء، وتم إرسال إشعار الرفض لمرجعك.": "We apologize, your application was not accepted for this period due to capacity.",
    "طلبك الآن في مرحلة (استقبال الطلب) وهو قيد التدقيق حالياً.": "Your request is currently in the (Request Received) stage.",
    "لا يوجد طلب مسجل برقم الهوية هذا.": "No application registered with this ID.",

    // --- صفحة إخلاء الطرف (Clearance) ---
    "Clearance Form / نموذج إخلاء طرف": "Clearance Form",
    "بيانات الإدارة والوقت": "Administration & Time Info",
    "التاريخ": "Date",
    "اسم الإدارة المعنية": "Administration Name",
    "بيانات المتدرب الشخصية": "Trainee Personal Data",
    "رقم المتدرب (Employee No)": "Employee No.",
    "الجنسية / Nationality": "Nationality",
    "سعودي / Saudi": "Saudi",
    "غير سعودي / Non-Saudi": "Non-Saudi",
    "الاسم بالعربية (كما في الهوية)": "Arabic Name (as in ID)",
    "English Name (As in Passport)": "English Name",
    "السجل المدني / ID Number": "National ID / Iqama",
    "إرسال طلب إخلاء الطرف": "Submit Clearance Request",

    // --- صفحة الداشبورد (Dashboard) ---
    "إدارة النظام الذكي": "Smart System Management",
    "وضع المشاهدة فقط": "Viewer Mode Only",
    "إجمالي الطلبات": "Total Applications",
    "رسائل التواصل": "Contact Messages",
    "تحت المراجعة": "Under Review",
    "طلبات المتقدمين": "Applicant Requests",
    "المتقدم": "Applicant",
    "الحالة": "Status",
    "العمليات": "Actions",
    "رسائل الاستفسارات": "Inquiry Messages",
    "المرسل": "Sender",
    "العنوان": "Subject",
    "معاينة": "Preview",
    "تحديد مقابلة": "Set Interview",
    "قبول وتوجيه": "Approve & Direct",
    "رفض وإشعار": "Reject & Notify",
    "المشرف العام": "General Supervisor",
    "طلبات إخلاء الطرف":"Requests for clearance",
    "رقم الموظف":"employe num",
    "الإدارة":"Administration",
    "تسجيلات البرامج القصيرة": "Short Program Registrations",
    "الاسم": "Name",
    "رقم الهوية": "National ID",
    "نوع التسجيل": "Registration Type",
    "تاريخ التسجيل": "Registration Date",
    "برنامج قصير": "Short Program",
    "حلقة تطبيقية": "Workshop",
    "لا توجد تسجيلات حالياً": "No registrations currently",

    // --- صفحة اللتقييم ---
    "عرض الملاحظات":"View notes",
    // --- صفحة الحضور (Attendance) ---
    "إدارة الحضور اليومي": "Daily Attendance Management",
    "قائمة التحضير المباشر": "Live Attendance List",
    "المتدرب": "Trainee",
    "المنشأة الموجه لها": "Assigned Facility",
    "وقت التسجيل": "Sign-in Time",
    "الحالة اليومية": "Daily Status",
    "قيد الانتظار": "Pending",
    "تحضير": "Check-in",
    "تأخير": "Mark Late",
    "حاضر": "Present",
    "متأخر": "Late",
    "مدينة الملك فهد الطبية": "King Fahd Medical City",

    // --- صفحة التقييم (Evaluation) ---
    "تقييم أداء المتدربين": "Trainee Performance Evaluation",
    "المنشأة": "Facility",
    "التقييم الحالي": "Current Rating",
    "لم يقيم": "Not Evaluated",
    "إجراء": "Action",
    "حفظ التقييم": "Save Evaluation",

    // --- صفحة الإعدادات (Settings) ---
    "إعدادات النظام": "System Settings",
    "مدير": "Admin",
    "مشاهد": "Viewer",
    "إضافة مستخدم": "Add User",
    "إنشاء حساب جديد للوصول للوحة التحكم": "Create a new account for dashboard access",
    "كلمة المرور": "Password",
    "الصلاحية": "Role",
    "مدير كامل الصلاحيات": "Full Access Admin",
    "مشاهدة فقط": "View Only",
    "حفظ البيانات": "Save Changes",
    "قائمة الموظفين": "Staff List",
    "المستخدمين الحاليين في النظام": "Current system users",
    "الموظف": "Employee",
    "لا يوجد موظفين مسجلين حالياً": "No staff registered currently.",
    "الإجراء": "Action",
    // --- صفحة البرامج والحلقات (Programs/Workshops) ---
    "الحلقات التطبيقية": "Applied Workshops",
    "البرامج التدريبية القصيرة": "Short Training Programs",
    "استكشف وقدم على الحلقات التطبيقية المتاحة في مختلف المدن": "Explore and apply for available workshops across cities",
    "ابحث عن اسم البرنامج، المدينة، أو التاريخ...": "Search by program, city, or date...",
    "البرنامج، الرمز، أو المجال...": "Program, code, or field...",
    "الكروت": "Cards",
    "الجدول": "Table",
    "التفاصيل:": "Details:",
    "المدة:": "Duration:",
    "أيام": "Days",
    "نوع البرنامج: حلقة تطبيقية": "Program Type: Workshop",
    "سجل الآن": "Register Now",
    "المجال": "Field",
    "الفئة المستهدفة": "Target Group",
    "البداية (ميلادي)": "Start Date (Gregorian)",
    "المقر": "Location",
    "سجل": "Reg",
    "لا توجد دورات تبدأ قريباً، جرب البحث لاحقاً": "No upcoming courses, try searching later",
    "🔍 ابحث عن اسم البرنامج، الرمز، أو المجال...": "🔍 Search by program, code, or field...",
    "عرض الكروت": "Show Cards",
    "عرض الجدول": "Show Table",
    "لا توجد بيانات متاحة حالياً.": "No data available currently.",
    "🔍 ابحث عن اسم البرنامج، المدينة، أو التاريخ...": "🔍 Search by program, city, or date...",
    "© 2026 مدينة الملك فهد الطبية - جميع الحقوق محفوظة": "© 2026 King Fahd Medical City - All rights reserved",
    "استعرض أقرب الفرص التدريبية المتاحة في مدينة الملك فهد الطبية ومرافق التجمع": "Explore the nearest available training opportunities in King Fahd Medical City and its facilities",
    // --- صفحة الخطوات (Registration Steps) ---
    "آلية التدريب في التجمع الصحي الثاني": "Training Mechanism in Second Health Cluster",
    "توضح هذه الصفحة مراحل استقبال طلبات التدريب وآلية القبول والمتابعة حتى إصدار شهادة إتمام التدريب.": "This page explains application stages, admission, and follow-up until certification.",
    "استقبال الطلب": "Application Receipt",
    "المراجعة والموافقة": "Review & Approval",
    "في حال القبول": "In Case of Acceptance",
    "بدء التدريب": "Training Commencement",
    "إنهاء التدريب": "Training Completion",
    "في حال الرفض": "In Case of Rejection",
    "تعبئة البيانات الشخصية": "Fill Personal Data",
    "رفع المستندات المطلوبة": "Upload Required Documents",
    "التحقق من استيفاء الشروط": "Verification of Requirements",
    "تقييم الأولويات": "Priority Assessment",
    "توجيه المتدرب إلى مقر التدريب": "Directing Trainee to Location",
    "متابعة تدريب الطالب": "Trainee Follow-up",
    "إصدار شهادة إتمام التدريب": "Issuance of Completion Certificate",
    "يتم إرسال إشعار اعتذار للمتدرب عبر البريد الإلكتروني.": "A rejection notification is sent via email.",
    "تقديم طلب التدريب عبر البوابة الإلكترونية": "Submit training application through the online portal.",
    "مراجعة المستندات": "Document Review",
    "إصدار قرار القبول أو الرفض": "Issuing a decision of acceptance or rejection.",
    "تحويل خطاب الطالب الجامعي إلى منسق المراكز" : "Forwarding the student's university letter to the center coordinator.",
    "إرسال نموذج المباشرة" : "Sending the commencement form.",
    "حضور الجلسات التدريبية": "Attending Training Sessions",
    "المشاركة في الحالات العملية": "Participating in Practical Cases",
    "تطبيق المهارات العملية": "Applying Practical Skills",
    "إرسال نموذج التقييم": "Sending Evaluation Form",
    "إدراج السجل التدريبي للطالب": "Adding Student's Training Record",

    // --- صفحة التواصل (Contact) ---
    "مركز التواصل والدعم": "Contact & Support Center",
    "نحن هنا لخدمتكم والإجابة على استفساراتكم على مدار الساعة": "We are here to serve you and answer your inquiries 24/7",
    "معلومات التواصل": "Contact Information",
    "رقم الهاتف": "Phone Number",
    "الموقع": "Location",
    "ساعات العمل": "Working Hours",
    "الأحد – الخميس | 8ص - 4م": "Sunday – Thursday | 8AM - 4PM",
    "أرسل لنا رسالة مباشرة": "Send us a direct message",
    "عنوان الرسالة": "Message Subject",
    "كيف يمكننا مساعدتك؟": "How can we help you?",
    "إرسال الرسالة الآن": "Send Message Now",
    "الأسئلة الشائعة": "FAQ",
    "كيف يمكنني التقديم على برامج التدريب؟": "How can I apply for training programs?",
    "كيف يمكنني متابعة حالة طلبي؟": "How can I track my application status?",

    // --- حالات النظام (Statuses) ---
    "استقبال الطلب": "Request Received",
    "مقابلة شخصية": "Interview Scheduled",
    "مقبول": "Accepted",
    "مرفوض": "Rejected",
    "مكتمل": "Completed",

//--- حضور والانصراف
// --- Attendance Page ---
"مركز الحضور والتقارير": "Attendance & Reports Center",
"التاريخ اليوم:": "Today's Date:",
"حاضرون اليوم": "Present Today",
"غائبون اليوم": "Absent Today",
"إنذارات الغياب": "Absence Warnings",
"ابحث عن اسم المتدرب أو المنشأة...": "Search by trainee or facility name...",
"التحضير المباشر (اضغط على الاسم لفتح الخيارات)": "Live Attendance (Click name for options)",
"المتدرب": "Trainee",
"المنشأة": "Facility",
"دخول": "Check In",
"خروج": "Check Out",
"الحالة": "Status",
"سجل الحضور الأسبوعي (آخر 7 أيام)": "Weekly Attendance Record (Last 7 Days)",
"تصدير Excel": "Export Excel",
"انصراف": "Check Out",
"تأخير بعذر": "Late (Excused)",
"تأخير مفاجئ": "Late (Unexcused)",
"استئذان": "Permission",
"مهمة عمل": "Work Mission",
"غياب بعذر": "Absent (Excused)",
"غياب كلي": "Absent (Unexcused)",
"إغلاق": "Close"
};

function applyLanguage() {
    const lang = localStorage.getItem('site_lang') || 'ar';
    const btnText = document.getElementById('lang-text');

    if (lang === 'en') {
        document.documentElement.dir = 'ltr';
        document.documentElement.lang = 'en';
        if (btnText) btnText.innerText = 'العربية';
        // ترجمة محتوى الصفحة
        translatePageContent(document.body);
    } else {
        document.documentElement.dir = 'rtl';
        document.documentElement.lang = 'ar';
        if (btnText) btnText.innerText = 'English';
    }
}

function translatePageContent(element) {
    element.childNodes.forEach(node => {
        if (node.nodeType === Node.TEXT_NODE) {
            const text = node.textContent.trim();
            if (dictionary[text]) {
                node.textContent = node.textContent.replace(text, dictionary[text]);
            }
        } else if (node.nodeType === Node.ELEMENT_NODE) {
            // ترجمة الـ Placeholders
            if (node.placeholder && dictionary[node.placeholder.trim()]) {
                node.placeholder = dictionary[node.placeholder.trim()];
            }
            // ترجمة الـ Value (للأزرار القديمة)
            if (node.tagName === "INPUT" && (node.type === "submit" || node.type === "button")) {
                if (dictionary[node.value.trim()]) {
                    node.value = dictionary[node.value.trim()];
                }
            }
            translatePageContent(node);
        }
    });
}

function toggleLanguage() {
    const currentLang = localStorage.getItem('site_lang') || 'ar';
    const newLang = currentLang === 'ar' ? 'en' : 'ar';
    localStorage.setItem('site_lang', newLang);
    location.reload(); 
}

document.addEventListener('DOMContentLoaded', applyLanguage);