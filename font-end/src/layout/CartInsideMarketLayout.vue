<template>
    <div class="row d-flex d-flex-column align-items-center justify-content-center mt-2 mx-2">
        <font-awesome-icon icon="fa-regular fa-circle-xmark" class="icon-hide fs-2 text-dark" @click="$emit('hideCart')" />
        <h3 class="m-0 text-center mt-4">Túi đồ  hôm nay</h3>
        <div class="d-flex justify-content-end w-75 mt-5 me-5">
            <button class="btn btn-dark btn-view-product-cart" :class="[isShowListItem ? 'btn-view-product-cart-activate' : '']" @click="showListItem" >
                <font-awesome-icon icon="fa-solid fa-list" class="text-white fs-5" />
            </button>
            <button class="btn btn-dark btn-view-product-cart" :class="[isShowGridItem ? 'btn-view-product-cart-activate' : '']" @click="showGridItem" >
                <font-awesome-icon icon="fa-solid fa-solar-panel" class="text-white fs-5" />
            </button>
        </div>
        <div v-if="isShowListItem" class="d-flex flex-column w-75 list-item-product scroll-list-product mb-5">
            <div v-for="item in dataItem"  class="mt-0 border border-2 my-2">
                <div class="d-flex flex-row align-items-center">
                    <div class="col-infor-item text-center"><img class="img-cart-market" :src="'http://127.0.0.1:8000/'+`${item.data}`" alt=""></div>
                    <div class="col-infor-item name-product-cart d-flex flex-column align-items-center text-center">
                        <span class="text-name-product-cart"> {{item.name}}</span>
                        <div class="text-price-product-cart"> <b>{{item.price}}vnđ</b> </div>
                        <div class="text-price-product-cart"> <b> <span class="text-info">Sale </span> {{item.sale}}%</b> </div>
                    </div>
                    <div class="col-infor-item d-flex align-items-center">
                        <div class="btn btn-dark me-1 fs-3 btn-number-product-cart d-flex align-items-center text-center p-0">
                            <font-awesome-icon class="fs-5 m-auto" icon="fa-solid fa-plus" />
                        </div>
                        <input type="number" class="col-infor-item text-center w-50" value="3">
                        <div class="btn btn-dark ms-1 fs-3 btn-number-product-cart d-flex align-items-center text-center p-0">
                            <font-awesome-icon class="fs-5 m-auto" icon="fa-solid fa-minus" />
                        </div>
                    </div>
                    <div class="col-infor-item">
                        <p class="text-danger m-0 text-center"><i><b>{{item.price * 3}}</b></i></p>
                    </div>
                    <div class="col-infor-item d-flex align-items-center justify-content-around">
                        <div class="button-45 w-25 d-flex flex-column align-items-center">
                            <span class="text-center"><b>Xóa</b></span>
                        </div>
                        <font-awesome-icon icon="fa-regular fa-heart" class="fs-3 icon-item-heart-cart" />
                    </div>
                </div>
            </div>
        </div>
        <div v-if="isShowGridItem" class="row w-75 list-item-product scroll-list-product mb-5">
            <div v-for="item in dataItem"  class="col-lg-3 col-sm-4 col-6 mt-0 my-3 h-sm-25 item-cart-market-grid px-2">
                <product-item-cart-inside-market :slug="item.slug" :photo="item.data" :name="item.name"
                        :price="item.price" :numberProduct=3 :status="item.status_heart" :hearts="item.count_heart"
                    />
            </div>
        </div>
        <div class="result-product-cart w-75">
            <div class="mt-0 border border-2 border-warning my-2">
                <div class="d-flex align-items-center">
                    <div class="col-infor-item text-center mt-2">
                        <p class="text-danger"><b>Tổng số sản phẩm </b></p>
                        <p class="text-dark"> 48</p>
                    </div>
                    <div class="col-infor-item text-center mt-2">
                        <p class="text-danger"><b>Thanh toán </b></p>
                        <p class="text-dark"> 1.440.000 vnđ</p>
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
                        <p class="text-secondary"> MT-203045756</p>
                    </div>
                </div>
            </div>
        </div>
        <div class="result-product-cart w-75">
            <div class="mt-0 border border-2 border-warning my-2">
                <div class="row d-flex align-items-center">
                    <div class="col-lg-6 my-2 d-flex flex-column col-item-total-cart justify-content-center">
                        <p class="m-0 text-danger text-center mb-2"><b>Địa chỉ</b></p>
                        <div class="d-flex justify-content-center">
                            <font-awesome-icon icon="fa-solid fa-location-dot" class="fs-4" />
                            <p class="m-0 ms-2">K144/29 - Nguyễn Lương Bằng - Hòa Khánh Bắc - tp Đà Nẵng</p>
                        </div>
                    </div>
                    <div class="col-lg-6 my-2 d-flex flex-column justify-content-center">
                        <p class="m-0 text-danger text-center mb-2"><b>Đi động</b></p>
                        <div class="d-flex justify-content-center">
                            <font-awesome-icon icon="fa-solid fa-phone" class="fs-4" />
                            <p class="m-0 ms-2">(+84)</p>
                            <img class="img-flag-phone-user mx-2" src="./../assets/images/flagflag.webp" alt="">
                            <p class="m-0">0889287686</p>
                            <p class="m-0 text-primary">(Nguyễn Hoàng Trường)</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="w-100 d-flex flex-column mt-3 mb-5 align-items-center">
            <div class="btn btn-warning"> Mua ngay </div>
        </div>
    </div>
</template>
<script>
import { mapGetters,mapActions } from 'vuex'
import ProductItemCartInsideMarket from './../components/product/ProductItemCartInsideMarket.vue'
export default ({
    name: 'CartInsideMarketLayout',
    props: {
        dataItem : []
    },
    components: {
        ProductItemCartInsideMarket,
    },
    data: () => ({
        isShowListItem :true ,
        isShowGridItem : false,
    }),
    methods: {
        showListItem(){
            this.isShowListItem = true;
            this.isShowGridItem = false
        },
        showGridItem(){
            this.isShowListItem = false;
            this.isShowGridItem = true;
        }
    },
    computed: {
    },
    created() {
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
.list-item-product {
    overflow-y: scroll;
    height:300px;
}
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
.col-item-total-cart {
    overflow-x: hidden;
}
.text-warning-stamp {
    color :#eca710
}
</style>