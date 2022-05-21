from flask import Flask
from threading import Thread

app = Flask('')
uptime = -5

@app.route('/')
def home():
  global uptime
  uptime += 5
  return str(uptime) + " mins online"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
  t = Thread(target = run)
  t.start()