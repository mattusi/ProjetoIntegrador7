#  @Author: Ewerson_Santos
#  @Date:   2021-05-25T15:44:30-03:00
#  @Filename: trans_Dados.h
#  @Last modified by:   ewerson
#  @Last modified time: 2021-05-26T19:28:29-02:00
#  @Copyright: (c) 2021 Ewerson Santos

import requests

###### Recebe as rotas >>>> envia ponto atual e estado do veiculo  >> retorno = prota_id, fk_partida e fk_chegada tabela plano_de_rota #######
print("Recebe as rota")


#   http://becsenac.life/api/recebe_rota.php?veic_id=1&veic_pt=1&veic_st=1&api_key=tPmAT5Ab3j7F9

payload = {'veic_id': '1', 'veic_pt': '2', 'veic_st': '1', 'api_key': 'tPmAT5Ab3j7F9'}
r = requests.get('http://becsenac.life/api/recebe_rota.php', params=payload)

print(r.url)
print(r.status_code)     # To print http response code  
print(r.text)            # To print response 


print("  ")

###### Atualiza o estado da rota ########
print("Atualiza o estado da rota")


# http://becsenac.life/api/atualiza_status_rota.php?prota_id=1&prota_st=2&api_key=tPmAT5Ab3j7F9


payload = {'prota_id': '1', 'prota_st': '2', 'api_key': 'tPmAT5Ab3j7F9'}
r = requests.get('http://becsenac.life/api/atualiza_status_rota.php', params=payload)

print(r.url)
print(r.status_code)     # To print http response code  
print(r.text)            # To print response 


print("  ")

###### Atualiza o estado do AGV  ########
print("Atualiza o estado do AGV")


# http://becsenac.life/api/atualiza_status_veiculo.php?veic_id=1&veic_pt=2&veic_st=1&api_key=tPmAT5Ab3j7F9


payload = {'veic_id': '1', 'veic_pt': '2', 'veic_st': '1', 'api_key': 'tPmAT5Ab3j7F9'}
r = requests.get('http://becsenac.life/api/atualiza_status_rota.php', params=payload)

print(r.url)
print(r.status_code)     # To print http response code  
print(r.text)            # To print response 