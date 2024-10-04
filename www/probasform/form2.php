<html>
  <body>
    <?php 
    
    // Se carga por primeira vez mostramos o formulario, se non móstrase a información input do usuario. O if chequea se hai un request con post (unha vez se fixo o submit) mostra o formulario, se non, pasa ao seguinte.


  if ($_SERVER["REQUEST_METHOD"] == "POST"){
    $nameErr=$emailErr="";
    $name = $email = "";
    // Estes if determinan se os campos están baleiros e actualizan os erros para mostralos, se teñen contido actualizan a variable pertinente co valor do input para mostrala e gardala posteriormente 
    if(empty($_POST["vNome"])){
      $nameErr = "Dame o nome mentireiro";
    }else{
      $name = test_input($_POST["vNome"]);
      if (!preg_match("/^[a-zA-Z-' ]*$/",$name)){
        $name ="";
        $nameErr = "Que nombre más raro pon uno normal";
      }
    }

    if(empty($_POST["vEmail"])){
      $emailErr = "Dame o email mentireiro";
    }else{
      $email = test_input($_POST["vEmail"]);
    }
    
  } 
  
  // Quitamoslle o else ao form de tal xeito que se cargue na segunda volta para mostrar a obligación ou non dos campos. 
?>
  
  <h1>EL FORM: </h1>
  <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>" method="POST">

      Name: <input type="text" name="vNome"/>

<!-- Este span faise co obxectivo de mostralo erro de que faltan datos requeridos, isto é, mostra o valor de nameErr, que se é vacío (pasou o check) non é nada, se non pasou o check mostra o valor que lle dimos antes (Erro de requerimento). Sempre mostra o asterisco para dara entender que é requerida -->

      <span style="color: red">*<?php echo $nameErr;?></span>
      <br />
      E-mail: <input type="text" name="vEmail"/>
      <span style="color: red">*<?php echo $emailErr;?></span>
      <br />
      <input type="submit" />
    </form>
<?php   

  // chequeamos se ambas variables de datos están actualizadas, é decir, se superaron o check anterior e polo tanto teñen data, de non ser así indicamolo erro. De ser así, permitimos o paso seguinte, mostralos datos finais.

      if($email!="" && $name!=""){
      echo  "<h1>EL OUTPUT</h1>";
      echo "Welcome ". $name."<br>";
      echo $email;
      }else echo "<h1> Falta data aa a </h1>";

?>
 

<?php
  function test_input($data){
    $data= trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
  }
?>
  </body>
</html>