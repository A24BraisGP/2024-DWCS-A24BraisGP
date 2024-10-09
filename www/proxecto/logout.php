<?php 
  session_start();
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
  session_unset();

  session_destroy();

  echo "<h1>You have been logged out</h1>"
?>
  <a href="index_proxecto.php">Go back to index</a>
</body>
</html>