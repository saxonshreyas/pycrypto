<template>
    <nav>
        <div class="menu-item"><a href="#">Home</a></div>
        <DropdownComponent title="Cryptocurrency News" :items="cryptoproviders" />
        <div class="menu-item"><a href="#">NFT News</a></div>
        <div class="menu-item"><a href="#">Web3 News</a></div>
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
                    link: '#'
                },
                {
                    title: 'Coinbase Blogs',
                    link: '#'
                },
                {
                    title: 'Another RSS Feed',
                    link: '#'
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
}
</style>