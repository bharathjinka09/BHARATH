<!DOCTYPE HTML> 
<!--<html>-->
<!--    <head><h1> Amazon </h1></head><br>
    
    <body>-->
        
<?php
// define variables and set to empty values
$productID = $productName = $description =  $email = $sendEmailFlag = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
//  $productID = test_input($_POST["productID"]);
//  $productName = test_input($_POST["productName"]);
//  $description = test_input($_POST["description"]);
//  $sendEmailFlag = test_input($_POST["sendEmail"]);
//  $email = test_input($_POST["email"]);
//  $productIcon = $_POST["productIcon"];
  $productID = 123445;
  $productName = 'Think Rich and Grow Rich';
  $description = 'Congratulations your order is confirmed';
  $sendEmailFlag = test_input($_POST["sendEmail"]);
  $email = 'bharathjinka09@gmail.com';
  $productIcon = 'https://images-eu.ssl-images-amazon.com/images/I/51q20ycKO1L.jpg';

}
//print_r($_POST);
//echo $productIcon.'================';

function test_input($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}
?>
<!--<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">-->

    <!--<a href="https://www.amazon.in/ref=nav_logo" title="Visit Amazon.in" style="text-decoration:none;color:rgb(0,102,153);font-size:13px;line-height:18px;font-family:Arial,san-serif" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&q=https://www.amazon.in/gp/r.html?C%3D11HNHBWMJJD95%26K%3D291RUI3GCK8W0%26M%3Durn:rtn:msg:201801041526558588871d30cc4d74af8e6731dfe0p0eu%26R%3D3JYVNU81CO2KK%26T%3DC%26U%3Dhttps%253A%252F%252Fwww.amazon.in%252Fref%253Dpe_386221_57731711_pe_520732_50917562M1%26H%3DRRSXUYDVERSD84UHNOYVKVVNG3AA%26ref_%3Dpe_386221_57731711_pe_520732_50917562M1&source=gmail&ust=1515392007719000&usg=AFQjCNHa0QR56eakNRRjERlZiJxurhTdtw"--> 
    <!--<img id="wed"src="https://upload.wikimedia.org/wikipedia/commons/b/b4/Amazon-icon.png"><br>-->
    <!--</a>-->
    <!--<span class="a-list-item">-->
        <!--<a class="a-link-normal  a-inline-block" href="/Think-Grow-Rich-Napoleon-Hill/dp/8192910911/ref=br_asw_pdt-6?pf_rd_m=A1VBAL9TL5WCBF&amp;pf_rd_s=&amp;pf_rd_r=7N7PN2RJ4JCWY9ZF4AQT&amp;pf_rd_t=36701&amp;pf_rd_p=e1efc5ee-e2be-419a-b048-131e7fb3fa95&amp;pf_rd_i=desktop"><img alt="Think and Grow Rich" src="https://images-eu.ssl-images-amazon.com/images/I/51Y8jwGiebL._AC_SY200_.jpg" class="product-image" height="200px" data-a-hires="https://images-eu.ssl-images-amazon.com/images/I/51Y8jwGiebL._AC_SY400_.jpg"><span class="red-sticker">-->
    <!--45% <p>off</p></span></a></span>-->
    
    <!--<img alt="Think and Grow Rich" src="https://images-eu.ssl-images-amazon.com/images/I/51Y8jwGiebL._AC_SY200_.jpg" class="product-image" height="200px" data-a-hires="https://images-eu.ssl-images-amazon.com/images/I/51Y8jwGiebL._AC_SY400_.jpg">-->
    
    <!--Product ID: <input type="text" name="productID" value="<?php echo $productID;?>">-->
  <!--<br><br>-->
    <!--Product Name: <input type="text" name="productName" value="<?php echo $productName;?>">-->
  <!--<br><br>-->
    <!--Description: <textarea name="description" rows="5" cols="40">-->
     //<?php // echo $description;?>
  <!--</textarea>-->
  <!--<br><br>-->
    <!--Email : <input type="text" name="email" value="<?php echo $email;?>">-->
  <!--<br><br>-->
    <!--Send Email:-->
  <!--<input type="radio" name="sendEmail" value="no">No-->
  <!--<input type="radio" name="sendEmail" value="yes">Yes-->
  <!--<br><br>-->
  <!--<input type="submit" name="submit" value="Submit">-->  
<!--</form>-->
    <!--</body>-->

<!--</html>-->
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
