import {ApiService}from './api.service'
import {actionJWT} from './jwt.service'
export const BlogApiService = {
    async get (params){
        return  await ApiService.query('blog/',params)
    },

    async postBlog (params){
        return await  ApiService.post('blog/',params)
    },
    async getBlogProduct (params){
        return await  ApiService.query('blog/product/',params)
    },
    async postHeartBlog(params){
        return await  ApiService.post('blog/heart/',params)
    }
}
export const blogAction = {
    async actionHeartBlog(params){
        let json = ''
        let check = false
        let numberRequest = 0
        while(check == false && numberRequest < 2){
            numberRequest += 1
            let jwt_token_access = localStorage.getItem('jwt_token_access')
            ApiService.setHeader(jwt_token_access)
            await BlogApiService.postHeartBlog(params).then((response)=>{
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