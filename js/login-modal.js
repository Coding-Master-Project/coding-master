function initializeLoginModal() {
    const modal = document.querySelector('.login-modal');
    const modalOpen = document.querySelector('.login-btn');
    const modalClose = document.querySelector('.login-closeBtn');

    if (modalOpen) {
        modalOpen.addEventListener('click', function () {
            modal.classList.add('on');
        });
    }

    if (modalClose) {
        modalClose.addEventListener('click', function () {
            modal.classList.remove('on');
        });
    }
}