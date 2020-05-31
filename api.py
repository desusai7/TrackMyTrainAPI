import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify, request 
app = Flask(__name__) 
@app.route('/status/<trainnum>', methods = ['GET']) 
def disp(trainnum): 
  date = '20200531'
  url = 'https://runningstatus.in/status/'+trainnum+'-on-'+date
  res = requests.get(url)
  soup = BeautifulSoup(res.text,'html.parser')
  divs = soup.find_all("div", class_="card-header")[0]
  result = "".join(divs.strings)
  print(result)
  return result
if __name__ == '__main__': 

	app.run(debug = True) 
