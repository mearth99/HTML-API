from flask import Flask, render_template, request
import requests

url = "https://main-gpt2-large-jeong-hyun-su.endpoint.ainize.ai/gpt2-large/long"

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/',methods = ['POST','GET'])
def result():
     if request.method == 'POST':
        result = request.form
        text = result["Name"]
        data = {
            "text": text, 
            "num_samples": 5,
            "length": 10
        }
        response = requests.post(url, data=data)

# print res if the request is successful
        if response.status_code == 200:
            res = response.json()
            print(res)
        else:
            print("Failed requests")
        return render_template("result.html",result = res)
    
if __name__ == '__main__':
    app.run(debug=True)

