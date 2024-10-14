<?php 
  // Checks if the input is adecuate and if so, initialices a session and redirects to the php page create_char
  $userErr = "";
  if($_SERVER["REQUEST_METHOD"] == "POST"){
    $logErr=false;
    $clearLogin = false;
    $user = test_input($_POST["user"]);
    if(empty($user)){
      $userErr = "User data empty";
    }
    $password = test_input($_POST["passw"]);
    $clearLogin= check_user($user,$password);
    if($clearLogin == false){
      $logErr = true;
      $user = $_POST["user"];
    } else {
      session_start();
      $_SESSION["user"] = $user;
      header("Location: create_char.php");
    }
  }
  function test_input($data) {
	  $data = trim($data);
	  $data = stripslashes($data);
	  $data = htmlspecialchars($data);
	  return $data;
  }

  
  // Checks if the input coincides with the data necesary to start a session
  function check_user($user,$password){
    if($user === "Blath" && $password === "123"){
      $clearLogin['name']= "Blath";
      return $clearLogin;
    } else {
    return false;
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
  <?php
    // Includes Header. Checks if the user was redirected from any other page (because the session_start() failed) 
    include 'header.php'; 
    if(isset($_GET["redirected"])){
      echo "<h2>Please introduce login to proceed</h2>";
    }
    if(isset($logErr) && $logErr == true){
      echo "<h2>Please check you data</h2>";
    }
  ?>  


  <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>" method="POST">

  User: <input id="user" name="user" type="text" value="<?php 
  if(isset($user)) echo $user;?>">
  <br>
  <?php echo $userErr?>
  <br>
  Password:
  <input type="password" name="passw" id="passw">

  <br>

  <input type="submit" name="sendLogin" value="Login">

  </form>
</body>
</html>