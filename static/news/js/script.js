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