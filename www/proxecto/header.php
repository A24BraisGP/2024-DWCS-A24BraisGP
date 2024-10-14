<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header>
    <!-- Navegation menu included to travel throught the pages 
    If the session is started, it can show a redirect to create char.php-->
    <img id="orangeDice" src="images/casino_40dp_F19E39_FILL0_wght400_GRAD0_opsz40.svg" alt="orange dice">
    <a href="index_proxecto.php">Go to index</a>
    <?php if(isset($_SESSION["user"])){
      ?>
     <a href="create_char.php">Create Character</a>
      <?php
    } ?>
    <a href="logout.php">Logout</a>
    <img id="whiteDice" src="images/casino_40dp_FDF3D0_FILL0_wght400_GRAD0_opsz40.svg" alt="white dice">
  </header>
</body>
</html>