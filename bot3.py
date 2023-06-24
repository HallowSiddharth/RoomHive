from flask import Flask, request, render_template, redirect,url_for
import asyncio
from telegram import Bot
import random

app = Flask(__name__)

async def send_telegram_message(chat_id, message_text):
    bot = Bot(token='6279996362:AAGM-yvAh1rVt6H2bpQn8yFAmWN3Maozjvg')
    await bot.send_message(chat_id=chat_id, text=message_text)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/backlogin', methods=['GET','POST'])
def backlogin():
    return redirect(url_for('home'))

@app.route('/test')
def forget():
    print('forget')
    return render_template('forgotpassword.html')

@app.route('/otp',methods=['GET','POST'])
def send_otp():
    x=random.randrange(1000,9999)
    print(x)
    if request.method== 'POST':
        chat_id= request.form.get('chat_id')
        print(chat_id)
        message_text = f'''
Dear Customer name,
an attempt has been made to login to your RoomHive account.
Your Login OTP is: {x}.
In case you didn't request it, change your password.
'''

        asyncio.run(send_telegram_message(chat_id, message_text))

    return render_template('otpconfirmation.html')

#5949869230
# @app.route('/', methods=['GET', 'POST'])
# def forgot_password():
#     if request.method == 'POST':
#         chat_id = request.form.get('chat_id')
#         print(chat_id)
#         message_text = '''
#         Dear {Customer name},
#         an attempt has been made to login to your RoomHive account.
#         Your Login OTP is: XXXXXX.
#         In case you didn't request it, change your password.
#         '''
#         asyncio.run(send_telegram_message(chat_id, message_text))

#     return render_template('forgotpassword.html')

# @app.route('/send_otp', methods=['GET', 'POST'])
# def bot():
#     if request.method=='POST':


if __name__ == '__main__':
    app.run()
