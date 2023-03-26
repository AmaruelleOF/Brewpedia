<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }} - My Bottle Application</title>
    <link rel="stylesheet" type="text/css" href="/static/content/bootstrap.css" />
    <link rel="stylesheet" type="text/css" href="/static/content/bootstrap-reboot.css">
    <link rel="stylesheet" type="text/css" href="/static/content/site.css" />
    <script src="/static/scripts/modernizr-2.6.2.js"></script>
</head>

<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-main-article" href="#">Brewpedia</a>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="navbar-item" aria-current="page" href="#">Articles</a>
        </li>
        <li class="nav-item">
          <a class="navbar-item" href="#">Brewing Methods</a>
        </li>
        <li class="nav-item">
          <a class="navbar-item" href="#">Coffee Beans</a>
        </li>
        <li class="nav-item">
          <a class="navbar-item" href="#">Roasting</a>
        </li>
          <li class="nav-item">
          <a class="navbar-item" href="#">Resources</a>
        </li>
      </ul>
    </div>
  </div>
</nav>

    <div class="container body-content">
        {{!base}}
        <hr />
        <footer>
            <p>&copy; {{ year }} - Brewpedia</p>
        </footer>
    </div>

    <script src="/static/scripts/jquery-1.10.2.js"></script>
    <script src="/static/scripts/bootstrap.js"></script>
    <script src="/static/scripts/respond.js"></script>

</body>
</html>
