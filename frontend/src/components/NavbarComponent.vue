<template>
    <nav>
        <div class="menu-item"><router-link :to="{name: 'Home'}">Home</router-link></div>
        <DropdownComponent title="Cryptocurrency News" :items="cryptoproviders" />
        <div class="menu-item"><router-link to="#">NFT News</router-link></div>
        <div class="menu-item"><router-link to="#">Web3 News</router-link></div>
        <div class="menu-item"><router-link to="#">Crypto Whitepapers</router-link></div>
    </nav>
</template>

<script>
import DropdownComponent from "../components/DropdownComponent.vue"
export default {
    name:'NavBar',
    components: {
        DropdownComponent
    },
    data() {
        return {
            cryptoproviders: [
                {
                    title: 'Cointelegraph News',
                    link: '/articles/cointelegraph',
                    id: 'cointelegraph',
                },
                {
                    title: 'Coinbase Blogs',
                    link: '/articles/coinbase',
                    id: 'coinbase',
                },
                {
                    title: 'Another RSS Feed',
                    link: '#',
                    id: '#'
                }
            ]
        }
    }
}
</script>

<style>
nav {
    display: flex;
    align-items: center;
    justify-content: center;
}

nav .menu-item {
    font-family: Avenir;
    color: white;
    padding: 10px 20px;
    position: relative;
    text-align: center;
    border-bottom: 3px solid transparent;
    display: flex;
    transition: 0.4s;
}

nav .menu-item.active,
nav .menu-item:hover {
    background-color: #444;
    border-bottom-color: #FF5858;
}

nav .menu-item a {
    color: inherit;
    text-decoration: none;
    padding: 4px;
    border-radius: 4px;
}

nav .menu-item a.router-link-exact-active {
    font-weight: bold;
}
</style>