% rebase('layout.tpl', title="Reviews", year=year)


<body>
  <h1>Leave a review about our work</h1>
  <form action="/home" method="post" id="myForm">
    <label for="name">Name:</label>
    <input class="form-control" type="text" id="name" name="name" required>

    <label for="email">Email:</label>
    <input class="form-control" type="email" id="email" name="email" required>

    <label for="review">Review:</label>
    <textarea id="review" class="form-control" name="review" rows="4" required></textarea>

    <input type="submit" value="Leave a review">
  </form>
  <hr>
  <h1>Reviews</h1>
  <div id="review-cards">
    % for review in reversed(reviews):
    <div class="review-card">
      <div class="avatar-container">
        <img src="/static/images/icon.png" alt="Avatar" class="avatar">
        <h3>{{ review["name"] }}</h3>
      </div>
      <div class="review-details">
        <p class="email">{{ review["timestamp"] }}</p>
        <p>{{ review["review"] }}</p>
      </div>
    </div>
    % end
  </div>
</body>
