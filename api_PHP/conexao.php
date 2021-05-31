<?php
//Cria as constantes com as credencias de acesso ao banco de dados
define( 'MYSQL_HOST', 'localhost' );
define( 'MYSQL_USER', 'XXXXX' );
define( 'MYSQL_PASSWORD', 'XXXXX' );
define( 'MYSQL_DB_NAME', 'XXXXXX' );

//Cria a conexão com banco de dados usando o PDO e a porta do banco de dados
//Utiliza o Try/Catch para verificar a conexão.
try
{
    $conexao = new PDO( 'mysql:host=' . MYSQL_HOST . ';dbname=' . MYSQL_DB_NAME, MYSQL_USER, MYSQL_PASSWORD );
}
catch ( PDOException $e )
{
    echo 'Erro ao conectar com o MySQL: ' . $e->getMessage();
}

?>