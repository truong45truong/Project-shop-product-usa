<template>
    <div class="d-flex flex-column list-product-layout " :class="[ toMarket == true & isShowLoginStore == false ? 'market bg-list-item-heart' : 'container flash-sale-top' ]">
        <div class="info-user-layout w-100 d-flex flex-column align-items-center">
            <InforUserLayout v-if="inforUser != false " :name="inforUser.name"  :address ="inforUser.address" :phone="inforUser.phones" :photo="inforUser.photo"
            :class="[ isInforUser == true ? 'info-user' : 'info-user-hide' ]" @hide="isShowInforUser"/>
        </div>
        <div class="info-user-layout w-100 d-flex flex-column align-items-center">
            <cart-inside-market-layout v-if="isCart != false " :class="[ isCart == true ? 'info-user' : 'info-user-hide' ]" @hideCart="isShowCart"/>
        </div>
        <div v-if="toMarket == false & isShowLoginStore == false" class="row d-flex justify-content-between  mx-3 " :class="[toMarket & isShowLoginStore == false ? 'layout-menu-market' : '']">
            <div class="col-3 d-flex align-items-center bulletin-board ">
                <font-awesome-icon icon="fa-solid fa-bookmark" class="text-dark bulletin-content" />
                <div class="bulletin-text">
                    <h5 class="text-white m-0 me-1 ms-4 fs-3">Chợ</h5>
                </div>
            </div>
            <div class="col-3 d-flex align-items-center btn-market-layout justify-content-end">
                <div class="btn-market d-flex align-items-center" @click="toTheMaket">
                    <p v-if="!toMarket " class="text-white m-0 btn-market-inside">Vào chợ </p>
                    <font-awesome-icon icon="fa-solid fa-arrow-right" class="text-white mx-4 fs-2 btn-icon-market" />
                </div>
            </div>
        </div>
        <div v-if="toMarket & isShowLoginStore == false" class="container" id="menu-list-item">
            <div class="row text-center">
                <h3 class="text-dark my-2">Chợ mua sắm</h3>
            </div>
            <div class="row my-1 d-flex align-items-center btn-market-layout justify-content-end">
                <div class="col-6">
                    <button v-if="toMarket & isShowLoginStore == false &  get_authenticated == false" class="btn btn-dark" @click="loginMarket">
                        Đăng nhập ngay
                    </button>
                    <font-awesome-icon v-if="toMarket & isShowLoginStore == false &  get_authenticated == true" icon="fa-solid fa-user" class="text-dark fs-2 icon-market me-5" @click="isShowInforUser"/>
                    <font-awesome-icon v-if="toMarket & isShowLoginStore == false &  get_authenticated == true" icon="fa-solid fa-basket-shopping" class="text-dark fs-2 icon-market me-5" @click="isShowCart" />
                </div>
                <div class="col-6 d-flex align-items-end justify-content-end">
                    <div class="btn-market d-flex" @click="toTheMaket">
                        <p v-if="toMarket & isShowLoginStore == false"  class="text-white m-0 btn-market-inside">Ra chợ </p>
                        <font-awesome-icon icon="fa-solid fa-arrow-right" class="text-white mx-4 fs-2 btn-icon-market" />
                    </div>
                </div>
            </div>
        </div>
        <div class="container">
            <div v-if="toMarket  & isShowLoginStore == false" class="row list-product-layout" :style="{ height: elementHeight + 'px' }">
                <div v-for="item in listProductItem"  class="col-lg-3 col-sm-4 col-6 mt-0 my-3 h-sm-25 px-2">
                    <product-item :slug="item.slug" :photo="item.data" :name="item.name" class=" bg-white" :sale="item.sale"
                            :price="item.price" :numberProduct=3 :status="item.status_heart" :hearts="item.count_heart"
                        />
                </div>
            </div>
            <div v-if="listProductItem.length > 0" class="row" >
                <Carousel v-if="!toMarket || isShowLoginStore == true" :settings="settings" :breakpoints="breakpoints" :wrap-around="true">
                    <Slide v-for="item in listProductItem" :key="item" :class="'mx-1 shawdo'">
                        <product-item :slug="item.slug" :photo="item.data" :name="item.name" 
                        :sale='item.sale' :price="item.price" :status="item.status_heart" 
                        :hearts="item.count_heart"
                        />
                    </Slide>
                    <template #addons>
                        <Pagination />
                        <Navigation class= "pagination-container" />
                    </template>
                </Carousel>
            </div>
        </div>
    </div>
</template>
  
<script>
import { Carousel, Navigation, Slide, Pagination } from 'vue3-carousel'
import { actionUser } from '../../common/user.service'
import { mapGetters} from 'vuex'
import { ProductApiService } from '../../common/product.service'
import CountDownFLashSale from '../../components/other/CountDowmFLashSale.vue'
import InforUserLayout from '../user/InforUserLayout.vue'
import ProductItem from '../../components/product/ProductItem.vue'
import CartInsideMarketLayout from '../cart/CartInsideMarketLayout.vue'
import ProductItemCartInsideMarket from '../../components/product/ProductItemCartInsideMarket.vue'
import 'vue3-carousel/dist/carousel.css'
import 'vue3-carousel/dist/carousel.js'
import { URL_PATH_SERVER , DOMAIN} from '../../common/constants'
export default ({
    name: 'ListProductItemFlashSale',
    components: {
        ProductItem,
        Pagination,
        Carousel,
        Slide,
        Navigation,
        CountDownFLashSale,
        InforUserLayout,
        CartInsideMarketLayout,
        ProductItemCartInsideMarket,
        
    },
    computed: {
		...mapGetters('auth', {
			get_user         : 'currentUser',
            get_authenticated: 'isAuthenticated',
            isShowLoginStore : 'isShowLogin'
		}),
	},
    data: () => ({
        listProductItem : [],
        URL_PATH_SERVER : URL_PATH_SERVER ,
        toMarket : false ,
        isInforUser : false,
        inforUser : false,
        isCart : false,
        arrayMarket : [],
        elementHeight : '',
        settings: {
            itemsToShow: 2,
            snapAlign: 'center',
        },
      // breakpoints are mobile first
      // any settings not specified will fallback to the carousel settings
      breakpoints: {
        400: {
          itemsToShow: 2,
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
        loginMarket(){
            this.$router.push({ name : 'sign-in' , query : {
            nextPage : String(window.location.href).replace(DOMAIN,'')
            }})
        },
        toTheMaket(){
            this.toMarket = ! this.toMarket;
            if(this.toMarket == true){

                new Promise((resolve) => {
                    const checkValue = () => {
                        if (document.getElementById('menu-list-item') != null) {
                            this.elementHeight = window.innerHeight - document.getElementById('menu-list-item').offsetHeight
                            resolve();
                        }
                        else {
                            setTimeout(checkValue, 500);
                        }

                    };

                    checkValue();
                });
            }
            let listQuery = {...this.$router.currentRoute._value.query}
            if(listQuery.nextMarket != null){
                delete listQuery.nextMarket
                this.$router.push({ query: listQuery });
            }else {
                this.$router.push({ query: { "nextMarket": true , ...listQuery} });
            }
            
            
        },
        async isShowInforUser() {
            this.isInforUser = ! this.isInforUser
            if( this.inforUser == false){
                await actionUser.getInforUser().then(async (response) => {
                    this.inforUser = {
                        photo : URL_PATH_SERVER  + response.user.photo,
                        address : response.user.address,
                        phones : response.user.phones,
                        name : response.user.name,
                    }
                })
            }
        },
        isShowCart(){
            this.isCart = ! this.isCart
        },
        async changeStatusHeartProduct(){
            await ProductApiService.get_order_today().then(res => {
                console.log(res)
                this.listProductItem = Array.from(res.data.products)
            })
        }
    },
    async created(){
        await ProductApiService.get().then(res => {
            console.log('array_market',res)
            this.listProductItem = Array.from(res.data.products)
        })
    },
    mounted() {
        window.addEventListener('resize', ()=> {
            console.log("this.elementHeight = window.innerHeight - document.getElementById('menu-list-item').offsetHeight;",document.getElementById('menu-list-item').offsetHeight)
            this.elementHeight = window.innerHeight - document.getElementById('menu-list-item').offsetHeight
        });
        let listQuery = {...this.$router.currentRoute._value.query}
        if(listQuery.nextMarket != null){
            this.toMarket = true
            new Promise((resolve) => {
                    const checkValue = () => {
                        if (document.getElementById('menu-list-item') != null) {
                            this.elementHeight = window.innerHeight - document.getElementById('menu-list-item').offsetHeight
                            resolve();
                        }
                        else {
                            setTimeout(checkValue, 500);
                        }

                    };

                    checkValue();
            });
        }
    },
})
</script>
<style>
.market{
    top:0%;
    left:0%;
    display:block;
    position:fixed !important;
    width:100% !important;
    z-index: 9999;
    background-color: white;
    border:5px solid rgb(36,41,47);
    align-content: center;
}
.info-user-layout {
    z-index: 1000;
}
.layout-product-item {
    max-width: 400px;
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
    max-width: 200px;
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
.carousel {
    max-width: 100%;;
}
.pagination-container {
  background-color: rgb(36,41,47);
  padding: 10px;
  margin-top: 10px;
  max-width: 100%;;
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
#menu-list-item {
    box-shadow: 0 4px 2px -2px rgb(175, 175, 175);
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
    max-width : 1440px;
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

.list-product-layout::-webkit-scrollbar {
  display: none;
}
.list-product-layout{
    height:fit-content;
    overflow-y: scroll;
}

@media only screen and (max-width: 524px) {
    .bulletin-board {
        justify-content: start !important;
        font-size: larger;
    }
    .bulletin-content {
        font-size: 120px;
    }
    .btn-market {
        padding:10px 20px;
    }
    .layout-menu-market  {
        position:fixed;
        top:2%;
        background-color: white;
        margin-left:0 !important;
        padding:0 !important;
    }
    .layout-list-product-market {
        height:fit-content !important;
    }
}
</style>