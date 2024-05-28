document.addEventListener('DOMContentLoaded', function () {
    // 닉네임
    const nicknameCheckButton = document.querySelector('.NicknameExistenceChecker');
    const nicknameAlert_e = document.querySelector('.NicknameExistenceAlert');
    const nicknameAlert_c = document.querySelector('.NicknameCheckerAlert');
    const nicknameInput = document.querySelector('.signup-nickname');
    let nicknameClickCount = 0;

    // 아이디
    const idCheckButton = document.querySelector('.IdExistenceChecker');
    const idAlert_e = document.querySelector('.IdExistenceAlert');
    const idAlert_c = document.querySelector('.IdCheckerAlert');
    const idInput = document.querySelector('.signup-id');
    let idClickCount = 0;

    // 비밀번호
    const passwordInput = document.querySelector('.signup-password');
    const passwordCheckInput = document.querySelector('.signup-password-check');
    const passwordCheckAlert = document.querySelector('.PasswordCheckValidator');

    const condition1 = document.querySelector('.condition1');
    const condition2 = document.querySelector('.condition2');
    const condition3 = document.querySelector('.condition3');

    const icon1 = condition1.querySelector('i');
    const icon2 = condition2.querySelector('i');
    const icon3 = condition3.querySelector('i');

    let flag1 = 0;
    let flag2 = 0;
    let flag3 = 0;

    let flag = 0;

    // 이메일
    const emailInput = document.querySelector('.signup-email');
    const emailAlert_e = document.querySelector('.EmailExistenceAlert');
    const emailAlert_v = document.querySelector('.EmailValidator');

    // 회원가입 버튼
    const submitButtn = document.querySelector('.signupBtn');


    // 이벤트
    // 닉네임 중복확인 버튼 클릭 이벤트
    nicknameCheckButton.addEventListener('click', validateNickname);

    // 아이디 중복확인 버튼 클릭 이벤트
    idCheckButton.addEventListener('click', validateId);

    // 비밀번호 조건 이벤트
    passwordInput.addEventListener('input', function () {
        validatePassword();
        if (flag == 1)
            validatePasswordCheck();
    });

    // 비밀번호 확인 이벤트
    passwordCheckInput.addEventListener('input', function () {
        validatePasswordCheck();
        flag = 1;
    })

    // 이메일 유효성 검사 이벤트
    emailInput.addEventListener('input', validateEmail);

    // 제출 검사 이벤트
    submitButtn.addEventListener('click', function () {
        // 닉네임
        if (!nicknameInput.value || nicknameInput.style.border != '2px solid green') {
            nicknameInput.focus();
            return;
        }

        // 아이디
        if (!idInput.value || idInput.style.border != '2px solid green') {
            idInput.focus();
            return;
        }

        // 비밀번호
        if (!passwordInput.value || passwordInput.style.border != '2px solid green') {
            passwordInput.focus();
            return;
        }

        // 비밀번호 확인
        if (!passwordCheckInput.value || passwordCheckInput.style.border != '2px solid green') {
            passwordCheckInput.focus();
            return;
        }

        // 이메일
        if (!emailInput.value || emailInput.style.border != '2px solid green') {
            emailInput.focus();
            return;
        }

        history.back();
        document.querySelector('.signup-container').submit();
    });


    // 함수
    // 닉네임 중복 확인 버튼 클릭 함수
    function validateNickname() {
        nicknameClickCount++;

        if (nicknameClickCount === 1) {
            nicknameAlert_e.style.display = 'block';
        } else if (nicknameClickCount === 2) {
            nicknameInput.style.border = '2px solid green';
            nicknameAlert_e.style.display = 'none';
        } else {
            nicknameInput.style.border = '1px solid gray';
            nicknameClickCount = 0;
        }
    }

    // 아이디 중복 확인 버튼 클릭 함수
    function validateId() {
        idClickCount++;

        if (idClickCount == 1)
            idAlert_e.style.display = 'block';
        else if (idClickCount == 2) {
            idInput.style.border = '2px solid green';
            idAlert_e.style.display = 'none';
        }
        else {
            idInput.style.border = '1px solid gray';
            idClickCount = 0;
        }
    }

    // 비밀번호 조건 확인 함수
    function validatePassword() {
        const password = passwordInput.value;

        if (password.length > 0) {
            // 영문/숫자/특수문자 중, 2가지 이상 포함
            const hasLetter = /[a-zA-Z]/.test(password);
            const hasNumber = /[0-9]/.test(password);
            const hasSpecial = /[^a-zA-Z0-9]/.test(password);
            if (hasLetter && hasNumber && hasSpecial) {
                condition1.style.color = 'green';
                icon1.classList.remove('fa-xmark');
                icon1.classList.add('fa-check');
                flag1 = 1;
            } else {
                condition1.style.color = 'red';
                icon1.classList.remove('fa-check');
                icon1.classList.add('fa-xmark');
                flag1 = 0;
            }

            // 8자 이상 30자 이하 입력 (공백 제외)
            if (password.length >= 8 && password.length <= 30 && !/\s/.test(password)) {
                condition2.style.color = 'green';
                icon2.classList.remove('fa-xmark');
                icon2.classList.add('fa-check');
                flag2 = 1;
            }
            else {
                condition2.style.color = 'red';
                icon2.classList.remove('fa-check');
                icon2.classList.add('fa-xmark');
                flag2 = 0;
            }

            // 연속 3자 이상 동일한 문자/숫자 제외
            const noThreeConsecutive = !/(.)\1\1/.test(password);
            if (noThreeConsecutive) {
                condition3.style.color = 'green';
                icon3.classList.remove('fa-xmark');
                icon3.classList.add('fa-check');
                flag3 = 1;
            }
            else {
                condition3.style.color = 'red';
                icon3.classList.remove('fa-check');
                icon3.classList.add('fa-xmark');
                flag3 = 0;
            }
        }
        else {
            condition1.style.color = '';
            condition2.style.color = '';
            condition3.style.color = '';
            icon1.classList.remove('fa-xmark');
            icon1.classList.add('fa-check');
            icon2.classList.remove('fa-xmark');
            icon2.classList.add('fa-check');
            icon3.classList.remove('fa-xmark');
            icon3.classList.add('fa-check');
            flag1 = 0;
            flag2 = 0;
            flag3 = 0;
        }
        if (flag1 == 1 && flag2 == 1 && flag3 == 1)
            passwordInput.style.border = '2px solid green';
        else {
            passwordInput.style.border = '';
        }
    }

    // 비밀번호 확인 함수
    function validatePasswordCheck() {
        const password = passwordInput.value;
        const passwordCheck = passwordCheckInput.value;

        if (password == passwordCheck && passwordCheck.length > 0) {
            passwordCheckInput.style.border = '2px solid green';
            passwordCheckAlert.style.display = 'none';
        }
        else {
            passwordCheckInput.style.border = '';
            passwordCheckAlert.style.display = 'block';
        }
    }

    // 이메일 유효성 검사 함수
    function validateEmail() {
        const email = emailInput.value;
        const emailPattern = /^[A-Za-z0-9_\.\-]+@[A-Za-z0-9\-]+\.[A-za-z0-9\-]+/.test(email);

        if (!emailPattern && email.length > 0) {
            emailAlert_e.style.display = 'block';
            emailAlert_v.style.display = 'block';
            emailInput.style.border = '';
        }
        else {
            emailAlert_e.style.display = 'none';
            emailAlert_v.style.display = 'none';
            emailInput.style.border = '2px solid green';
            if (email.length == 0)
                emailInput.style.border = '';
        }
    }
});