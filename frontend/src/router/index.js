import {createWebHistory, createRouter} from "vue-router"
import HomeComponent from "../views/HomeComponent.vue"
import ArticlesComponent from "../views/ArticlesComponent.vue"

const routes = [
    {
        path: '/',
        name: 'Home',
        component: HomeComponent
    },
    {
        path: '/articles/:id',
        name: 'Articles',
        component: ArticlesComponent,
        props: true
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router