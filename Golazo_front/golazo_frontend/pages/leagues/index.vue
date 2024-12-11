<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";

const leagues = ref([]);
const isLoading = ref(true);

onMounted(async () => {
    try {
        const { data } = await axios.get(
            "http://127.0.0.1:8000/leagues/leagues/"
        );
        leagues.value = data.results;
    } catch (error) {
        console.error("Ошибка загрузки лиг:", error);
    } finally {
        isLoading.value = false;
    }
});
</script>

<template>
    <div class="container my-5 min-vh-100">
        <h1 class="text-center mb-4">Football Leagues</h1>

        <div v-if="isLoading" class="text-center">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
        </div>

        <div v-else class="row g-4">
            <div
                class="col-md-6 col-lg-4"
                v-for="league in leagues"
                :key="league.id"
            >
                <div class="card shadow-sm h-100">
                    <img
                        :src="league.logo"
                        :alt="`${league.name} Logo`"
                        class="card-img-top p-3"
                        style="height: 180px; object-fit: contain"
                    />
                    <div class="card-body">
                        <h5 class="card-title">{{ league.name }}</h5>
                        <p class="card-text text-muted">
                            Country: <strong>{{ league.country }}</strong>
                        </p>
                        <p class="card-text">
                            <strong>Season:</strong> {{ league.start_date }} -
                            {{ league.end_date }}
                        </p>
                    </div>
                    <div class="card-footer text-center bg-light">
                        <button class="btn btn-primary">View Details</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.card {
    border-radius: 15px;
    overflow: hidden;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.15);
}

.card-img-top {
    background-color: #f8f9fa;
    border-bottom: 1px solid #ddd;
}

.card-title {
    font-size: 1.25rem;
    font-weight: bold;
    color: #003580;
}

.card-text {
    font-size: 0.95rem;
}
</style>
