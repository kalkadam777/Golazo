<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { useRoute } from "vue-router";

const route = useRoute();
const player = ref({});
const isLoading = ref(true);

onMounted(async () => {
    try {
        const { id } = route.params; // Получаем ID из URL
        const { data } = await axios.get(
            `http://127.0.0.1:8000/players/${id}/`
        );
        player.value = data;
        console.log(data);
        isLoading.value = false;
    } catch (error) {
        console.error("Ошибка при загрузке игрока:", error);
        isLoading.value = false;
    }

    try {
        const { id } = route.params; // Получаем ID из URL
        const { data } = await axios.get(
            `http://127.0.0.1:8000/players/${id}/`
        );
        player.value = data;
        console.log(data);
        isLoading.value = false;
    } catch (error) {
        console.error("Ошибка при загрузке игрока:", error);
        isLoading.value = false;
    }
});
</script>

<template>
    <div class="container my-5 min-vh-100">
        <div class="row">
            <!-- Player Photo Section -->
            <div class="col-md-4 text-center">
                <img
                    :src="player.photo"
                    alt=""
                    class="img-fluid rounded mb-4"
                    style="max-width: 100%"
                />
            </div>

            <!-- Player Info Section -->
            <div class="col-md-8">
                <h1 class="mb-3">{{ player.name }}</h1>
                <h4 class="text-muted mb-4">{{ player.position }}</h4>
                <ul class="list-group mb-4">
                    <li class="list-group-item">
                        <strong>Current Club:</strong>
                        {{ player.current_club?.name || "Not Available" }}
                    </li>
                    <li class="list-group-item">
                        <strong>Country:</strong> {{ player.country }}
                    </li>
                    <li class="list-group-item">
                        <strong>Value:</strong> {{ player.value }} €
                    </li>
                    <li class="list-group-item">
                        <strong>Age:</strong> {{ player.age }}
                    </li>
                    <li class="list-group-item">
                        <strong>Goals:</strong> {{ player.goals }}
                    </li>
                    <li class="list-group-item">
                        <strong>Assists:</strong> {{ player.assists }}
                    </li>
                </ul>

                <!-- Back to Players List Button -->
                <NuxtLink to="/players" class="btn btn-primary">
                    Back to Players List
                </NuxtLink>
            </div>
        </div>

        <table class="table">
            <thead class="thead-dark">
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">First</th>
                    <th scope="col">Last</th>
                    <th scope="col">Handle</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <th scope="row">1</th>
                    <td>Mark</td>
                    <td>Otto</td>
                    <td>@mdo</td>
                </tr>
                <tr>
                    <th scope="row">2</th>
                    <td>Jacob</td>
                    <td>Thornton</td>
                    <td>@fat</td>
                </tr>
                <tr>
                    <th scope="row">3</th>
                    <td>Larry</td>
                    <td>the Bird</td>
                    <td>@twitter</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<style scoped>
.table {
    margin-top: 50px;
}
</style>
