<?php
function tripleCheck(array $numbers){
      $count = 0; //Count the number of times in a row
      $check = false;
      $anterior ="";
      foreach($numbers as $comp){
            if($comp == $anterior){
                  $count++;
            }
            else $count = 0;
            if($count == 2){
                  $check = true;
                  break;
            }
            $anterior = $comp;
      }
            echo "<br>O resultado é: ";
            return var_dump($check); 
      }     
function countries(array $ceu): void{
      foreach($ceu as $country=>$capital){
            echo "The capital of $country is $capital <br>";
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
      <div>
            <?php
      echo "<h1> Triple Check </h1>";
      tripleCheck([1, 1, 2, 2, 1] );
    
      tripleCheck([1, 1, 2, 1, 2, 3 ]);
     
      tripleCheck([1, 1, 1, 2, 2, 2, 1]);

      echo "<h1>Countries </h1>";


      countries($ceu = array( "Italy"=>"Rome", "Luxembourg"=>"Luxembourg", "Belgium"=> "Brussels", "Denmark"=>"Copenhagen", "Finland"=>"Helsinki", "France" => "Paris", "Slovakia"=>"Bratislava", "Slovenia"=>"Ljubljana", "Germany" => "Berlin", "Greece" => "Athens", "Ireland"=>"Dublin", "Netherlands"=>"Amsterdam", "Portugal"=>"Lisbon", "Spain"=>"Madrid", "Sweden"=>"Stockholm", "United Kingdom"=>"London", "Cyprus"=>"Nicosia", "Lithuania"=>"Vilnius", "Czech Republic"=>"Prague", "Estonia"=>"Tallin", "Hungary"=>"Budapest", "Latvia"=>"Riga", "Malta"=>"Valetta", "Austria" => "Vienna", "Poland"=>"Warsaw"));
      
            ?>
      </div>
</body>
</html>