<?php 
  session_start();
  if(!isset($_SESSION['user'])){
    header("Location: login_user.php?redirected=true");
  }
  $userName= $_SESSION["name"];
  $usetRace = $_SESSION["race"];
  $userWeapon = $_SESSION["weapon"];
  $userStrength = $_SESSION["strength"];
  $userDefense = $_SESSION["defense"];
  $userEvasion = $_SESSION["evasion"];
  $userHP = $_SESSION["hpUser"];
  $_SESSION["damageDealt"];

  ?>
<?php
class Enemy{
    public $eName;
    public $eWeapon;
    public $eStrength;
    public $eDefense;
    public $eEvasion;
    public $hpEnemy;

    public function __construct($eName = "", $eWeapon ="", $eStrength = 0, $eDefense = 0, $eEvasion = 0, $hpEnemy = 0){
      $this->eName = $eName;
      $this->eWeapon = $eWeapon;
      $this->eStrength = $eStrength;
      $this->eDefense = $eDefense;
      $this->eEvasion = $eEvasion;
      $this->hpEnemy = $hpEnemy;
    }

    public function get_eName(){
      return $this->eName;
    }
    public function get_eWeapon(){
      return $this->eWeapon;
    }

    public function set_eWeapon($eWeapon){
      $this->eWeapon = $eWeapon;
    }

    public function get_eStrength(){
      return $this->eStrength;
    }

    public function set_eStrength($eStrength){
      $this->eStrength = $eStrength;
    }

    public function get_eDefense(){
      return $this->eDefense;
    }

    public function set_eDefense($eDefense){
      $this->eDefense = $eDefense;
    }

    public function get_eEvasion(){
      return $this->eEvasion;
    }

    public function set_eEvasion($eEvasion){
      $this->eEvasion = $eEvasion;
    }
    
    public function get_hpEnemy(){
      return $this->hpEnemy;
    }

    public function set_hpEnemy($hpEnemy){
      $this->hpEnemy = $hpEnemy;
    }
    

    public function __toString(){
      return "<h1> Name of the enemy:  $this->eName <br> Weapon of the enemy: $this->eWeapon <br> HP of the enemy: $this->hpEnemy </h1>";
    }
    // function _constructForm(){}

  }
?>
<?php
    $enemyRat = new Enemy("Rat","",10,8,12,40);
    $enemyHuman = new Enemy("BadHuman", "",14,8,6,40);
    $enemyElf = new Enemy("BadElf", "", 12,8,8,40);
    $arrayEnemies = array(
      ["name"=>"enemyRat","object"=>$enemyRat],
      ["name"=>"enemyHuman","object"=>$enemyHuman],
      ["name"=>"enemyElf","object"=>$enemyElf]
    )

?>
<?php
  if($_SERVER["REQUEST_METHOD"] == "POST"){
    $dado = $_POST["diceRoll"];
    $mod = $_POST["mod"];
    $modEn = $_POST["modEn"];
    if(isset($_POST["advdis"])) $advdis = $_POST["advdis"];
    if(isset($_POST["advdisEn"])) $advdisEn = $_POST["advdisEn"];
    $enemySelect = $_POST["enemySelect"];
    $enemyFinal = adjustEnemy($enemySelect,$arrayEnemies);
    $enemyFinal->set_eWeapon($_POST["enemyWeaponSelect"]);
    adjustStatsEnemy($enemyFinal);
    
  } 



  function adjustEnemy($enemySelected, $arrayEnemies){
    $enemyObject = ""; 
    foreach($arrayEnemies as $enemy){
      if($enemy["name"] == $enemySelected){
        $enemyObject = $enemy["object"];
      }
    }
    return $enemyObject;
  }

  function adjustStatsEnemy($enemy){
    if($enemy->get_eWeapon()== "eFist"){
      $enemy->set_eDefense($enemy->get_eDefense()-3);
      $enemy->set_eEvasion($enemy->get_eEvasion()+3);
      $enemy->set_eStrength($enemy->get_eStrength()+1);
    } else if($enemy->get_eWeapon()== "eSword"){
      $enemy->set_eDefense($enemy->get_eDefense()+1);
      $enemy->set_eEvasion($enemy->get_eEvasion()-1);
      $enemy->set_eStrength($enemy->get_eStrength()+2);
    } else if($enemy->get_eWeapon()== "eMagic"){
      $enemy->set_eDefense($enemy->get_eDefense()-5);
      $enemy->set_eEvasion($enemy->get_eEvasion()+4);
      $enemy->set_eStrength($enemy->get_eStrength()+2);
    }
  }

?>
<?php 
  function calcRollUser($dado, $mod){
    $resultadoUser= 0;

    if(isset($_POST["advdis"])) $resultadoUser = calcAdvdis($dado);
      else $resultadoUser = rand(1, $dado);
    if ($resultadoUser == 1) echo "<br>Critical Failure USER<br>";
      else if($resultadoUser == $dado) echo "<br>Critical Success USER <br>";
    echo "User has rolled: ".$resultadoUser."<br>";
    if(empty($_POST["mod"])){
      $mod=0;
    }
    $resultadoUser = $resultadoUser +$mod;
    return $resultadoUser;
  }
  function calcRollenemy($dado, $modEn){
    $resultadoEnemy= 0;
    if(isset($_POST["advdisEn"])) $resultadoEnemy = calcAdvdisEn($dado);
      else $resultadoEnemy = rand(1, $dado);
    if ($resultadoEnemy == 1) echo "<br>Critical Failure ENEMY<br>";
      else if($resultadoEnemy == $dado) echo "<br>Critical Success ENEMY<br>";
    echo "Enemy has rolled: ".$resultadoEnemy."<br>";
    if(empty($_POST["modEn"])){
      $modEn=0;
    }
    $resultadoEnemy = $resultadoEnemy + $modEn;
    return $resultadoEnemy ;
  }

  function calcAdvdis($data){
      if($_POST["advdis"]==1){
        $dado1 = rand(1, $data);
        $dado2 = rand(1,$data);
        if($dado1 > $dado2) $resultado=$dado2;
        else $resultado = $dado1;
      }
       elseif($_POST["advdis"]==2){
        $dado1 = rand(1, $data);
        $dado2 = rand(1,$data);
        if($dado1 < $dado2) $resultado=$dado2;
        else $resultado = $dado1;
  
      }
      return $resultado;
    }
     function calcAdvdisEn($data){
      if($_POST["advdisEn"]==1){
        $dado1 = rand(1, $data);
        $dado2 = rand(1,$data);
        if($dado1 > $dado2) $resultado=$dado2;
        else $resultado = $dado1;
      }
       elseif($_POST["advdisEn"]==2){
        $dado1 = rand(1, $data);
        $dado2 = rand(1,$data);
        if($dado1 < $dado2) $resultado=$dado2;
        else $resultado = $dado1;
  
      }
      return $resultado;
    }

   function doesItHit($resultUser, $resultEnemy){
      $userHit = false;
      if($resultUser>$resultEnemy){
        $userHit = true;
      }
      return $userHit;
    }

    function damageCalculator($hitCheck,$userStrength,$userDefense,$userEvasion, $enemy){
      $damageDealtUser = 0;
      $damageDealtEnemy = 0;
      if($hitCheck){
        $damageDealtUser = $enemy->get_eDefense()- $userStrength;
        if(rand(0,20)<$enemy->get_eEvasion()){
          $damageDealtUser = 0;
          echo "YOU MISSED";
        }
      }
      else{
        $damageDealtEnemy = $userDefense - $enemy->get_eStrength();
        if(rand(0,20)<$userEvasion){
          $damageDealtEnemy =0;
          echo "THE ENEMY MISSED";
        }
      }
      $_SESSION["damageDealt"] += $damageDealtUser;
      $enemy->set_hpEnemy($enemy->get_hpEnemy()+$_SESSION["damageDealt"]);
      return $damageDealtEnemy;
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
  <header class="explanation">Explanation of the system</header>
  <aside class="input"><form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"])?>" method="post">
    <table>
      <th>Input the modifiers</th>
      <tr>
        <td>
          <select name="diceRoll" id="diceRoll">
            <option name="diceD20" value="20">D20</option>
            <option name="diceD12" value="12">D12</option>
            <option name="diceD6" value="6">D6</option>
            <option name="diceD4" value="4">D4</option>
      </select>
        </td>
      </tr>
      <tr>
        <td>
        Disadvantage:<input type="radio" name="advdis" id="adv" value="1">
        Advantage: <input type="radio" name="advdis" id="dis" value="2">
        </td>
      </tr>
      <tr>
        <td>
          Enemy Disadvantage:<input type="radio" name="advdisEn" id="advEn" value="1">
          Enemy Advantage: <input type="radio" name="advdisEn" id="disEn" value="2">
        </td>
      </tr>
      <tr>
        <td>
          Does it have modifiers: <input type="number" name="mod" id="mod">
        </td>
      </tr>
      <tr>
        <td>
           Does the enemy have modifiers: <input type="number" name="modEn" id="modEn">
        </td>
      </tr>
      <tr>
        <td>
          Select the enemy: 
          <select name="enemySelect" id="enemySelect">
           <option value="enemyRat" <?php if(isset($enemySelect)&& $enemySelect=="enemyRat") echo "selected"?>>Rat</option>
           <option value="enemyHuman" <?php if(isset($enemySelect)&& $enemySelect=="enemyHuman") echo "selected"?>>Human</option>
           <option value="enemyElf" <?php if(isset($enemySelect)&& $enemySelect=="enemyElf") echo "selected"?>>Elf</option>
          </select>
        </td>
      </tr>
      <tr>
        <td>
          Select enemy weapon:
          <select name="enemyWeaponSelect" id="enemyWeaponSelect">
            <option value="eSword">Sword</option>
            <option value="eFist">Fist</option>
            <option value="eMagic">Magic</option>
          </select>
        </td>
      </tr>
    </table>
    <input type="submit" value="Let's fight!" name="fight">
   </form>
  </aside>
  <main class="results">
    <?php 
    if(isset($enemyFinal)){
      echo "<h3> The enemy is :". $enemyFinal."</h3>";
    }
    if(isset($dado)){
    $hitCheck = doesItHit(calcRollUser($dado,$mod),calcRollEnemy($dado,$modEn));
    echo ($hitCheck)? "User Hit!" : "Enemy Hit! Brace yourselves!";
    $damageEnemy = damageCalculator($hitCheck, $userStrength, $userDefense,$userEvasion,$enemyFinal);
    echo "<br>";
    echo "The enemy dealt: ".$damageEnemy."<br>";
    echo "You've dealt: ".$_SESSION["damageDealt"]."<br>";
    $_SESSION["hpUser"] = $_SESSION["hpUser"] + $damageEnemy;
    echo "Your HP now is: ".$_SESSION["hpUser"]."<br>";
    echo "Enemy's HP now is: ".$enemyFinal->get_hpEnemy()."<br>";
    if($enemyFinal->get_hpEnemy() < 0){
      echo "<h1>The enemy has fallen</h1>";
      ?>
      <table>
     <tr>
      <td>
        <a href="create_char.php">Go back to create char</a>
      </td>
     </tr>
     <tr>
      <td>
            <a href="index_proxecto.php">Go back to index</a>
      </td>
     </tr> 
    </table>
      <?php 
    }
    }
    ?>
    <table>
     <tr>
      <td>
        <a href="create_char.php">Go back to create char</a>
      </td>
     </tr>
     <tr>
      <td>
            <a href="index_proxecto.php">Go back to index</a>
      </td>
     </tr> 
    </table>
  </main>
</body>
</html>