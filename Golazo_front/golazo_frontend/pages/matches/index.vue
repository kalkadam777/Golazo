<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";

const matches = ref([]);
const isLoading = ref(true);

onMounted(async () => {
    try {
        const { data } = await axios.get(
            "http://127.0.0.1:8000/leagues/matches/"
        );
        matches.value = data.results;
    } catch (error) {
        console.error("Ошибка загрузки матчей:", error);
    } finally {
        isLoading.value = false;
    }
});

const formatDate = (date) => {
    return new Date(date).toLocaleDateString("en-US", {
        year: "numeric",
        month: "long",
        day: "numeric",
    });
};
</script>

<template>
    <div class="container py-4">
        <h1 class="text-center my-4">Upcoming Matches</h1>

        <div v-if="isLoading" class="text-center my-5">
            <div class="spinner-border" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
        </div>

        <div v-else>
            <div v-if="matches.length === 0" class="alert alert-warning">
                No matches found.
            </div>

            <div class="row g-3">
                <div
                    class="col-md-6 col-lg-4"
                    v-for="match in matches"
                    :key="match.id"
                >
                    <div class="card shadow-sm">
                        <div class="card-body">
                            <h5 class="card-title">
                                {{ match.home_team }} vs {{ match.away_team }}
                            </h5>
                            <p class="card-text">
                                <strong>Date:</strong>
                                {{ formatDate(match.match_date) }}
                            </p>
                            <p class="card-text">
                                <strong>League ID:</strong> {{ match.league }}
                            </p>
                            <p class="card-text">
                                <strong>Score:</strong>
                                {{ match.home_team_score }} -
                                {{ match.away_team_score }}
                            </p>
                            <NuxtLink class="btn btn-primary btn-sm">
                                View Details
                            </NuxtLink>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.card-title {
    font-size: 1.2rem;
    font-weight: bold;
}

.card-text {
    font-size: 0.95rem;
    margin-bottom: 0.5rem;
}

.spinner-border {
    width: 3rem;
    height: 3rem;
}
</style>
