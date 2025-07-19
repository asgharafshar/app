import requests
import os

def main(context):
    try:
        data = context.req.json()
        context.log("📥 داده دریافتی:", str(data))

        message = data.get("message", {})
        chat = message.get("chat", {})
        chat_id = chat.get("id")
        text = message.get("text")

        if not chat_id or not text:
            return context.res.text("❌ پیام نامعتبره")

        BOT_TOKEN = os.environ.get("Bale_BOT_TOKEN")
        if not BOT_TOKEN:
            return context.res.text("❌ توکن تعریف نشده")

        # ارسال پیام به کاربر در Bale
        response = requests.post(
            f"https://tapi.bale.ai/bot{BOT_TOKEN}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": f"✅ دریافت شد: {text}"
            }
        )

        context.log("🟢 پاسخ ارسال شد:", str(response.text))
        return context.res.text("پاسخ برای Bale ارسال شد")

    except Exception as e:
        context.error("❌ خطا در ارسال پیام:", str(e))
        return context.res.text("خطا")
