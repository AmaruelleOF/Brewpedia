% rebase('layout.tpl', title='Active Users', year=2023)

<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">

    <title>Active Users</title>
</head>
<body>
<div class="container">
    <h1 class="my-4">Active Users</h1>
    <div class="row row-cols-1 row-cols-md-3 g-4">
        % for user in users:
        <div class="col">
            <div class="card h-100">
                <div class="card-body">
                    <h3 class="card-title">{{user['username']}}</h3>
                    <p class="card-text">
                        <span class="badge bg-warning">Date Registered: {{user['date_registered']}}</span><br>
                        <span class="badge bg-secondary">Last Active: {{user['last_active']}}</span>
                    </p>
                </div>
            </div>
        </div>
        % end
    </div>

    <h2 class="my-4">Add New User</h2>
    <form action="/add_user" method="post">
        <div class="mb-3">
            <label for="username" class="form-label">Username</label>
            <input type="text" class="form-control" id="username" name="username" required>
        </div>
        <div class="mb-3">
            <label for="date_registered" class="form-label">Date Registered</label>
            <input type="date" class="form-control" id="date_registered" name="date_registered" required>
        </div>
        <div class="mb-3">
            <label for="last_active" class="form-label">Last Active</label>
            <input type="date" class="form-control" id="last_active" name="last_active" required>
        </div>
        <button type="submit" class="btn btn-warning">Submit</button>
    </form>
</div>

<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.min.js"></script>
</body>
</html>
