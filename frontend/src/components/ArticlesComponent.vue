<template>
    <div class="article_container">
        <div class="article_content">
            <h1>Articles</h1>
            <ul class="article_list">
                <li v-for="article in articles" :key="article.uid">
                    <h2>{{ article.title }}</h2>
                    <p>{{ article.description }}</p>
                    <button @click="readArticle(article)"> Read Article</button>
                    <button @click="likeArticle(article)">+1</button>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>

    console.log("Hello")

    export default {
        data() {
            return {
                // articles
                articles: ['']
            }
        },
        methods: {
            async getData() {
                try {
                    // fetch articles
                    this.axios.get('http://127.0.0.1:8000/news/newsapi/').then(response => (this.articles = response.data)); 
                } catch (error) {
                    // log the error
                    console.log(error);
                }
            },
        },
        created() {
            // Fetch tasks on page load
            this.getData();
        }
    }
</script>