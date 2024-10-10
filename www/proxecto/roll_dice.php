<?php 
  session_start();
  if(!isset($_SESSION['user'])){
    header("Location: login_user.php?redirected=true");
  }
  echo "name: ".$_SESSION["name"];
  echo "race: ".$_SESSION["race"];
  echo "weapon: ".$_SESSION["weapon"]."<br>";
  echo "str: ".$_SESSION["strenght"];
  echo "defense: ".$_SESSION["defense"];
  echo "evasion: ".$_SESSION["evasion"]."<br>";

  ?>
<?php
class Enemy{
    public $eName;
    public $eWeapon;
    public $eStrength;
    public $eDefense;
    public $eEvasion;

    public function __construct($eName = "", $eWeapon ="", $eStrength = 0, $eDefense = 0, $eEvasion = 0){
      $this->eName = $eName;
      $this->eWeapon = $eWeapon;
      $this->eStrength = $eStrength;
      $this->eDefense = $eDefense;
      $this->eEvasion = $eEvasion;
    }

    public function get_eName(){
      return $this->eName;
    }
    public function get_eWeapon(){
      return $this->eWeapon;
    }
    public function get_eStrength(){
      return $this->eStrength;
    }
    public function get_eDefense(){
      return $this->eDefense;
    }
    public function get_eEvasion(){
      return $this->eEvasion;
    }

    public function __toString(){
      return "<h1> Name of the enemy:  $this->eName Weapon of the enemy: $this->eWeapon  </h1>";
    }
    // function _constructForm(){}

  }
?>
<?php
    $enemyRat = new Enemy("Rat","Fist",12,12,12);
    $enemyHuman = new Enemy("BadHuman", "Magic",12,12,12);
    $enemyElf = new Enemy("BadElf", "Sword", 12,21,12);
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

?>
<?php 
  function calcRollUser($dado, $mod){
    $resultadoUser= 0;

    if(isset($_POST["advdis"])) $resultadoUser = calcAdvdis($dado);
      else $resultadoUser = rand(1, $dado);
    if ($resultadoUser == 1) echo "<br>Pifia absoluta <br>";
      else if($resultadoUser == $dado) echo "<br>TOMAAAAAA Crítico!!! <br>";
    echo "User has rolled: ".$resultadoUser;
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
    if ($resultadoEnemy == 1) echo "<br>Pifia absoluta <br>";
      else if($resultadoEnemy == $dado) echo "<br>TOMAAAAAA Crítico!!! <br>";
    echo "Enemy has rolled: ".$resultadoEnemy;
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
        <option name="diceD4" value="4">D4</option>
        <option name="diceD6" value="6">D6</option>
        <option name="diceD12" value="12">D12</option>
        <option name="diceD20" value="20">D20</option>
      </select>
        </td>
      </tr>
      <tr>
        <td>
        Disadvantage:<input type="radio" name="advdis" id="adv" value="1">
        Advantage: <input type="radio" name="advdis" id="dis" value="2">
        Enemy Disadvantage:<input type="radio" name="advdisEn" id="advEn" value="1">
        Enemy Advantage: <input type="radio" name="advdisEn" id="disEn" value="2">
        </td>
      </tr>
      <tr>
        <td>
          Does it have modifiers: <input type="number" name="mod" id="mod">
          Does the enemy have modifiers: <input type="number" name="modEn" id="modEn">
        </td>
      </tr>
      <tr>
        <td>
          <select name="enemySelect" id="enemySelect">
           <option value="enemyRat" <?php if(isset($enemySelect)&& $enemySelect=="enemyRat") echo "selected"?>>Rat</option>
           <option value="enemyHuman" <?php if(isset($enemySelect)&& $enemySelect=="enemyHuman") echo "selected"?>>Human</option>
           <option value="enemyElf" <?php if(isset($enemySelect)&& $enemySelect=="enemyElf") echo "selected"?>>Elf</option>
          </select>
        </td>
      </tr>
    </table>
    <input type="submit" value="Let's fight!" name="fight">
   </form>
  </aside>
  <main class="results">
    <?php 
    if(isset($dado)){
    calcRollUser($dado,$mod);
    calcRollEnemy($dado,$modEn);
    }
    ?>
  </main>
</body>
</html>