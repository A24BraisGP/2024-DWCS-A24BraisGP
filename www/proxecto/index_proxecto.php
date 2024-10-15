<?php 
  session_start();
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link href='https://fonts.googleapis.com/css?family=Press+Start+2P' rel='stylesheet' type='text/css'>
 <link rel="stylesheet" href="style.css">
 <link href="rpgui.css" rel="stylesheet" type="text/css" >
<script src="rpgui.js"></script>
</head>
<body>
  <main id="main-index" class="rpgui-container framed">
  <header class="rpgui-container framed">
    <h2>WELCOME TO THE SIMULATOR</h2>
  </header>

  <div class="logindiv">
    <a href="login_user.php">
      <button class="rpgui-button" type="button">
      Login
    </button>
    </a>
  </div>
  <div class="creatediv">
    <a href="create_char.php">
      <button class="rpgui-button">
     Create a Character
      </button>
    </a>
  </div>
  <div class="rolldiv">
    <a href="roll_dice.php">
     <button class="rpgui-button">
      Roll the dice
     </button>
    </a>
  </div>


<footer>
  <div class="logout">
    <a href="logout.php">
      <button class="rpgui-button">
        <em>Logout</em>
      </button>
   </a>
  </div>

</footer>
</main>
</body>
</html>