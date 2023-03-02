import { OrderAction } from './../common/order.service'
const initialState = {
    data: [],
    indexOrder : false,
    numberProduct : 0,
    isLoading : false ,
    isHaveData : false,
    orderSelectedProduct : {
        data : [],
        totalPrice : 0,
        numberProduct : 0,
        voucher : false,
    }
}
// Promise.resolve(user);
export const cart = {
    namespaced: true,
    state: initialState,
    getters: {
        getData: state => state.data,
        isLoading : state => state.content,
        getNumberProduct : state => state.numberProduct,
        getIsHaveData : state => state.isHaveData,
        getorderSelectedProduct : state => state.orderSelectedProduct
    },
    actions: {

        async actionGetData({commit ,state}){
            if( state.isLoading )  return ;
            commit('startGetData')
            return await OrderAction.actionGetOrderCart({
                params: {
                  token_permission_infor_user: localStorage.getItem('token_permission_infor_user')
                }
              }).then(res => {
                commit('getDataSuccess',{data : Array.from(res.success) , numberProduct : res.number_product})
              }).catch(error => {
                console.log("ERROR GET DATAT" , error)
                commit('getDataFailure')
            })
        },
        async actionAddToCart({commit,state},payload){
            if( state.isLoading )  return ;
            commit('startAddToCart')
            return await OrderAction.actionAddToCart({
                params : {
                    token_permission_infor_user: localStorage.getItem('token_permission_infor_user'),
                    product_slug : payload.product_slug
                }
            }).then(res => {
                if(res.success == false){
                    commit('addToCartFailure')
                }
                else commit('addToCartSuccess',{product : res.success})
            }).catch(error => {
                console.log("ERROR ADD TO CART" , error)
            })
        },
        async actionRemoveProductInCart({commit,state},payload){
            if( state.isLoading )  return ;
            return await OrderAction.actionRemoveProductInCart({
                params : {
                    token_permission_infor_user: localStorage.getItem('token_permission_infor_user'),
                    product_slug : payload.product_slug,
                    name_order : "emty"
                }
            }).then(res => {
                console.log("remove to card",res)
            })
        },
        /* ------------------------- action selected product ------------------------ */
        actionSelectProductInCart({commit,state},payload){
            if( state.isLoading )  return ;
            commit('startSelectProductInCart')
            let productSelected = state.data[payload.indexOrder].products[payload.index];
            if( productSelected != null){
                commit('selectProductInCartSuccess',{productSelected :productSelected });
            } 
            else {
                commit('selectProductInCartFailure');
            }
        },
        actionRemoveSelectedProductInCart({commit,state},payload){
            if( state.isLoading )  return ;
            commit('startRemoveSeletedProductInCart');
            let productSelected = state.data[payload.indexOrder].products[payload.index];
            if( productSelected != null){
                commit('removeSeletedProductInCartSucess',{productSelected :productSelected });
            }
            else {
                commit('removeSeletedProductInCartFailure');
            }
        },
        actionSelectedVoucher({commit,state},payload){
            if( state.isLoading )  return ;
            commit('selectVoucerSucess',{voucher : payload.voucher});
        }
    },

    mutations: {
        /* ---------------------------- get order of user --------------------------- */
        startGetData(state){
            state.isLoading = true;
        },
        getDataSuccess(state,payload) {
            console.log(payload.data.success)
            state.data = payload.data;
            state.numberProduct = payload.numberProduct;
            state.isLoading = false;
            state.isHaveData = true;
        },
        getDataFailure(state) {
            state.data = [] ;
            state.numberProduct = 0 ;
            state.isLoading = false;
        },
        /* --------------------------- add product to cart -------------------------- */
        startAddToCart(state){
            state.isLoading = true;
        },
        addToCartSuccess(state,payload){
            state.data[0].products.push(payload.product);
            state.numberProduct = state.numberProduct + 1;
            state.isLoading = false;
        },
        addToCartFailure(state){
            state.isLoading = false;
        },
        /* ------------------------- remove product in cart ------------------------- */
        startRemoveProductInCart(state){
            state.isLoading = true;
        },
        removeProductInCartSuccess(state,payload){
            state.data[state.data.length - 1].products = state.data[state.data.length - 1].products.filter((product) => {
                product.slug != payload.success.product_slug
                return product
            })
            state.numberProduct = state.numberProduct - 1;
        },
        removeProductInCartFailure(state){
            state.isLoading  = false;
        },
        /* ------------------------- add select product in cart ------------------------- */
        startSelectProductInCart(state){
            state.isLoading = true;
        },
        selectProductInCartSuccess(state,payload){
            state.orderSelectedProduct.data.push(payload.productSelected);
            state.orderSelectedProduct.totalPrice += payload.productSelected.product_price_total;
            state.orderSelectedProduct.numberProduct += 1;
            state.isLoading = false;
            console.log("state.orderSelectedProduct.data",state.orderSelectedProduct.data)
        },
        selectProductInCartFailure(state){
            state.isLoanding = false;
        },
        /* --------------------- remove selected product in cart -------------------- */
        startRemoveSeletedProductInCart(state){
            state.isLoading = true;
        },
        removeSeletedProductInCartSucess(state,payload){
            console.log(state.orderSelectedProduct.data)
            state.orderSelectedProduct.data = state.orderSelectedProduct.data.filter((product) => {
                console.log(product)
                return product.product_slug != payload.productSelected.product_slug
            });
            state.orderSelectedProduct.totalPrice -= payload.productSelected.product_price_total;
            state.orderSelectedProduct.numberProduct -= 1;
            state.isLoading = false;
        },
        removeSeletedProductInCartFailure(state){
            state.isLoanding = false;
        },
        /* --------------------- voucher selectedproduct in cart -------------------- */
        selectVoucerSucess(state,payload){
            state.isLoanding = false;
            state.orderSelectedProduct.voucher = payload.voucher
        }
    }
};