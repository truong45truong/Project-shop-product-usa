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
    },
    async getProductHeart(params){
        let json = await ApiService.query('product-heart/')
        return json
    },
    async getProductCategory(params) {
        let json = await ApiService.query('product-category/',params)
        return json  
    },
    async searchProduct(params) {
        let json = await ApiService.query('product/search/',params)
        return json  
    },
    async searchProductCategory(params) {
        let json = await ApiService.query('product/search-product-category/',params)
        return json  
    },
}
export const ProductAction = {
    async actionPostHeart(params){
        let json = ''
        let check = false
        let numberRequest = 0
        while(check == false && numberRequest < 2){
            numberRequest += 1
            let jwt_token_access = localStorage.getItem('jwt_token_access')
            ApiService.setHeader(jwt_token_access)
            await ProductApiService.post(params).then((response)=>{
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
    async actionGetProductHeart(params){
        let json = ''
        let check = false
        let numberRequest = 0
        while(check == false && numberRequest < 2){
            numberRequest += 1
            let jwt_token_access = localStorage.getItem('jwt_token_access')
            ApiService.setHeader(jwt_token_access)
            await ProductApiService.getProductHeart().then((response)=>{
                json =  response.data.data
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
    async actionGetProductCategory(params){
        let json = ''
        let check = false
        let numberRequest = 0
        while(check == false && numberRequest < 2){
            numberRequest += 1
            let jwt_token_access = localStorage.getItem('jwt_token_access')
            ApiService.setHeader(jwt_token_access)
            await ProductApiService.getProductCategory(params).then((response)=>{
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
        return json
    }
}