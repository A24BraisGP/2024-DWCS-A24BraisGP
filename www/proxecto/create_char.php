<?php 
  session_start();
  if(!isset($_SESSION['user'])){
    header("Location: login_user.php?redirected=true");
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
  <?php echo $_SESSION['user']?>
  <aside id="formLeft">
  <form action="" method="POST" name="personalisation">
  Name:<input type="text" name="vName" placeholder="Name"><br>
  Race:<input type="text" name="vRace" placeholder="Race"><br>
  Class:<input type="text" name="vClass" placeholder="Class"><br>
  Weapon:
  <select type="text" name="vWeapon">
    <option value="Sword" name="vSword">Sword</option>
    <option value="Magic" name="vMagic">Magic</option>
    <option value="Fist" name="vFist">Fist</option>
  </form>
  </aside>
  <br>
  <aside id="formRigth">
  <form action="" method="POST" name="statistics">
    <input type="number" name="Strenght" max=<?php if(isset($weapon))echo check_weapon_max($weapon)?> min="<?php if(isset($weapon))echo check_weapon_min($weapon)?>" >

    <input type="number" name="Defense" max=<?php if(isset($weapon))echo check_weapon_max($weapon)?> min="<?php if(isset($weapon))echo check_weapon_min($weapon)?>">
    
    <input type="number" name="Evasion" max=<?php if(isset($weapon))echo check_weapon_max($weapon)?> min="<?php if(isset($weapon))echo check_weapon_min($weapon)?>">
  </form>
  </aside>
</body>
</html>