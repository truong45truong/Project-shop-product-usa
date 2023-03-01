import axios from "axios";


class AxiosService {
    constructor(){
        const instance = axios.create()
        this.instance = instance
    }
    get(url , params){
        return this.instance.get(url , params)
    }

    post(url , params , newConfig){
        return this.instance.post(url , params , newConfig)
    }
}

const newAxiosService = new AxiosService();

export default newAxiosService;