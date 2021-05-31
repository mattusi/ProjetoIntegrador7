#  @Author: Ewerson_Santos
#  @Date:   2021-05-25T15:44:30-03:00
#  @Filename: trans_Dados.h
#  @Last modified by:   ewerson
#  @Last modified time: 2021-05-26T19:28:29-02:00
#  @Copyright: (c) 2021 Ewerson Santos


###  Tabela ponto  ###
# pt_id descricao
# 1     Expedição
# 2     Oficina
# 3     Almoxarifado
# 4     Usinagem

###  Tabela rota_status ###
# rstatus_id    tipo
# 1             Aguardando
# 2             Recebido
# 3             Em Rota
# 4             Concluído
# 5             Cancelado

###  Tabela plano_de_rota  ###
# prota_id    fk_partida  fk_destino      data                fk_rstatus_id
# 1           1           3           "2021-05-31 10:46:45"   2

###  Tabela veiculo  ###
# veic_id nome        fk_ponto    fk_vstatus_id
# 1       Azul        2           1
# 2       Vermelho    2           1

###  Tabela veic_status  ###
# vstatus_id  tipo
# 1           Livre
# 2           Parado
# 3           Horária
# 4           Anti-Horária
# 5           Manutenção

import requests

###### Recebe a rota >>>> envia ponto atual e estado do veiculo  >> retorno = prota_id, fk_partida e fk_chegada tabela plano_de_rota #######
print("Recebe a rota")

# envia x,y,z  x = veic_id  y = fk_ponto (ponto onde se encontra o veiculo ver Tabela ponto) z = fk_vstatus_id (estado atual do veiculo ver Tabela veic_status)
# retorno  x,y,z     x = prota_id   y = fk_partida  z = fk_chegada   se retorno = 0 sem rotas disponiveis

#   http://becsenac.life/api/recebe_rota.php?veic_id=1&veic_pt=1&veic_st=1&api_key=tPmAT5Ab3j7F9

payload = {'veic_id': '1', 'veic_pt': '2', 'veic_st': '1', 'api_key': 'tPmAT5Ab3j7F9'}
r = requests.get('http://becsenac.life/api/recebe_rota.php', params=payload)

print(r.url)
print(r.status_code)     # To print http response code  
print(r.text)            # To print response 

print("  ")

###### Atualiza o estado da rota ########
print("Atualiza o estado da rota")

# Envia x, y  onde  x = prota_id   y = fk_rstatus_id (ver tabela rota_status)
# Retorno = 1 comando execurado com sucesso     Retorno = 0 falha no envio

# http://becsenac.life/api/atualiza_status_rota.php?prota_id=1&prota_st=2&api_key=tPmAT5Ab3j7F9

payload = {'prota_id': '1', 'prota_st': '2', 'api_key': 'tPmAT5Ab3j7F9'}
r = requests.get('http://becsenac.life/api/atualiza_status_rota.php', params=payload)

print(r.url)
print(r.status_code)     # To print http response code  
print(r.text)            # To print response 



print("  ")

###### Atualiza o estado do AGV  ########
print("Atualiza o estado do AGV")

# Envia x,y,z onde x = veic_id   x = veic_id  y = fk_ponto (ponto onde se encontra o veiculo ver Tabela ponto) z = fk_vstatus_id (estado atual do veiculo ver Tabela veic_status)
# Retorno = 1 comando execurado com sucesso     Retorno = 0 falha no envio

# http://becsenac.life/api/atualiza_status_veiculo.php?veic_id=1&veic_pt=2&veic_st=1&api_key=tPmAT5Ab3j7F9


payload = {'veic_id': '1', 'veic_pt': '2', 'veic_st': '1', 'api_key': 'tPmAT5Ab3j7F9'}
r = requests.get('http://becsenac.life/api/atualiza_status_rota.php', params=payload)

print(r.url)
print(r.status_code)     # To print http response code  
print(r.text)            # To print response 

