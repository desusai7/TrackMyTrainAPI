import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
from flask import Flask, jsonify, request 

app = Flask(__name__) 
@app.route('/', methods = ['GET', 'POST']) 
def home(): 
    if(request.method == 'GET'): 
  
        data = "hello world"
        return jsonify({'data': data}) 

@app.route('/status/<trainnum>', methods = ['GET']) 
def disp(trainnum): 
  date = '20200601'
  url = 'https://runningstatus.in/status/'+trainnum+'-on-'+date
  headers = {'Host': 'runningstatus.in','Connection': 'keep-alive','Cache-Control': 'max-age=0','Upgrade-Insecure-Requests': 1,'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Sec-Fetch-Site': 'cross-site','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Dest': 'document','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9,hi;q=0.8'}
  res = requests.get(url,headers=headers)
  if not res:
    return str(res.status_code)
  soup = BeautifulSoup(res.text,'html.parser')
  divs = soup.find_all("div", class_="card-header")[0]
  result = "".join(divs.strings)
  return result

  
if __name__ == '__main__': 

	app.run() 
