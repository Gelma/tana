
<!doctype html>
<html lang="it">
<head>
  <meta charset="utf-8">
  <title>jQuery UI Datepicker - Display multiple months</title>
  <link rel="stylesheet" href="//code.jquery.com/ui/1.11.3/themes/smoothness/jquery-ui.css">
  <script src="//code.jquery.com/jquery-1.10.2.js"></script>
  <script src="//code.jquery.com/ui/1.11.3/jquery-ui.js"></script>
  <link rel="stylesheet" href="/resources/demos/style.css">
  <script>
  $(function() {
    $( "#datepicker" ).datepicker({
      numberOfMonths: 3,
      showButtonPanel: true
    });
  });
  </script>
</head>
<body>
 
<p>Data: <input type="text" id="datepicker"></p>
 
 
</body>
</html>
