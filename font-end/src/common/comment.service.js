import {ApiService} from './api.service'
import {actionJWT} from './jwt.service'
export const CommentApiService = {
    async postCommentBlog (params){
        return await  ApiService.post('comment/blog/',params)
    },
    async postCommentProduct (params){
        return await  ApiService.post('comment/product/create/',params)
    },
    async getCommentChild(params){
        return await  ApiService.query('comment/child/',params)
    },
    async getCommentProduct(params){
        return await  ApiService.query('comment/product/',params)
    },
    async postHeartComment(params) {
        return ApiService.post('comment/heart/',params)
    },
    async editComment(params){
        return ApiService.post('comment/edit/',params)
    },
    async deleteComment(params){
        return ApiService.post('comment/delete/',params)
    }
}
export const  CommentAction = {
    async actionPostCommentBlog(params){
        let json = ''
        let check = false
        let numberRequest = 0
        while(check == false && numberRequest < 2){
            numberRequest += 1
            let jwt_token_access = localStorage.getItem('jwt_token_access')
            ApiService.setHeader(jwt_token_access)
            await CommentApiService.postCommentBlog(params).then((response)=>{
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
    async actionPostCommentProduct(params){
        let json = ''
        let check = false
        let numberRequest = 0
        while(check == false && numberRequest < 2){
            numberRequest += 1
            let jwt_token_access = localStorage.getItem('jwt_token_access')
            ApiService.setHeader(jwt_token_access)
            await CommentApiService.postCommentProduct(params).then((response)=>{
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
    async actionHeartComment(params){
        let json = ''
        let check = false
        let numberRequest = 0
        while(check == false && numberRequest < 2){
            numberRequest += 1
            let jwt_token_access = localStorage.getItem('jwt_token_access')
            ApiService.setHeader(jwt_token_access)
            await CommentApiService.postHeartComment(params).then((response)=>{
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
    async actionEditComment(params){
        let json = ''
        let check = false
        let numberRequest = 0
        while(check == false && numberRequest < 2){
            numberRequest += 1
            let jwt_token_access = localStorage.getItem('jwt_token_access')
            ApiService.setHeader(jwt_token_access)
            await CommentApiService.editComment(params).then((response)=>{
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
    async actionDeleteComment(params){
        let json = ''
        let check = false
        let numberRequest = 0
        while(check == false && numberRequest < 2){
            numberRequest += 1
            let jwt_token_access = localStorage.getItem('jwt_token_access')
            ApiService.setHeader(jwt_token_access)
            await CommentApiService.deleteComment(params).then((response)=>{
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