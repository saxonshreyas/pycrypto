import { createApp } from 'vue'
import App from './App.vue'
// import Axios
import axios from 'axios'
import router from './router'

const app = createApp(App)
app.use(router)
app.config.globalProperties.axios = axios
app.mount('#app')