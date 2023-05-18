% rebase('layout.tpl', title="Reviews", year=year)


<body>
  <div class="my-4">Leave a review about our work</div>
  <form action="/home" method="post" id="myForm">
    <label for="name">Name:</label>
    <input class="form-control" type="text" id="name" name="name" required>

    <label for="phone">Phone:</label>
    <input class="form-control" type="tel" id="phone" name="phone" required>

    <label for="review">Review:</label>
    <textarea id="review" class="form-control" name="review" rows="4" required></textarea>

    <input type="submit" value="Leave a review">
  </form>
  <div class="my-4">Reviews</div>
  <hr>
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
