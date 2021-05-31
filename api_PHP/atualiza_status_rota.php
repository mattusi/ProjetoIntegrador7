<?php
    include "conexao.php"; 

    $s1_rec = $_GET['prota_id'];

    $s2_rec = $_GET['prota_st'];   

    $api_key= $_GET['api_key'];

    // http://becsenac.life/api/atualiza_status_rota.php?prota_id=1&prota_st=2&api_key=tPmAT5Ab3j7F9

    if( $api_key =='tPmAT5Ab3j7F9'){ 

        $SQL_UPDATE = "UPDATE plano_de_rota SET fk_rstatus_id='$s2_rec' WHERE prota_id='$s1_rec'";    

        $stmt = $conexao->prepare($SQL_UPDATE);    

        $stmt->bindParam(":prota_id", $s1_rec);

        $stmt->bindParam(":fk_rstatus_id", $s2_rec);    

        if($stmt->execute()) {    

            echo "1"; // salvo_com_sucesso

        } else {    

            echo "0";  // erro_ao_salvar 

        }
    }else{
        echo "API key incorreto!";
   }     

?>