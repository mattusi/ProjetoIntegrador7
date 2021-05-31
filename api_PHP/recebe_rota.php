<?php
    include "conexao.php"; 

    $s1_rec = $_GET['veic_id'];

    $s2_rec = $_GET['veic_pt'];

    $s3_rec = $_GET['veic_st'];

    $api_key = $_GET['api_key'];

    // http://becsenac.life/api/recebe_rota.php?veic_id=1&veic_pt=1&veic_st=1&api_key=tPmAT5Ab3j7F9

    if( $api_key =='tPmAT5Ab3j7F9'){ 
        $result = $conexao->query("SELECT recebe_rota('$s1_rec','$s2_rec','$s3_rec') as recebe");
        $row = $result->fetch();

        $resultado = $row['recebe'];

        if ($resultado > 0 ){
                echo "$resultado";

        }else{
            echo "0"; // Sem rotas disponiveis
        }

    }else{
        echo "API key incorreto!";
   } 

?>