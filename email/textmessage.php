<?php
// Sending an SMS using the Twilio API
// Get the PHP helper library from twilio.com/docs/php/install
require_once '/path/to/vendor/autoload.php'; // Loads the library
use Twilio\Rest\Client;
// Your Account Sid and Auth Token from twilio.com/user/account
$sid = "ACf8d5681cda40c0556663470a0238d231";
$token = "c8af78cddbdee792ff2b00c44158dc78";
$client = new Client($sid, $token);
$client->messages->create(
  "+919441575993",
  array(
    'from' => "+919110334114",
    'body' => "Your order is confirmed and will be delivered within seven days",
    'mediaUrl' => "https://climacons.herokuapp.com/clear.png",
  )
);
