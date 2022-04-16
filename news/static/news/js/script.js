window.addEventListener('DOMContentLoaded', () => {
    const menu = document.querySelector('.topmenu'),
    menuItem = document.querySelectorAll('.topmenu_item'),
    hamburger = document.querySelector('.hamburger');

    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('hamburger_active');
        menu.classList.toggle('topmenu_active');
    });

    menuItem.forEach(item => {
        item.addEventListener('click', () => {
            hamburger.classList.toggle('hamburger_active');
            menu.classList.toggle('topmenu_active');
        })
    })
})

$("#toggle_btn1").click(function(){
    $("#toggle_box1").slideToggle();
});

$("#toggle_btn2").click(function(){
    $("#toggle_box2").slideToggle();
});

$("#toggle_btn3").click(function(){
    $("#toggle_box3").slideToggle();
});

$("#toggle_btn4").click(function(){
    $("#toggle_box4").slideToggle();
});

// // When document is ready...
// $(document).ready(function() {
//     // If cookie is set, scroll to the position saved in the cookie.
//     if ( $.cookie("scroll") !== null ) {
//         $(document).scrollTop( $.cookie("scroll") );
//     }
//     // When a button is clicked...
//     $('#submit').on("click", function() {
//         // Set a cookie that holds the scroll position.
//         $.cookie("scroll", $(document).scrollTop() );
//     });
// });
