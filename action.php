<!DOCTYPE HTML>  
<html>
    <head><h1> Amazon </h1></head><br>

    
<body>
    <h1>
        Congratulations, you have purchased this product
    </h1>
</body>
</html>
<?php
$productID = $productName = $description = $email = "";
$sendEmailFlag = "";

//if ($_SERVER["REQUEST_METHOD"] == "POST") {
//  $productID = test_input($_POST["productID"]);
//  $productName = test_input($_POST["productName"]);
//  $description = test_input($_POST["description"]);
//  $sendEmailFlag = test_input($_POST["sendEmail"]);
//  $email = test_input($_POST["email"]);
//  $productIcon = $_POST["productIcon"];
  $productID = 212512;
  $productName = 'Book';
  $description = 'Your product has been confirmed';
  $email = 'bharathjinka09@gmail.com';
//}
//print_r($_POST);
//echo $productIcon.'================';

function test_input($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}
?>

<?php
echo 'Your Input:';
echo $productID;
echo "<br>";
echo $productName;
echo "<br>";
echo $description;
echo "<br>";
echo $sendEmailFlag;
$productFullText = "<h2>Your Product Details are:</h2>"."<br>".
                   "<h3>Image :</h3>". "<img src='https://upload.wikimedia.org/wikipedia/commons/b/b4/Amazon-icon.png' width='60' height='80' >"."<br>".
                   "<h3>Product ID</h3> :". $productID."<br>".
                   "<h3>Product Name</h3> :". $productName."<br>".
                   "<h3>Description</h3> :". $description."<br>";

//if($sendEmailFlag === 'yes') {
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
//} elseif  

//($sendEmailFlag === 'no') {
//    echo '<br> <h1>Mail Not sent</h1>';
//}

?>

