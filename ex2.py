from flask import Flask, request, render_template, redirect, url_for, abort, flash
from location import get_coordinates
import random, pandas as pd
from hotel_details import get_nearby_hotels, return_hostels_csv, desired_results
from telegram import Bot
import mysql.connector
import csv

temp_chat_id= None
DATA=None
conn=mysql.connector.connect(host="localhost", user="root", password="vishal", database ='id')
try:
    if conn.is_connected():
        print("yes")
except:
    print("Errored")

cur=conn.cursor()
x = random.randrange(1000, 9999)

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'area-ku-vada'


async def send_telegram_message(chat_id, message_text):
    print('hi')
    bot = Bot(token='6279996362:AAGM-yvAh1rVt6H2bpQn8yFAmWN3Maozjvg')
    await bot.send_message(chat_id=chat_id, text=message_text)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == "POST":
        data = request.get_json()
        username = data['username']
        password = data['password']

        
        cur.execute("SELECT USERNAME,PASSWORD FROM ID;")
        res = cur.fetchall()

        username1 = []
        password1 = []
        for i in res:
            username1.append(i[0])
            password1.append(i[1])
        if username in username1:
            ind = username1.index(username)
            if password1[ind] == password:
                print("verified")
                return success()

            else:
                print("Login credentials dont match!!!")
                flash("login credentials dont match!!!")
                
                return submit()
                # abort(400)
                # return redirect(url_for('index'))

        else:
            print("Username/Password does not exist!!!")
            flash("Username not in the database!!!")
            # return submit()
            #abort(400)

    # conn.close()
    return success()


@app.route('/search')
def success():
    return render_template('searchhome.html')


@app.route('/sub', methods=['GET', 'POST'])
def sub():
    name = request.form.get('clgname')
    location = get_coordinates(name)
    # print(location)
    lat = location['lat']
    lng = location['lon']
    hostel_details = get_nearby_hotels(lat, lng)
    # print(hostel_details)
    ans = return_hostels_csv(hostel_details)
    # print(ans)
    foodo = request.form.get('foodo')
    occ = request.form.get('occ')
    aco = request.form.get('aco')
    rangeo = request.form.get('rangeo')
    # print(foodo)
    # print(occ)
    # print(aco)
    # print(rangeo)
    final = desired_results(foodo, aco, occ, rangeo)
    print("p", final)

    df = pd.DataFrame(final, columns=['Name', 'Address', 'Price', 'Food', 'AC', 'Occupancy'])
    df.to_csv('output.csv', index=False)
    global DATA
    data = []
    with open('output.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    print(data)
    DATA=data
    return render_template('saerchmain.html', hot=data)

    # return render_template('saerchmain.html')
    # return 'success'


@app.route('/dummy')
def dummy():
    data = []
    with open('output.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    return render_template('saerchmain.html', hot=data)


#     return render_template('saerchmain.html', hot=data)
@app.route('/backlogin', methods=['GET', 'POST'])
def backlogin():
    return redirect(url_for('index'))


@app.route('/forgotpassword')
def forget():
    return render_template('forgotpassword.html')



@app.route('/send_otp', methods=['POST'])
async def send_otp():
    #x = random.randrange(1000, 9999)
    if request.method == 'POST':
        global temp_chat_id
        chat_id = request.form.get('chat_id')
        temp_chat_id = chat_id
        message_text = f'''
        Dear Customer,
an attempt has been made to login to your RoomHive account.
Your Login OTP is: {x}.
In case you didn't request it, change your password.
'''
        #asyncio.run(send_telegram_message(chat_id, message_text))
        await send_telegram_message(chat_id, message_text)


        return render_template('otpconfirmation.html')

@app.route('/telegram2', methods=['POST'])
async def telegram2():
    if request.method == 'POST':
        print('DATA')
        print(DATA)
        L=[]
        for i in DATA:
            L1=[]
            L1.append(i['Name'])
            L1.append(i['Address'])
            L1.append(i['Price'])
            L.append(L1)
        S=''
        for i in L:
            for j in i:
                S+=j+'  '
            S+='''

'''
        message_text=S

        chat_id=5949869230
        #asyncio.run(send_telegram_message(chat_id, message_text))
        await send_telegram_message(chat_id, message_text)

    return render_template('index.html')


        


@app.route('/get_otp', methods=['POST'])
def get_otp():
    if request.method == 'POST':
        otp = request.form.get('otp')
        print(x)
        print(otp)
        print(type(x), type(otp))
        if x == int(otp):
            return render_template('resetpassword.html')
        else:
            return "Invalid OTP"
        
@app.route('/back', methods=['GET','POST'])
def back():
    if request.method=='POST':
        pwd=request.form['pwd']
        cnfrmpwd=request.form['cnfrmpwd']
        global temp_chat_id
        print(pwd,cnfrmpwd,temp_chat_id)
        if pwd==cnfrmpwd:
            q="UPDATE ID SET PASSWORD=(%s) WHERE TB=(%s)"
            v=(pwd,temp_chat_id)
            cur.execute(q,v)
            conn.commit()
            print("CONFIRM")

            return render_template('index.html')

@app.route('/registerr')
def registerr():
    
    return render_template('register.html')


@app.route('/register', methods=['GET','POST'])
def register():
    if request.method=='POST':
        username=request.form['username']
        tele=request.form['telegram']
        password=request.form['password']
        confirm=request.form['confirmpassword']
        if password==confirm:
            q="INSERT INTO ID VALUES(%s,%s,%s)"
            v=(username,password,tele)
            cur.execute(q,v)
            conn.commit()

            print('EXECUTED')
        return render_template('searchhome.html')


app.run()