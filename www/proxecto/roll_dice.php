<?php 
  session_start();
  if(!isset($_SESSION['user'])){
    header("Location: login_user.php?redirected=true");
  }
  echo "name: ".$_SESSION["name"];
  echo "race: ".$_SESSION["race"];
  echo "weapon: ".$_SESSION["weapon"]."<br>";
  echo "str: ".$_SESSION["strenght"];
  echo "defense: ".$_SESSION["defense"];
  echo "evasion: ".$_SESSION["evasion"];
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