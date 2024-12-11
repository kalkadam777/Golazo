<script setup>
import { ref, onMounted } from "vue";
import { Chart, registerables } from "chart.js";

Chart.register(...registerables);

const chartRef = ref(null);
const myChart = ref(null);

const createChart = () => {
    const ctx = chartRef.value.getContext("2d");
    myChart.value = new Chart(ctx, {
        type: "bar",
        data: {
            labels: [
                "Real Madrid",
                "Bayern Munchin",
                "Barcelona",
                "Arsenal",
                "PSG",
                "Monaco",
            ],
            datasets: [
                {
                    label: "Cost of the teams",
                    data: [120, 190, 300, 500, 200, 300],
                    backgroundColor: [
                        "rgba(255, 99, 132, 0.2)",
                        "rgba(54, 162, 235, 0.2)",
                        "rgba(255, 206, 86, 0.2)",
                        "rgba(75, 192, 192, 0.2)",
                        "rgba(153, 102, 255, 0.2)",
                        "rgba(255, 159, 64, 0.2)",
                    ],
                    borderColor: [
                        "rgba(255, 99, 132, 1)",
                        "rgba(54, 162, 235, 1)",
                        "rgba(255, 206, 86, 1)",
                        "rgba(75, 192, 192, 1)",
                        "rgba(153, 102, 255, 1)",
                        "rgba(255, 159, 64, 1)",
                    ],
                    borderWidth: 1,
                },
            ],
        },
        options: {
            responsive: true,
            maintainAspectRatio: false, // Отключает автоматическое соотношение сторон
            scales: {
                y: {
                    beginAtZero: true,
                },
            },
        },
    });
};

onMounted(() => {
    createChart();
});
</script>

<template>
    <div class="chart-container">
        <canvas ref="chartRef"></canvas>
    </div>
</template>

<style scoped>
.chart-container {
    width: 100%; /* Заполняет ширину родительского контейнера */
    height: 800px; /* Увеличиваем высоту диаграммы */
    margin: auto;
    padding: 20px;
    background-color: #f8f9fa;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}
</style>
