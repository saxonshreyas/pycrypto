<template>
    <div class="home">
        <div class="menu">
            <header>
                <NavbarComponent/>
            </header>
        </div>
        <div class="articles">
            <ArticleListComponent :publisherName="id"/>
        </div>
    </div>
</template>

<script>
import NavbarComponent from "../components/NavbarComponent.vue"
import ArticleListComponent from "../components/ArticleListComponent.vue"
export default {
    name: "ArticlesComponent",
    components: {
        NavbarComponent,
        ArticleListComponent,
    },
    data() {
        return {
            id: this.$route.params.id
        }
    }
};
</script>

<style>
header {
  opacity: 80%;
  width:100vw;
  background-color:#2c3e50;
  padding:15px;
}
#articles {
  font-family: Avenir, Montserrat, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>