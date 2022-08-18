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

app = Flask(__name__)

line_bot_api = LineBotApi('yFLty6SI3AVhqg0jV38n6XjLsOJXdyEF3A/fjqGAqvLXS1n2ijRrEmTA7ewkxuzfXLu1CLaiIEoyJ9l9AS09YfnS4YnkKbHdDggSTMfu2rgzmLTG5qcrB3PAfp6TwpaRD4KdEq2ALmIpAS9D87E4WQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('93219b5ef6345012825b7616b711d547')


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
    msg = event.message.text
    r= '許志安牛逼'

    if msg in ['hi','Hi']:
        r = '嗨'
    elif msg == '區塊練牛逼':
        r = '傳銷騙局'
    elif msg == 'NFT牛逼':
        r = '都是jpg'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()