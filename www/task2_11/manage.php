<?php
  $dataSelect = array(
      "Java Programming",
      "Web design",
      "Docker administration",
      "Django framework", 
      "Mongo database"
    );
$selectedOption ="";
 if ($_SERVER["REQUEST_METHOD"] == "POST"){
   $cookie_subject=$dataSelect[$_POST["opcion"]];
   $cookie_name=$_POST["vName"];
   setcookie($cookie_name,$cookie_subject,time() + (86400 * 30), "/" );
    if(empty($_COOKIE[$cookie_name])){
      echo "<h1>COMEBACK AND WRITE A NAME</h1>";
    }else{
    $name = test_input($cookie_name);
    $dataSubject = test_input($cookie_subject);
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
      $cookie_subject=$dataSelect[$_POST["opcion"]];
      $cookie_name=$_POST["vName"];
      setcookie($cookie_name,$cookie_subject,time() + (86400 * 30), "/" );
      $name = test_input($cookie_name);
      $dataSubject = test_input($cookie_subject);
      $selectedOption = $_GET["classes"];
      if(empty($selectedOption)){
      echo "$name"." wants to enroll in the following subject: ".$dataSubject;
    }elseif(!empty($selectedOption)){
      $cookie_n="selectedFormat";
      $cookie_value=$selectedOption;
      setcookie($cookie_n,$cookie_value,time() + (86400 * 30), "/" );
      var_dump($_COOKIE[$cookie_value]);

      echo "$name"." wants to enroll in the following subject: ".$dataSubject. " in the ".$_COOKIE[$cookie_value]. " format";
      ?>
       <a href="manage2.php?vName=<?php echo $name?>&vSubject=<?php echo $dataSubject ?>">Link to manage2.php</a>
     <?php
    }
  }
  

?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  
   
</head>
<body>
  
 
</body>
</html>