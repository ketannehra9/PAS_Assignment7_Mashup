from flask import Flask, render_template, request, send_file
import os
import zipfile
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import sys

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mashup', methods=['POST'])
def mashup():
    singer = request.form['singer']
    count = request.form['count']
    duration = request.form['duration']
    email = request.form['email']


    output_filename = "mashup_output.mp3"
    

    cmd = f'python3 102303871.py "{singer}" {count} {duration} {output_filename}'
    os.system(cmd)
    
    
    zip_filename = "mashup_output.zip"
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        zipf.write(output_filename)
        
    send_email(email, zip_filename)
    
    return "Mashup created and sent to your email!"

def send_email(to_addr, filename):
    from_addr = "some_email" 
    password = "some_password_key" 
    
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = "Your Mashup File - from Ketan Nehra (102303871)"
    
    body = "Here is the mashup file you requested."
    msg.attach(MIMEText(body, 'plain'))
    
    attachment = open(filename, "rb")
    
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)
    
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    
    try:
        s.login(from_addr, password)
        text = msg.as_string()
        s.sendmail(from_addr, to_addr, text)
        s.quit()
    except Exception as e:
        print("Email failed:", e)

if __name__ == '__main__':
    app.run(debug=True, port=5000)