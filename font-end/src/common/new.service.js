import { ApiService } from './api.service'
import  { actionJWT } from './jwt.service'
export const NewApiService = {
    async get (params){
        return  await ApiService.query('new/')
    },
}

export const actionNew = {
    async get_new(){
        let json = []
            await NewApiService.get().then((response)=>{
                json = response
            })
        return json
    }
}