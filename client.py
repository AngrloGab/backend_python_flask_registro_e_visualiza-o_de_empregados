import requests

#data = {"username": "Carlos", "secret":"12345", "nome":"Marcos", "cargo":"analista","salario":4000}
#reponse = requests.post("http://127.0.0.1:5000/register",data=data)

#data = {"username": "Carlos", "secret":"12345", "info":"salario", "value":5000}
#reponse = requests.post("http://127.0.0.1:5000/informations",data=data)

reponse = requests.get("http://127.0.0.1:5000/empregados")


if reponse.status_code == 200:
    message = reponse.json()
    print(message['empregados'])
else:
    print(reponse.status_code)