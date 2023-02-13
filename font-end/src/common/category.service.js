import {ApiService} from './api.service'

export const CategoryApiService = {
    async get (params){
        return  await ApiService.query('category/',params)
    },
}