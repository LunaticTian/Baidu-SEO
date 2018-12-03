from flask import Flask,request
import requests

app = Flask(__name__)

listurl = ""

def baidu():
    for i in range(1500):
        
        r = requests.post(url='http://data.zz.baidu.com/urls?site=www.lunatic.wang&token=xxxxxxx',data=listurl)
        print(r.text)
        print(listurl)

@app.route('/getsitemap',methods=['POST'])
def getsitemap():
    global listurl
    list = request.json['url']
    listurl = list
    baidu()
    print(list)
    return 'ok'
    


if __name__ == '__main__':

    app.run(debug=True,host='0.0.0.0',port=9090)


