<?php
$cookie_name=$_POST["vName"];
$cookie_subject=$_POST["opcion"]["name"];
setcookie($cookie_name,$cookie_subject,time() + (86400 * 30), "/" )
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <?php
  // Array asociativo para imprimilo select 

    $dataSelect = array(
      "javaprogramming"=> ["name" => "Java Programming", "value" => 0],
      "webdesign" => ["name" => "Web design", "value"=> 1],
      "dockeradministration" => ["name" => "Docker administration", "value"=>2],
      "djangoframework"=>["name"=>"Django framework", "value"=>3],
      "mongodatabase"=>["name"=>"Mongo database","value"=>4]);

      $nameErr="";

        if(empty($_POST["vName"])){
          $nameErr = "Name is required";
        }
        else{
          $name= test_input($_POST["vName"]);
        }

     ?>
     <?php

 function test_input($dataInput){
          $dataInput = trim($dataInput);
          $dataInput = stripslashes($dataInput);
          $dataInput = htmlspecialchars($dataInput);
          return $dataInput;
        }

        // Función que imprime o select dinámico, se metemos máis valores no array vanse imprimir tm
    function imprimeSelect($data){
      ?>
   <select name="opcion">
    <?php 
      foreach($data as $claveValorSelect => $valor){
        ?>
        <option value="<?php echo $valor["value"];?>">
          <?php echo $valor["name"];?>
      </option>
      <?php
      };
   
     
    ?>
    </select>
    <?php
    }
  ?>
</head>
<body>
  <h1>First practice using forms</h1>

  <form action="manage.php" method="POST">
  <label>Name and surnames: <input type="text" name="vName" >
</label>
 <span style="color:red"><?php echo $nameErr;?></span>
  <br>
  <label>Subject to enroll:
      <?php imprimeSelect($dataSelect)?>

  </label>
  <input type="submit">
  </form>
</body>
</html>