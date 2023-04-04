<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }} - Brewpedia</title>
    <link rel="stylesheet" type="text/css" href="/static/content/bootstrap.css" />
    <link rel="stylesheet" type="text/css" href="/static/content/bootstrap-reboot.css"/>
    <link rel="stylesheet" type="text/css" href="/static/content/site.css" />
    <script src="/static/scripts/modernizr-2.6.2.js"></script>
</head>

<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light" style="position: fixed; top: 0; width: 100%; box-shadow: 0 2px 3px rgba(0,0,0,.1); z-index: 999;">
  <div class="container-fluid">
    <a class="navbar-main-article" href="/">Brewpedia</a>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="navbar-item" aria-current="page" href="/articles">Articles</a>
        </li>
        <li class="nav-item">
          <a class="navbar-item" href="/brewing">Brewing Methods</a>
        </li>
        <li class="nav-item">
          <a class="navbar-item" href="/beans">Coffee Beans</a>
        </li>
        <li class="nav-item">
          <a class="navbar-item" href="/roasting">Roasting</a>
        </li>
          <li class="nav-item">
          <a class="navbar-item" href="/contact">Contact</a>
        </li>
      </ul>
    </div>
  </div>
</nav>

    <div class="container body-content" style="margin-top: 6rem;">
        {{!base}}
        <hr/>
        <footer class="footer-main">
            <p>&copy; {{ year }} - Brewpedia</p>
        </footer>
    </div>

    <script src="/static/scripts/jquery-1.10.2.js"></script>
    <script src="/static/scripts/bootstrap.js"></script>
    <script src="/static/scripts/respond.js"></script>

</body>
</html>
