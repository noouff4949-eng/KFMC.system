import pandas as pd
from app import app, db, Course
from datetime import datetime

def find_column_by_keywords(df, keywords):
    """دالة تبحث عن اسم العمود الصحيح بناءً على كلمات دلالية لتجنب أخطاء الإملاء"""
    for col in df.columns:
        # تنظيف اسم العمود من المسافات الزائدة قبل المقارنة
        clean_col = str(col).strip()
        if any(key in clean_col for key in keywords):
            return col
    return None

def load_excel_to_db(file_path):
    try:
        # قراءة الملف
        df = pd.read_excel(file_path)
    except Exception as e:
        print(f"خطأ في قراءة الملف: {e}")
        return

    with app.app_context():
        # البحث عن أسماء الأعمدة الفعلية في ملفك
        col_map = {
            'branch': find_column_by_keywords(df, ['الفرع']),
            'category': find_column_by_keywords(df, ['المجال']),
            'code': find_column_by_keywords(df, ['رمز']),
            'title': find_column_by_keywords(df, ['اسم البرنامج']),
            'date_h': find_column_by_keywords(df, ['هجري']),
            'date_m': find_column_by_keywords(df, ['ميلادي']),
            'duration': find_column_by_keywords(df, ['التنفيذ','مدة', 'مده']),
            'target': find_column_by_keywords(df, ['الفئة', 'الفئه']),
            'location': find_column_by_keywords(df, ['مقر'])
        }

        # التأكد من العثور على الأعمدة الأساسية على الأقل
        if not col_map['title'] or not col_map['date_m']:
            print("خطأ: لم يتم العثور على الأعمدة الأساسية في ملف الإكسل.")
            return

        count = 0
        for index, row in df.iterrows():
            try:
                # معالجة التاريخ الميلادي
                raw_date = row[col_map['date_m']]
                if pd.isna(raw_date):
                    continue
                
                # تحويل التاريخ إلى تنسيق يفهمه بايثون
                clean_date = pd.to_datetime(raw_date).date()

                new_course = Course(
                    branch=str(row[col_map['branch']]) if col_map['branch'] else "غير محدد",
                    category=str(row[col_map['category']]) if col_map['category'] else "عام",
                    course_code=str(row[col_map['code']]) if col_map['code'] else "-",
                    title=str(row[col_map['title']]),
                    start_date_h=str(row[col_map['date_h']]) if col_map['date_h'] else "-",
                    start_date_m=clean_date,
                    duration=str(row[col_map['duration']]) if col_map['duration'] else "-",
                    target_group=str(row[col_map['target']]) if col_map['target'] else "الجميع",
                    location=str(row[col_map['location']]) if col_map['location'] else "عن بعد"
                )
                db.session.add(new_course)
                count += 1
            except Exception as e:
                print(f"تخطي السطر {index} بسبب: {e}")

        db.session.commit()
        print(f"✅ تم بنجاح! تم رفع {count} دورة تدريبية إلى قاعدة البيانات.")

if __name__ == "__main__":
    # تأكد أن ملف الإكسل في نفس المجلد وبنفس الاسم
    load_excel_to_db('programs.xlsx')