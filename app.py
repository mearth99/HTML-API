from unicodedata import category
from flask import Flask, render_template, request
import requests, random, json

url = "https://master-gpt2-everytime-fpem123.endpoint.ainize.ai/everytime/fix-length"

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/',methods = ['POST','GET'])
def result():
     if request.method == 'POST':
        result = request.form
        text = result["Name"]
        category = result["Select"]
        qurl_num = int(result["Number"])
        data = {
            "text": text, 
            "category": category,
            "length": 10
        }
        if(qurl_num>10):
            qurl_num=10
        sum = []
        for i in range(0,qurl_num):
            data["length"] = random.randrange(10,30)
            response = requests.post(url, data=data)
# print res if the request is successful
            if response.status_code == 200:
                res = response.json()
                output = res["0"]
                sum.append(str(i)+". " + output)
            else:
                print("Failed requests")
        return render_template("result.html",result = sum)



if __name__ == '__main__':
    app.run(debug=True)

