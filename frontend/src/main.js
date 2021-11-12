import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

createApp(App).use(router).mount('#app')

/* window.loaderFunction = function(el) {

    return new Vue({
        el: el,
        template: '<my-component></my-component>'
    })
} */
