import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify, request 
payload = ""
headers = {
        'accept-language': "en-US,en;q=0.9",
        'accept-encoding': "gzip, deflate, br",
        'accept': "*/*",
        'x-api-source': "pc",
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        'if-none-match-': "55b03-e2b4b3f247507f7c1a18fda4a09f1340",
        'x-requested-with': "XMLHttpRequest",
        'connection': "keep-alive",
        'host': "runningstatus.in"
        }
app = Flask(__name__) 
@app.route('/', methods = ['GET', 'POST']) 
def home(): 
    if(request.method == 'GET'): 
  
        data = "hello world"
        return jsonify({'data': data}) 

@app.route('/status/<trainnum>', methods = ['GET']) 
def disp(trainnum): 
  date = '20200531'
  url = 'https://runningstatus.in/status/'+trainnum+'-on-20200531'
  res = requests.get(url,data=payload, headers=headers)
  return res.text

  
if __name__ == '__main__': 

	app.run(debug=True) 
