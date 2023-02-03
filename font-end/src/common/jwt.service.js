import ApiService from './api.service'


export const jwtService = {
    async refeshToken (jwt_token_refresh){
        let json = await ApiService.post('token/refresh/',{
            "refresh" : jwt_token_refresh
        })
        return json
    },
    async getToken (params){
        let json = await ApiService.post('token/',{
            "username" : params.params.username,
            "password" : params.params.password
        })
        return json
    },
    async verifyToken(jwt_token_access){
        let json = await ApiService.post('token/verify/',{
            "token" : jwt_token_access
        })
        return json
    }
}

export const actionJWT =  {
    async setLocalTokenJWT (params) {
        return await jwtService.getToken(params).then(res=>{
            localStorage.setItem('jwt_token_access',res.data.access);
            localStorage.setItem('jwt_token_refresh',res.data.refresh);
            ApiService.setHeader(res.data.access)
        })
    },
    async refreshTokenJWT() {
        console.log("refresh runing")
        let jwt_token_refresh = localStorage.getItem('jwt_token_refresh')
        console.log("jwt_token_refresh before",jwt_token_refresh)
        return await jwtService.refeshToken(jwt_token_refresh).then(res => {
            localStorage.setItem('jwt_token_access',res.data.access);
            console.log("jwt_token_refresh",res.data.access)
        })
    },
    async verifyTokenJWT(){
        let jwt_token_access = localStorage.getItem('jwt_token_access')
        return await jwtService.verifyToken(jwt_token_access).catch(async (res)=>{
              console.log("checktoken res",res.response.status)
              if(res.response.status === 401){
                await this.refreshTokenJWT()
              }
            }
          )
    }
}
