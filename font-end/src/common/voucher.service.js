import  { ApiService } from './api.service'
import {actionJWT} from './jwt.service'
export const VoucherApiService = {
    async get (params){
        let json = await ApiService.query('voucher/',params)
        return json  
    },

}
export const VoucherAction = {
    async actionGetVoucher(params){
        let json = ''
        await actionJWT.verifyTokenJWT().then(async ()=>{
            let jwt_token_access = localStorage.getItem('jwt_token_access')
            ApiService.setHeader(jwt_token_access)
            await VoucherApiService.get(params).then((response)=>{
                json = response.data
            })
          })
        return json
    },
}