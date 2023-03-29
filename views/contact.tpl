% rebase('layout.tpl', title=title, year=year)

<div class="page">
    <h1>Contact Us</h1>
    <hr/>
    <p>
        Here you can share your feature request, or report a bug.
    </p>
    <form>
      <div class="mb-3">
        <label for="exampleInputEmail1" class="form-label">Email address</label>
        <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp"/>
        <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
      </div>
      <div class="mb-3">
        <label for="exampleFormControlTextarea1" class="form-label">Message</label>
        <input class="form-control" id="exampleFormControlTextarea1" style="height: 200px!important;"/>
      </div>
      <div class="mb-3 form-check">
        <input type="checkbox" class="form-check-input" id="exampleCheck1"/>
        <label class="form-check-label" for="exampleCheck1">I'm agree with Terms of Conditions</label>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
</div>
