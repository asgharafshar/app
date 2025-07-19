def main(context):
    try:
        ###

        ## 4:27
        print("تست اجرا شد")
        data = context.req.body_json
        context.log("📥 داده دریافتی:", str(data))

        return context.res.text("✅ فانکشن اجرا شد")
    except Exception as e:
        context.error(f"❌ خطا در اجرا: {str(e)}")
        return context.res.text("❌ خطا در دریافت داده")
