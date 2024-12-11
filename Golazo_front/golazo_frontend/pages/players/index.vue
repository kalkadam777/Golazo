<script setup>
import { ref, computed, onMounted, watch } from "vue";
import axios from "axios";

const players = ref([]);
const isLoading = ref(true);
const currentPage = ref(1);
const totalPages = ref(42); // Обновите это значение динамически
const searchQuery = ref("");
const position = ref("");
const minValue = ref(0);
const maxValue = ref(100000000);

// const fetchPlayers = async (page = 1) => {
//     try {
//         const { data } = await axios.get(
//             http://127.0.0.1:8000/players/?page=${page}
//         );
//         players.value = data.results;
//         currentPage.value = data.current_page;
//         totalPages.value = data.total_pages;
//         isLoading.value = false;
//     } catch (error) {
//         console.error("Error fetching players:", error);
//     }
// };

const fetchPlayers = async (page = 1) => {
    isLoading.value = true;
    try {
        // Формируем параметры запроса
        const params = {
            search: searchQuery.value,
        };

        // Запрашиваем данные у API
        const { data } = await axios.get(
            `http://127.0.0.1:8000/players/?page=${page}`,
            {
                params,
            }
        );

        players.value = data.results;
        currentPage.value = data.current_page;
        totalPages.value = data.total_pages;
    } catch (error) {
        console.error("Ошибка при загрузке игроков:", error);
    } finally {
        isLoading.value = false;
    }
};

watch([searchQuery, position, minValue, maxValue], fetchPlayers);

onMounted(fetchPlayers);

const goToPage = (page) => {
    if (page >= 1 && page <= totalPages.value) {
        fetchPlayers(page);
    }
};

const visiblePages = computed(() => {
    const pages = [];
    const range = 2; // Количество страниц, видимых слева и справа от текущей
    const start = Math.max(currentPage.value - range, 1);
    const end = Math.min(currentPage.value + range, totalPages.value);

    for (let i = start; i <= end; i++) {
        pages.push(i);
    }

    return pages;
});

// Fetch initial data
// fetchPlayers();
</script>

<template>
    <div class="container">
        <h1 class="my-5">Players</h1>

        <form
            method="GET"
            action=""
            class="row g-4 p-4 bg-light rounded shadow-sm"
        >
            <!-- Поле поиска -->
            <div class="col-md-6">
                <label for="searchQuery" class="form-label fw-bold"
                    >Поиск игроков:</label
                >
                <div class="input-group">
                    <span class="input-group-text bg-primary text-white">
                        <i class="bi bi-search"></i>
                    </span>
                    <input
                        id="searchQuery"
                        type="text"
                        name="q"
                        class="form-control"
                        v-model="searchQuery"
                        placeholder="Введите имя игрока..."
                    />
                </div>
            </div>

            <!-- Фильтр по позиции -->
            <div class="col-md-3">
                <label for="position" class="form-label fw-bold"
                    >Позиция:</label
                >
                <select id="position" name="position" class="form-select">
                    <option value="">Все позиции</option>
                    <option value="GK">Вратарь</option>
                    <option value="DF">Защитник</option>
                    <option value="MF">Полузащитник</option>
                    <option value="FW">Нападающий</option>
                </select>
            </div>

            <!-- Фильтр по минимальной стоимости -->
            <div class="col-md-3">
                <label for="min_value" class="form-label fw-bold">
                    Минимальная стоимость (€):
                </label>
                <input
                    type="range"
                    id="min_value"
                    name="min_value"
                    min="0"
                    max="100000000"
                    step="100000"
                    class="form-range"
                    oninput="minValueOutput.textContent = this.value + ' €'"
                />
                <span
                    id="minValueOutput"
                    class="form-text text-muted d-block text-center mt-1"
                >
                    0 €
                </span>
            </div>

            <!-- Фильтр по максимальной стоимости -->
            <div class="col-md-3">
                <label for="max_value" class="form-label fw-bold">
                    Максимальная стоимость (€):
                </label>
                <input
                    type="range"
                    id="max_value"
                    name="max_value"
                    min="0"
                    max="100000000"
                    step="100000"
                    class="form-range"
                    oninput="maxValueOutput.textContent = this.value + ' €'"
                />
                <span
                    id="maxValueOutput"
                    class="form-text text-muted d-block text-center mt-1"
                >
                    100,000,000 €
                </span>
            </div>

            <!-- Кнопка фильтрации -->
            <div class="col-12 d-flex justify-content-end">
                <button type="submit" class="btn btn-primary px-4 py-2">
                    <i class="bi bi-funnel"></i> Применить фильтры
                </button>
            </div>
        </form>
        <!-- <div v-if="isLoading" class="spinner">Loading...</div> -->

        <!-- <div v-else> -->
        <!-- Список игроков -->
        <div class="row mt-4" v-auto-animate>
            <div
                class="col-md-4 mb-4"
                v-for="(player, index) in players"
                :key="index"
            >
                <div class="card shadow-sm h-100">
                    <div class="row g-0">
                        <!-- Фотография игрока -->
                        <div class="col-4">
                            <img
                                :src="player.photo"
                                alt="Player Photo"
                                class="img-fluid rounded-start"
                                style="height: 160px; width: auto"
                            />
                        </div>
                        <!-- Информация об игроке -->
                        <div class="col-8">
                            <div class="card-body">
                                <h5 class="card-title">
                                    <NuxtLink
                                        :to="`/players/${player.id}`"
                                        class="text-decoration-none"
                                    >
                                        {{ player.name }}
                                    </NuxtLink>
                                </h5>
                                <p class="card-text">
                                    <strong>Position:</strong>
                                    {{ player.position }} <br />
                                    <strong>Value:</strong>
                                    {{ player.value }} €
                                </p>
                                <NuxtLink
                                    :to="`/players/${player.id}`"
                                    class="btn btn-outline-primary"
                                >
                                    View Details
                                </NuxtLink>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Пагинация -->
        <nav class="mt-4">
            <ul class="pagination justify-content-center">
                <!-- Кнопка для перехода на первую страницу -->
                <li class="page-item" :class="{ disabled: currentPage === 1 }">
                    <button
                        class="page-link"
                        @click="goToPage(1)"
                        :disabled="currentPage === 1"
                    >
                        &laquo; First
                    </button>
                </li>

                <!-- Кнопка "Предыдущая" -->
                <li class="page-item" :class="{ disabled: currentPage === 1 }">
                    <button
                        class="page-link"
                        @click="goToPage(currentPage - 1)"
                        :disabled="currentPage === 1"
                    >
                        Previous
                    </button>
                </li>

                <!-- Видимые страницы -->
                <li
                    v-for="page in visiblePages"
                    :key="page"
                    class="page-item"
                    :class="{ active: currentPage === page }"
                >
                    <button
                        class="page-link"
                        @click="goToPage(page)"
                        :disabled="currentPage === page"
                    >
                        {{ page }}
                    </button>
                </li>

                <!-- Кнопка "Следующая" -->
                <li
                    class="page-item"
                    :class="{ disabled: currentPage === totalPages }"
                >
                    <button
                        class="page-link"
                        @click="goToPage(currentPage + 1)"
                        :disabled="currentPage === totalPages"
                    >
                        Next
                    </button>
                </li>

                <!-- Кнопка для перехода на последнюю страницу -->
                <li
                    class="page-item"
                    :class="{ disabled: currentPage === totalPages }"
                >
                    <button
                        class="page-link"
                        @click="goToPage(totalPages)"
                        :disabled="currentPage === totalPages"
                    >
                        Last &raquo;
                    </button>
                </li>
            </ul>
        </nav>
        <!-- </div> -->
    </div>
</template>

<style scoped>
.form-label {
    font-weight: bold;
    color: #003580;
}

input[type="range"]::-webkit-slider-thumb {
    background-color: #003580;
    border: 2px solid #ffd700;
    width: 16px;
    height: 16px;
    border-radius: 50%;
    cursor: pointer;
}

input[type="range"]::-webkit-slider-runnable-track {
    background: linear-gradient(90deg, #ffd700, #003580);
    height: 4px;
    border-radius: 2px;
}
.spinner {
    text-align: center;
    font-size: 1.5rem;
    color: #003580;
    margin-top: 50px;
}
.pagination .page-item.active .page-link {
    background-color: #003580;
    color: white;
    border-color: #003580;
}

.pagination .page-item.disabled .page-link {
    cursor: not-allowed;
    opacity: 0.6;
}

.pagination .page-link {
    color: #003580;
    border: 1px solid #ddd;
    padding: 8px 15px;
    border-radius: 5px;
    transition: background-color 0.3s ease;
}

.pagination .page-link:hover {
    background-color: #ffd700;
    color: #003580;
}
</style>
