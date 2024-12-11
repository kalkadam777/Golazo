export default defineNuxtRouteMiddleware(() => {
    const token = localStorage.getItem("authToken");

    if (!token) {
        return navigateTo("/login"); // Перенаправление на страницу логина
    }
});
