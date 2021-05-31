<?php
    include "conexao.php"; 

    $s1_rec = $_GET['veic_id'];

    $s2_rec = $_GET['veic_pt'];
    
    $s3_rec = $_GET['veic_st'];    

    $api_key= $_GET['api_key'];

        // /atualiza_status_veiculo.php?veic_id="+veic_id+"&fk_vstatus_id="+String(fk_vstatus_id)+"&api_key="+apiKeyValue+ "

        // http://becsenac.life/api/atualiza_status_veiculo.php?veic_id=1&fk_ponto=2&fk_vstatus_id=1&api_key=tPmAT5Ab3j7F9   

    if( $api_key =='tPmAT5Ab3j7F9'){ 

        $SQL_UPDATE = "UPDATE veiculo SET fk_ponto= '$s2_rec', fk_vstatus_id = '$s3_rec' WHERE veic_id =  '$s1_rec'";    

        $stmt = $conexao->prepare($SQL_UPDATE);   

        $stmt->bindParam(":veic_id", $s1_rec);

        $stmt->bindParam(":fk_ponto", $s2_rec);

        $stmt->bindParam(":fk_vstatus_id", $s3_rec);    

        if($stmt->execute()) {    

            echo "1"; // salvo_com_sucesso

        } else {    

            echo "0";   // erro_ao_salvar

        }
    }else{
        echo "API key incorreto!";
   }     

?>