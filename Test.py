from flask import Flask
import os
import datetime
import subprocess

app = Flask(_name_)
# i am learning
@app.route('/htop')
def htop():
    username = os.getenv("USER", "codespace-user")
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    try:
        top_output = subprocess.check_output("top -b -n 1", shell=True).decode("utf-8")
    except Exception as e:
        top_output = str(e)
    response = f"""
    <h1>System Info</h1>
    <p><b>Name:</b> Karthik Shetty K</p>
    <p><b>Username:</b> {username}</p>
    <p><b>Server Time (IST):</b> {ist_time}</p>
    <pre>{top_output}</pre>
    """
    return response

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)