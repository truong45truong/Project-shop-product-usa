<template>
    <div class="d-flex flex-column mt-5" :class="[ toMarket == true ? 'market' : 'container flash-sale-top' ]">
        <div class="info-user-layout w-100 d-flex flex-column align-items-center">
            <InforUserLayout :class="[ isInforUser == true ? 'info-user' : 'info-user-hide' ]" @hide="isShowInforUser"/>
        </div>
        <div class="row  d-flex mx-3 justify-content-between">
            <div class="col-lg-3 d-flex align-items-center bulletin-board ">
                <font-awesome-icon icon="fa-solid fa-bookmark" class="text-dark bulletin-content" />
                <div class="bulletin-text">
                    <h5 class="text-white m-0 me-1 ms-4 fs-3">Chợ</h5>
                </div>
            </div>
            <div v-if="toMarket" class="col-3 d-flex align-items-center btn-market-layout">
            </div>
            <div class="col-lg-3 d-flex align-items-center btn-market-layout justify-content-end">
                <font-awesome-icon v-if="toMarket" icon="fa-solid fa-user" class="text-dark fs-2 icon-market me-5" @click="isShowInforUser"/>
                <font-awesome-icon v-if="toMarket" icon="fa-solid fa-basket-shopping" class="text-dark fs-2 icon-market me-5" />
                <div class="btn-market d-flex align-items-center" @click="toTheMaket">
                    <p v-if="!toMarket" class="text-white m-0 btn-market-inside">Vào chợ </p>
                    <p v-if="toMarket" class="text-white m-0 btn-market-inside">Ra chợ </p>
                    <font-awesome-icon icon="fa-solid fa-arrow-right" class="text-white mx-4 fs-2 btn-icon-market" />
                </div>
            </div>
        </div>
        <div class="row mx-3">
            <Carousel :settings="settings" :breakpoints="breakpoints">
                <Slide v-for="item in listProductItem" :key="item" :class="'mx-1 shawdo'">
                    <product-item :slug="item.slug" :photo="item.photo_products[0]" :name="item.name"
                        :price="item.prices[0]"
                    />
                </Slide>
                <template #addons>
                    <Pagination />
                    <Navigation class= "pagination-container" />
                </template>
            </Carousel>
        </div>
    </div>
</template>
  
<script>
import { Carousel, Navigation, Slide, Pagination } from 'vue3-carousel'
import { ProductApiService } from '../common/product.service'
import CountDownFLashSale from '../components/other/CountDowmFLashSale.vue'
import InforUserLayout from './InforUserLayout.vue'
import ProductItem from '../components/product/ProductItem.vue'
import 'vue3-carousel/dist/carousel.css'
import 'vue3-carousel/dist/carousel.js'
export default ({
    name: 'ListProductItemFlashSale',
    components: {
        ProductItem,
        Pagination,
        Carousel,
        Slide,
        Navigation,
        CountDownFLashSale,
        InforUserLayout
    },
    data: () => ({
        listProductItem : [],
        toMarket : false ,
        isInforUser : false,


        settings: {
            itemsToShow: 2,
            snapAlign: 'center',
        },
      // breakpoints are mobile first
      // any settings not specified will fallback to the carousel settings
      breakpoints: {
        400: {
          itemsToShow: 1,
          snapAlign: 'center',
        },
        // 700px and up
        700: {
          itemsToShow: 3,
          snapAlign: 'center',
        },
        // 1024 and up
        1024: {
          itemsToShow: 4,
          snapAlign: 'center',
        },
      },
    }),
    methods: {
        toTheMaket(){
            this.toMarket = ! this.toMarket;
            console.log("vao chợ")
        },
        isShowInforUser() {
            this.isInforUser = ! this.isInforUser
            console.log("show infor user",this.isInforUser)
        }
    },
    async created(){
        await ProductApiService.get().then(res => {
            let array = []
            for(let item of res.data){
                console.log(item)
                array.push(item)
            }
            this.listProductItem = array
            console.log(this.listProductItem)
        })
    }
})
</script>
<style>
.market{
    top:0%;
    left:0%;
    display:block;
    position:fixed !important;
    width:100% !important;
    height: 100% !important;
    z-index: 9999;
    background-color: white;
    border:5px solid rgb(36,41,47);
    transition:all 0.5s;
    align-content: center;
}
.box-demo {
    height:85%;
    position:relative;
    overflow:hidden
}
.bulletin-board {
    position:relative;
}
.btn-market-layout {
    position:relative;
}
.btn-market {
    position:relative;
    background-color: rgb(36,41,47);
    top:-20%;
    padding: 15px 20px;
    border-radius: 15px;
}
.icon-market{
    position:relative;
    top:-20%;
    transition:2.5s;
}
.bulletin-content {
    position:relative;
    top:-20%;
    font-size: 11rem;
    z-index: 10;
}
.bulletin-text {
    position:absolute;
    top:5%;
    z-index: 11;
}
.show-all-product-flash-sale{
    font-family: 'Sassy Frass', cursive;
    font-weight: 700;
}

.pagination-container {
  background-color: rgb(36,41,47);
  padding: 10px;
  margin-top: 10px;
}
.carousel__icon{
  color:white;
}
.carousel__icon path{
  color:white;
  font-size: larger;
}
.pagination-button {
  background-color: rgb(36,41,47);
  color: white;
  font-size: 14px;
  padding: 8px 16px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-right: 8px;
}
.btn-icon-market{
    width:100%;
    position:relative;
    right:10%;
    transition:1.5s;
}
@keyframes hoverBtnMarket {
    from {
        right:10%;
    }
  to {right:-25%;}
}
.btn-market:hover {
    cursor:pointer;
    
}
.btn-market:hover .btn-icon-market {
    animation-name: hoverBtnMarket;
    animation-duration: 1.5s;
    right:-25%;
    cursor:pointer;
}
@keyframes inforUserShow {
    from {
        top:-100%;
    }
  to {top : 0%;}
}
@keyframes inforUserHide {
    from {
        top:0;
    }
  to {top : -100%;}
}
.info-user{
    width : 75%;
    position:absolute;
    background-color: white ;
    border: 3px solid black;
    top:0%;
    animation-name: inforUserShow;
    animation-duration: .75s;
    z-index: 99;
    border-radius: 20px;
}
.info-user-hide {
    position:absolute;
    top : -100%;
    animation-name: inforUserHide;
    animation-duration: .5s;
}
.icon-market:hover {
    cursor: pointer;
    color :brown !important;   
}
</style>