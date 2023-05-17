<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" crossorigin="anonymous"></script>
    <title>Pending Orders</title>
</head>
<body class="container py-4">
    <h1 class="mb-4">Pending Orders</h1>
    <table class="table table-striped">
        <thead>
            <tr>
                <th scope="col">Username</th>
                <th scope="col">Deadline</th>
                <th scope="col">Description</th>
                <th scope="col">Phone</th>
            </tr>
        </thead>
        <tbody>
            % for order in orders:
                <tr>
                    <td>{{order['username']}}</td>
                    <td>{{order['deadline']}}</td>
                    <td>{{order['description']}}</td>
                    <td>{{order['phone']}}</td>
                </tr>
            % end
        </tbody>
    </table>

    <h2 class="my-4">Add New Order</h2>
    <form action="/add_order" method="post">
        <div class="mb-3">
            <label for="username" class="form-label">Username:</label>
            <input type="text" class="form-control" id="username" name="username" required>
        </div>
        <div class="mb-3">
            <label for="deadline" class="form-label">Deadline:</label>
            <input type="date" class="form-control" id="deadline" name="deadline" required>
        </div>
        <div class="mb-3">
            <label for="description" class="form-label">Description:</label>
            <textarea class="form-control" id="description" name="description" rows="4" required></textarea>
        </div>
        <div class="mb-3">
            <label for="phone" class="form-label">Phone:</label>
            <input type="tel" class="form-control" id="phone" name="phone" pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}" required>
            <small class="form-text">Format: 123-456-7890</small>
        </div>
        <input type="submit" class="btn btn-primary" value="Add Order">
    </form>
</body>
</html>
