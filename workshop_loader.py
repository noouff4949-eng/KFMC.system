import pandas as pd

def load_workshops_to_db(file_path, db, AppliedWorkshop):
    try:
        df = pd.read_excel(file_path)
        df.columns = df.columns.str.strip()
    except Exception as e:
        print(f"❌ خطأ في قراءة ملف الإكسل: {e}")
        return

    try:
        # حذف البيانات القديمة (اختياري)
        db.session.query(AppliedWorkshop).delete()

        count = 0

        for index, row in df.iterrows():
            try:
                workshop = AppliedWorkshop(
                    title=str(row.get('اسم البرنامج', '')),
                    duration=str(row.get('مدة البرنامج', '')),
                    riyadh_dates=str(row.get('مدينة الرياض', '')) if pd.notna(row.get('مدينة الرياض')) else "",
                    jeddah_dates=str(row.get('محافظة جدة', '')) if pd.notna(row.get('محافظة جدة')) else "",
                    dammam_dates=str(row.get('مدينة الدمام', '')) if pd.notna(row.get('مدينة الدمام')) else "",
                    abha_dates=str(row.get('مدينة أبها', '')) if pd.notna(row.get('مدينة أبها')) else ""
                )

                db.session.add(workshop)
                count += 1

            except Exception as e:
                print(f"❌ خطأ في السطر {index}: {e}")

        db.session.commit()
        print(f"✅ تم رفع {count} حلقة تطبيقية بنجاح")

    except Exception as e:
        db.session.rollback()
        print(f"❌ خطأ أثناء الحفظ في قاعدة البيانات: {e}")
