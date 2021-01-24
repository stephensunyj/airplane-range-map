<?php
//Database details
$db_host = 'webhosting2011.is.cc';
$db_username = 'joshuane_joshneronha';
$db_password = 'joshuajn8';
$db_name = 'joshuane_airlines';

//Create connection and select DB
$conn = mysqli_connect($db_host, $db_username, $db_password, $db_name);
if (mysqli_connect_errno()) {
    echo "Failed to connect to MySQL: " . mysqli_connect_error();
}