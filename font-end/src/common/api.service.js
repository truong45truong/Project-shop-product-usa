import app from './../main'
import axios from "axios";
import VueAxios from "vue-axios";
//import JwtService from "./jwt.service";
import API_URL  from "./config";

const getCookie = (name) => {
    let value = "; " + document.cookie;
    let parts = value.split("; " + name + "=");
    if (parts.length === 2) return parts.pop().split(";").shift();
  }
  
const csrfToken = getCookie('csrftoken');
const ApiService = {
    init() {
        app.use(VueAxios, axios)
        axios.defaults.baseURL = API_URL
    },
    setHeader(jwt_token) {
        console.log(document.cookie)
        app.axios.defaults.headers.common[
            "Authorization"
        ] = `Bearer ${jwt_token}`;
        app.axios.defaults.headers.common['X-CSRFToken'] = csrfToken;
    },
    query(resource, params) {
        return app.axios.get(`${resource}`,params).catch(error => {
            throw new Error(`[RWV] ApiService ${error}`);
        });
    },

    get(resource, slug = "") {
        return app.axios.get(`${resource}/${slug}`).catch(error => {
            throw new Error(`[RWV] ApiService ${error}`);
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
export default ApiService;