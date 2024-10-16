<?php 
  // Tries to iniciate session
  session_start();
  if(!isset($_SESSION['user'])){
    header("Location: login_user.php?redirected=true");
  }

    function test_input($data) {
	  $data = trim($data);
	  $data = stripslashes($data);
	  $data = htmlspecialchars($data);
	  return $data;
  }

  // Once the data is sent, it is attributed to the adecuate session variables 
  if($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST["formPerso"])){
    $_SESSION["hpUser"] = 50;
    //I get the string of value of the select
    $_SESSION["weapon"] = test_input($_POST["vWeapon"]);
    $weapon= test_input($_POST["vWeapon"]);
    $_SESSION["damageDealt"] = 0;

  }
  
  if($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST["formStats"])){
    $_SESSION["strength"] = test_input($_POST["Strength"]);
    $_SESSION["defense"] =  test_input($_POST["Defense"]);
    $_SESSION["evasion"] =  test_input($_POST["Evasion"]); 
  }

  // Series of methods that determine the maximum and minimun value of each variable depending on the outcome of the select["vWeapon"]
  function check_weapon_max_str($weapon){
    $max = 0;
    switch($weapon){
      case "Magic":
        $max = 14;
        break;
      case "Sword";
        $max = 18;
        break;
      default:
        $max = 16;
        break;  
    }
    return $max;
  }

  function check_weapon_min_str($weapon){
    $min = 0;
    switch($weapon){
      case "Magic":
        $min = 8;
        break;
      case "Sword";
        $min = 12;
        break;
      default:
        $min = 10;
        break;  
    }
    return $min;
  }

  function check_weapon_max_def($weapon){
    $max = 0;
    switch($weapon){
      case "Magic":
        $max = 18;
        break;
      case "Sword";
        $max = 16;
        break;
      default:
        $max = 14;
        break;  
    }
    return $max;
  }

  function check_weapon_min_def($weapon){
    $min = 0;
    switch($weapon){
      case "Magic":
        $min = 8;
        break;
      case "Sword";
        $min = 10;
        break;
      default:
        $min = 10;
        break;  
    }
    return $min;
  }

  function check_weapon_max_ev($weapon){
    $max = 0;
    switch($weapon){
      case "Magic":
        $max = 12;
        break;
      case "Sword";
        $max = 12;
        break;
      default:
        $max = 16;
        break;  
    }
    return $max;
  }

  function check_weapon_min_ev($weapon){
   $min = 0;
    switch($weapon){
      case "Magic":
        $min = 6;
        break;
      case "Sword";
        $min = 6;
        break;
      default:
        $min = 10;
        break;  
    }
    return $min;
  }
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <?php 
  include 'header.php';
  include 'footer.php';
  ?>
  <aside id="formLeft">
    <table>
    <tbody>
  <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"])?>" method="POST" name="personalisation">
    <th>CHARACTER PERSONALISATION</th>
    <tr>
      <td> Name:</td>
      <td><?php echo $_SESSION["user"]?></td>
     </tr>
  <tr>
    <td>
      Weapon:
    </td>
    <td>
      <select class="selectInput" type="text" name="vWeapon">
        <option value="Sword" name="vSword"  <?php if(isset($weapon) && $weapon ==  "Sword") echo "selected"?>>Sword</option>
        <option value="Magic" name="vMagic" <?php if(isset($weapon) && $weapon ==  "Magic") echo "selected"?>>Magic</option>
        <option value="Fist" name="vFist" <?php if(isset($weapon) && $weapon ==  "Fist") echo "selected"?>>Fist</option>
    </td>
  </tr>
   <tr>
       <td>
<input class="submitInput" type="submit" value="Proceed to stats" name="formPerso">

       </td>  
     </tr>
</form>
  </tbody>
    </table>

</aside>
  <br>
  <!-- Once the weapon is set, that is, some information has been sent, the following form is displayed -->
  <?php if (isset($weapon)) {
    ?>
<aside id="formRight">
    <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"])?>" method="POST">
    <table>
    <th>CHARACTER STATISTICS</th>
    <tbody>
      <tr>
        <td>Strength: </td>
        <td><input type="number" name="Strength" value="<?php if(isset($weapon)) echo check_weapon_min_str($weapon)?>" max=<?php if(isset($weapon))echo check_weapon_max_str($weapon)?> min="<?php if(isset($weapon))echo check_weapon_min_str($weapon)?>"></td>
      </tr>
      <tr>
        <td>Defense:</td>
        <td><input type="number" name="Defense" value="<?php if(isset($weapon)) echo check_weapon_min_def($weapon)?>" max=<?php if(isset($weapon))echo check_weapon_max_def($weapon)?> min="<?php if(isset($weapon))echo check_weapon_min_def($weapon)?>"></td>
      </tr>
      <tr>
        <td>Evasion:</td>
        <td> <input type="number" name="Evasion" value="<?php if(isset($weapon)) echo check_weapon_min_ev($weapon)?>" max=<?php if(isset($weapon))echo check_weapon_max_ev($weapon)?> min="<?php if(isset($weapon))echo check_weapon_min_ev($weapon)?>"></td>
      </tr> 
      <tr>
       <td>
          <input class="submitInput" type="submit" value="Let's Roll!" name="formStats">

       </td>  
     </tr>
  </form>
  </tbody>
  </table>
</aside>  
<?php
}
 // Once the second form is sent, a link to the roll page is displayed, asking before hand if all data is correct
 if($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST["formStats"])){
  ?>
  <table id="tableStats">
    <th>Your stats:</th>
<tr>
  <td>
    Strength:
    <?php echo $_SESSION["strength"]. "<br>" ?>
  </td>
</tr>
<tr>
  <td>
    Defense: 
    <?php echo $_SESSION["defense"]. "<br>" ?>
  </td>
</tr>
<tr>
  <td>
    Evasion: 
    <?php echo $_SESSION["evasion"]. "<br>" ?>
  </td>
</tr>
<tr>
  <td>
    Weapon: 
    <?php echo $_SESSION["weapon"]. "<br>" ?>
  </td>
</tr>
  </table>
  <div id="rollAnchor"><a href="roll_dice.php">Roll the die</a></div>
  <?php
 }
?>
</body>
</html>