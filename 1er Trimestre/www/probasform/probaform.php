<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <form action="probaform.php" method="POST">
    Nome: <input type="text" name="nome">
    Idade: <input type="number" name="idade">
    <input type="submit">
  </form>

  Encantado:
  <?php   
    echo $_POST["nome"];
  ?>
  Tes: 
  <?php
    echo $_POST["idade"];
  ?>
</body>
</html>