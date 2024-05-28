function initializeLoginModal() {
    const modal = document.querySelector('.login-modal');
    const modalOpen = document.querySelector('.login-btn');
    const modalClose = document.querySelector('.login-closeBtn');
    const findId = document.querySelector('.findIdBtn');
    const findPassword = document.querySelector('.findPasswordBtn');
    const signup = document.querySelector('.signupNavigator');

    // 모달 열기
    if (modalOpen) {
        modalOpen.addEventListener('click', function () {
            modal.classList.add('on');
        });
    }

    // 모달 닫기
    if (modalClose) {
        modalClose.addEventListener('click', function () {
            modal.classList.remove('on');
        });
    }

    // 모달 외부 클릭하면 모달 닫기
    window.onclick = function (event) {
        if (event.target == modal) {
            modal.classList.remove('on');
        }
    }

    signup.addEventListener('click', function () {
        modal.classList.remove('on');
        window.location.href = '/html/Login/signup.html';
    });

    findId.addEventListener('click', function () {
        modal.classList.remove('on');
        window.location.href = '/html/Login/findId.html';
    });

    findPassword.addEventListener('click', function () {
        modal.classList.remove('on');
        window.location.href = '/html/Login/findPassword.html';
    })
}