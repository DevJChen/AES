import base64
import os
from email6.mime.multipart import MIMEMultipart
from email6.mime.text import MIMEText
from email6.mime.base import MIMEBase
from email6 import encoders
import mimetypes
from Scrapper import Scrapper
from Google import Create_Service
from Google import Comment_Service
import time

def Sendmail():
    start = time.time()
    time.sleep(1)
    CLIENT_SECRET_FILE = 'client_secret.json'
    API_NAME = "gmail"
    API_VERSION = 'v1'
    SCOPES = ["https://mail.google.com/"]
    meme_path = "C:\\Users\\john\PycharmProjects\\AutomatedGmail\\memes"
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    file_attatchments = []
    Scrapper(4)
    for f in os.listdir(meme_path):
        file = os.path.join(meme_path, f)
        file_attatchments.append(file)

    emailMsg = "Here you go sir"
    mimeMessage = MIMEMultipart()
    mimeMessage["to"] = "johnchenrs@gmail.com"
    mimeMessage["subject"] = "Memes"
    mimeMessage.attach(MIMEText(emailMsg, "plain"))

    for file in file_attatchments:
        content_type, encoding = mimetypes.guess_type(file)
        main_type, sub_type = content_type.split("/", 1)
        file_name = os.path.basename(file)

        f = open(file, "rb")

        myFile = MIMEBase(main_type, sub_type)
        myFile.set_payload(f.read())
        myFile.add_header("Content-Disposition", "attachment", filename=file_name)
        encoders.encode_base64(myFile)

        f.close()
        mimeMessage.attach(myFile)
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_string().encode()).decode()
    message = service.users().messages().send(
        userId = "me",
        body={'raw': raw_string}).execute()
    end = time.time()
    print(end - start)
    print(message)
    mailid = message["id"]
    return meme_path, mailid

def DeleteFiles(path, mailid):
    """CLIENT_SECRET_FILE = 'client_secret.json'
    API_NAME = "gmail"
    API_VERSION = 'v1'
    SCOPES = ["https://mail.google.com/"]
    service = Comment_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    message = service.users().messages().get(
        userId="me",
        id=mailid
    ).execute()
    print(message)"""
    for f in os.listdir(path):
        os.unlink(os.path.join(path, f))
    print("FILES DELETED")
path, mailid = Sendmail()
DeleteFiles(path=path, mailid=mailid)