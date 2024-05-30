# Tvojou úlohou bude napísať program, ktorý získa pomocou API 10 náhodných faktov o mačkách a uloží ich do súboru 
# vo formáte JSON. Použijeme API, konkrétne endpoint https://cat-fact.herokuapp.com/facts. Ako vyfiltrujeme fakty, 
# chceme si z nich vytvoriť zoznam, ktorý bude obsahovať všetky získané fakty. K reťazcom obsahujúcim fakty pridáme
# ešte ich očíslovanie, aby sme si boli istí, že ich máme presne 10.


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
    


# Náhodných faktov o mačkách nie je nikdy dosť. Preto si vypýtame ešte nejaké navyše. 
# Keďže sme nedočkaví, nastavíme si timeout na 0.001, nech ich máme čo najrýchlejšie. 
# Tu však môže nastať problém, že nám endpoint nestihne do tej doby odpovedať. 
# Vtedy by nám spadol program s výnimkou balíčku requests, ktorá sa volá Timeout. 
# Ako vieme, vyhodenie výnimky by nám zhodilo program, čo úplne nechceme. 
# Preto napíšeme túto časť kódu tak, aby nám zachytil výnimku a namiesto nej len vypísal, že sme príliš nedočkaví.


try:
    response = requests.get("https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=10",timeout=0.001)
    data = response.json()
except requests.Timeout:
    print("Jsi velmi nedočkavá.")
