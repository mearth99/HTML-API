import requests

url = "https://main-gpt2-large-jeong-hyun-su.endpoint.ainize.ai/gpt2-large/long"

data = {
    "text": "i want to go intern", 
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