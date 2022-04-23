<template>
    <div class="article_container">
        <div class="article_content">
            <h1>Articles from {{publisher}}</h1>
            <ul class="article_list" style="list-style: none;">
                <li v-for="article in articles" :key="article.uid">
                    <h2>{{ article.title }}</h2>
                    <p><b>{{article.pub_date}}</b> {{ article.description }}</p>
                    <button class = "Read" style = "margin-right: 10px;" @click="readArticle(article)"> Read Article</button>
                    <button class = "Like" @click="likeArticle(article)">+1</button>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
    const publisherIDMappings = {
        'cointelegraph':'1',
        'coinbase':'2'
    }
    export default {
        props: ['publisherName'],
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
                    const pubID = publisherIDMappings[this.$props.publisherName] // should convert cointelegraph to 1 
                    const urltofetch = 'http://127.0.0.1:8000/news/newsapi/' + pubID + '/'
                    this.axios.get(urltofetch).then(response => {
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
