#------------------------------------------------------------------------------------------------------------------
from flask import Flask , render_template , redirect , request
#------------------------------------------------------------------------------------------------------------------
import razorpay
#------------------------------------------------------------------------------------------------------------------
from twilio import *
from twilio.rest import Client
TWILIO_ACCOUNT_SID = 'AC333d326c087b159d679e54c80cca21e1'
TWILIO_AUTH_TOKEN = 'aa000cfe9e12a671539a7c4fd3b7192b'
TWILIO_PHONE_NUMBER = '+12059461695'
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
#------------------------------------------------------------------------------------------------------------------
#Global variables
#------------------------------------------------------------------------------------------------------------------
name1=""
phone1=None
bus_route1=""
total_amount=int()
#------------------------------------------------------------------------------------------------------------------

app  =  Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    global phone1,name1,bus_route1,total_amount
    name1=name = request.form['name']
    phone1= phone =request.form['phone']
    bus_route1=bus_route = request.form['bus_route']
    adults = int(request.form['adult'])
    children = int(request.form['child'])

    if (bus_route == "kakinada-Bangalore"):
      total_amount = (500* adults) + (250 * children)
    elif (bus_route == "kakinada-Hyderabad"):
      total_amount = (500 * adults) + (250 * children)
    elif (bus_route == "kakinada-Vizag"):
      total_amount = (500 * adults) + (250 * children)
    else:
      return render_template('index.html')
    
    return render_template('verification.html', name=name, phone=phone, bus_route=bus_route, adults=adults, children=children, total_amount=total_amoun)

@app.route("/success")
def success():
  global phone1,name1,bus_route1
  message = f"Hello {name1}! Your bus ticket to {bus_route1} has been booked successfully."
  #client.messages.create(to=phone1, from_=+12059461695, body=message)
  return render_template("success.html")

@app.route("/failed")
def decline():
  global phone1,name1,bus_route1
  message = f"Hello {name1}! Your bus ticket to {bus_route1} not booked due to some issues."
  client.messages.create(to=phone1, from_=+12059461695, body=message)
  return render_template("Failed.html")

@app.route("/return_", methods=["GET"])
def return_():
  if request.method=="GET":
    return render_template("Home.html")

if __name__ == '__main__':
  app.run(debug="True" ,port=1111)