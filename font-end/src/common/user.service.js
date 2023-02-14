import {ApiService} from './api.service'
import {actionJWT} from './jwt.service'
export const UserApiService = {
    async get (params){
        return  await ApiService.query('user/',params)
    },

    async reggisterUser (params){
        return await  ApiService.post('register-user/',params)
    },

    async getInfor (params){
        return await ApiService.query('get-infor-user/',params)
    },
    async createAddress(params){
        return await  ApiService.post('address-user/',params)
    },
    async deleteAddress(params){
        return await ApiService.post('address-user/delete/',params)
    }
}
export const actionUser = {
    async getInforUser(params){
        let infor = false
        await actionJWT.verifyTokenJWT().then(async ()=>{
            let jwt_token_access = localStorage.getItem('jwt_token_access')
            ApiService.setHeader(jwt_token_access)
            await UserApiService.getInfor(params).then((response)=>{
              infor = response.data
            })
          })
        return infor
    },
    async createAdressUser(params){
        let json = false
        await actionJWT.verifyTokenJWT().then(async ()=>{
            let jwt_token_access = localStorage.getItem('jwt_token_access')
            ApiService.setHeader(jwt_token_access)
            await UserApiService.createAddress(params).then((response)=>{
              json = response.data
            })
          })
        return json
    },
    async deteleAddressUser(params) {
        let json = false
        await actionJWT.verifyTokenJWT().then(async ()=>{
            let jwt_token_access = localStorage.getItem('jwt_token_access')
            ApiService.setHeader(jwt_token_access)
            await UserApiService.deleteAddress(params).then((response)=>{
              json = response.data
            })
          })
        return json
    }
}