<template>
    <div class="home">
        <div class="menu">
            <header>
                <NavbarComponent/>
            </header>
        </div>
        <div class="body">
            <h1>Welcome to the pyCrypto News Aggregator!</h1>
            <p> This is a news aggregator containing information about the latest cryptocurrency, NFT and Web3 News. 
                We are also currently working on releasing information on crypto whitepapers so you can keep up to date with the latest information on the future!</p>
            <b>For any concerns about the quality of the website, please contact Shreyas S at the email <a href="mailto:saxonshreyas@gmail.com">saxonshreyas@gmail.com</a></b>
        </div>
    </div>
</template>

<script>
import NavbarComponent from "../components/NavbarComponent.vue"
export default {
    name: "HomeComponent",
    components: {
        NavbarComponent,
    },
};
</script>

<style>
header {
  opacity: 80%;
  width:100vw;
  background-color:#2c3e50;
  padding: 0px;
  margin: 0px;
}
</style>