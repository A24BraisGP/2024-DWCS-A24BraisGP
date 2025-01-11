<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <form action="manage.php" method="GET">
    <input type="radio" name="classes" value="inperson">In-person classes<br>
    <input type="radio" name="classes" value="distant">Distance classes<br>
    <input hidden name="vName" value="<?php echo $_GET["vName"]?>"><br>
    <input name="vSubject" value="<?php echo $_GET["vSubject"]?>" hidden>
    <input type="submit">
  </form>
</body>
</html>