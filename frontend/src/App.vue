<template>
  <div id="app">
    <header>
      <Navbar/>
    </header>
    <div id="articles">
      <ArticlesComponent />
    </div>
  </div>
</template>
<script>
import ArticlesComponent from "./components/ArticlesComponent.vue";
import Navbar from "./components/NavbarComponent.vue"
export default {
  name: "App",
  components: {
    Navbar,
    ArticlesComponent,
  },
};
</script>
<style>
#articles {
  font-family: Avenir, Montserrat, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

header {
  opacity: 80%;
  width:100vw;
  background-color:#2c3e50;
  padding:15px;
}
</style>