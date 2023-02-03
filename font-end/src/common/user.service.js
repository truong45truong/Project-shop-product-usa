import ApiService from './api.service'

export const UserApiService = {
    async get (params){
        return  await ApiService.query('user/',params)
    },

    async reggisterUser (params){
        return await  ApiService.post('user/',params)
    }
}