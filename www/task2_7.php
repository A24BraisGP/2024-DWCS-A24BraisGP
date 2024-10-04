<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <?php 
  
  // Sintaxis da declaración dun array asociativo en php

  $beberages = array(
  "cocacola"=>["text"=>"Coca Cola","precio"=>2.1],
  "pepsicola"=>["text"=>"Pepsi Cola","precio"=>2],
  "fantanaranja"=>["text"=>"Fanta Naranja","precio"=>2.5],
  "trinamanzana"=>["text"=>"Trina Manzana","precio"=>2.3]);

    //No caso de non precisalo check numérico queda este comprobante positivo: 

  // if($_SERVER["REQUEST_METHOD"] == "POST"){
  //   if(!empty($_POST["vCantidad"])&& $_POST["vCantidad"]>0){
  //     $cantidad = test_input($_POST["vCantidad"]);
  //     imprimeFinal($cantidad,$beberages[$_POST["opcion"]]);
  //   }else {
  //     echo "<h1>Si no quieres nada pírate</h1>";
  //   }
  // }

  //De ser input type text teríamos que comprobar que o input é numérico: 
  if($_SERVER["REQUEST_METHOD"] == "POST"){
    if(is_numeric($_POST["vCantidad"]) && $_POST["vCantidad"] > 0){
      $cantidad = test_input($_POST["vCantidad"]);
      imprimeFinal($cantidad,$beberages[$_POST["opcion"]]);
    } else echo "<h1> GIMMIE A NUMBERO POSITIV </h1>";
  }



  // Función para crealo select dinámico con un array asociativo
  function imprimeBebida(array $beberages){
    ?>
    
    <select name ="opcion">;
    <?php
    foreach($beberages as $claveValorSelect => $valor){
      ?>
      <option  value="<?php echo $claveValorSelect?>"> 
        <?php echo $valor["text"] ?> 
        <?php echo "(".$valor["precio"].")" ?>
      </option>;
      <?php
    };
    ?>
    </select>
    <?php
  }


function imprimeFinal($cantidad, array $data){
  $precio = floatval($data["precio"]) * floatval($cantidad);
  $nombre = $data["text"];
  echo "<h1> YOU HAVE ASKED FOR ".$cantidad." CANS OF  ".$nombre."  TOTAL PRICE TO PAY: ". $precio."  €</h1>";
}
?>

</head>
<body>
  <h1> TASK 2_7 </h1>
  <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>" method="POST">
    Produto: <?php imprimeBebida($beberages); ?>
    <br>
    Cuántas bebidas quieres: <input type="text" name="vCantidad">
  <input type="submit" >
  </form>

<?php 
  function test_input($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
  return $data;
}
?>
</body>

</html>


