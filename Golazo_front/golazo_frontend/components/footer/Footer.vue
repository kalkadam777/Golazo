<script></script>

<template>
    <div class="footer">
        <div class="container footer-content">
            <div class="footer-logo">
                <p>&copy; 2024 Golazo | Your Ultimate Football Hub</p>
            </div>
            <ul class="footer-links">
                <li><NuxtLink to="/players">Players</NuxtLink></li>
                <li><NuxtLink to="/clubs">Clubs</NuxtLink></li>
                <li><NuxtLink to="/about">About Us</NuxtLink></li>
            </ul>
        </div>
    </div>
</template>

<style scoped>
.footer {
    background: linear-gradient(90deg, #002b5c, #003580, #0044a8);
    color: white;
    padding: 30px 0;
    text-align: center;
    box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.1);
}

.footer-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 20px;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

.footer-logo {
    flex: 1;
    font-size: 1rem;
    font-family: "Arial", sans-serif;
    text-align: left;
}

.footer-links {
    flex: 1;
    display: flex;
    justify-content: flex-end;
    list-style: none;
    gap: 20px;
    padding: 0;
    margin: 0;
}

.footer-links li a {
    color: #ffd700;
    text-decoration: none;
    font-size: 1rem;
    font-weight: 600;
    transition: color 0.3s ease, transform 0.3s ease;
}

.footer-links li a:hover {
    color: #ffffff;
    transform: scale(1.1);
}

.footer-logo p {
    margin: 0;
    font-size: 1rem;
}

@media (max-width: 768px) {
    .footer-content {
        flex-direction: column;
        text-align: center;
        gap: 15px;
    }

    .footer-logo,
    .footer-links {
        flex: unset;
    }
}

@media (max-width: 480px) {
    .footer-links {
        flex-direction: column;
        gap: 10px;
    }

    .footer-links li a {
        font-size: 0.9rem;
    }
}
</style>
