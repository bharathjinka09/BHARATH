<?php

// If you are using Composer (recommended)
require '/sendgrid-php/vendor/autoload.php';
//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

// If you are not using Composer
 require("/sendgrid-php/sendgrid-php.php");

$from = new SendGrid\Email("Example User", "bharathjinka09@gmail.com");
$subject = "Order Confirmation";
$to = new SendGrid\Email("Example User", "bharathjinka09@gmail.com");
$content = new SendGrid\Content("text/plain", "SAMPLE MESSAGE from sendgrid");
$mail = new SendGrid\Mail($from, $subject, $to, $content);

$apiKey = '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';
$sg = new \SendGrid($apiKey);

$response = $sg->client->mail()->send()->post($mail);
echo $response->statusCode();
print_r($response->headers());
echo $response->body();
?>