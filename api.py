import requests
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
   url = "https://runningstatus.in/status/02566"
   headers = {'Host': 'runningstatus.in',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': "1",
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Sec-Fetch-Site': 'none',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Dest': 'document',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
'Cookie': '_ga=GA1.2.1680708864.1591117356; _gid=GA1.2.696354975.1591117356; __gads=ID=4d8e2ef44b77926f:T=1591117245:S=ALNI_MawBXYX63SwtdI-PQkpwIk5LevhRA; _yeti_currency_2={"dataAsOf":"2020-06-01T10:00:53.803Z","conversions":{"USD":{"CAD":1.3721264368,"HKD":7.7538613506,"ISK":135.4166666667,"PHP":50.4947916667,"DKK":6.6937859195,"HUF":313.1555316092,"CZK":24.1747485632,"GBP":0.8089798851,"RON":4.3546156609,"SEK":9.4172054598,"IDR":14610.003591954,"INR":75.5230783046,"BRL":5.3568606322,"RUB":70.4396551724,"HRK":6.8130387931,"JPY":107.1210488506,"THB":31.8103448276,"CHF":0.9626436782,"EUR":0.8979885057,"MYR":4.3475215517,"BGN":1.7562859195,"TRY":6.8337823276,"CNY":7.1350574713,"NOK":9.6875,"NZD":1.6040768678,"ZAR":17.4424389368,"USD":1,"MXN":22.0635775862,"SGD":1.4109195402,"AUD":1.4979346264,"ILS":3.5079920977,"KRW":1235.8207614943,"PLN":3.9955998563},"GBP":{"CAD":1.69611935,"HKD":9.584739366,"ISK":167.3918834917,"PHP":62.4178580943,"DKK":8.274353965,"HUF":387.0992807033,"CZK":29.8830032857,"GBP":1,"RON":5.3828478821,"SEK":11.6408400675,"IDR":18059.7859870349,"INR":93.3559408578,"BRL":6.6217476245,"RUB":87.0721960749,"HRK":8.421765385,"JPY":132.4149720274,"THB":39.32155226,"CHF":1.1899476068,"EUR":1.1100257526,"MYR":5.3740786786,"BGN":2.1709883669,"TRY":8.4474069798,"CNY":8.8198206198,"NOK":11.974957819,"NZD":1.9828390019,"ZAR":21.5610292159,"USD":1.2361246781,"MXN":27.2733327413,"SGD":1.7440724625,"AUD":1.8516339579,"ILS":4.3363156025,"KRW":1527.6285409822,"PLN":4.9390595862}}}; s[04674]=02-06-2020; s[02566]=02-06-2020; _gat=1'}
   res  = requests.get(url,headers = headers)
   return str(res.status_code)

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
