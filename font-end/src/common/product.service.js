import  { ApiService } from './api.service'
import {actionJWT} from './jwt.service'
export const ProductApiService = {
    async get (params){
            let json = await ApiService.query('product/',params)
            return json  
    },
    async post(params){
        let json = await ApiService.post('heart/post/',params)
        return json
    }
}
export const ProductAction = {
    async actionPostHeart(params){
        let json = ''
        await actionJWT.verifyTokenJWT().then(async ()=>{
            let jwt_token_access = localStorage.getItem('jwt_token_access')
            ApiService.setHeader(jwt_token_access)
            await ProductApiService.post(params).then((response)=>{
                json = response.data
            })
          })
        return json
    }
}