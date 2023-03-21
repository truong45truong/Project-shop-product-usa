import app from './../main'
import axios from "axios";
import VueAxios from "vue-axios";
//import JwtService from "./jwt.service";
import API_URL  from "./config";

export const ApiService = {
    init() {
        app.use(VueAxios, axios)
        axios.defaults.baseURL = API_URL
        axios.defaults.withCredentials = true;
        console.log(axios.defaults)
    },
    setHeader() {
        app.axios.defaults.headers.common[
            "Authorization"
        ] = `Bearer ${localStorage.getItem("jwt_token_access")}`;
        //app.axios.defaults.headers.common["Cookie"] = 'tabstyle=html-tab; csrftoken='+csrf_token; 
    },
    getCookie(){
        console.log("app.axios.defaults.headers",app.axios.defaults.headers)
        return app.axios.defaults.headers['set-cookie']
    },
    query(resource, params) {
        return app.axios.get(`${resource}`,params).catch(error => {
            throw new Error(`[RWV] ApiService ${error}`);
        });
    },

    get(resource, slug = "") {
        return app.axios.get(`${resource}/${slug}`).catch(error => {
            return;
        });
    },

    post(resource, params) {
        return app.axios.post(`${resource}`, params);
    },

    update(resource, slug, params) {
        return app.axios.put(`${resource}/${slug}`, params);
    },

    put(resource, params) {
        return app.axios.put(`${resource}`, params);
    },

    delete(resource) {
        return app.axios.delete(resource).catch(error => {
            throw new Error(`[RWV] ApiService ${error}`);
        });
    }

}
