from flask import Flask, request
import psycopg2
import sms_handler

app = Flask(__name__)

@app.route('/api/v1/sms')
def sms_webhook():
	print("***** API DATA ******")
	conn = psycopg2.connect(dbname="financial_chatbot_website", user="postgres", host="localhost", password="password")
	cur = conn.cursor()
	cur.execute("select * from users where phone_number=303;")
	user = cur.fetchone()
	print(user)
	cur.close()
	conn.close()
	print(request.form)
	return 'In api'

@app.route('/')
def hello_world():
    return 'Hello, World!'
