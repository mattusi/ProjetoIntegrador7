import requests, time, threading

def updateRoute(currentStop, direction):
    payload = {'veic_id': '1', 'veic_pt': currentStop, 'veic_st': currentStop, 'api_key': 'tPmAT5Ab3j7F9'}
    r = requests.get('http://becsenac.life/api/recebe_rota.php', params=payload)
    print(r.status_code)
    myText = r.text
    print("[API RETURN]" + myText)
    if myText == "Sem rotas disponiveis":
        return []
    else:
        return myText.split(",")
    

print(updateRoute("2", 4))