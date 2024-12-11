<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";

const clubs = ref([]);
const isLoading = ref(false);
const currentPage = ref(1);
const totalPages = ref(1);

const fetchClubs = async (page = 1) => {
    isLoading.value = true;
    try {
        const { data } = await axios.get("http://127.0.0.1:8000/clubs/", {
            params: { page },
        });
        clubs.value = data.results;
        totalPages.value = Math.ceil(data.count / 10); // API count divided by page size (default 10)
        currentPage.value = page;
    } catch (error) {
        console.error("Error fetching clubs:", error);
    } finally {
        isLoading.value = false;
    }
};

const goToPage = (page) => {
    if (page >= 1 && page <= totalPages.value) {
        fetchClubs(page);
    }
};

onMounted(() => fetchClubs());
</script>

<template>
    <div class="container2">
        <section class="section-clubs">
            <div class="clubs-header">
                <h1>Discover the Best Football Clubs</h1>
            </div>

            <div v-if="isLoading" class="text-center my-5">
                <div class="spinner-border text-primary" role="status">
                    <span class="visually-hidden">Loading...</span>
                </div>
            </div>

            <div v-else>
                <ul class="clubs-list" v-auto-animate>
                    <li
                        class="club-card"
                        v-for="(club, index) in clubs"
                        :key="index"
                    >
                        <NuxtLink :to="`/clubs/${club.id}`" class="link_nuxt">
                            <img
                                :src="club.emblem"
                                alt=" Emblem"
                                class="club-logo"
                            />
                            <div class="club-details">
                                <p class="club-link">{{ club.name }}</p>
                                <p class="club-info">
                                    {{ club.league }} - {{ club.value }} €
                                </p>
                            </div>
                        </NuxtLink>
                    </li>
                </ul>

                <!-- Пагинация -->
                <nav v-if="totalPages > 1" class="mt-4">
                    <ul class="pagination justify-content-center">
                        <!-- Кнопка для перехода на первую страницу -->
                        <li
                            class="page-item"
                            :class="{ disabled: currentPage === 1 }"
                        >
                            <button
                                class="page-link"
                                @click="goToPage(1)"
                                :disabled="currentPage === 1"
                            >
                                &laquo; First
                            </button>
                        </li>

                        <!-- Кнопка "Предыдущая" -->
                        <li
                            class="page-item"
                            :class="{ disabled: currentPage === 1 }"
                        >
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
                            v-for="page in totalPages"
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
            </div>
        </section>
    </div>
</template>

<style scoped>
.container2 {
    margin-top: 50px;
    max-width: 1200px;
    margin: 0 auto;
}

.link_nuxt {
    text-decoration: none;
}

.section-clubs {
    margin-top: 50px;
}

.clubs-header h1 {
    text-align: center;
    font-size: 2.5rem;
    color: #003580;
    margin-bottom: 30px;
    font-weight: bold;
    letter-spacing: 1px;
}

.clubs-list {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 20px;
    list-style-type: none;
    padding: 0;
}

.club-card {
    background-color: #fff;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    text-align: center;
    padding: 20px;
}

.club-logo {
    width: 120px;
    height: 100px;
    border-radius: 0%;
    margin-bottom: 15px;
}

.club-details {
    text-align: center;
}

.club-link {
    font-size: 1.3rem;
    color: #003580;
    font-weight: bold;
    text-decoration: none;
    transition: color 0.3s ease;
}

.club-link:hover {
    color: #0056b3;
}

.club-info {
    font-size: 1rem;
    color: #777;
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
