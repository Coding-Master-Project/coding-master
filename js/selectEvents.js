document.addEventListener('DOMContentLoaded', function () {
    const selectBox = document.querySelector('.selectBox');
    const selectArrow = document.querySelector('.selectArrow');

    selectBox.addEventListener('focus', function () {
        selectArrow.classList.add('clicked');
    });

    selectBox.addEventListener('blur', function () {
        selectArrow.classList.remove('clicked');
    });

    selectArrow.addEventListener('click', function () {
        selectBox.focus();
        this.classList.toggle('clicked');
    });
});