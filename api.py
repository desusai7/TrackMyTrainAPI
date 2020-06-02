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
  res = requests.get(url)
  if not res:
    return res.status_code
  soup = BeautifulSoup(res,'html.parser')
  divs = soup.find_all("div", class_="card-header")[0]
  result = "".join(divs.strings)
  return res.status_code

  
if __name__ == '__main__': 

	app.run() 
