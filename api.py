import requests,re
from bs4 import BeautifulSoup
from flask import Flask, jsonify, request 
from requests_html import HTMLSession
from datetime import date 
from datetime import timedelta 
app = Flask(__name__) 
@app.route('/', methods = ['GET', 'POST']) 
def home(): 
    if(request.method == 'GET'): 
  
        data = "hello world"
        return jsonify({'data': data}) 
@app.route('/status/<trainnum>/<day>',methods = ['GET'])
def check(trainnum,day):
   print(day)
   today = date.today() 
   yesterday = today - timedelta(days = 1) 
   if(day == "today"):
      url = 'https://www.confirmtkt.com/train-running-status/'+trainnum+'&Date='+str(today)
   else:
      url = 'https://www.confirmtkt.com/train-running-status/'+trainnum+'&Date='+str(yesterday)
   r = requests.get(url)
   page_html = r.content
   finder = re.findall(r'currentStnName = .*;', page_html.decode("utf-8"))
   midvalue = finder[0].split("currentStnName = \"")[1]
   stationname = midvalue.split("\";")[0]
   stationname = stationname.strip()
   soup = BeautifulSoup(page_html,'html.parser')
   divs = soup.find_all("div", class_="row status-summary")[0]
   result = "".join(divs.strings)
   resultlist = result.splitlines()
   resultlist[1] = resultlist[1]+stationname
   print(resultlist[1])
   print(resultlist[2])
   return resultlist[1]+" "+resultlist[2]

@app.route('/status/<trainnum>', methods = ['GET']) 
def disp(trainnum): 
   url = 'https://www.confirmtkt.com/train-running-status/'+trainnum
   r = requests.get(url)
   page_html = r.content
   finder = re.findall(r'currentStnName = .*;', page_html.decode("utf-8"))
   midvalue = finder[0].split("currentStnName = \"")[1]
   stationname = midvalue.split("\";")[0]
   stationname = stationname.strip()
   soup = BeautifulSoup(page_html,'html.parser')
   divs = soup.find_all("div", class_="row status-summary")[0]
   result = "".join(divs.strings)
   resultlist = result.splitlines()
   resultlist[1] = resultlist[1]+stationname
   print(resultlist[1])
   print(resultlist[2])
   return resultlist[1]+" "+resultlist[2]
  

  
if __name__ == '__main__': 

	app.run() 
