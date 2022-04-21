<template>
    <div class="article_container">
        <div class="article_content">
            <h1>Articles from {{publisher}}</h1>
            <ul class="article_list">
                <li v-for="article in articles" :key="article.uid">
                    <h2>{{ article.title }}</h2>
                    <p><b>{{article.pub_date}}</b> {{ article.description }}</p>
                    <button @click="readArticle(article)"> Read Article</button>
                    <button @click="likeArticle(article)">+1</button>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                // articles and publisher
                publisher: '',
                articles: ['']
            }
        },
        methods: {
            async getData() {
                try {
                    // fetch articles
                    this.axios.get('http://127.0.0.1:8000/news/newsapi/2/').then(response => {
                        this.articles = response.data;
                        if (this.articles.length > 0) {
                            this.publisher = this.articles[0].publisher
                        }
                    });
                } catch (error) {
                    // log the error
                    console.log(error);
                }
            },
            async readArticle(article){
                console.log(article.link)
                window.open(article.link, '_blank').focus()
            }
        },
        created() {
            // Fetch tasks on page load
            this.getData();
        }
    }
</script>