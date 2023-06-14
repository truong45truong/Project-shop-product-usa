<template>
    <div class="row d-flex d-flex-column align-items-center justify-content-center mt-2 mx-2 position-absolute layout-cart-inside">
        <div class="bg-dark back-cart " @click="$emit('hideCart')"> 
            <p class="text-white w-100 text-center my-1">click để thoát</p> 
        </div>
        <h3 class="m-0 text-center mt-4">Túi đồ  hôm nay</h3>
        <!-- <div class="d-flex justify-content-end w-75 mt-5 me-5">
            <button class="btn btn-dark btn-view-product-cart" :class="[isShowListItem ? 'btn-view-product-cart-activate' : '']" @click="showListItem" >
                <font-awesome-icon icon="fa-solid fa-list" class="text-white fs-5" />
            </button>
            <button class="btn btn-dark btn-view-product-cart" :class="[isShowGridItem ? 'btn-view-product-cart-activate' : '']" @click="showGridItem" >
                <font-awesome-icon icon="fa-solid fa-solar-panel" class="text-white fs-5" />
            </button>
        </div> -->
        <div v-if="dataItem.length > 0" class="d-flex flex-column w-75 list-item-product scroll-list-product mb-5" id="list_product-cart-inside">
            <div v-for="item,index in dataItem"  class="col mt-0 my-3 h-sm-25 item-cart-market-grid px-2" 
            :id="'item-in-list-' + `${item.product_slug}`" >
                <product-cart-inside :product_slug="item.product_slug" :photo_product="item.photo_product" :product_name="item.product_name"
                        :product_price_total="item.product_price_total" :product_quantity="item.product_quantity" :product_sale="item.product_sale"
                        :product_price="item.product_price" :index="index" :name_order="orderInformation.name"
                        @changePriceTotalOrder="changePriceTotalOrder" @hideCart="hide"
                    />
            </div>
        </div>
        <!-- <div v-if="isShowGridItem" class="row w-75 list-item-product scroll-list-product mb-5" id="grid_product-cart-inside" >
            <div v-for="item in dataItem"  class="col-lg-3 col-sm-4 col-6 mt-0 my-3 h-sm-25 item-cart-market-grid px-2"
            :id="'item-in-grid-' + `${item.product_slug}`"
            >
                <product-item-cart-inside-market :slug="item.product_slug" :photo="item.photo_product" :name="item.product_name"
                        :price="item.product_price_total" :numberProduct="item.product_quantity" :sale="item.product_sale"
                />
            </div>
        </div> -->
        <!-- <div v-if="dataItem.length > 0" class="result-product-cart w-75">
            <div class="mt-0 border border-2 border-warning my-2">
                <div class="d-flex align-items-center">
                    <div class="col-infor-item text-center mt-2">
                        <p class="text-danger"><b>Tổng số sản phẩm </b></p>
                        <p class="text-dark"> {{numberProduct}}</p>
                    </div>
                    <div class="col-infor-item text-center mt-2">
                        <p class="text-danger"><b>Thanh toán </b></p>
                        <p class="text-dark"> {{orderInformation.total_price}}</p>
                    </div>
                    <div class="col-infor-item text-center mt-2">
                        <p class="text-danger"><b>Voucher giám giá </b></p>
                        <p class="text-warning"> <b>KATIE-YOYO</b></p>
                    </div>
                    <div class="col-infor-item text-center mt-2">
                        <p class="text-danger"><b>Phương thức thanh toán </b></p>
                        <p class="text-warning-stamp"> Thanh toán khi nhận hàng</p>
                    </div>
                    <div class="col-infor-item text-center mt-2">
                        <p class="text-danger"><b>Mã đơn hàng </b></p>
                        <p class="text-secondary text-name-order"> {{orderInformation.name}}</p>
                    </div>
                </div>
            </div>
        </div> -->
        <div v-if="dataItem.length > 0" class="result-product-cart w-75">
            <div class="mt-0 border border-2 border-warning my-2">
                <div class="row d-flex align-items-center position-relative">
                    <user-select-address ref="selectAddressUser" @selectAddress="selectedAddress" />
                    <user-select-phone ref="selectPhoneUser"  @selectPhone="selectedPhone" />
                    <div class="col-lg-6 my-2 d-flex flex-column col-item-total-cart justify-content-center position-relative">
                        <p class="m-0 text-danger text-center mb-2"><b>Địa chỉ</b></p>
                        <div class="d-flex justify-content-center">
                            <font-awesome-icon icon="fa-solid fa-location-dot" class="fs-4" />
                            <p v-if="addressSelected == false" class="m-0 ms-2">{{ orderInformation.address_receiver}}</p>
                            <p class="m-0 ms-2" v-if="addressSelected != false">
                                {{addressSelected.address_content}}
                            </p>
                            <font-awesome-icon icon="fa-solid fa-pen-to-square" class="fs-4 ms-2 icon-cancel" @click="showSelectedAddress" />
                        </div>
                    </div>
                    <div class="col-lg-6 my-2 d-flex flex-column justify-content-center position-relative">
                        <p class="m-0 text-danger text-center mb-2"><b>Đi động</b></p>  
                        <div class="d-flex justify-content-center">
                            <font-awesome-icon icon="fa-solid fa-phone" class="fs-4" />
                            <p class="m-0 ms-2">(+84)</p>
                            <img class="img-flag-phone-user mx-2" src="./../../assets/images/flagflag.webp" alt="">
                            <p v-if="phoneSelected == false" class="m-0">{{orderInformation.phone_receiver}}</p>
                            <p v-if="phoneSelected == false " class="m-0 text-primary">({{orderInformation.receiver}})</p>
                            <p class="m-0 ms-2" v-if="phoneSelected != false">
                                
                                <p class="m-0">
                                    {{phoneSelected.phone}}
                                    <span class="ms-1 text-primary">({{phoneSelected.name}})</span>
                                </p>
                            </p>
                            <font-awesome-icon icon="fa-solid fa-pen-to-square" class="fs-4 ms-2 icon-cancel" @click="showSelectedPhone" />
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div v-if="dataItem.length > 0" class="w-100 d-flex flex-column mt-3 mb-5 align-items-center">
            <div class="btn btn-warning"> Mua ngay </div>
        </div>
        <div v-if="dataItem.length == 0" class="w-100 d-flex flex-column mt-3 mb-5 align-items-center">
            <div class="">
                Chưa có sản phẩm nào trong giỏ hôm nay
            </div>
        </div>
    </div>
</template>
<script>
import { mapGetters,mapActions } from 'vuex'
import {OrderAction} from '../../common/order.service'
import UserSelectAddress from '../../components/user/UserSelectAddress.vue'
import UserSelectPhone from '../../components/user/UserSelectPhone.vue'
import ProductItemCartInsideMarket from '../../components/product/ProductItemCartInsideMarket.vue'
import ProductCartInside from '../../components/product/ProductCartInside.vue'
export default ({
    name: 'CartInsideMarketLayout',
    props: {
        msg : ''
    },
    components: {
        ProductItemCartInsideMarket,
        UserSelectAddress,
        UserSelectPhone,
        ProductCartInside
    },
    data: () => ({
        isShowListItem :true ,
        isShowGridItem : false,
        dataItem : [],
        orderInformation : false,
        numberProduct: 0,
        addressSelected : false,
        phoneSelected : false
    }),
    methods: {
        showListItem(){
            this.isShowListItem = true;
            this.isShowGridItem = false
        },
        showGridItem(){
            this.isShowListItem = false;
            this.isShowGridItem = true;
        },
        showSelectedAddress(){
            this.$refs.selectAddressUser.isShow = true
        },
        selectedAddress(item){
            this.addressSelected = item
        },
        selectedPhone(item){
            this.phoneSelected= item
        },
        showSelectedPhone(){
            this.$refs.selectPhoneUser.isShow = true
        },
        changePriceTotalOrder(price,product_slug,isDelete,numberQuantity){
            if(isDelete == true){
                this.orderInformation.total_price += price
                let listProductCartInside = document.getElementById('list_product-cart-inside')
                let nodeChild = document.getElementById('item-in-list-'+product_slug)
                listProductCartInside.removeChild(nodeChild)
                // gridProductCartInside = document.getElementById('grid_product-cart-inside')
                // nodeChildGrid = document.getElementById('item-in-grid-'+product_slug)
                // gridProductCartInside.removeChild(nodeChildGrid)
                this.numberProduct += numberQuantity
            }
            if(isDelete == false){
                this.orderInformation.total_price += price
                this.numberProduct += numberQuantity
            }
        },
        hide(){
            this.$emit('hideCart')
        }
    },
    computed: {
    },
    async created() {
        await OrderAction.actionGetOrderToday().then(res => {
            console.log(res.data[0])
            this.dataItem = Array.from(res.data[0].products)
            this.orderInformation= res.data[0].order
            this.numberProduct = res.numberProduct
        })
    },
    async mounted() {
    }
})
</script>
<style> 
.col-infor-item {
    width:20%;
}
.btn-view-product-cart{
    border-radius: 0% !important;

}
.item-cart-market-grid{
    position :relative;
    overflow: hidden;
    padding: 0 calc(100% - 15px );
}
.btn-view-product-cart-activate {
    background-color: #b9b7b7 !important;
}
.btn-view-product-cart-activate svg{
    color:#D33A2C !important;

}
.img-cart-market {
    width:20%;
}
.btn-number-product-cart{
    width : 40px ;
    height : 40px;
}
.text-name-product-cart {
    color :brown
}
.text-price-product-cart {
    color:rgb(88, 85, 86)
}

.button-45 {
  align-items: center;
  background-color: #FFE7E7;
  background-position: 0 0;
  border: 1px solid #FEE0E0;
  border-radius: 11px;
  box-sizing: border-box;
  color: #D33A2C;
  cursor: pointer;
  display: flex;
  font-size: 1rem;
  font-weight: 700;
  line-height: 33.4929px;
  padding: 2px 12px;
  text-align: left;
  text-decoration: none;
  text-shadow: none;
  text-underline-offset: 1px;
  transition: border .2s ease-in-out,box-shadow .2s ease-in-out;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  white-space: nowrap;
  word-break: break-word;
}

.button-45:active,
.button-45:hover,
.button-45:focus {
  outline: 0;
}


.button-45:active {
  background-color: #D33A2C;
  box-shadow: rgba(0, 0, 0, 0.12) 0 1px 3px 0 inset;
  color: #FFFFFF;
}

.button-45:hover {
  background-color: #FFE3E3;
  border-color: #FAA4A4;
}

.button-45:active:hover,
.button-45:focus:hover,
.button-45:focus {
  background-color: #D33A2C;
  box-shadow: rgba(0, 0, 0, 0.12) 0 1px 3px 0 inset;
  color: #FFFFFF;
}
.icon-item-heart-cart {
    color:#f77f7f;
}
.checkbox-item-cart{
    width:20px;
    height:20px;
    background-color: #f77f7f !important;
}
.checkbox-item-cart::before {
    transform-origin: bottom left !important;
    clip-path: polygon(14% 44%, 0 65%, 50% 100%, 100% 16%, 80% 0%, 43% 62%) !important;
}

.checkbox-item-cart:checked{
    background-color: #D33A2C;
}
/* .list-item-product {
    overflow-y: scroll;
} */
.scroll-list-product::-webkit-scrollbar-track {
  background-color: transparent;
}

.scroll-list-product::-webkit-scrollbar {
  background-color: transparent;
  transition: .3s;
}

.scroll-list-product:hover::-webkit-scrollbar {
  width: 15px !important;
}

.scroll-list-product::-webkit-scrollbar-thumb {
  border-radius: 10px;
  border: 2px solid #444;
}

.text-warning-stamp {
    color :#eca710
}
.text-name-order {
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
.layout-cart-inside {
    position:fixed;
}
.back-cart{
    cursor:pointer;
    border-radius: 20px;
}
</style>