<?php declare(strict_types=1);
 function naming(?String $name,int $age, String $surname = "Apelido"): void{
      echo "<b>" . $name . "  ".$surname."</b> is <b>".$age."</b> years old";
      echo "<br/>";
 }
?>
<!DOCTYPE html>
<html lang="en">
<head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Task 2_4</title>
</head>
<body>
<div class="container-fluid">
        <?php
            echo "<h2>Naming Function</h2>";
            naming("Brais", 25, "Garcia");
            naming(null, 25);
            naming("Brais", 3);
        ?>
    </div>
</body>
</html>