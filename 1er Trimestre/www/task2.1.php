<html>
    <head>
        <title>Factorial Task</title>
        <meta charset="utf-8">
        <?php 
            echo "<title>Factorial of a number</title>"
        ?>
    </head>
    <body>
        <div class="container-fluid">
            <?php
                echo "<h1>TASK 2.1</h1>";
                $fact= 4;
                $y = 1;
                for ($x = $fact;$x >1; $x--){
                   $y=$y*$x;     
                  ## echo $y."<br/>";
                }
                echo "<h3>Aquí tienes el factorial de $fact: ".$y."</h3>";
            ?>
        </div>
    </body>
</html>