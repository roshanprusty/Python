import  requests
import json
from tkinter.messagebox import showerror,showinfo
from tkinter import *

def send_sms(number, message):
    url = "https://www.fast2sms.com/dev/bulkV2"

    prams = {
        "authorization" : "CW7tOQhzax5V0M9bHGeZ8vBk6KYAXJSmTRnIi3su2UNp1Lqlrd5ZNPeJo6VqhAvlCHLcakfY3bB4zyg0",
        "sender_id" : "FSTSMS",
        "route" : "p",
        "language" : "unicode",
        "numbers" : number,
        "message" : message
    }
    response = requests.get(url, params= prams)
    dic = response.json()
    # print(dic)
    # return dic.get('return')


send_sms(7008280274,"hello")