import  { ApiService } from './api.service'
import {actionJWT} from './jwt.service'
export const OrderApiService = {
    async get (){
        let json = await ApiService.query('order/')
        return json  
    },
    async getInfor (params){
        let json = await ApiService.query('order/infor',params)
        return json  
    },
    async getInforProduct(params){
        let json = await ApiService.query('order/infor/product',params)
        return json  
    },
    async getTransport (){
        let json = await ApiService.query('transport/')
        return json  
    },
    async get_order_today (){
        let json = await ApiService.query('order/today/')
        return json  
    },
    async getAllOrderBeWaitingPaid (){
        let json = await ApiService.query('order/paid/')
        return json  
    },
    async getAllOrderPaymented (){
        let json = await ApiService.query('order/paid/paymented')
        return json  
    },
    async getOrderCheckout (params){
        let json = await ApiService.query('order/checkout/',params)
        return json  
    },
    async updatePhoneOrderWaitingBePaid (params){
        let json = await ApiService.post('order/update/phone/',params)
        return json  
    },
    async updateVoucherOrderWaitungBePaid (params){
        let json = await ApiService.post('order/paid/voucher/update/',params)
        return json  
    },
    async updateAddressOrderWaitingBePaid (params){
        let json = await ApiService.post('order/update/address/',params)
        return json  
    },
    async updateTransport (params){
        let json = await ApiService.post('order/update/transport/',params)
        return json  
    },
    async addProductIntoOrder(params){
        let json = await ApiService.post('order/',params)
        return json
    },
    async createOrderWaitingBePaid(params){
        let json = await ApiService.post('order/paid/create',params)
        return json
    },
    async removeProductInOrder(params){
        let json = await ApiService.post('order/remove-product/',params)
        return json
    },
    async changQuantityProductInOrder(params){
        let json = await ApiService.post('order/change-quantity-product/',params)
        return json
    },
    async changeOrderToday(params){
        let json = await ApiService.post('order/change-order-today/',params)
        return json
    },
    async paymentSuccess(params){
        let json = await ApiService.post('order/payment/success',params)
        return json
    },
}
export const OrderAction = {
    async actionGetOrderCart(){
        let json = ''
        let check = false
        let numberRequest = 0
        while(check == false && numberRequest < 2){
            numberRequest += 1
            let jwt_token_access = localStorage.getItem('jwt_token_access')
            ApiService.setHeader(jwt_token_access)
            await OrderApiService.get().then((response)=>{
                json =  response.data
                console.log("actionGetOrderCart",response)
                check = true
            }, async (error) => {
                await actionJWT.refreshTokenJWT().then(response => {
                    if(response == 404){
                        check = true
                    }
                })
            })
        }
        return json
    },
    async getAllOrderBeWaitingPaid(){
        let json = ''
        let check = false
        let numberRequest = 0
        while(check == false && numberRequest < 2){
            numberRequest += 1
            let jwt_token_access = localStorage.getItem('jwt_token_access')
            ApiService.setHeader(jwt_token_access)
            await OrderApiService.getAllOrderBeWaitingPaid().then((response)=>{
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
        return json
    },
    async getOrderCheckout(params){
        let json = ''
        let check = false
        let numberRequest = 0
        while(check == false && numberRequest < 2){
            numberRequest += 1
            let jwt_token_access = localStorage.getItem('jwt_token_access')
            ApiService.setHeader(jwt_token_access)
            await OrderApiService.getOrderCheckout(params).then((response)=>{
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
        return json
    },
    async actionGetOrderToday(){
        let json = ''
        let check = false
        let numberRequest = 0
        while(check == false && numberRequest < 2){
            numberRequest += 1
            let jwt_token_access = localStorage.getItem('jwt_token_access')
            ApiService.setHeader(jwt_token_access)
            await OrderApiService.get_order_today().then((response)=>{
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
        return json
    },
    async actionAddToCart(params){
        let json = ''
        let numberRequest = 0
        let check = false
        while(check == false && numberRequest < 2){
            numberRequest += 1
            let jwt_token_access = localStorage.getItem('jwt_token_access')
            ApiService.setHeader(jwt_token_access)
            await OrderApiService.addProductIntoOrder(params).then((response)=>{
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
        return json
    },
    async createOrderWaitingBePaid(params){
        let json = ''
        let numberRequest = 0
        let check = false
        while(check == false && numberRequest < 2){
            numberRequest += 1
            let jwt_token_access = localStorage.getItem('jwt_token_access')
            ApiService.setHeader(jwt_token_access)
            await OrderApiService.createOrderWaitingBePaid(params).then((response)=>{
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
        return json
    },
    async updatePhoneOrderWaitingBePaid(params){
        let json = ''
        let numberRequest = 0
        let check = false
        while(check == false && numberRequest < 2){
            numberRequest += 1
            let jwt_token_access = localStorage.getItem('jwt_token_access')
            ApiService.setHeader(jwt_token_access)
            await OrderApiService.updatePhoneOrderWaitingBePaid(params).then((response)=>{
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
        return json
    },
    async updateVoucherOrderWaitungBePaid(params){
        let json = ''
        let numberRequest = 0
        let check = false
        while(check == false && numberRequest < 2){
            numberRequest += 1
            let jwt_token_access = localStorage.getItem('jwt_token_access')
            ApiService.setHeader(jwt_token_access)
            await OrderApiService.updateVoucherOrderWaitungBePaid(params).then((response)=>{
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
        return json
    },
    async updateAddressOrderWaitingBePaid(params){
        let json = ''
        let numberRequest = 0
        let check = false
        while(check == false && numberRequest < 2){
            numberRequest += 1
            let jwt_token_access = localStorage.getItem('jwt_token_access')
            ApiService.setHeader(jwt_token_access)
            await OrderApiService.updateAddressOrderWaitingBePaid(params).then((response)=>{
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
        return json
    },
    async updateTransport(params){
        let json = ''
        let numberRequest = 0
        let check = false
        while(check == false && numberRequest < 2){
            numberRequest += 1
            let jwt_token_access = localStorage.getItem('jwt_token_access')
            ApiService.setHeader(jwt_token_access)
            await OrderApiService.updateTransport(params).then((response)=>{
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
        return json
    },
    async actionRemoveProductInCart(params){
        let json = ''
        let check = false
        let numberRequest = 0
        while(check == false && numberRequest < 2){
            numberRequest += 1
            let jwt_token_access = localStorage.getItem('jwt_token_access')
            ApiService.setHeader(jwt_token_access)
            await OrderApiService.removeProductInOrder(params).then((response)=>{
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
        return json
    },
    async actionChangeQuantityProductInCart(params){
        let json = ''
        let check = false
        let numberRequest = 0
        while(check == false && numberRequest < 2){
            numberRequest += 1
            let jwt_token_access = localStorage.getItem('jwt_token_access')
            ApiService.setHeader(jwt_token_access)
            await OrderApiService.changQuantityProductInOrder(params).then((response)=>{
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
        return json
    },
    async actionChangeOrderToday(params){
        let json = ''
        let check = false
        let numberRequest = 0
        while(check == false && numberRequest < 2){
            numberRequest += 1
            let jwt_token_access = localStorage.getItem('jwt_token_access')
            ApiService.setHeader(jwt_token_access)
            await OrderApiService.changeOrderToday(params).then((response)=>{
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
        return json
    },
    async paymentSuccess(params) {
        let json = ''
        let check = false
        let numberRequest = 0
        while(check == false && numberRequest < 2){
            numberRequest += 1
            let jwt_token_access = localStorage.getItem('jwt_token_access')
            ApiService.setHeader(jwt_token_access)
            await OrderApiService.paymentSuccess(params).then((response)=>{
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
        return json
    },
    async getAllOrderPaymented (){
        let json = ''
        let check = false
        let numberRequest = 0
        while(check == false && numberRequest < 2){
            numberRequest += 1
            let jwt_token_access = localStorage.getItem('jwt_token_access')
            ApiService.setHeader(jwt_token_access)
            await OrderApiService.getAllOrderPaymented().then((response)=>{
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
        return json
    },
    async getInfor(params) {
        let json = ''
        let check = false
        let numberRequest = 0
        while(check == false && numberRequest < 2){
            numberRequest += 1
            let jwt_token_access = localStorage.getItem('jwt_token_access')
            ApiService.setHeader(jwt_token_access)
            await OrderApiService.getInfor(params).then((response)=>{
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
        return json
    },
    async getInforProduct(params) {
        let json = ''
        let check = false
        let numberRequest = 0
        while(check == false && numberRequest < 2){
            numberRequest += 1
            let jwt_token_access = localStorage.getItem('jwt_token_access')
            ApiService.setHeader(jwt_token_access)
            await OrderApiService.getInforProduct(params).then((response)=>{
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
        return json
    },
}