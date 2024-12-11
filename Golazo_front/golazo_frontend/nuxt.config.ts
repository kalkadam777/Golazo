// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    compatibilityDate: "2024-11-01",
    devtools: { enabled: true },
    modules: ["@vueuse/nuxt", "usebootstrap", "@formkit/auto-animate/nuxt"],
    css: ["@/assets/global.css", "bootstrap-icons/font/bootstrap-icons.css"],
    plugins: ["~/plugins/axios.js"],
});
