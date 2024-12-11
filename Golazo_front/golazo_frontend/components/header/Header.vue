<template>
    <header class="header">
        <nav class="navbar">
            <div class="navbar-container">
                <NuxtLink to="/" class="navbar-brand">Golazo</NuxtLink>
                <div
                    class="navbar-toggle"
                    id="navbar-toggle"
                    @click="toggleMenu"
                >
                    <span class="navbar-icon"></span>
                    <span class="navbar-icon"></span>
                    <span class="navbar-icon"></span>
                </div>
                <ul class="nav-menu" :class="{ active: isMenuActive }">
                    <li>
                        <NuxtLink
                            to="/players"
                            class="nav-link"
                            :class="{ active: activeLink === 'players' }"
                            @click="setActiveLink('players')"
                            >Players</NuxtLink
                        >
                    </li>
                    <li>
                        <NuxtLink
                            to="/coaches"
                            class="nav-link"
                            :class="{ active: activeLink === 'coaches' }"
                            @click="setActiveLink('coaches')"
                            >Coaches</NuxtLink
                        >
                    </li>
                    <li>
                        <NuxtLink
                            to="/clubs"
                            class="nav-link"
                            :class="{ active: activeLink === 'clubs' }"
                            @click="setActiveLink('clubs')"
                            >Clubs</NuxtLink
                        >
                    </li>
                    <li>
                        <NuxtLink
                            to="/leagues"
                            class="nav-link"
                            :class="{ active: activeLink === 'leagues' }"
                            @click="setActiveLink('leagues')"
                            >Leagues</NuxtLink
                        >
                    </li>
                    <li>
                        <NuxtLink
                            to="/matches"
                            class="nav-link"
                            :class="{ active: activeLink === 'matches' }"
                            @click="setActiveLink('matches')"
                            >Matches</NuxtLink
                        >
                    </li>
                    <li>
                        <NuxtLink
                            to="/articles"
                            class="nav-link"
                            :class="{ active: activeLink === 'articles' }"
                            @click="setActiveLink('articles')"
                            >Articles</NuxtLink
                        >
                    </li>
                    <li v-if="isAuthenticated">
                        <NuxtLink
                            to="/profile"
                            class="nav-link profile-icon"
                            :class="{
                                active: activeLink === 'profile',
                            }"
                            @click="setActiveLink('profile')"
                        >
                            <i class="bi bi-person-circle"></i> Profile
                        </NuxtLink>
                    </li>
                    <li v-if="!isAuthenticated">
                        <div class="log_and_sign">
                            <NuxtLink
                                to="/loginPage"
                                class="logIn_btn"
                                :class="{ active: activeLink === 'loginPage' }"
                                @click="setActiveLink('loginPage')"
                                >Log In</NuxtLink
                            >
                            <NuxtLink
                                to="/register"
                                class="signIn_btn"
                                :class="{ active: activeLink === 'register' }"
                                @click="setActiveLink('register')"
                                >Sign Up</NuxtLink
                            >
                        </div>
                    </li>
                </ul>
            </div>
        </nav>
    </header>
</template>

<script setup>
import { ref, onMounted, watch } from "vue";
import { useRoute } from "vue-router";

const route = useRoute();
const isMenuActive = ref(false);
const activeLink = ref("");
const isAuthenticated = ref(false);

onMounted(() => {
    const token = localStorage.getItem("authToken");
    isAuthenticated.value = !!token; // Если токен есть, считаем пользователя авторизованным
});

const setActiveLink = () => {
    const currentPath = route.path;
    if (currentPath.startsWith("/players")) activeLink.value = "players";
    else if (currentPath.startsWith("/coaches")) activeLink.value = "coaches";
    else if (currentPath.startsWith("/clubs")) activeLink.value = "clubs";
    else if (currentPath.startsWith("/leagues")) activeLink.value = "leagues";
    else if (currentPath.startsWith("/matches")) activeLink.value = "matches";
    else if (currentPath.startsWith("/articles")) activeLink.value = "articles";
    else if (currentPath.startsWith("/profile")) activeLink.value = "profile";
    else if (currentPath.startsWith("/loginPage"))
        activeLink.value = "loginPage";
    else if (currentPath.startsWith("/register")) activeLink.value = "register";
    else activeLink.value = "";
};

watch(route, setActiveLink, { immediate: true });

const toggleMenu = () => {
    isMenuActive.value = !isMenuActive.value;
};
</script>

<style scoped>
/* Основные стили шапки */
.header {
    position: sticky;
    top: 0;
    z-index: 1000;
    background: linear-gradient(90deg, #003580, #0044a8);
    padding: 15px 30px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

/* Стили для контейнера навигации */
.navbar-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 1200px;
    margin: 0 auto;
    width: 100%;
}

.navbar-brand {
    font-size: 2rem;
    font-weight: bold;
    color: white;
    text-decoration: none;
    text-transform: uppercase;
    letter-spacing: 2px;
    transition: color 0.3s;
}

.navbar-brand:hover {
    color: #ffd700;
}

/* Стили для меню */
.nav-menu {
    display: flex;
    gap: 30px;
    list-style: none;
    margin: 0;
    padding: 0;
}

.nav-menu li {
    position: relative;
}

.nav-link {
    color: white;
    text-decoration: none;
    font-size: 1.1rem;
    font-weight: 600;
    padding: 10px 15px;
    border-radius: 5px;
    transition: background-color 0.3s ease, color 0.3s ease;
    display: flex;
    align-items: center;
    gap: 5px;
}

.nav-link:hover {
    background-color: #ffd700;
    color: #003580;
}

/* Стили для активной ссылки */
.nav-link.active {
    background-color: #ffd700;
    color: #003580;
}

.profile-icon {
    display: flex;
    align-items: center;
    gap: 8px;
}

/* Адаптивность для мобильных устройств */
@media (max-width: 768px) {
    .nav-menu {
        display: none;
        flex-direction: column;
        gap: 20px;
        position: absolute;
        top: 70px;
        right: 30px;
        background-color: #003580;
        width: 250px;
        padding: 20px;
        border-radius: 10px;
    }

    .nav-menu.active {
        display: flex;
    }

    .navbar-toggle {
        display: flex;
    }
}

.log_and_sign {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;

    gap: 15px;
}

.logIn_btn {
    /* margin-top: 5px; */
    color: white;
    text-align: center;
    font-family: Poppins;
    font-size: 1.1rem;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
    text-decoration: none;
    display: flex;
    align-items: center;
    gap: 5px;
    position: relative;
}

.logIn_btn::after {
    content: "";
    position: absolute;
    bottom: -5px; /* Расстояние до нижнего края */
    left: 0;
    width: 0; /* Изначально скрыто */
    height: 3px; /* Толщина полоски */
    background-color: #ffd700; /* Жёлтый цвет */
    transition: width 0.3s ease; /* Плавный эффект */
}

.logIn_btn.active::after {
    width: 100%; /* Полоска становится видимой */
}

.signIn_btn {
    margin-top: 3px;
    text-align: center;
    text-decoration: none;
    border-radius: 8px;
    background: rgba(236, 188, 118, 1);
    color: #003580;
    text-align: center;
    font-family: Poppins;
    font-size: 1.1rem;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
    width: 120px;
    height: 40px;
    flex-shrink: 0;
    display: flex;
    align-items: center;
    justify-content: center;
}

.signIn_btn:hover {
    background: rgba(236, 188, 118, 0.8);
}
</style>
