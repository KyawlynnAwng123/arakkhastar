$(document).ready(function () {
    $('#navbar-toggler').click(function () {
        $('#navbar').toggleClass('navbar-class');
    })
    $('.image').hover(function () {
        // $('.category-hide').toggle();
    })
})
let left = document.getElementById('left');
let right = document.getElementById('right');
let relative = document.getElementsByClassName('relative')[0];
right.addEventListener('click', () => {
    relative.scrollLeft += 360;
})
left.addEventListener('click', () => {
    relative.scrollLeft -= 360;
})