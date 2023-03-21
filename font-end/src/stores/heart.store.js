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
            return await ProductAction.actionGetProductHeart().then(res => {
                console.log("product heart",res)
                commit('getDataaSuccess',{data : Array.from(res)})
              })
        },
        async actionUnlikeItems({commit}){
            return commit('unlikeItems')
        },
        async actionlikeItems({commit}){
            return commit('likeItems')
        },
        actionExitHeart({commit}){
            commit('exitHeartSuccess')
        },
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
        },
        exitHeartSuccess(state){
            state.data =  [];
            state.numberProduct = 0;
            state.isLoading = false ;
            state.isHaveData = false;
        }
    }
};