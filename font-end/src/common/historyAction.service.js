import { ApiService } from './api.service'
export const HistoryService = {
    async updateActionHistory (params){
        return  await ApiService.post('update-action-history',params)
    },
    async getProductRecommend (){
        return  await ApiService.query('product-recommendation')
    },
} 

export const ActionHistory = {
    async updateActionHistory(params) {
        let infor = false;
          let jwt_token_access = localStorage.getItem("jwt_token_access");
          ApiService.setHeader(jwt_token_access);
          await HistoryService.updateActionHistory(params).then((response) => {
            infor = response.data;
          });
        return infor;
      },
      async getProductRecommend (){
        let infor = false;
          let jwt_token_access = localStorage.getItem("jwt_token_access");
          ApiService.setHeader(jwt_token_access);
          await HistoryService.getProductRecommend().then((response) => {
            infor = response.data;
          });
        return infor;
      },
}