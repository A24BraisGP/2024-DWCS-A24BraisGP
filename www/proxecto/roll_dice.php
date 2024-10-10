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
  echo "evasion: ".$_SESSION["evasion"];
  ?>
<?php
class Enemy{
    public $eName;
    public $eWeapon;
    public $eStrength;
    public $eDefense;
    public $eEvasion;

    public function _construct(){
      $this->eName = $eName;
      $this->eWeapon = $eWeapon;
      $this->eStrength = $eStrength;
      $this->eDefense = $eDefense;
      $this->eEvasion = $eEvasion;
    }

    function get_eName(){
      return $this->eName;
    }
    function get_eWapon(){
      return $this->eWeapon;
    }
    function get_eStrength(){
      return $this->eStrength;
    }
    function get_eDefense(){
      return $this->eDefense;
    }
    function get_eEvasion(){
      return $this->eEvasion;
    }

    public function __toString(){
      return $this->eName;
    }
    // function _constructForm(){}

  }
    $enemyRat = new Enemy("Rat","Fist",12,12,12);
    $enemyHuman = new Enemy("BadHuman", "Magic",12,12,12);
    $enemyElf = new Enemy("BadElf", "Sword", 12,21,12);
    $arrayEnemies = array(
      $enemyRat,
      $enemyHuman,
      $enemyElf
    )
?>
<?php
  if($_SERVER["REQUEST_METHOD"] == "POST"){
    $dado = $_POST["diceRoll"];
    $modifier = $_POST["mod"];
    if(isset($_POST["advdis"])) $advdis = $_POST["advdis"];
    $enemySelect = $_POST["enemySelect"];
    showEnemy($enemySelect,$arrayEnemies);
  } 

  function showEnemy($enemySelected, $arrayEnemies){
    $enemyObject;
    switch($enemySelected){
      case "enemyRat":
        $enemyObject = $arrayEnemies[0];
        break;
      case "enemyHuman":
        $enemyObject = $arrayEnemies[1];
        break;
      default:
        $enemyObject = $arrayEnemies[2];
        break;
    }
    echo  var_dump($arrayEnemies[0]);
    echo "<h1>".$enemyObject->get_eStrength()."</h1>";
  }

?>
<?php 
  function calcRoll(){

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
        </td>
      </tr>
      <tr>
        <td>
          Does it have modifiers: <input type="number" name="mod" id="mod">
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
    //calcRoll();
    ?>
  </main>
</body>
</html>