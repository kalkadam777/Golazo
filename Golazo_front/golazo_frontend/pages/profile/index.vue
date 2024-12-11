<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";

// Example user data (can be replaced with an API call)
const user = ref({
    name: "Daulet Darmen",
    email: "Daulet777@example.com",
    avatar: "../../assets/images/avatar.jpg",
    bio: "Football enthusiast and software developer. Passionate about sports analytics and creating amazing web apps.",
    stats: {
        matches: 120,
        goals: 45,
        assists: 30,
    },
    socialLinks: {
        twitter: "https://twitter.com/johndoe",
        instagram: "https://instagram.com/johndoe",
    },
});

const router = useRouter();

const logout = () => {
    localStorage.removeItem("authToken");
    router.push("/login");
};

onMounted(() => {
    // Here you can load user data from API
    // axios.get('/api/user/profile').then(response => user.value = response.data)
});
</script>

<template>
    <div class="container py-5 min-vh-100">
        <!-- Profile Card -->
        <div class="card shadow-lg rounded-lg overflow-hidden">
            <div class="card-header bg-primary text-white">
                <div class="d-flex align-items-center">
                    <img
                        src="../../assets/dauka.jpg"
                        alt="User Avatar"
                        class="rounded-circle me-3"
                        width="100"
                        height="100"
                    />
                    <div>
                        <h2 class="mb-0">{{ user.name }}</h2>
                        <p class="mb-0">{{ user.email }}</p>
                    </div>
                </div>
            </div>

            <!-- Profile Content -->
            <div class="card-body">
                <h4 class="card-title mb-4">About Me</h4>
                <p class="card-text text-muted">{{ user.bio }}</p>

                <!-- Stats -->
                <div class="row row-cols-1 row-cols-md-3 g-4 mt-4">
                    <div class="col">
                        <div class="card text-center">
                            <div class="card-body">
                                <h5 class="card-title text-primary">
                                    {{ user.stats.matches }}
                                </h5>
                                <p class="card-text">Matches Played</p>
                            </div>
                        </div>
                    </div>
                    <div class="col">
                        <div class="card text-center">
                            <div class="card-body">
                                <h5 class="card-title text-success">
                                    {{ user.stats.goals }}
                                </h5>
                                <p class="card-text">Goals Scored</p>
                            </div>
                        </div>
                    </div>
                    <div class="col">
                        <div class="card text-center">
                            <div class="card-body">
                                <h5 class="card-title text-warning">
                                    {{ user.stats.assists }}
                                </h5>
                                <p class="card-text">Assists Made</p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Social Links -->
                <div class="mt-4">
                    <h4 class="mb-3">Connect With Me</h4>
                    <div class="d-flex gap-3">
                        <a
                            v-if="user.socialLinks.twitter"
                            :href="user.socialLinks.twitter"
                            target="_blank"
                            class="btn btn-outline-info"
                        >
                            <i class="bi bi-twitter"></i> Twitter
                        </a>
                        <a
                            v-if="user.socialLinks.instagram"
                            :href="user.socialLinks.instagram"
                            target="_blank"
                            class="btn btn-outline-danger"
                        >
                            <i class="bi bi-instagram"></i> Instagram
                        </a>
                    </div>
                </div>

                <!-- Actions -->
                <div class="mt-4 d-flex justify-content-end gap-3">
                    <button class="btn btn-warning">
                        <i class="bi bi-pencil"></i> Edit Profile
                    </button>
                    <button class="btn btn-danger" @click="logout">
                        <i class="bi bi-box-arrow-right"></i> Logout
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
/* Scoped CSS */
.card-header {
    background-color: #0056b3;
    border-bottom: 4px solid #004085;
}

.card-title {
    font-size: 1.5rem;
    font-weight: bold;
}

.card-body {
    background-color: #f8f9fa;
}

.card-body .card-title {
    font-size: 1.25rem;
    font-weight: bold;
}

.card-body .card-text {
    font-size: 1rem;
}

.btn-outline-info,
.btn-outline-danger {
    font-size: 1rem;
    padding: 0.75rem 1.25rem;
}

.card-body i {
    margin-right: 0.5rem;
}

/* Customize avatar */
img.rounded-circle {
    border: 4px solid white;
}

@media (max-width: 768px) {
    .card-header {
        text-align: center;
    }
}
</style>
