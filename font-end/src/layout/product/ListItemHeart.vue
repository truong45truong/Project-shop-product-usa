<template>
    <div class="h-100 w-100 bg-list-item-heart "
    :class="[ isShowComponent == true ? 'list-item-heart' : isShowComponent == false ? 'hide-list-item-heart' : 'already-list-item-heart']"
    >   
        <div class="position-fixed d-flex icon-cancel-cart align-items-center" @click="$emit('hideListItemHeart', false)">
            <font-awesome-icon  icon="fa-solid fa-arrow-left-long" class="m-3 icon-cancel-cart" />
            <p class="m-0 me-1 text-dark text-icon-cancel">Trở về</p>
        </div>

        <div class="header-shopping-cart text-center">
            <h2 class="title-cart mt-2">Yêu thích</h2>
        </div>
        <div class="bg-dark mb-3">
            <div v-if="checkReponsive == false" class="container action-show">
                <div class="d-flex align-items-center">
                    <div class="d-flex ms-2 align-items-center change-model-show" @click="changeModeShow">
                        <p class="text-white text-action-show m-0 me-2"> Đổi</p>
                        <font-awesome-icon v-if="isShowList" icon="fa-solid fa-list" class="text-white icon-change-action-show" />
                        <font-awesome-icon v-if="!isShowList" icon="fa-solid fa-grip-vertical" class="text-white icon-change-action-show"/>
                    </div>
                    <p v-if="isShowList" class="text-white text-action-show m-0 ms-4" > chế độ danh sách</p>
                    <p v-if="!isShowList" class="text-white text-action-show m-0 ms-4" > chế độ bảng</p>
                </div>
            </div>
            <div v-if="checkReponsive" class="py-2">
                
            </div>
        </div>
        <div v-if="isShowList">
            <div class="container layout-list-item-heart scroll-list-product">
                <div class="d-flex flex-column">
                    <div v-for="item in dataItem" class="mt-0 shadow my-2 bg-list">
                        <div class="d-flex flex-row align-items-center">
                            <div class="col-item-list-heart text-center"><img class="img-cart-market"
                                    :src="'http://127.0.0.1:8000/' + `${item.photo_products__data}`" alt=""></div>
                            <div
                                class="col-item-list-heart  name-product-cart d-flex flex-column align-items-center text-center">
                                <span class="text-name-product-cart"> {{ item.name }}</span>
                                <div class="text-price-product-cart"> <b>{{ item.prices__price }}vnđ</b> </div>
                                <div class="text-price-product-cart"> <b> <span class="text-info">Sale </span>
                                        {{ item.prices__sale }}%</b> </div>
                            </div>
                            <div class="col-item-list-heart d-flex justify-content-around">
                                <a class="btn btn-warning"  :href="'http://127.0.0.1:8080/product/' + item.slug">Chi tiết</a>
                            </div>
                            <div class="col-item-list-heart d-flex justify-content-center">
                                <div class="ms-2 d-flex align-items-center btn-unheart-item"
                                    @click="deleteProductHeart(item.slug)">
                                    <font-awesome-icon icon="fa-solid fa-heart-circle-xmark" />
                                    <p class="m-0 ms-1">Xóa yêu thích</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div v-if="!isShowList">
            <div class="container layout-list-item-heart scroll-list-product">
                <div  class="row  mb-5">
                    <div v-for="item in dataItem"
                        class="col-lg-3 col-md-4 col-sm-6 mt-0 my-3 h-sm-25 item-cart-market-grid px-2">
                        <product-item-heart :name="item.name" :slug="item.slug" :photo="item.photo_products__data" 
                        :sale="item.prices__sale" :price="item.prices__price" @deleteProductHeart="deleteProductHeart" />
                    </div>
                </div>
            </div>
        </div>
        <div class="footer-heart d-flex h-100 py-5" :class="[ get_authenticated == true ?  'flex justify-content-center' : 'justify-content-center']">
                <p class="m-0 text-dark fs-3"> Theo dõi tại đây để nhận nhiều Voucher 
                    <span class="button-78">KHỦNG</span>
                </p>
        </div>

    </div>
</template>

<script>
import { ProductAction } from '../../common/product.service'
import { mapGetters, mapActions } from 'vuex'
import ProductItemHeart from '../../components/product/ProductItemHeart.vue'
export default {
    name: "ListItemHeart",
    props: {
        dataProps: false,
        isShowComponent : null
    },
    data: () => ({
        data: false,
        isShow: false,
        dataItem: false,
        isShowGrid: true,
        isShowList: false,
        checkReponsive : false
    }),
    components: {
        ProductItemHeart,
    },
    computed: {
        ...mapGetters('auth', {
			get_authenticated: 'isAuthenticated'
		}),
        ...mapGetters('notice', {
            get_accept: 'isAccept'
        }),

    },
    async created() {
        console.log("isShowComponent",this.isShowComponent)
        await ProductAction.actionGetProductHeart().then(res => {
            console.log(res)
            this.dataItem = Array.from(res)
        })
    },
    mounted(){
        if(window.innerWidth < 624){
            this.checkReponsive = true
        }
    },
    methods: {
        deleteProductHeart(product_slug) {
            this.isShowNoticeCarefully()
            return new Promise((resolve) => {
                const checkValue = () => {
                    console.log('this.get_accept', this.get_accept)
                    if (this.get_accept === true) {
                        ProductAction.actionPostHeart({
                            params: {
                                product_slug: product_slug
                            }
                        }).then(res => {
                            console.log(res)
                            this.$store.dispatch('notice/actionComplete')
                            this.$store.dispatch('heart/actionUnlikeItems')
                            this.dataItem = this.dataItem.filter((product) => {
                                return product.slug != product_slug
                            })
                        })
                        resolve();
                    }
                    if (this.get_accept === false || this.get_accept === true) {
                        this.$store.dispatch('notice/actionComplete')
                    }
                    else {
                        setTimeout(checkValue, 500);
                    }
                };

                checkValue();
            });
        },
        isShowNoticeCarefully() {
            this.$store.dispatch('notice/actionTypeNotice', { content: 'Bạn có chắc chắn muốn xóa sản phẩm này khỏi yêu thích', type: 'Xóa' })
            this.$store.dispatch('notice/activateShow')
        },
        changeModeShow(){
            this.isShowList = ! this.isShowList
        },
        nextPageDetailProduct(slug){
            this.$router.push('/product/'+ slug)
        },

    }
};
</script>
<style>
@keyframes showListItemHeart {
    from {
        right: -100%;
        top: 0;
    }

    to {
        right: 0%;
    }
}
.bg-list-item-heart {
    background-image: linear-gradient(to bottom, rgb(255, 255, 255), rgb(231, 228, 228), rgb(148, 148, 148));
}
.bg-list {
    background-image: linear-gradient(to bottom, rgb(255, 255, 255), rgb(255, 255, 255));
}
.icon-change-action-show {
    cursor: pointer;
}

.icon-change-action-show:hover {
    color: aqua !important;
}

.list-item-heart {
    position: fixed;
    top: 0;
    z-index: 999;
    right: 0%;
    animation-name: showListItemHeart;
    animation-duration: .75s;
}
@keyframes hideListItemHeart {
    from {
        right: 0%;
        top: 0;
    }

    to {
        right: -100%;
    }
}
.hide-list-item-heart{
    position: fixed;
    top: 0;
    right:-100%;
    z-index: 999;
    animation-name: hideListItemHeart;
    animation-duration: .75s;
}
.already-list-item-heart{
    position: fixed;
    top: 0;
    right:-100%;
}
.icon-cancel-list-heart {
    font-size: 24px;
    cursor: pointer;
}

.icon-cancel-list-heart:hover {
    color: brown;
}

.title-heart {
    background: linear-gradient(to right, #f6f1d3, #648880 85%);
    opacity: 0.96;
}
.footer-heart {
    opacity: 0.96;
    height:20vh;
}


.title-heart h3 {

    color: #ffffff;
    opacity: 1;
}

.col-item-list-heart {
    width: 25%;
}

.layout-list-item-heart {
    overflow-y: scroll;
    height: 60vh;
}

.text-action-show {
    font-size: 18px;
}

.list-item-heart .scroll-list-product::-webkit-scrollbar-thumb {
    border-radius: 10px;
    border: 2px solid black;
}

.btn-unheart-item {
    cursor: pointer;
}

.btn-unheart-item:hover {
    color: brown;
}
.change-model-show{
    cursor:pointer;
}

/* CSS */
.button-78 {
  align-items: center;
  appearance: none;
  background-clip: padding-box;
  background-color: initial;
  background-image: none;
  border-style: none;
  box-sizing: border-box;
  color: #fff;
  cursor: pointer;
  display: inline-block;
  flex-direction: row;
  flex-shrink: 0;
  font-family: Eina01,sans-serif;
  font-size: 16px;
  font-weight: 800;
  justify-content: center;
  line-height: 24px;
  margin: 0;
  min-height: 64px;
  outline: none;
  overflow: visible;
  padding: 19px 26px;
  pointer-events: auto;
  position: relative;
  text-align: center;
  text-decoration: none;
  text-transform: none;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  vertical-align: middle;
  width: auto;
  word-break: keep-all;
  z-index: 0;
}

@media (min-width: 768px) {
  .button-78 {
    padding: 19px 32px;
  }
}

.button-78:before,
.button-78:after {
  border-radius: 80px;
}

.button-78:before {
  background-image: linear-gradient(92.83deg, #ff7426 0, #f93a13 100%);
  content: "";
  display: block;
  height: 100%;
  left: 0;
  overflow: hidden;
  position: absolute;
  top: 0;
  width: 100%;
  z-index: -2;
}

.button-78:after {
  background-color: initial;
  background-image: linear-gradient(#541a0f 0, #0c0d0d 100%);
  bottom: 4px;
  content: "";
  display: block;
  left: 4px;
  overflow: hidden;
  position: absolute;
  right: 4px;
  top: 4px;
  transition: all 100ms ease-out;
  z-index: -1;
}

.button-78:hover:not(:disabled):before {
  background: linear-gradient(92.83deg, rgb(255, 116, 38) 0%, rgb(249, 58, 19) 100%);
}

.button-78:hover:not(:disabled):after {
  bottom: 0;
  left: 0;
  right: 0;
  top: 0;
  transition-timing-function: ease-in;
  opacity: 0;
}

.button-78:active:not(:disabled) {
  color: #ccc;
}

.button-78:active:not(:disabled):before {
  background-image: linear-gradient(0deg, rgba(0, 0, 0, .2), rgba(0, 0, 0, .2)), linear-gradient(92.83deg, #ff7426 0, #f93a13 100%);
}

.button-78:active:not(:disabled):after {
  background-image: linear-gradient(#541a0f 0, #0c0d0d 100%);
  bottom: 4px;
  left: 4px;
  right: 4px;
  top: 4px;
}

.button-78:disabled {
  cursor: default;
  opacity: .24;
}
.box-register-list-item-heart{
    background-color:#6d8194;
    opacity: 1;
}
</style>