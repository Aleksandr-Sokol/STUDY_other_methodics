import threading
from flask import Flask
from flask_mail import Mail, Message
import datetime
from flask_apscheduler import APScheduler
from os import path
from conf import configuration_data

app = Flask (__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = configuration_data['mail_login']
app.config['MAIL_PASSWORD'] = configuration_data['mail_password']
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

app.config['RQ_OTHER_HOST'] = 'localhost'
app.config['RQ_OTHER_PORT'] = 6379
app.config['RQ_OTHER_PASSWORD'] = None
app.config['RQ_OTHER_DB'] = 0

scheduler = APScheduler()

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

@app.route('/send_email')
def send_email():
    dir = configuration_data['directory']
    name = configuration_data['file_name']
    path_file = path.join(dir, name)
    current_date_time = datetime.datetime.now()
    current_time = current_date_time.time()
    msg = Message('Set Image', sender=configuration_data['mail_login'], \
                  recipients=[configuration_data['mail_recipients']])
    msg.body = f"Image from {current_time}"
    with app.open_resource(path_file) as fp:
       msg.attach(name, "image/jpg", data=fp.read())
    thread = threading.Thread(target=send_async_email, args=[app, msg])
    thread.start()
    return 'success'

if __name__ == '__main__':
    hour = configuration_data['sent_time'].split(':')[0]
    scheduler.add_job(id='task', func=send_email, trigger='cron', hour=hour, minute=0, second=0)
    scheduler.start()
    app.run(debug=True, host='127.0.0.1', port='8080')