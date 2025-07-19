import requests
import os

def main(context):
    try:
        context.log("🚀 تست دستی اجرا شد")

        BOT_TOKEN = os.environ.get("Bale_BOT_TOKEN")
        if not BOT_TOKEN:
            return context.res.text("❌ توکن Bale تنظیم نشده")

        # یک chat_id واقعی از ربات خودت تست کن (برای شروع می‌تونی خودت رو انتخاب کنی)
        chat_id = 123456789  # اینو با عدد واقعی جایگزین کن

        response = requests.post(
            f"https://tapi.bale.ai/bot{BOT_TOKEN}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": "✅ این پیام از طریق اجرای دستی فانکشن ارسال شد!"
            }
        )

        context.log("📤 پاسخ Bale:", str(response.text))
        return context.res.text("پیام ارسال شد به Bale")

    except Exception as e:
        context.error(f"❌ خطا در ارسال: {str(e)}")
        return context.res.text("خطا")
