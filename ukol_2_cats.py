import requests
import json
from pprint import pprint 

response = requests.get("https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=10")
data = response.json()

seznam=[]

for i in range(0,10):
    veta=(data[i]["text"])
    seznam.append(f"{i+1}.{veta}")

pprint(data)
print(seznam)

with open('cats_1.json', mode='w',encoding='utf-8') as file:
    json.dump(seznam,file,indent=4,ensure_ascii=False)
    

try:
    response = requests.get("https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=10",timeout=0.001)
    data = response.json()
except requests.Timeout:
    print("Jsi velmi nedočkavá.")
