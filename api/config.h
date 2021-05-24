/**
 * @Author: Ewerson_Santos
 * @Date:   2021-04-15T17:34:37-03:00
 * @Filename: config.h
 * @Last modified by:   ewerson
 * @Last modified time: 2021-05-20T10:21:16-02:00
 * @Copyright: (c) 2021 Ewerson Santos
 */
#ifndef config_h
#define config_h

// INCLUDES

#include <HTTPClient.h>


// DADOS UPLOAD
// Mantenha este valor de chave de API para ser compatível com o código PHP fornecido na página do projeto.
// Se você alterar o valor de apiKeyValue, o arquivo PHP /post-esp-data.php também precisa ter a mesma chave
String apiKeyValue = "tPmAT5Ab3j7F9";

//#define httpPort 80
String host = "http://becsenac.life/api";

// Variaveis Globais

String veic_id = "1"; // Define o ID do Veiculo no DB.

String veic_pt = "2"; // Ponto que o veiculo está ou passou

String veic_st = "2"; // Status do veiculo

String prota_id = "2"; // ID do plano de rota em curso

String prota_st = "2"; // Status da rota

#endif