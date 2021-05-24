/**
 * @Author: Ewerson_Santos
 * @Date:   2021-04-13T12:33:40-02:00
 * @Filename: trans_Dados.h
 * @Last modified by:   ewerson
 * @Last modified time: 2021-04-27T11:31:29-02:00
 * @Copyright: (c) 2021 Ewerson Santos
 */

#ifndef trans_dados_h
#define trans_dados_h

#include "config.h"
#define RETRY_LIMIT 2

void atualiza_Status_Rota() {

    if(WiFi.status()== WL_CONNECTED){

      HTTPClient http;

      //Serial.print("[HTTP] begin...\n");

     http.begin(host+"/atualiza_status_rota.php?prota_id="+prota_id+"&fk_rstatus_id="+prota_st+"&api_key="+apiKeyValue+""); // http://becsenac.life/api/atualiza_status_rota.php?prota_id=1&fk_rstatus_id=2&api_key=tPmAT5Ab3j7F9

      Serial.print("[HTTP] GET...\n");
      // iniciar conexão e enviar cabeçalho HTTP
      int httpCode = http.GET();
 
      // httpCode será negativo em caso de erro
      if(httpCode > 0) {
          // O cabeçalho HTTP foi enviado e o cabeçalho de resposta do servidor foi tratado
          //Serial.printf("[HTTP] GET... code: %d\n", httpCode);

          // arquivo encontrado no servidor
          if(httpCode == HTTP_CODE_OK) {
              String payload = http.getString();
              //Serial.print("R. atualiza_Status: ");
              //Serial.println(payload);
          }
      } else {
          //Serial.printf("[HTTP] GET... falha, erro: %s\n", http.errorToString(httpCode).c_str());
      }
    }
}

void atualiza_Status_Veiculo() {

    if(WiFi.status()== WL_CONNECTED){

      HTTPClient http;

      //Serial.print("[HTTP] begin...\n");

     http.begin(host+"/atualiza_status_veiculo.php?veic_id="+veic_id+"&fk_ponto="+veic_pt+"&fk_vstatus_id="+veic_st+"&api_key="+apiKeyValue+""); // http://becsenac.life/api/atualiza_status_veiculo.php?veic_id=1&fk_ponto=2&fk_vstatus_id=1&api_key=tPmAT5Ab3j7F9

      Serial.print("[HTTP] GET...\n");
      // iniciar conexão e enviar cabeçalho HTTP
      int httpCode = http.GET();
 
      // httpCode será negativo em caso de erro
      if(httpCode > 0) {
          // O cabeçalho HTTP foi enviado e o cabeçalho de resposta do servidor foi tratado
          //Serial.printf("[HTTP] GET... code: %d\n", httpCode);

          // arquivo encontrado no servidor
          if(httpCode == HTTP_CODE_OK) {
              String payload = http.getString();
              //Serial.print("R. atualiza_Status: ");
              //Serial.println(payload);
          }
      } else {
          //Serial.printf("[HTTP] GET... falha, erro: %s\n", http.errorToString(httpCode).c_str());
      }
    }
}


void recebe_Rota() {

    if(WiFi.status()== WL_CONNECTED){

      HTTPClient http;

      //Serial.print("[HTTP] begin...\n");

     http.begin(host+"/recebe_rota.php?veic_id="+veic_id+"&veic_pt="+veic_pt+"&veic_st="+veic_st+"&api_key="+apiKeyValue+ ""); // http://becsenac.life/api/recebe_rota.php?veic_id=1&veic_pt=1&veic_st=1&api_key=tPmAT5Ab3j7F9 

      //Serial.print("[HTTP] GET...\n");
      // iniciar conexão e enviar cabeçalho HTTP
      int httpCode = http.GET(); 
      // httpCode será negativo em caso de erro
      if(httpCode > 0) {
          // O cabeçalho HTTP foi enviado e o cabeçalho de resposta do servidor foi tratado
          //Serial.printf("[HTTP] GET... code: %d\n", httpCode);
          // arquivo encontrado no servidor
          if(httpCode == HTTP_CODE_OK) {
              String payload = http.getString();
              //Serial.print("R. recebe_Rota: ");
              //Serial.println(payload);

            int retorno = payload.toInt();    
            //Serial.println(retorno);        

            int digit[4]={}; 
            int v1 = retorno;
            for (int i = 0; i < 4; i++)
            {
                int d = v1 % 10;
                v1 /= 10;
                digit[i]=d;                   
            } 
            //int s1 =  digit[3];
            int s2 =  digit[2];
            int s3 =  digit[1];
            int s4 =  digit[0];

            //Serial.print(s1);
            //Serial.print(s2);
            //Serial.print(s3);
            //Serial.println(s4);            
            // s1 = status   s2 = rota_id     s3= chegada   s4 = partida

          }
      } else {
          //Serial.printf("[HTTP] GET... falhou, erro: %s\n", http.errorToString(httpCode).c_str());
      }     
    }
}
#endif