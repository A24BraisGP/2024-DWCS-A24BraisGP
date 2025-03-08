<?php declare(strict_types=1);
            function factorial(int $fact): int{
                $y=1;
                if($fact <0){
                    throw new Exception("Number is less than 0");
                    echo "Number is less than 0";
                }
                if($fact >= 0){
                for ($x = $fact;$x >1; $x--){
                    $y=$y*$x;  
                }
                }
                return (int)$y;
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
                echo "<h1>TASK 2.2</h1>";
                define("NUM", 4);
                try{
                echo "<h3>Aquí tienes el factorial de " . NUM . "  :" . factorial(NUM) . "</h3>";
                }
                catch(Exception $erro){
                    echo "O número é inválido";
                }
            ?>
        </div>
    </body>
</html>