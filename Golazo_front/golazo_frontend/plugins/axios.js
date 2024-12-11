// plugins/axios.js
import axios from "axios";

export default defineNuxtPlugin((nuxtApp) => {
    const instance = axios.create({
        baseURL: "http://127.0.0.1:8000", // Замените на ваш URL
    });

    // Добавляем интерсепторы, если нужно
    instance.interceptors.request.use(
        (config) => {
            // Пример: добавление токена из localStorage
            const token = localStorage.getItem("authToken");
            if (token) {
                config.headers.Authorization = `Token ${token}`;
            }
            return config;
        },
        (error) => {
            return Promise.reject(error);
        }
    );

    nuxtApp.provide("axios", instance);
});
