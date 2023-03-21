import {ApiService} from './api.service'

export const decryptRsaApiService = {
    async decryptToken (params){
        return  await ApiService.post('token-decryt-rsa/',params)
    },
}