import requests,re
from bs4 import BeautifulSoup
from flask import Flask, jsonify, request 
from requests_html import HTMLSession
app = Flask(__name__) 
@app.route('/', methods = ['GET', 'POST']) 
def home(): 
    if(request.method == 'GET'): 
  
        data = "hello world"
        return jsonify({'data': data}) 
@app.route('/check',methods = ['GET'])
def check():
   url = 'https://www.confirmtkt.com/train-running-status/01093'
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
