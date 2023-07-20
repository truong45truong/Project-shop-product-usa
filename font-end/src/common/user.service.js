import { ApiService } from "./api.service";
import { actionJWT } from "./jwt.service";
/* -------------------------------------------------------------------------- */
/*                                 API SERVICE                                */
/* -------------------------------------------------------------------------- */
export const UserApiService = {
  getCookie(){
    return ApiService.getCookie()
  },
  async get(params) {
    return await ApiService.query("user/", params);
  },
  async postUploadPhoto(params) {
    return await ApiService.post("upload-photo/", params);
  },
  async uploadInformation(params) {
    return await ApiService.post("upload-info/", params);
  },
  async getPhoneUser() {
    return await ApiService.query("phone-user/");
  },
  async getAddressUser() {
    return await ApiService.query("address-user/");
  },
  async setPhoneDefault(params) {
    return await ApiService.post("phone-user/default", params);
  },
  async loginUser(params) {
    return await ApiService.post("login/", params);
  },
  async logoutUser(params) {
    return await ApiService.post("logout/", params);
  },
  async reggisterUser(params) {
    return await ApiService.post("register-user/", params);
  },

  async getInfor(params) {
    return await ApiService.query("get-infor-user/", params);
  },
  async createAddress(params) {
    return await ApiService.post("address-user/create/", params);
  },
  async setAddressDefault(params) {
    return await ApiService.post("address-user/default", params);
  },
  async deleteAddress(params) {
    return await ApiService.post("address-user/delete/", params);
  },
  async deletePhone(params) {
    return await ApiService.post("phone-user/delete/", params);
  },
  async createPhone(params) {
    return await ApiService.post("phone-user/create/", params);
  },
  async changePassword(params) {
    return await ApiService.post("user/change-password/", params);
  },
};
/* -------------------------------------------------------------------------- */
/*                                   ACTION                                   */
/* -------------------------------------------------------------------------- */
export const actionUser = {
  async getInforUser(params) {
    let infor = false;
      let jwt_token_access = localStorage.getItem("jwt_token_access");
      ApiService.setHeader(jwt_token_access);
      await UserApiService.getInfor(params).then((response) => {
        infor = response.data;
      });
    return infor;
  },
  async uploadPhoto(params) {
    let json = ''
    let check = false
    let numberRequest = 0
    while(check == false && numberRequest < 2){
        numberRequest += 1
        let jwt_token_access = localStorage.getItem('jwt_token_access')
        ApiService.setHeader(jwt_token_access)
        await UserApiService.postUploadPhoto(params).then((response)=>{
            json =  response
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
  async uploadInformation(params) {
    let json = ''
    let check = false
    let numberRequest = 0
    while(check == false && numberRequest < 2){
        numberRequest += 1
        let jwt_token_access = localStorage.getItem('jwt_token_access')
        ApiService.setHeader(jwt_token_access)
        await UserApiService.uploadInformation(params).then((response)=>{
            json =  response
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
  async getAdressUser() {
    let json = ''
    let check = false
    let numberRequest = 0
    while(check == false && numberRequest < 2){
        numberRequest += 1
        let jwt_token_access = localStorage.getItem('jwt_token_access')
        ApiService.setHeader(jwt_token_access)
        await UserApiService.getAddressUser().then((response)=>{
            json =  response
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
  async createAdressUser(params) {
    let json = ''
    let check = false
    let numberRequest = 0
    while(check == false && numberRequest < 2){
        numberRequest += 1
        let jwt_token_access = localStorage.getItem('jwt_token_access')
        ApiService.setHeader(jwt_token_access)
        await UserApiService.createAddress(params).then((response)=>{
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
  async setAddressDefault(params) {
    let json = ''
    let check = false
    let numberRequest = 0
    while(check == false && numberRequest < 2){
        numberRequest += 1
        let jwt_token_access = localStorage.getItem('jwt_token_access')
        ApiService.setHeader(jwt_token_access)
        await UserApiService.setAddressDefault(params).then((response)=>{
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
  async deteleAddressUser(params) {
    let json = ''
    let check = false
    let numberRequest = 0
    while(check == false && numberRequest < 2){
        numberRequest += 1
        let jwt_token_access = localStorage.getItem('jwt_token_access')
        ApiService.setHeader(jwt_token_access)
        await UserApiService.deleteAddress(params).then((response)=>{
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
  async createPhoneUser(params) {
    let json = ''
    let check = false
    let numberRequest = 0
    while(check == false && numberRequest < 2){
        numberRequest += 1
        let jwt_token_access = localStorage.getItem('jwt_token_access')
        ApiService.setHeader(jwt_token_access)
        await UserApiService.createPhone(params).then((response)=>{
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
  async setPhoneDefault(params) {
    let json = ''
    let check = false
    let numberRequest = 0
    while(check == false && numberRequest < 2){
        numberRequest += 1
        let jwt_token_access = localStorage.getItem('jwt_token_access')
        ApiService.setHeader(jwt_token_access)
        await UserApiService.setPhoneDefault(params).then((response)=>{
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
  async getPhoneUser() {
    let json = ''
    let check = false
    let numberRequest = 0
    while(check == false && numberRequest < 2){
        numberRequest += 1
        let jwt_token_access = localStorage.getItem('jwt_token_access')
        ApiService.setHeader(jwt_token_access)
        await UserApiService.getPhoneUser().then((response)=>{
            json =  response
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
  async detelePhoneUser(params) {
    let json = ''
    let check = false
    let numberRequest = 0
    while(check == false && numberRequest < 2){
        numberRequest += 1
        let jwt_token_access = localStorage.getItem('jwt_token_access')
        ApiService.setHeader(jwt_token_access)
        await UserApiService.deletePhone(params).then((response)=>{
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
  async changePassword(params) {
    let json = ''
    let check = false
    let numberRequest = 0
    while(check == false && numberRequest < 2){
        numberRequest += 1
        let jwt_token_access = localStorage.getItem('jwt_token_access')
        ApiService.setHeader(jwt_token_access)
        await UserApiService.changePassword(params).then((response)=>{
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
  async loginUser(params) {
      return await UserApiService.loginUser(params)
  },
  async logoutUser(params) {
    return await UserApiService.logoutUser(params)
},
  async RegisterUser(params) {
    return await UserApiService.reggisterUser(params)
  }
};
