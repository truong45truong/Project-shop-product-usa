import {ApiService} from './api.service'


export const jwtService = {
    async refeshToken (jwt_token_refresh){
        let json = await ApiService.post('token/refresh/')
        console.log("refresh token",json)
        return json
    }
}

export const actionJWT =  {
    async refreshTokenJWT() {
        let status
        let jwt_token_refresh = localStorage.getItem('jwt_token_refresh')
        await jwtService.refeshToken(jwt_token_refresh).then(res => {
            localStorage.setItem('jwt_token_access',res.data.access_token);
            status = res.data.status
        })
        return status
    }
}
