<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";

const valuablePlayers = ref([]);
const youngPlayers = ref([]);

onMounted(async () => {
    try {
        const { data } = await axios.get(
            "http://127.0.0.1:8000/players/valuable/"
        );
        valuablePlayers.value = data.results;
        console.log(data);
    } catch (error) {
        console.error(error);
    }

    try {
        const { data } = await axios.get(
            "http://127.0.0.1:8000/players/young/"
        );
        youngPlayers.value = data.results;
        console.log(data);
    } catch (error) {
        console.error(error);
    }
});
</script>

<template>
    <div class="player-lists">
        <h2>Самые ценные игроки</h2>
        <div class="player-list-grid">
            <div
                class="player-item"
                v-for="(player, index) in valuablePlayers"
                :key="index"
            >
                <img :src="player.photo" alt="" />
                <!-- <img src="../public/favicon.ico" alt="No Image" /> -->
                <div class="player-info">
                    <h3>{{ player.name }}</h3>
                    <p>{{ player.position }}</p>
                    <div class="player-club">
                        <img :src="player.current_club.emblem" alt="" />
                        <p>{{ player.current_club.name }}</p>
                    </div>
                    <p class="player-value">{{ player.value }}млн €</p>
                </div>
            </div>
        </div>

        <h2>Самые молодые игроки</h2>
        <div class="player-list-grid">
            <div
                class="player-item"
                v-for="(player, index) in youngPlayers"
                :key="index"
            >
                <img :src="player.photo" alt="" />
                <div class="player-info">
                    <h3>{{ player.name }}</h3>
                    <p>{{ player.position }}</p>
                    <div class="player-club">
                        <img :src="player.current_club.emblem" alt="" />
                        <p>{{ player.current_club.name }}</p>
                    </div>
                    <p class="player-age">{{ player.age }} лет</p>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.players-list {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
}

.player-item {
    background-color: #fff;
    padding: 20px;
    box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
    text-align: center;
    transition: all 0.3s ease;
}

.player-item:hover {
    box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.2);
}

.player-item a {
    text-decoration: none;
    font-size: 1.2rem;
    font-weight: bold;
    color: #003580;
}

.player-item img {
    max-width: 100%;
    height: auto;
    margin-bottom: 15px;
}

.player-lists {
    margin: 40px auto;
    max-width: 1200px;
}

.player-lists h2 {
    color: #003580;
}

.player-list-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 20px;
    padding-top: 30px;
    padding-bottom: 20px;
}

.player-item {
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 0px;
    padding: 15px;
    text-align: center;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
}

.player-item img {
    width: 100%;
    height: 200px;
    border-radius: 0%;
}

.player-info {
    margin-top: 10px;
}

.player-info h3 {
    font-size: 1.2rem;
    color: #003580;
    margin: 5px 0;
}

.player-info p {
    margin: 5px 0;
    color: #555;
}

.player-club {
    display: flex;
    align-items: center;
    justify-content: center;
}

.player-club img {
    width: 40px;
    height: 40px;
    margin-right: 10px;
}

.player-value,
.player-age {
    font-weight: bold;
    color: #003580;
    margin-top: 5px;
}

h2 {
    font-size: 1.8rem;
    color: #003580;
    margin-bottom: 20px;
    text-transform: uppercase;
}
</style>
