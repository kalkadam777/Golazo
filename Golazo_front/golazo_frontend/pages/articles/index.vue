<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";

const articles = ref([]);

onMounted(async () => {
    try {
        const { data } = await axios.get("http://127.0.0.1:8000/articles/api/");
        articles.value = data.results;
    } catch (error) {
        console.log(error);
    }
});
</script>

<template>
    <div class="container2">
        <h2>Articles</h2>
        <div class="row">
            <div
                class="col-md-4"
                v-for="(article, index) in articles"
                :key="index"
            >
                <div class="card mb-4">
                    <img
                        :src="article.image"
                        class="card-img-top"
                        alt="Article Image"
                    />
                    <div class="card-body">
                        <h5 class="card-title">{{ article.title }}</h5>
                        <p class="card-text">
                            {{ article.content }}
                        </p>
                        <p class="text-muted">
                            By
                            {{
                                article.author
                                    ? article.author.username
                                    : "Unknown Author"
                            }}
                            on
                            {{ article.created_at }}
                        </p>
                        <a href="#" class="btn btn-primary">Read More</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.container2 {
    height: 100vh;
    margin-top: 20px;
    padding-left: 100px;
    padding-right: 100px;
}

h2 {
    margin-top: 20px;
    margin-bottom: 100px;
}
</style>
