if($sendEmailFlag === 'yes') {
// If you are using Composer (recommended)
require ("/sendgrid-php/vendor/autoload.php");

// If you are not using Composer
require("/sendgrid-php/sendgrid-php.php");

$from = new SendGrid\Email("Example User", "bharathjinka09@gmail.com");
$subject = "Order Confirmation Message";
$to = new SendGrid\Email("Example User", $email);
$content = new SendGrid\Content("text/html", $productFullText);
$mail = new SendGrid\Mail($from, $subject, $to, $content);

$apiKey = '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';
$sg = new \SendGrid($apiKey);

$response = $sg->client->mail()->send()->post($mail);
echo '<br> <h1>Mail sent successfully</h1>';
//echo $response->statusCode();
//print_r($response->headers());
//echo $response->body();
} elseif  

($sendEmailFlag === 'no') {
    echo '<br> <h1>Mail Not sent</h1>';
}



?> 
<!--<html>-->
<!--<a href= '/email/.php' target="_blank">
    <button type="button">Buy now</button>
</a>
<a href="http://www.iamwire.com/wp-content/uploads/2013/06/amazonin.png" target="_blank">
 
    
</a>
</html>-->