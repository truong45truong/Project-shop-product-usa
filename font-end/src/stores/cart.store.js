import { faLessThanEqual } from '@fortawesome/free-solid-svg-icons';
import { OrderAction } from './../common/order.service'
const initialState = {
    data: [],
    indexOrder : false,
    numberProduct : 0,
    isLoading : false ,
    isHaveData : false,
    isOrderToday : false ,
    orderSelectedProduct : {
        data : [],
        totalPrice : 0,
        numberProduct : 0,
        voucher : false,
        address : false,
        transport : false
    }
}
// Promise.resolve(user);
export const cart = {
    namespaced: true,
    state: initialState,
    getters: {
        getData: state => state.data,
        isLoading : state => state.isLoading,
        getNumberProduct : state => state.numberProduct,
        getIsHaveData : state => state.isHaveData,
        getorderSelectedProduct : state => state.orderSelectedProduct,
        getIsOrderToday : state => state.isOrderToday
    },
    actions: {
        /* -------------------------------------------------------------------------- */
        /*                               ACTION GET DATA                              */
        /* -------------------------------------------------------------------------- */
        async actionGetData({commit ,state}){
            commit('startGetData')
            return await OrderAction.actionGetOrderCart({
                params: {
                  token_permission_infor_user: localStorage.getItem('token_permission_infor_user')
                }
              }).then(res => {
                commit('getDataSuccess',{data : Array.from(res.success) , numberProduct : res.number_product , isOrderToday : res.check_order_today})
              }).catch(error => {
                console.log("ERROR GET DATAT" , error)
                commit('getDataFailure')
            })
        },
        /* -------------------------------------------------------------------------- */
        /*                             ACTION ADD TO CART                             */
        /* -------------------------------------------------------------------------- */
        async actionAddToCart({commit,state,dispatch},payload){
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
                else {
                    if(state.isOrderToday == false){

                        console.log("startGetData")
                        dispatch('actionGetData')
                    }
                    commit('addToCartSuccess',{product : res.success, checkProductAlreadyInCart : res.check_detail_order})
                }
            }).catch(error => {
                commit('addToCartFailure')
                console.log("ERROR ADD TO CART" , error)
            })
        },
        /* -------------------------------------------------------------------------- */
        /*                        ACTION REMOVE PRODUCT IN CART                       */
        /* -------------------------------------------------------------------------- */
        async actionRemoveProductInCart({commit,state},payload){
            if( state.isLoading )  return ;
            commit('startRemoveProductInCart')
            return await OrderAction.actionRemoveProductInCart({
                params : {
                    token_permission_infor_user: localStorage.getItem('token_permission_infor_user'),
                    product_slug : payload.product_slug,
                    name_order : payload.name_order
                }
            }).then(res => {
                commit('removeProductInCartSuccess' , { indexOrder:payload.indexOrder , index : payload.index })
            }).catch(error => {
                commit('removeProductInCartFailure')
                console.log("ERROR REMOVE TO CART" , error)
            })
        },
        /* -------------------------------------------------------------------------- */
        /*                            ACTION SELECT PRODUCT                           */
        /* -------------------------------------------------------------------------- */
        actionSelectProductInCart({commit,state},payload){
            if( state.isLoading )  return ;
            commit('startSelectProductInCart')
            let productSelected = state.data[payload.indexOrder].products[payload.index];
            state.data[payload.indexOrder].products[payload.index].isSelectOrder = true
            if( productSelected != null){
                commit('selectProductInCartSuccess',{productSelected :JSON.parse(JSON.stringify(productSelected)) });
            } 
            else {
                commit('selectProductInCartFailure');
            }
        },
        /* -------------------------------------------------------------------------- */
        /*                    ACTION REMOVE SELECT PRODUCT IN CART                    */
        /* -------------------------------------------------------------------------- */
        actionRemoveSelectedProductInCart({commit,state},payload){
            if( state.isLoading )  return ;
            commit('startRemoveSeletedProductInCart');
            let productSelected = state.data[payload.indexOrder].products[payload.index];
            state.data[payload.indexOrder].products[payload.index].isSelectOrder = false
            if( productSelected != null){
                commit('removeSeletedProductInCartSucess',{product_slug :productSelected.product_slug });
            }
            else {
                commit('removeSeletedProductInCartFailure');
            }
        },
        /* -------------------------------------------------------------------------- */
        /*                           ACTION SELECTED VOUCHER                          */
        /* -------------------------------------------------------------------------- */
        actionSelectedVoucher({commit,state},payload){
            if( state.isLoading )  return ;
            commit('selectVoucerSucess',{voucher : payload.voucher});
        },
        /* -------------------------------------------------------------------------- */
        /*                            ACTION SELECT ADDRESS                           */
        /* -------------------------------------------------------------------------- */
        actionSelectedAddress({commit,state},payload){
            if( state.isLoading )  return ;
            commit('selectAddressSuccess',{address : payload.address});
        },
        /* -------------------------------------------------------------------------- */
        /*                           ACTION SELECT TRANSPORT                          */
        /* -------------------------------------------------------------------------- */
        actionSelectedTransport({commit,state},payload){
            if( state.isLoading )  return ;
            commit('selectedTransportSuccess',{transport : payload.transport});
        },
        /* -------------------------------------------------------------------------- */
        /*                   ACTION CHANGE QUANTITY PRODUCT IN ORDER                  */
        /* -------------------------------------------------------------------------- */
        actionChangeQuangtityProductInOrder({commit,state},payload){
            if( state.isLoading )  return ;
            commit('changeQuantityProductInOrderSuccess' , {product_slug :payload.product_slug, value : payload.value})
        },
        /* -------------------------------------------------------------------------- */
        /*                    ACTION CHANG QUANTITY PRODUCT IN CART                   */
        /* -------------------------------------------------------------------------- */
        actionChangeQuangtityProductInCart({commit,state},payload){
            if( state.isLoading )  return ;
            commit('startChangeQuantityProductInCart')
            commit('changeQuantityProductInCartSuccess' , {indexOrder : payload.indexOrder, index : payload.index , value : payload.value})
        }
    },

    mutations: {
        /* -------------------------------------------------------------------------- */
        /*                         MUTATIONS GET ORDER OF USER                        */
        /* -------------------------------------------------------------------------- */
        startGetData(state){
            state.isLoading = true;
        },
        getDataSuccess(state,payload) {
            console.log(payload.data.success)
            state.data = payload.data.filter((order) => {
                order.products = order.products.filter(product => {
                    product.isSelectOrder = false
                    return product
                })
                return order
            });
            state.numberProduct = payload.numberProduct;
            state.isOrderToday = payload.isOrderToday;
            state.isLoading = false;
            state.isHaveData = true;
        },
        getDataFailure(state) {
            state.data = [] ;
            state.numberProduct = 0 ;
            state.isLoading = false;
        },
        /* -------------------------------------------------------------------------- */
        /*                 MUTATUIONS CHANGE QUANTITY PRODUCT IN CART                 */
        /* -------------------------------------------------------------------------- */
        startChangeQuantityProductInCart(state){
            state.isLoading = true;
        },
        changeQuantityProductInCartSuccess(state,payload){
            state.data[payload.indexOrder].products[payload.index].product_quantity += payload.value
            state.isLoading = false;
            console.log("state.orderSelectedProduct.data",state.data[payload.indexOrder].products[payload.index].product_quantity)

        },
        changeQuantityProductInCartFailure(state){
            state.isLoading = false;
        },
        /* -------------------------------------------------------------------------- */
        /*                            MUTATIONS ADD TO CART                           */
        /* -------------------------------------------------------------------------- */
        startAddToCart(state){
            state.isLoading = true;
        },
        addToCartSuccess(state,payload){
            if (payload.checkProductAlreadyInCart == false){
                state.data[0].products.push(payload.product);
                state.numberProduct = state.numberProduct + 1;
            }else {
                state.data[0].products = state.data[0].products.filter((product) => {
                    if(product.product_slug == payload.checkProductAlreadyInCart){
                        product.product_quantity += 1;
                        console.log("checkProductAlreadyInCart",payload.checkProductAlreadyInCart)
                    }
                    return product;
                })
            }
            state.isLoading = false;
        },
        addToCartFailure(state){
            state.isLoading = false;
        },
        /* -------------------------------------------------------------------------- */
        /*                      MUTATIONS REMOVE PRODUCT IN CART                      */
        /* -------------------------------------------------------------------------- */
        startRemoveProductInCart(state){
            state.isLoading = true;
        },
        removeProductInCartSuccess(state,payload){
            console.log("product",state.data[payload.indexOrder][payload.index])
            state.data[payload.indexOrder].products=state.data[payload.indexOrder].products.filter(product => {
                return (product.product_slug != state.data[payload.indexOrder].products[payload.index].product_slug)
            })
            state.numberProduct = state.numberProduct - state.data[payload.indexOrder].products[payload.index].product_quantity;
            state.isLoading  = false;
        },
        removeProductInCartFailure(state){
            state.isLoading  = false;
        },
        /* -------------------------------------------------------------------------- */
        /*                      MUTATIONS SELECT PRODUCT IN CART                      */
        /* -------------------------------------------------------------------------- */
        startSelectProductInCart(state){
            state.isLoading = true;
        },
        selectProductInCartSuccess(state,payload){
            let productSelected = payload.productSelected
            state.orderSelectedProduct.voucher = false
            productSelected.voucher_activate = false
            state.orderSelectedProduct.data.push(productSelected);
            state.orderSelectedProduct.totalPrice += productSelected.product_price_total*productSelected.product_quantity;
            state.orderSelectedProduct.numberProduct += productSelected.product_quantity;
            state.isLoading = false;
            console.log("state.orderSelectedProduct.data",state.orderSelectedProduct.data)
        },
        selectProductInCartFailure(state){
            state.isLoanding = false;
        },
        /* -------------------------------------------------------------------------- */
        /*                   MUTATIONS REMOVE SELECT PRODUCT IN CART                  */
        /* -------------------------------------------------------------------------- */
        startRemoveSeletedProductInCart(state){
            state.isLoading = true;
        },
        removeSeletedProductInCartSucess(state,payload){
            state.orderSelectedProduct.data = state.orderSelectedProduct.data.filter((product) => {
                if(product.product_slug == payload.product_slug){
                    console.log("product select",product)
                    state.orderSelectedProduct.totalPrice -= product.product_price_total*product.product_quantity;
                    state.orderSelectedProduct.numberProduct -= product.product_quantity;
                }
                return product.product_slug != payload.product_slug
            });
            state.isLoading = false;
        },
        removeSeletedProductInCartFailure(state){
            state.isLoanding = false;
        },
        /* -------------------------------------------------------------------------- */
        /*                   MUTATIONS CHANGE QUANTITY PRODUCT ORDER                  */
        /* -------------------------------------------------------------------------- */
        startChangeQuantityProductInOrder(state){
            state.isLoading = true;
        },
        changeQuantityProductInOrderSuccess(state,payload){
            let total_price = 0
            state.orderSelectedProduct.data = state.orderSelectedProduct.data.filter((product) => {
                if (product.product_slug == payload.product_slug){
                    product.product_quantity += payload.value
                }
                if(product.voucher_activate == true){
                    total_price += product.price_after_voucher*product.product_quantity
                }else {
                    total_price += product.product_price_total*product.product_quantity
                }
                return product
            });
            state.orderSelectedProduct.totalPrice = total_price
            state.orderSelectedProduct.numberProduct += payload.value
            state.isLoading = false;
        },
        changeQuantityProductInOrderFailure(state){
            state.isLoading = false;
        },
        /* -------------------------------------------------------------------------- */
        /*                          MUTATIONS SELECT VOUCHER                          */
        /* -------------------------------------------------------------------------- */
        selectVoucerSucess(state,payload){
            let total_price = 0
            state.isLoanding = false;
            state.orderSelectedProduct.voucher = payload.voucher
            state.orderSelectedProduct.data = state.orderSelectedProduct.data.filter((product) => {
                product.voucher_activate = false
                return product
            });
            state.orderSelectedProduct.voucher.product_in_vouchers.filter((productInVoucher)=>{
                state.orderSelectedProduct.data = state.orderSelectedProduct.data.filter((product) => {
                    if( product.product_slug == productInVoucher.product_slug_in_voucher){
                        product.voucher_activate = true
                        let price_after_voucher = parseInt(product.product_price_total)*parseInt(state.orderSelectedProduct.voucher.voucher.sale)/100
                        if( price_after_voucher < parseInt(state.orderSelectedProduct.voucher.voucher.limited_price)*1000){
                            product.price_after_voucher = product.product_price_total - price_after_voucher
                        }else {
                            product.price_after_voucher = product.product_price_total - state.orderSelectedProduct.voucher.voucher.limited_price*1000
                        }
                    } 
                    return product
                });
            })
            state.orderSelectedProduct.data.filter((product) => {
                if(product.voucher_activate == true){
                    total_price += product.price_after_voucher*product.product_quantity
                }else {
                    total_price += product.product_price_total*product.product_quantity
                }
            })
            state.orderSelectedProduct.totalPrice = total_price
        },
        /* -------------------------------------------------------------------------- */
        /*                          MUTATIONS SELECT ADDRESS                          */
        /* -------------------------------------------------------------------------- */
        selectAddressSuccess(state,payload){
            state.orderSelectedProduct.address = payload.address
        },
        /* -------------------------------------------------------------------------- */
        /*                          MUTATION SELECT TRANSPORT                         */
        /* -------------------------------------------------------------------------- */
        selectedTransportSuccess(state,payload){
            state.orderSelectedProduct.transport = payload.transport
        },
    }
};