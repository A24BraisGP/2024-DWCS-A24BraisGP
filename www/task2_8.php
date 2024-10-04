<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <?php 

    //Función que garante seguridade no input ao formatear o texto 

    function test_input($data){
      $data = trim($data);
      $data = stripslashes($data);
      $data = htmlspecialchars($data);
      return $data;
    }

    // Declaramos as variables que imos empregar como vacías para comprobar se seguen vacías ou teñen contido

    $vUser = $vPass = $vServer = $vCity = $vSignon = $vRole = "";
    $userErr = $passErr = $cityErr = "";

    // Comprobación de se algún submit foi feito sobre o post

    if ($_SERVER["REQUEST_METHOD"] == "POST"){

      //Se o datos pertinentes están vacíos, cambíase o contido da variable que usamos como comprobante de erro para mostrala logo. No caso do radio e checkbox usei un titular auxiliar

      if(empty($_POST["vRole"])){
        echo "<h2> YOU GOTTA GIME A ROLE</h2>";
      } else{
        $vRole = $_POST["vRole"];
      }
      if(empty($_POST["vUser"])){
        $userErr = "YOU've gotta give me an user man";
      } else{
         $vUser = test_input($_POST["vUser"]);
         if (!preg_match("/^[a-zA-Z-' ]*$/",$vUser)) {
      $userErr = "Only letters and white space allowed";
    }
      }
      if(empty($_POST["vPass"])){
        $passErr = "YOU've gotta give me a pass man";
      } else{
         $vPass = test_input($_POST["vPass"]);
      }
      if(empty($_POST["vCity"])){
        $userErr = "YOU've gotta give me a city man";
      } else{
         $vCity = test_input($_POST["vCity"]);
          if (!preg_match("/^[a-zA-Z-' ]*$/",$vCity)) {
      $cityErr = "Only letters and white space allowed";
    }
      }

      // Como o checkbox é de selección múltiple, cada entrada ten o seu propio nome e asignación, temos que comprobar se teñen valor antes de facer a asignación. Como o select está limitado ao código hardcoded non temos que facer comprobacións extras.

      $vServer = $_POST["vServer"];
      echo "<h1> ".$vServer." </h1>";
      if(isset($_POST["vSignon1"])){
        $vSignon1 = $_POST["vSignon1"];
      }
      if(isset($_POST["vSignon2"])){
        $vSignon2 = $_POST["vSignon2"];
      }
      if(isset($_POST["vSignon3"])){
        $vSignon3 = $_POST["vSignon3"];
      }
    }

  ?>
</head>
<body>
  <h3>Novell Services Login</h3> 
  <br>

    <!-- Comezamos co etiquetado do formulario, como acción invocamos á mesma páxina co código php $_SERVER["PHP_SELF"], como method, POST-->

    <form action ="<?php
     echo htmlspecialchars($_SERVER["PHP_SELF"]); 
     ?>" method="POST">

    <!-- Pedimos os inputs en tipo texto, para os cales dámoslle o valor cun código php da variable que actualizamos arriba despois do primeiro input, durante o primeiro input non teñen valor xa que a inicializamos en branco.
    Ademais, dentro do span situamos outro código php co echo sobre a variable do erro pertinente, que de non inializarse será, tamén, branco. -->

      Username: <input type="text" name="vUser"
      value="<?php echo $vUser ; ?>">
      <span style="color: red"><?php echo $userErr ?></span>
      <br>

      Password: <input type="text" name="vPass" 
      value="<?php echo $vPass ; ?>">
      <span style="color: red"><?php echo $passErr ?></span>
      <br>

      City of Employment: <input type="text" name="vCity" 
      value="<?php echo $vCity ; ?>">
      <span style="color: red"><?php echo $cityErr ?></span> 
      <br>

      <!-- Exemplo de select, no seu caso comprobamos con php se foi actualizada a variable e, de selo, se ten o valor exacto da posición que queremos seleccionar, de ser así, introducimos a etiqueta "selected" no html mediante o código php echo "selected"  -->

      Web server: <select name="vServer">

        <option value="europe" 
          <?php if 
          (isset($vServer) && $vServer=="europe") echo "selected"; 
        ?>>Europe</option>

       <option value="canada"
          <?php if 
          (isset($vServer) && $vServer=="canada") echo "selected"; 
        ?>>Canada</option>

        <option value="asia"
          <?php if 
          (isset($vServer) && $vServer=="asia") echo "selected"; 
        ?>>Asia</option>
      </select>
    <br>

    <!-- Pasamos a realizalo input radio, semellante ao select anterior pero co atributo checked en vez de selected inxectado polo código php. Como solo un pode ser seleccionado de cada vez é imperativo comprobar a exactitude do valor -->
     <label for="idvRole">Please specify your role:</label> 
      <input id="idvRole" type="radio" name="vRole" 
      <?php if (isset($vRole) && $vRole=="admin") echo "checked"; ?> value="admin"> Admin

      <input type="radio" name="vRole" 
      <?php if (isset($vRole) && $vRole=="engineer") echo "checked"; ?> value="engineer"> Engineer

      <input type="radio" name="vRole" 
      <?php if (isset($vRole) && $vRole=="manager") echo "checked"; ?> value="manager"> Manager

      <input type="radio" name="vRole" 
      <?php if (isset($vRole) && $vRole=="guest") echo "checked"; ?> value="guest"> Guest
      <br>


    <!-- Por último, pasamos ao checkbox. Como poden estar varios seleccionados cada un ten o seu nome independiente, ademais, refiren a unha variable propia que simplemente comprobamos se está ou non activa, de estalo, chekeamos a caixa co php echo "checked" inxectado no html. -->

    
    <label for="idSingon">Single Sign-on to the Following: </label>
      <input id="idSingon" type="checkbox" name="vSignon1" value="mail" 
      <?php if (isset($vSignon1)) echo "checked"; ?> 
      > Mail

      <input type="checkbox" name="vSignon2" value="payroll" 
      <?php if (isset($vSignon2)) echo "checked"; ?> 
      > Payroll

      <input type="checkbox" name="vSignon3" value="self" 
      <?php if (isset($vSignon3)) echo "checked"; ?> 
      > Self-service

    <br>

    <label><input type="submit" value="LOGIN"></label>

    <!-- Reset restaura los contenidos de un formulario a sus valores predeterminados -->
    <label><input type="reset" value="RESET" name="vReset"></label> 

  </form>
</body>
</html>