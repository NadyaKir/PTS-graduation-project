$(document).ready(function() {
  $(window).scroll(function() {
    if ($(this).scrollTop() > 50) {
      $(".inner-wrapper").css({"opacity": "0", "transition": ".4s ease-in-out"})
    }
    else {
      $(".inner-wrapper").css({"opacity": "1"})
    }
  })
})