from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)



CHANNEL_ACCESS_TOKEN = "DTHgm/qRsEjKmINhGyR3FiyVErnALoq1q9pv7GkGDeQNWOBxl75XXsolGIfiGC047D0AxH8QUxxhrq99MlYe+SC5U0Q/HwEO6/sh4+zef+YHfc1OPfRCP7PVa0jArloerkH6U9cHDPnkyoZhLC5yfQdB04t89/1O/w1cDnyilFU="
CHANNEL_SECRET = "44da6f9e8f3ca3dbfa2a31f0433f6a1c"

app = Flask(__name__)

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()