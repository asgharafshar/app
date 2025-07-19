import os
import requests

def main(context):
    try:
        context.log("🆕 ✅ نسخه‌ی جدید فانکشن اجرا شد!")

        # نمایش کل داده دریافتی
        raw_data = context.req.body_raw
        json_data = context.req.body_json

        context.log("📦 داده‌ی خام دریافتی:", str(raw_data))
        context.log("📥 داده‌ی JSON دریافتی:", str(json_data))

        # استخراج اطلاعات از پیام
        message = json_data.get("message", {})
        chat = message.get("chat", {})
        chat_id = chat.get("id")
        text = message.get("text")

        if not chat_id or not text:
            context.log("⚠️ پیام ناقص بود.")
            return context.res.text("پیام ناقص دریافت شد")

        # نمایش اطلاعات استخراج‌شده
        context.log(f"👤 chat_id: {chat_id}")
        context.log(f"💬 text: {text}")

        # ارسال پاسخ به Bale
        BOT_TOKEN = os.environ.get("Bale_BOT_TOKEN")
        if not BOT_TOKEN:
            context.error("❌ توکن Bale تنظیم نشده")
            return context.res.text("توکن تعریف نشده")

        response = requests.post(
            f"https://tapi.bale.ai/bot{BOT_TOKEN}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": f"✅ این نسخه‌ی جدید اجرا شد و پیام شما دریافت شد: {text}"
            }
        )

        context.log("📤 نتیجه‌ی ارسال به Bale:", str(response.text))
        return context.res.text("پیام ارسال شد")

    except Exception as e:
        context.error(f"❌ خطا در فانکشن: {str(e)}")
        return context.res.text("خطا در اجرای فانکشن")
