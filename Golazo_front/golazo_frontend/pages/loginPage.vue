<script setup>
import axios from "axios";
import { ref } from "vue";
import { useRouter } from "vue-router";

const username = ref("");
const password = ref("");
const errorMessage = ref("");
const router = useRouter();
const passwordVisible = ref(false);

const togglePasswordVisibility = () => {
    passwordVisible.value = !passwordVisible.value;
    const passwordInput = document.getElementById("password");
    if (passwordInput) {
        passwordInput.type = passwordVisible.value ? "text" : "password";
    }
};

const login = async () => {
    try {
        const response = await axios.post(
            "http://127.0.0.1:8000/user/api/token/",
            {
                username: username.value,
                password: password.value,
            }
        );

        if (response && response.data.access) {
            localStorage.setItem("authToken", response.data.access);
            localStorage.setItem("refreshToken", response.data.refresh); // Сохраняем refresh токен
            errorMessage.value = "";
            router.push("/"); // Перенаправление на главную страницу
        } else {
            errorMessage.value = "Invalid credentials. Please try again.";
        }
    } catch (error) {
        if (error.response && error.response.status === 401) {
            errorMessage.value = "Неверный логин или пароль.";
        } else {
            errorMessage.value = "Ошибка входа. Проверьте соединение.";
        }
        console.error("Ошибка авторизации:", error);
    }
};
</script>

<template>
    <div class="main_container">
        <div class="left_side">
            <div class="logo">GOLAZO</div>
            <div class="sign_form">
                <div class="texts">
                    <div class="main_text">Login with Golazo</div>
                    <div class="text2">
                        If you don’t have an account register
                    </div>
                    <div class="text3">
                        You can
                        <NuxtLink to="register">Register here !</NuxtLink>
                    </div>
                </div>

                <form method="POST" @submit.prevent="login">
                    <div class="label">User name</div>
                    <input
                        type="email"
                        id="email"
                        placeholder="Type your username here"
                        class="input-field"
                        v-model="username"
                        required
                    />
                    <div class="label">Enter your Password</div>
                    <div class="password-container">
                        <input
                            type="password"
                            id="password"
                            placeholder="Enter your password"
                            v-model="password"
                            class="input-field"
                            required
                        />
                        <img
                            src="../assets/eye_icon.svg"
                            alt=""
                            class="icon_eye"
                            @click="togglePasswordVisibility"
                        />
                    </div>
                </form>
                <span class="forgot_text">Forgot Password ?</span>
                <button type="submit" class="login_btn" @click="login">
                    Login
                </button>
                <div v-if="errorMessage" class="error">{{ errorMessage }}</div>
            </div>
        </div>
        <div class="right_side"></div>

        <div class="logo_img">
            <img src="../assets/ronaldo.jpg" alt="" />
        </div>
    </div>
</template>

<style scoped>
.error {
    margin-top: 10px;
    color: red;
}
.main_container {
    display: flex;
    height: 100vh;
}
.left_side {
    padding: 40px;
    width: 65%;
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}
.right_side {
    width: 35%;
    height: 100vh;
    background: rgba(10, 47, 182, 1);
}

.sign_form {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    gap: 20px;
}

.texts {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 20px;
}

.main_text {
    color: #000;
    font-family: "Open Sans";
    font-size: 35px;
    font-style: normal;
    font-weight: 600;
    line-height: normal;
}

.text2,
.text3 {
    color: #000;
    font-family: Poppins;
    font-size: 16px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
}
.to_sign {
    color: #0c21c1;
    font-family: Poppins;
    font-size: 16px;
    font-style: normal;
    font-weight: 600;
    line-height: normal;
}

.label {
    color: #263a43;
    font-family: "Nunito Sans";
    font-size: 20px;
    font-style: normal;
    font-weight: 600;
    line-height: 156.5%; /* 31.3px */
}

input {
    width: 399px;
    height: 70px;
    flex-shrink: 0;
    border-radius: 6px;
    border: 0.6px solid #b1b1b1;
    background: #fff;
    padding-left: 16px;
    transition: all 0.3s ease;
}

input {
    color: #000;
    font-family: "Nunito Sans";
    font-size: 17px;
    font-style: normal;
    font-weight: 300;
    line-height: 156.5%; /* 26.605px */
}

.input-field {
    border: 1px solid #ccc;
    border-radius: 6px;
    outline: none; /* Убираем стандартный фокус */
    transition: all 0.3s ease; /* Плавный переход */
}

/* Стили при фокусе */
.input-field:focus {
    border-color: #54e28d; /* Зеленая граница */
    border-bottom: 4px solid #54e28d; /* Зеленая полоска снизу */
    border-radius: 6px 6px 0 0; /* Оставляем радиус сверху */
}

.password-container {
    position: relative;
    width: 100%;
}

.icon_eye {
    position: absolute;
    right: 20px; /* Располагаем иконку справа */
    top: 50%;
    transform: translateY(-50%); /* Центрируем по вертикали */
    cursor: pointer;
}
.forgot_text {
    color: #8e8e8e;
    font-family: "Nunito Sans";
    font-size: 16px;
    font-style: normal;
    font-weight: 400;
    line-height: 156.5%; /* 25.04px */
}

.login_btn {
    margin-top: 20px;
    width: 399px;
    height: 70px;
    flex-shrink: 0;
    border-radius: 6px;
    background: #0a2fb6;
    box-shadow: 0px 4px 30px 0px rgba(38, 58, 67, 0.15);
    color: #fff;
    font-family: "Nunito Sans";
    font-size: 20px;
    font-style: normal;
    font-weight: 700;
    line-height: 156.5%; /* 31.3px */
}

form {
    display: flex;
    flex-direction: column;
    gap: 15px;
    margin-top: 20px;
}
#email {
    margin-bottom: 30px;
}

.logo {
    color: #0a2fb6;
    font-family: Roboto;
    font-size: 30px;
    font-style: normal;
    font-weight: 900;
    line-height: normal;
    position: absolute;
    top: 20px; /* отступ от верхнего края */
    left: 40px; /* отступ от левого края */
}

.logo_img {
    position: absolute;
    bottom: 20px; /* отступ от нижнего края */
    right: 60px; /* отступ от правого края */
    border-radius: 30px;
}

.logo_img img {
    width: 620px;
    height: 720px;
    border-radius: 30px;
}
</style>
