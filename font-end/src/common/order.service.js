import  { ApiService } from './api.service'
import {actionJWT} from './jwt.service'
export const OrderApiService = {
    async get (params){
        let json = await ApiService.query('order/',params)
        return json  
    },
    async addProductIntoOrder(params){
        let json = await ApiService.post('order/',params)
        return json
    },
    async removeProductInOrder(params){
        let json = await ApiService.post('order/remove-product/',params)
        return json
    },
}
export const OrderAction = {
    async actionGetOrderCart(params){
        let json = ''
        await actionJWT.verifyTokenJWT().then(async ()=>{
            let jwt_token_access = localStorage.getItem('jwt_token_access')
            ApiService.setHeader(jwt_token_access)
            await OrderApiService.get(params).then((response)=>{
                json = response.data
            })
          })
        return json
    },
    async actionAddToCart(params){
        let json = false
        await actionJWT.verifyTokenJWT().then(async ()=>{
            let jwt_token_access = localStorage.getItem('jwt_token_access')
            ApiService.setHeader(jwt_token_access)
            await OrderApiService.addProductIntoOrder(params).then((response)=>{
              json = response.data
            })
          })
        return json
    },
    async actionRemoveProductInCart(params){
        let json = false
        await actionJWT.verifyTokenJWT().then(async ()=>{
            let jwt_token_access = localStorage.getItem('jwt_token_access')
            ApiService.setHeader(jwt_token_access)
            await OrderApiService.removeProductInOrder(params).then((response)=>{
              json = response.data
            })
          })
        return json
    }
}