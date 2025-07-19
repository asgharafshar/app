import requests
def main(context):
    try:
        data = context.req.json()
        context.log("📥 داده دریافتی:", str(data))

        return context.res.text("فانکشن اجرا شد")

    except Exception as e:
        context.error(f"❌ خطا: {str(e)}")
        return context.res.text("خطا در اجرا")
