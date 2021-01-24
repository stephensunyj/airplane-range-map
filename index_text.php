<!DOCTYPE html>
<html>
<head>
    <title>PHP Retrieve Data from MySQL using Drop Down Menu</title>
</head>
<body>

    <form>
        City:
        <select>
            <option disabled selected>-- Select Aircraft --</option>
            <?php
            include "dbConn.php";  // Using database connection file here
            $records = mysqli_query($db, "SELECT Model From airdata");  // Use select query here

            while($data = mysqli_fetch_array($records))
            {
            echo "
            <option value='". $data['Model'] ."'>" .$data['Model'] ."</option>";  // displaying data in option menu
            }
            ?>
        </select>
    </form>

    <?php mysqli_close($db);  // close connection ?>

</body>
</html>