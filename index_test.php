<?php require_once 'config.php';
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Populating drop down menu from MySQL and PHP</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
    <div class="container" style="max-width:800px;margin:0 auto;margin-top:50px;">
        <div>
            <h2 style="margin-bottom:50px;">Live Demo: Populating drop down menu from MySQL and PHP</h2>
        </div>
        <div>
            <select name="category" id="category">
                <option value=''>Select Category</option>
                <?php
                $sql = mysqli_query($conn, "SELECT * FROM airdata");
                while ($row = mysqli_fetch_array($sql)) {
                $id = $row['id'];
                $Model = $row['Model'];
                ?>
                <option value='<?php echo $id; ?>'><?php echo $Model; ?></option>
                <?php } ?>
            </select>
        </div>
    </div>
</body>
</html>