<?php
$to = "bharathjinka66@gmail.com";
$subject = "My subject";
$txt = "Hello world!";
$headers = "From: bharathjinka09@gmail.com" . "\r\n" .
//"CC: somebodyelse@example.com";

mail($to,$subject,$txt,$headers);
?>