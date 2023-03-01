<template>
    <div class="d-flex align-items-center justify-content-center h-100 w-100 position-relative row">
        <slide-image-product  :photos="photo"/>
        <div class="col-4">
            <div class=" px-1 mt-2">
                <p class="my-0 text-center text-center text-dark fw-bolder">{{ price }} vnđ</p>
            </div>
            <div class="name-product-in-cart d-flex w-100 justify-content-between">
                <div class="mt-1 w-100">
                    <p class="m-0 text-dark text-center fw-bolder">{{ name }}</p>
                </div>
            </div>
            <div class=" px-1 mt-2">
                <p class="my-0 text-center btn-remove-item-in-cart text-center text-dark fw-bolder">Xóa</p>
            </div>
        </div>
        <div class="d-flex justify-content-around my-2 col-4">
                <div class="w-25 text-center">
                    <div class="button-35 btn-down m-auto" @click="decliningQuantity">-</div>
                </div>
                <input v-model="numberQuantity" type="number" class="input-quantity-product w-25 text-center">
                <div class="w-25 text-center">
                    <div class="button-35" @click="icreasingQuantity">+</div>
                </div>
        </div>  
        <input v-model="checkedSelected" type="checkbox" class="check-box-cart" @click="selectedProduct">
    </div>
</template>
  
<script>
import { Carousel, Navigation, Slide, Pagination } from 'vue3-carousel'
import SlideImageProduct from './../other/SlideImageProduct.vue'
export default ({
    name: 'ProductCart',
    props: {
        slug: false,
        name: false,
        descriptions: false,
        category: false,
        price: false,
        photo: false,
        numberProduct: 1,
        sale: 0,
        total_price : false,
        price_status : false,
        indexOrder : false,
        index : false ,
    },
    components: {
      Pagination,
      Carousel,
      Slide,
      Navigation,
      SlideImageProduct
    },
    data: () => ({
        isShowDetail: false,
        isHoverPrice: false,
        status_heart: false,
        checkedSelected : false,
        numberQuantity: 1,
        settings: {
            itemsToShow: 1,
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
                itemsToShow: 1,
                snapAlign: 'center',
                },
                // 1024 and up
                1024: {
                itemsToShow: 1,
                snapAlign: 'center',
                },
        },
    }),
    methods: {
        showDetail(){
            this.isShowDetail = ! this.isShowDetail
        },
        selectedProduct(){
            if(this.checkedSelected == false){
                this.$store.dispatch('cart/actionSelectProductInCart', { product_slug: this.slug ,indexOrder : this.indexOrder ,index : this.index })
            }
            else{
                this.$store.dispatch('cart/actionRemoveSelectedProductInCart', { product_slug: this.slug ,indexOrder : this.indexOrder ,index : this.index });
            }
            this.checkedSelected = ! this.checkedSelected 
        },
        icreasingQuantity(){
            this.numberQuantity += 1
        },
        decliningQuantity(){
            if(this.numberQuantity > 1)
            this.numberQuantity -=1
        }
    },

})
</script>
<style>
.price-product-cart{
    max-width:100% ;
}
.check-box-cart {
    position:absolute;
    top:5%;
    left: 51.3%;
    z-index: 999;
    transform: scale(1.5);
    transition: 120ms transform ease-in-out;
    box-shadow: inset 1em 1em rgba(66, 7, 114, 0);
}
.price-product-in-cart {
    background-color: rgb(230, 230, 230);
    position:absolute;
    bottom : 23%;
}

/* CSS */
.button-35 {
  align-items: center;
  background-color: #fff;
  border-radius: 50%;
  box-shadow: transparent 0 0 0 3px,rgba(18, 18, 18, .1) 0 6px 20px;
  box-sizing: border-box;
  width:25px;
  height:25px;
  color: #121212;
  cursor: pointer;
  display: inline-flex;
  flex: 1 1 auto;
  font-family: Inter,sans-serif;
  font-size: 1.2rem;
  font-weight: 700;
  justify-content: center;
  line-height: 1;
  margin: 0;
  outline: none;
  padding: 0.5rem 0.75rem;
  text-align: center;
  text-decoration: none;
  transition: box-shadow .2s,-webkit-box-shadow .2s;
  white-space: nowrap;
  border: 1px solid black;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
}

.button-35:hover {
  box-shadow: #121212 0 0 0 3px, transparent 0 0 0 0;
}
.btn-down{
    padding : 0 .915rem;
}
.input-quantity-product{
    width:fit-content;
}
.btn-remove-item-in-cart{
    cursor:pointer;
    opacity: 0.8;
}
.btn-remove-item-in-cart:hover{
    opacity : 1;
}
</style>