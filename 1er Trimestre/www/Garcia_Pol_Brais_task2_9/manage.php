<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <?php
$selectedOption ="";
 if ($_SERVER["REQUEST_METHOD"] == "POST"){

    $dataSelect = array(
      "Java Programming",
      "Web design",
      "Docker administration",
      "Django framework", 
      "Mongo database"
    );
    if(empty($_POST["vName"])){
      echo "<h1>COMEBACK AND WRITE A NAME</h1>";
    }else{
    $name = test_input($_POST["vName"]);
    $dataSubject = test_input($dataSelect[$_POST["opcion"]]);
     if(empty($selectedOption)){
      echo "$name"." wants to enroll in the following subject: ".$dataSubject;
    }elseif(!empty($selectedOption)){
      echo "$name"." wants to enroll in the following subject: ".$dataSubject. " in the ".$selectedOption. " format";
    }
    ?>
     <a href="manage2.php?vName=<?php echo $name?>&vSubject=<?php echo $dataSubject ?>">Link to manage2.php</a>
     <?php
    }
  }
   function test_input($dataInput){
          $dataInput = trim($dataInput);
          $dataInput = stripslashes($dataInput);
          $dataInput = htmlspecialchars($dataInput);
          return $dataInput;
        }

    if ($_SERVER["REQUEST_METHOD"] == "GET"){
      $name = test_input($_GET["vName"]);
      $dataSubject = test_input($_GET["vSubject"]);
      $selectedOption = $_GET["classes"];
      if(empty($selectedOption)){
      echo "$name"." wants to enroll in the following subject: ".$dataSubject;
    }elseif(!empty($selectedOption)){
      echo "$name"." wants to enroll in the following subject: ".$dataSubject. " in the ".$selectedOption. " format";
    }
    ?>
     <a href="manage2.php?vName=<?php echo $name?>&vSubject=<?php echo $dataSubject ?>">Link to manage2.php</a>
    <?php
    }
  ?>
</head>
<body>
  
 
</body>
</html>