import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc
import pandas as pd
import datetime
import numpy as np
import urllib
import datetime as dt
from matplotlib import style

def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter    

def get_data(stock):

        
    stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10y/csv'
    source_code =  urllib.request.urlopen(stock_price_url).read().decode()
    stock_data = []
    split_source = source_code.split('\n')
    for line in split_source:
        split_line = line.split(',')
        if len(split_line) == 6:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)

    global date, closep,highp,lowp,openp,volume
    date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data,
                                                          delimiter=',',
                                                          unpack=True,
                                                          converters={0: bytespdate2num('%Y%m%d')})
    print(stock_data)

def sms_sender(message):
    from twilio.rest import TwilioRestClient
    
    account_sid = "ACc55db698849f6b3b1b2c87e8da66d81d" # Your Account SID from www.twilio.com/console
    auth_token  = "559d2c06a2ab6861750b417f4abb6940"  # Your Auth Token from www.twilio.com/console
    
    client = TwilioRestClient(account_sid, auth_token)
    
    message_send = client.messages.create(body=message,
        to="+15512083809",    # Replace with your phone number
        from_="+16468462195") # Replace with your Twilio number
    
    print(message_send.sid)
    
#sms_sender("I will rock this")
get_data("EBAY")

