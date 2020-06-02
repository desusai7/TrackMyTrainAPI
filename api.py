import requests
import random
import time
from urllib.request import urlopen
import urllib.request, urllib.error
from bs4 import BeautifulSoup
from flask import Flask, jsonify, request 

app = Flask(__name__) 
@app.route('/', methods = ['GET', 'POST']) 
def home(): 
    if(request.method == 'GET'): 
  
        data = "hello world"
        return jsonify({'data': data}) 
@app.route('/check',methods = ['GET'])
def check():
   url = 'http://runningstatus.in/status/02566'
   headers = {'user-agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
   r = requests.get(url, headers=headers)
   page_html = r.content
   return str(r.status_code)
@app.route('/status/<trainnum>', methods = ['GET']) 
def disp(trainnum): 
  date = '20200601'
  url = 'https://runningstatus.in/status/'+trainnum+'-on-'+date
  headers = {'Host': 'runningstatus.in','Connection': 'keep-alive','Cache-Control': 'max-age=0','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Sec-Fetch-Site': 'cross-site','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Dest': 'document','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9,hi;q=0.8'}
  cookies = {'Cookie': '_ga=GA1.2.1922577627.1591073486; _gid=GA1.2.134316881.1591073486; __gads=ID=01b865e6bdbef1a3:T=1591073375:S=ALNI_MYkHuHfHVSNZX__qy6qHWyImDaj6w; s[02232]=01-06-2020; _yeti_currency_2={"dataAsOf":"2020-05-21T10:00:54.069Z","conversions":{"USD":{"CAD":1.3881182698,"HKD":7.7501368863,"ISK":142.8180324877,"PHP":50.5995619639,"DKK":6.804617631,"HUF":319.9580215368,"CZK":25.0319401351,"GBP":0.8154590254,"RON":4.4186895419,"SEK":9.6338747947,"IDR":14717.5031940135,"INR":75.6191823325,"BRL":5.7178317211,"RUB":71.728508852,"HRK":6.9145829531,"JPY":107.6382551561,"THB":31.8196751232,"CHF":0.9658696842,"EUR":0.9125752875,"MYR":4.3515240007,"BGN":1.7848147472,"TRY":6.7912940318,"CNY":7.1003832816,"NOK":9.9256251141,"NZD":1.6297682059,"ZAR":18.0236356999,"USD":1,"MXN":23.4007118087,"SGD":1.4147654682,"AUD":1.5197116262,"ILS":3.5040153313,"KRW":1228.0616900894,"PLN":4.1468333638},"GBP":{"CAD":1.7022538553,"HKD":9.5040175474,"ISK":175.1382081067,"PHP":62.0504039929,"DKK":8.3445242731,"HUF":392.3655408581,"CZK":30.6967479129,"GBP":1,"RON":5.4186530585,"SEK":11.814051344,"IDR":18048.121041205,"INR":92.7320441371,"BRL":7.0117952506,"RUB":87.9608988563,"HRK":8.4793750979,"JPY":131.9971351194,"THB":39.0205689474,"CHF":1.18444907,"EUR":1.1190939815,"MYR":5.3362877414,"BGN":2.188724009,"TRY":8.328185501,"CNY":8.7072226326,"NOK":12.1718256899,"NZD":1.9985899416,"ZAR":22.1024418631,"USD":1.2263031849,"MXN":28.6963674209,"SGD":1.7349313995,"AUD":1.8636272074,"ILS":4.2969851608,"KRW":1505.9759618613,"PLN":5.0852749614}}}; s[01093]=01-06-2020; s[01061]=01-06-2020; s[02541]=01-06-2020; s[0243212]=02-06-2020; s[02432]=02-06-2020'}
  res = requests.get(url,headers=headers,cookies=cookies)
  if not res:
    return str(res.status_code)
  soup = BeautifulSoup(res.text,'html.parser')
  divs = soup.find_all("div", class_="card-header")[0]
  result = "".join(divs.strings)
  return result

  
if __name__ == '__main__': 

	app.run() 
