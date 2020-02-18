import cgi
form = cgi.FieldStorage()
v_name = form.getvalue('name')
print(f'''
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Hello Python!</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    
    <!-- import the webpage's stylesheet -->
    <link rel="stylesheet" href="/style.css">
    
    <!-- import the webpage's javascript file -->
    <script src="/script.js" defer></script>
  </head>  
  <body>
    <h1>Hello {v_name}!</h1>
    
    <p>
      <form action="" method="get" class="form-example">
      <div class="form-example">
      <label for="name">Enter your name: </label>
      <input type="text" name="name" id="name" required>
      </div>
      </form>
    </p>

    <!-- include the Glitch button to show what the webpage is about and
          to make it easier for folks to view source and remix -->
    <div class="glitchButton" style="position:fixed;top:20px;right:20px;"></div>
    <script src="https://button.glitch.me/button.js"></script>
  </body>
</html>
''')
