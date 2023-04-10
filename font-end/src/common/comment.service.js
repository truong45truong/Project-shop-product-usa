import {ApiService} from './api.service'
import {actionJWT} from './jwt.service'
export const CommentApiService = {
    async postComment (params){
        return await  ApiService.post('comment/',params)
    },
    async getCommentChild(params){
        return await  ApiService.query('comment/child/',params)
    },
    async postHeartComment(params) {
        return ApiService.post('comment/heart/',params)
    }
}
export const  CommentAction = {
    async actionPostComment(params){
        let json = ''
        let check = false
        let numberRequest = 0
        while(check == false && numberRequest < 2){
            numberRequest += 1
            let jwt_token_access = localStorage.getItem('jwt_token_access')
            ApiService.setHeader(jwt_token_access)
            await CommentApiService.postComment(params).then((response)=>{
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
    }
}