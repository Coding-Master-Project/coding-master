function checkForm() {
    const idInput = document.querySelector('.nickname-input');
    const emailInput = document.querySelector('.email-input');

    const idError = document.querySelector('.nicknameAlert');
    const emailError1 = document.querySelector('.emailAlert');
    const emailError2 = document.querySelector('.emailAlert_Validator');

    const findIdBtn = document.querySelector('.findBtn');

    const id = idInput.value;
    const email = emailInput.value;
    const emailPattern = /^[A-Za-z0-9_\.\-]+@[A-Za-z0-9\-]+\.[A-za-z0-9\-]+/.test(email);

    let validForm = true;

    if (!id) {
        idError.style.display = 'block';
        validForm = false;
    }
    else
        idError.style.display = 'none';

    if (!email && !emailPattern) {
        emailError1.style.display = 'block';
        emailError2.style.display = 'none';
        validForm = false;
    }
    else if (email && !emailPattern) {
        emailError1.style.display = 'none';
        emailError2.style.display = 'block';
        validForm = false;
    }
    else {
        emailError1.style.display = 'none';
        emailError1.style.display = 'none';
    }

    return validForm;
}
