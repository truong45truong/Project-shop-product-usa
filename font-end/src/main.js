import { createApp } from "vue";
import { createPinia } from "pinia";
import { createStore } from 'vuex';
import App from "./App.vue";
import router from "./router";
import { library ,dom } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { fab } from '@fortawesome/free-brands-svg-icons';
import { far } from '@fortawesome/free-regular-svg-icons';
// Import Bootstrap and BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import './assets/Roboto/Roboto-Regular.ttf'
import './assets/Sassy_Frass/SassyFrass-Regular.ttf'
// Make BootstrapVue available throughout your project
import storeConfig from './stores/index'

import {ApiService } from './common/api.service'
library.add(fas, far, fab)
dom.watch();
const app = createApp(App);
const store = createStore(storeConfig)
export default app;
app.component('font-awesome-icon', FontAwesomeIcon)
ApiService.init()
app.use(createPinia());
app.use(router);
app.use(store)
// Optionally install the BootstrapVue icon components plugin
app.mount("#app");
