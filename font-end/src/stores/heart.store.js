import { ProductAction } from './../common/product.service'
const initialState = {
    data: [],
    numberProduct : 0,
    isLoading : false ,
    isHaveData : false,
}
// Promise.resolve(user);
export const heart = {
    namespaced: true,
    state: initialState,
    getters: {
        getData: state => state.data,
        isLoading : state => state.content,
        getNumberProduct : state => state.numberProduct,
        getIsHaveData : state => state.isHaveData
    },
    actions: {
        async actionGetData({commit}){
            return await ProductAction.actionGetProductHeart({
                params: {
                    token_permission_infor_user: localStorage.getItem('token_permission_infor_user') ? localStorage.getItem('token_permission_infor_user') : "nono"
                }
            }).then(res => {
                commit('getDataaSuccess',{data : Array.from(res.data)})
              })
        },
        async actionUnlikeItems({commit}){
            return commit('unlikeItems')
        },
        async actionlikeItems({commit}){
            return commit('likeItems')
        }
    },

    mutations: {
        getDataaSuccess(state,payload) {
            console.log(payload.data)
            state.numberProduct = payload.data.length;
            state.isLoading = false;
            state.isHaveData = true;
        },
        unlikeItems(state){
            state.numberProduct = state.numberProduct - 1;
        },
        likeItems(state){
            state.numberProduct = state.numberProduct + 1;
        }
    }
};