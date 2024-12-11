<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { useRoute } from "vue-router";

const route = useRoute();
const club = ref(null);
const isLoading = ref(true); // Для отображения состояния загрузки

onMounted(async () => {
    try {
        const { data } = await axios.get(
            `http://127.0.0.1:8000/clubs/${route.params.id}/`
        );
        club.value = data;
        isLoading.value = false; // Данные загружены
        console.log(data);
    } catch (error) {
        console.error("Error fetching club details:", error);
        isLoading.value = false; // Загрузка завершена с ошибкой
    }
});
</script>

<template>
    <div class="container_div">
        <div v-if="isLoading" class="loading">
            <p>Loading club details...</p>
        </div>

        <div v-else-if="club" class="club-detail">
            <h1>{{ club.name }}</h1>
            <img :src="club.emblem" alt="Emblem" class="club-emblem-detail" />
            <p>Country: {{ club.country }}</p>
            <p>League: {{ club.league }}</p>
            <p>Value: {{ club.value }} €</p>

            <h2>Players in {{ club.name }}</h2>

            <div class="players-grid">
                <div
                    class="player-card"
                    v-for="(player, index) in club.players"
                    :key="index"
                >
                    <img :src="player.photo" alt="" class="player-photo" />
                    <div class="player-info">
                        <h3>{{ player.name }}</h3>
                        <p>{{ player.position }}</p>
                    </div>
                </div>
            </div>

            <NuxtLink to="/" class="btn">Back to Clubs</NuxtLink>
        </div>

        <div v-else class="error-message">
            <p>Club not found or failed to load data.</p>
        </div>
    </div>
</template>

<style scoped>
.container_div {
    min-height: 100vh;
    min-width: 1200px;
    padding-left: 100px;
    padding-right: 100px;
}

.loading {
    padding-top: 50px;
    text-align: center;
    margin-top: 50px;
    font-size: 1.5rem;
    color: #555;
}

.error-message {
    text-align: center;
    margin-top: 50px;
    font-size: 1.5rem;
    color: #ef2757;
}

.club-detail {
    text-align: center;
    margin-bottom: 40px;
    padding-top: 50px;
}

.club-emblem-detail {
    max-width: 200px;
    height: auto;
    margin-bottom: 20px;
}

h1 {
    font-size: 2.5rem;
    color: #003580;
}

h2 {
    font-size: 2rem;
    margin-top: 30px;
    color: #003580;
}

.btn {
    display: inline-block;
    padding: 10px 20px;
    margin-top: 20px;
    background-color: #003580;
    color: white;
    text-decoration: none;
    border-radius: 5px;
    transition: background-color 0.3s ease;
}

.btn:hover {
    background-color: #ffd700;
    color: #003580;
}

.players-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 20px;
    margin-top: 40px;
}

.player-card {
    background-color: #fff;
    padding: 20px;
    border-radius: 0px;
    text-align: center;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease;
}

.player-card:hover {
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
}

.player-photo {
    max-width: 100%;
    height: auto;
    border-radius: 50%;
    margin-bottom: 15px;
    object-fit: cover;
}

.player-info h3 {
    font-size: 1.2rem;
    color: #003580;
    margin-bottom: 5px;
}

.player-info p {
    font-size: 1rem;
    color: #555;
}
</style>
