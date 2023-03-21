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
        let numberRequest = 0
        let check = false
        while(check == false && numberRequest < 2){
            numberRequest += 1
            let jwt_token_access = localStorage.getItem('jwt_token_access')
            ApiService.setHeader(jwt_token_access)
            await VoucherApiService.get(params).then((response)=>{
                console.log(response)
                json =  response.data
                check = true
            }, async (error) => {
                await actionJWT.refreshTokenJWT().then(response => {
                    if(response == 404){
                        check = true
                    }
                })
            })
        }
        return json;
    },
}