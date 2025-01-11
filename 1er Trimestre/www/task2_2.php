<?php declare(strict_types=1);
      function twoint(int $base, int $exponent=2){
            $y=1;
            if ($exponent>0){
        for($x = 0; $x < $exponent; $x++){

            $y = $y * $base;
        } 
        } else echo"exponente muy bajo"; 
        return (float) $y ;
      }
?>
<html>
<head>
    <title>Task 2.2</title>
    <meta charset="utf-8">

</head>
<body>
    <div class="container-fluid">
        <?php
            echo "<h1>We'll show 5 to the power of 2 and of 3</h1>";
            try{
                echo "<h3>".twoint("pedro", 3)."</h3";
            } catch (TypeError $erro){
                echo "<p> Type Error: ".$erro->getMessage()."<p>";
            }
            echo "<h3>".twoint(5)."</h3>";
            echo "<h3>".twoint(5, 3)."</h3";
            
        ?>
    </div>
</body>
</html>