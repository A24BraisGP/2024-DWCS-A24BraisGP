<html>
<body>
<?php 
  $name = $email = "";

  if ($_SERVER["REQUEST_METHOD"] == "GET"){
    $name = test_input($_GET["vNome"]);
    $email = test_input($_GET["vEmail"]);
  }

  function test_input($data){
    $data= trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
  }
?>

Welcome <?php echo $name; ?><br>
Your email address is: <?php echo $email; ?>
<br>

</body>
</html>
