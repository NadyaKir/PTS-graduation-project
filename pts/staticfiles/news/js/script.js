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


