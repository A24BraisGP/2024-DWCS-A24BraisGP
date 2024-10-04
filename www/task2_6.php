<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <?php 
$beberages = array(
  "cocacola"=>["text"=>"Coca Cola","precio"=>2.1],
  "pepsicola"=>["text"=>"Pepsi Cola","precio"=>2],
  "fantanaranja"=>["text"=>"Fanta Naranja","precio"=>2.5],
  "trinamanzana"=>["text"=>"Trina Manzana","precio"=>2.3]);

  // Función para crealo select dinámico con un array multidimensional
  function imprimeBebida(array $beberages){
    ?>
    <h1> TASK 2_6 </h1>
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
    </select>;
    <?php
  }
imprimeBebida($beberages);


?>
</head>
<body>
  <!-- <form>
  <select name="opcion">
    <option value="cocacola"><?php imprimeBebida(0) ?></option>
    <option value="pepsicola"><?php imprimeBebida(1) ?></option>
    <option value="fantanaranja"><?php imprimeBebida(2) ?></option>
    <option value="trinamanzana"><?php imprimeBebida(3) ?></option>
  </select>
</form> -->
</body>
</html>


