<?php

$domain = "http://54.149.49.212/cp/";
$domain = "http://poorvi.cse.iitd.ac.in/~cs1120233/cp/";

$rdomain = "http://classpundit.com/";
$rdomain = "http://poorvi.cse.iitd.ac.in/~cs1120233/cp/godady.php";

$url = $domain."?nhost=".urlencode($rdomain).(isset($_GET["pid"]) ? "&pid=".$_GET["pid"]:"");

?>
<!DOCTYPE html>
<html style='padding:0px;margin:0px;height:100%;width:100%;' >
<body style="padding:0px;margin:0px;height:100%;width:100%;overflow-y:hidden;" >

<iframe src="<?php echo $url; ?>" style="width:100%;height:100%;border:solid black 0px;" >
  <p>Your browser does not support iframes.</p>
</iframe>

</body>
</html>
