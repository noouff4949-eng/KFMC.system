import pandas as pd
from datetime import datetime

def load_workshops_to_db(file_path, db, AppliedWorkshop):
    try:
        # قراءة ملف الإكسل (تأكد أن اسم الملف مطابق)
        df = pd.read_excel(file_path)
        # تنظيف مسافات مسميات الأعمدة
        df.columns = df.columns.str.strip()
    except Exception as e:
        print(f"خطأ في قراءة الملف: {e}")
        return

    with app.app_context():
        # اختياري: مسح البيانات القديمة لجدول الحلقات فقط قبل الرفع الجديد
        db.session.query(AppliedWorkshop).delete()

        count = 0
        for index, row in df.iterrows():
            try:
                # إنشاء سجل جديد لكل سطر في الإكسل
                workshop = AppliedWorkshop(
                    title=str(row['اسم البرنامج']),
                    duration=str(row['مدة البرنامج']),
                    riyadh_dates=str(row['مدينة الرياض']) if pd.notna(row['مدينة الرياض']) else "",
                    jeddah_dates=str(row['محافظة جدة']) if pd.notna(row['محافظة جدة']) else "",
                    dammam_dates=str(row['مدينة الدمام']) if pd.notna(row['مدينة الدمام']) else "",
                    abha_dates=str(row['مدينة أبها']) if pd.notna(row['مدينة أبها']) else ""
                )
                db.session.add(workshop)
                count += 1
            except KeyError as e:
                print(f"خطأ: لم يتم العثور على عمود {e} في الإكسل. تأكد من مسميات الأعمدة.")
                return
            except Exception as e:
                print(f"خطأ في السطر {index}: {e}")

        db.session.commit()
        print(f"✅ مبروك! تم رفع {count} حلقة تطبيقية بنجاح إلى جدول المصفوفة.")

if __name__ == "__main__":
    # استبدل 'workshops.xlsx' باسم ملفك الفعلي
    load_workshops('workshops.xlsx')
