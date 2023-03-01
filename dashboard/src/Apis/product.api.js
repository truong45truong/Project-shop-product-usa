import * as urlApi from './constants.api.js'
import AxiosService from './../Utills/axiosService.utill'


export const getAllProductApi = () => {
    return AxiosService.get(urlApi.API_GET_PRODUCT,{
        params : {
            token_permission_infor_user : false
        }
    })
}