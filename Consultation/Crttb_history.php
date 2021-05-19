<?php
$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "hospital";

// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

// sql to create table
$sql = "CREATE TABLE history (
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
patient_name VARCHAR(30) NOT NULL,
doctor_name VARCHAR(30) NOT NULL,
consult_date DateTime,
consult_time TIMESTAMP
)";

if (mysqli_query($conn, $sql)) {
    echo "Table history created successfully";
} else {
    echo "Error creating table: " . mysqli_error($conn);
}

mysqli_close($conn);
?>
