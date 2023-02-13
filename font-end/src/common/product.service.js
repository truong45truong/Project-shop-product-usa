import  { ApiService } from './api.service'
export const ProductApiService = {
    async get (params){
            let json = await ApiService.query('product/',params)
            return json  
    },
}