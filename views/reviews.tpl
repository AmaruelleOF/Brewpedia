% rebase('layout.tpl', title="Reviews", year=year)

<body>
    <img src="/static/images/cafe_orange.svg" alt="Brewing Methods of Coffee" class="page-icon"/>
    <article>
    <hr>
    <h2></h2>
    <form action="/home" method="post" id="myForm">
        <label for="name">Имя:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Почта:</label>
        <input type="email" id="email" name="email" required>

        <label for="review">Отзыв:</label>
        <textarea id="review" name="review" rows="4" required></textarea>

        <input type="submit" value="Отправить">
    </form>
    <hr>
            <h1>Reviews</h1>
    <div id="review-cards">
        % for review in reviews:
        <div class="review-card">
            <div class="avatar-container">
                <img src="/static/images/icon.png" alt="Avatar" class="avatar">
                <h3>{{ review["name"] }}</h3>
            </div>
            <div class="review-details">
                <p class="email">{{ review["email"] }}</p>
                <p>{{ review["review"] }}</p>
            </div>
        </div>
        % end
    </div>
    </article>
</body>