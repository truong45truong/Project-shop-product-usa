const initialState = {
    isShowLayout: {
        isShowDashBoard : true ,
        isShowUser : false ,
        isShowOrder : false ,
        isShowProduct : false ,
    },
    isLoanding : false,
    isShowDetailProduct : false,
    productDetail : false,
    showVoucher : {
        show : false,
        isShowAdd : false,
        isShowAddProduct : false,
        isShowDetail : false,
        voucherDetail : false,
        isShowList : false,
    },
    showFlashSale : {
        show : false,
        isShowAdd : false,
        isShowAddProduct : false,
        isShowDetail : false,
        flashSaleDetail : false,
        isShowList : false,
    },
}
export const dashboard = {
    namespaced: true,
    state: initialState,
    getters: {
        getIsShowLayout: state => state.isShowLayout,
        getIsShowDetailProduct: state => state.isShowDetailProduct,
        getProductDetail : state => state.productDetail ,
        getShowVoucher : state => state.showVoucher ,
        getShowFlashSale: state => state.showFlashSale ,
    },
    actions: {
        async actionSelectedLayout({commit,state} , payload){
            
            if (state.isLoangding == true) return;
            state.isLoanding = true
            commit('selectedLayout',{ type : payload.type })
        },
        async actionSelectedDetailProduct({commit,state} , payload){
            
            if (state.isLoangding == true) return;
            state.isLoanding = true
            commit('selectedDetailProduct',{ product_id : payload.product_id })
        },
        async actionShowVoucher({commit,state} , payload){
            
            if (state.isLoangding == true) return;
            state.isLoanding = true
            if(payload.type == 4 ) commit('showDetailVoucher',{ voucher_id : payload.voucher_id })
            else commit('showVoucher',{ type : payload.type })
        },
        async actionShowFlashSale({commit,state} , payload){
            
            if (state.isLoangding == true) return;
            state.isLoanding = true
            if(payload.type == 4 ) commit('showDetailFLashSale',{ flash_sale_id : payload.flash_sale_id })
            else commit('showFLashSale',{ type : payload.type })
        },
        async actionHideVoucher({commit,state} , payload){
            
            if (state.isLoangding == true) return;
            state.isLoanding = true
            commit('hideVoucher')
        },

    },

    mutations: { 
        hideVoucher(state){
            state.isLoanding = false
            state.showVoucher.show = false
            state.showVoucher.isShowAdd = false
            state.showVoucher.isShowAddProduct = false
            state.showVoucer.isShowList = false
            state.showVoucher.isShowDetail = false
        },
        showDetailVoucher(state,payload){
            state.isShowDetailProduct = false
            state.isShowLayout.isShowDashboard = false
            state.isShowLayout.isShowUser = false
            state.isShowLayout.isShowOrder = false
            state.isShowLayout.isShowProduct = false
            state.isLoanding = false

            state.showVoucher.show = true
            state.showVoucher.isShowAdd = false
            state.showVoucher.isShowAddProduct = false
            state.showVoucher.isShowList = false
            state.showVoucher.isShowDetail = true
            state.showVoucher.voucherDetail = payload.voucher_id

            state.showFlashSale.isShowAdd = false
            state.showFlashSale.show = false
            state.showFlashSale.isShowAddProduct = false
            state.showFlashSale.isShowList = false
            state.showFlashSale.isShowDetail = false
        },
        showVoucher(state,payload){
            state.isShowDetailProduct = false
            state.isShowLayout.isShowDashboard = false
            state.isShowLayout.isShowUser = false
            state.isShowLayout.isShowOrder = false
            state.isShowLayout.isShowProduct = false

            state.isLoanding = false
            state.showVoucher.show = true
            state.showVoucher.isShowDetail = false

            state.showFlashSale.isShowAdd = false
            state.showFlashSale.show = false
            state.showFlashSale.isShowAddProduct = false
            state.showFlashSale.isShowList = false
            state.showFlashSale.isShowDetail = false

            switch (payload.type) {
                case 1:
                    state.showVoucher.isShowAdd = false
                    state.showVoucher.isShowAddProduct = false
                    state.showVoucher.isShowList = true
                    state.showVoucher.isShowDetail = false
                    break;
                case 2:
                    state.showVoucher.isShowAdd = true
                    state.showVoucher.isShowAddProduct = false
                    state.showVoucher.isShowList = false
                    state.showVoucher.isShowDetail = false
                    break;
                case 3:
                    state.showVoucher.isShowAdd = false
                    state.showVoucher.isShowAddProduct = true
                    state.showVoucher.isShowList = false
                    state.showVoucher.isShowDetail = false
                    break;
                default:
                    state.showVoucher.isShowAdd = false
                    state.showVoucher.isShowAddProduct = false
                    state.showVoucher.isShowList = true
                    state.showVoucher.isShowDetail = false
                    break;
            }
        },
        showFLashSale(state,payload){
            state.isShowDetailProduct = false
            state.isShowLayout.isShowDashboard = false
            state.isShowLayout.isShowUser = false
            state.isShowLayout.isShowOrder = false
            state.isShowLayout.isShowProduct = false
            state.isLoanding = false
            state.showVoucher.show = false
            state.showVoucher.isShowDetail = false
            state.showVoucher.isShowAdd = false
            state.showVoucher.isShowAddProduct = false
            state.showVoucher.isShowList = false
            state.showVoucher.isShowDetail = false
            state.showFlashSale.show = true
            switch (payload.type) {
                case 1:
                    state.showFlashSale.isShowAdd = false
                    state.showFlashSale.isShowAddProduct = false
                    state.showFlashSale.isShowList = true
                    state.showFlashSale.isShowDetail = false
                    break;
                case 2:
                    state.showFlashSale.isShowAdd = true
                    state.showFlashSale.isShowAddProduct = false
                    state.showFlashSale.isShowList = false
                    state.showFlashSale.isShowDetail = false
                    break;
                case 3:
                    state.showFlashSale.isShowAdd = false
                    state.showFlashSale.isShowAddProduct = true
                    state.showFlashSale.isShowList = false
                    state.showFlashSale.isShowDetail = false
                    break;
                default:
                    state.showFlashSale.isShowAdd = false
                    state.showFlashSale.isShowAddProduct = false
                    state.showFlashSale.isShowList = true
                    state.showFlashSale.isShowDetail = false
                    break;
            }
        },
        showDetailFLashSale(state,payload){
            state.isShowDetailProduct = false
            state.isShowLayout.isShowDashboard = false
            state.isShowLayout.isShowUser = false
            state.isShowLayout.isShowOrder = false
            state.isShowLayout.isShowProduct = false
            state.isLoanding = false

            state.showVoucher.show = false
            state.showVoucher.isShowAdd = false
            state.showVoucher.isShowAddProduct = false
            state.showVoucher.isShowList = false
            state.showVoucher.isShowDetail = false
            state.showVoucher.voucherDetail = false

            state.showFlashSale.isShowAdd = false
            state.showFlashSale.isShowAddProduct = false
            state.showFlashSale.isShowList = false
            state.showFlashSale.isShowDetail = true
            state.showFlashSale.flashSaleDetail = payload.flash_sale_id
        },
        selectedLayout(state,payload) {
            state.isLoanding = false
            state.isShowDetailProduct = false
            state.isLoanding = false
            state.isShowDetailProduct = false

            state.showVoucher.show = false
            state.showVoucher.isShowAdd = false
            state.showVoucher.isShowAddProduct = false
            state.showVoucher.isShowList = false
            state.showVoucher.isShowDetail = false

            state.showFlashSale.isShowAdd = false
            state.showFlashSale.show = false
            state.showFlashSale.isShowAddProduct = false
            state.showFlashSale.isShowList = false
            state.showFlashSale.isShowDetail = false
            switch (payload.type) {
                case 1:
                    state.isShowLayout.isShowDashboard = true
                    state.isShowLayout.isShowUser = false
                    state.isShowLayout.isShowOrder = false
                    state.isShowLayout.isShowProduct = false
                    break;
                case 2:
                    state.isShowLayout.isShowDashboard = false
                    state.isShowLayout.isShowUser = true
                    state.isShowLayout.isShowOrder = false
                    state.isShowLayout.isShowProduct = false
                    break;
                case 3:
                    state.isShowLayout.isShowDashboard = false
                    state.isShowLayout.isShowUser = false
                    state.isShowLayout.isShowOrder = true
                    state.isShowLayout.isShowProduct = false
                    break;
                case 4:
                    state.isShowLayout.isShowDashboard = false
                    state.isShowLayout.isShowUser = false
                    state.isShowLayout.isShowOrder = false
                    state.isShowLayout.isShowProduct = true
                    break;

                default:
                    state.isShowLayout.isShowDashboard = true
                    state.isShowLayout.isShowUser = false
                    state.isShowLayout.isShowOrder = false
                    state.isShowLayout.isShowProduct = false
            }
        },
        selectedDetailProduct(state,payload) {
            state.isShowDetailProduct = true
            state.isShowLayout.isShowDashboard = false
            state.isShowLayout.isShowUser = false
            state.isShowLayout.isShowOrder = false
            state.isShowLayout.isShowProduct = false
            state.productDetail = payload.product_id
            state.isLoanding = false

            state.showVoucher.show = false
            state.showVoucher.isShowAdd = false
            state.showVoucher.isShowAddProduct = false
            state.showVoucher.isShowList = false
            state.showVoucher.isShowDetail = false

            state.showFlashSale.isShowAdd = false
            state.showFlashSale.show = false
            state.showFlashSale.isShowAddProduct = false
            state.showFlashSale.isShowList = false
            state.showFlashSale.isShowDetail = false
        }
    }
};