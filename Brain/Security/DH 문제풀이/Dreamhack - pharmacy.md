# Code

- index.php
```php
<?php
require("supermarket.php");
?>

<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="style.css">
    <title>Pharmacy</title>
</head>
<body>
    <h1>Pharmacy💊</h1>
    <h2>Upload your prescription in gif format...</h2>
    <form action="index.php" method="post" enctype="multipart/form-data" class="file-upload-form">
        <input type="file" name="fileToUpload" id="fileToUpload" class="file-upload-input">
        <input type="submit" value="upload" name="submit" class="file-upload-button">
    </form>
    <br>

<?php
$targetDirectory = "uploads/";
$uploadOK = 1;

if( isset($_POST["submit"])) {
    echo '<pre class="file-upload-form">';
    $tmpFile = $_FILES["fileToUpload"]["tmp_name"];
    $currentFile = $_FILES["fileToUpload"]["name"];
    $fileExtension = strtolower(pathinfo($currentFile, PATHINFO_EXTENSION));

    if (mime_content_type($tmpFile) !== "image/gif" || $fileExtension !== "gif") {
        echo "Prescription not gif!\n";
        $uploadOK = 0;
    }

    if ($uploadOK == 0) {
        echo "Prescription upload failed.\n";
    } else {
        $randomFileName = bin2hex(random_bytes(16));
        $targetFile = $targetDirectory . $randomFileName . "." . $fileExtension;
        if (move_uploaded_file($tmpFile, $targetFile)) {
            if (isset($_POST['emergent']))
                $targetFile = 'phar://' . $targetFile;
            else
                $targetFile = $targetFile;

            if (file_exists($targetFile)) {
                echo "Prescription submitted!\n";
            }
        } else {
            echo "Prescription upload failed.\n";
        }
    }
    echo '</pre>';
}
?>

</body>
</html>

```

- supermarket.php
```php
<?php
function goodbye($customer) {
    echo "Good bye, $customer!\n";
}

class Supermarket {
    public $greet = 'goodbye';
    public $customer = 'dream';
    function __destruct() {
        call_user_func($this->greet, $this->customer);
    }
}
?>
```


---
# Analysis
- `php` 환경에서 발생하는 `phar Deserialize` 취약점
- 


---
# Write-UP