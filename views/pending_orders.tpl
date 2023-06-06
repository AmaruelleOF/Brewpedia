% rebase('layout.tpl', title='Pending Orders', year=2023)

<body class="container py-4">
<article>
    <h1 class="mb-4">Pending Orders</h1>
    <hr/>
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
    <hr/>
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
            <input type="tel" class="form-control" id="phone" name="phone" required>
            <small class="form-text">Format: 123-456-7890</small>
        </div>
        <p id="user-check" style="color: red"></p>
        <input type="submit" class="btn btn-warning" value="Add Order">
    </form>
    </article>
</body>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script>
    $(document).ready(function() {
      $('form').on('submit', function(event) {
        event.preventDefault();
          let phone = $('#phone').val();
          let username = $('#username').val();
          let description = $('#description').val();
          let deadline = $('#deadline').val();
          $.ajax({
          url: '/add_order',
          data: {'username': username, 'phone': phone, 'description': description, 'deadline': deadline},
          type: 'POST',
          success: function(response) {
            $('#user-check').text(response.status);
          },
          error: function(error) {
            console.log(error);
          }
        });
      });
    });
</script>
