// JavaScript for toggling between Login and Register forms
document.addEventListener('DOMContentLoaded', function() {
    const loginBtn = document.querySelector('.login-btn');
    const registerBtn = document.querySelector('.register-btn');
    const btnActiveBack = document.querySelector('.btn-active-back');
    const loginForm = document.querySelector('.login-form');
    const registerForm = document.querySelector('.register-form');
  
    loginBtn.addEventListener('click', function() {
        loginForm.style.left = '0%';
        registerForm.style.left = '200%';
        btnActiveBack.style.left = '0%';
    });
  
    registerBtn.addEventListener('click', function() {
        loginForm.style.left = '-200%';
        registerForm.style.left = '0%';
        btnActiveBack.style.left = '50%';
    });
  });
  