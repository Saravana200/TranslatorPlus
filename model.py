import requests
import json


#mistral model is running locally on machine using ollama 
async def prompt(sentence):
    model = "mistral-openorca"
    res=""
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    data = json.dumps({"model": model, "prompt": sentence})
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        for line in response.text.splitlines():
            data = json.loads(line)
            res=res+data["response"]
        return res
    else:
        print("Error:", response.status_code, response.text)
        return ""