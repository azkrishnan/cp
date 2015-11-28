<?php
	echo microtime(true);
	$deg = 23.5;
?>
<!DOCTYPE html>
<html>
	<head>
		<style type="text/css">
			div.rotate {
				-ms-transform: rotate(<?php echo $deg; ?>deg); /* IE 9 */
				-webkit-transform: rotate(<?php echo $deg; ?>deg); /* Safari */
				transform: rotate(<?php echo $deg; ?>deg);
			}
		</style>
	</head>
	<body>
		<div style="margin-top:30px;" align="center" >
			
			<div class="rotate" >
				<img src="photo/globe2.png">
			</div>

		</div>
		<script type='text/javascript' >
			var jsdata = {"_server": "csc", "HOST": "http://privateweb.iitd.ac.in/~cs1120233/cp/", "BASE": "http://privateweb.iitd.ac.in/~cs1120233/cp/index.php/", "curpage": "index"};
		</script>
		<script type='text/javascript' >
			var ec  = jsdata['_ec'] ;
		</script>
		<script src='mslib/js/jquery-2.1.1.min.js'  type='text/javascript' >
		</script>
		<script src='mslib/js/materialize.min.js'  type='text/javascript' >
		</script>
		<script src='mslib/js/jquery.bxslider.min.js'  type='text/javascript' >
		</script>
		<script src='mslib/js/jquery.easing.1.3.js'  type='text/javascript' >
		</script>
		<script src='mslib/js/jquery.raty.js'  type='text/javascript' >
		</script>
		<script src='mslib/js/lib.js'  type='text/javascript' >
		</script>
		<script src='mslib/js/mohit.js'  type='text/javascript' >
		</script>
		<script src='mslib/js/mohitlib.js'  type='text/javascript' >
		</script>
		<script src='mslib/js/main.js'  type='text/javascript' >
		</script>
		<script src='js/main.js'  type='text/javascript' >
		</script>
		<script src='js/index.js'  type='text/javascript' >
		</script>
	</body>
</html>
<?php
	echo microtime(true);
?>
