<template>
    <div class="row ">
        <div class="w-100 d-flex justify-content-between">
            <div class="name-product-in-cart d-flex w-100 justify-content-between">
                <div class="mt-1 w-100">
                    <p class="m-0 text-dark text-center fw-bolder text-name-product-cart">{{ name }}</p>
                </div>
            </div>
            <input v-model="checkedSelected" type="checkbox" class="check-box-cart" @click="selectedProduct"
            :checked="isSelectOrder == true"
            >
        </div>
    </div>
    <div class="d-flex info-product-cart align-items-center justify-content-center h-100 w-100 position-relative row">
        <slide-image-product  :photos="photo"/>
        <div class="col-4 position-relative d-flex flex-column align-items-center">
            <div v-if="sale > 0" class="d-flex flex-column sale-product-category ">
                <div class="content-sale">
                    <p class="m-0 text-content-sale">
                        <span>
                        <font-awesome-icon icon="fa-solid fa-bolt" class="text-danger" />
                        </span> <b>Giảm sốc</b>
                    </p>
                </div>
                <div class="text-center">
                    <p class="text-content-sale m-0">
                        <span class="text-danger"> lên tới </span>
                        <b class="ms-1">{{sale}} %</b>
                    </p>
                </div>
            </div>
            <div class=" px-1 mt-2">
                <p class="my-0 text-center text-center text-dark fw-bolder">{{ price_total}} vnđ</p>
            </div>
            <div class=" px-1 mt-2 d-flex justify-content-center my-2">
                <button class="my-0 text-center text-center text-dark fw-bolder btn btn-dark btn-remove-item-in-cart "
                    @click="removeProductInCart">
                    <p class="m-0 text-white">Xóa</p>
                </button>
            </div>
        </div>
        <div class="my-2 col-sm-4 d-flex flex-column justify-content-between align-items-center ">
                <div class="d-flex justify-content-around">
                    <div class="w-25 text-center">
                        <button :class=" numberQuantity == 1 ? 'disable-button' : 'button-35'  " class=" btn-down m-auto text-center"  @click="decliningQuantity">-</button>
                    </div>
                    <input v-model="numberQuantity" type="number" class="input-quantity-product w-25 text-center"
                    @change="changeNumberQuantity" >
                    <div class="w-25 text-center">
                        <div class="button-35" @click="icreasingQuantity">+</div>
                    </div>
                </div>

                <button class="button-481 mt-2" @click="nextPageDetailProduct"><span>Chi tiết</span></button>
        </div>  
    </div>
</template>
  
<script>
import { Carousel, Navigation, Slide, Pagination } from 'vue3-carousel'
import SlideImageProduct from './../other/SlideImageProduct.vue'
import qs from 'qs';
export default ({
    name: 'ProductCart',
    emits: ['hideCart'],
    props: {
        slug: false,
        name: false,
        descriptions: false,
        category: false,
        price: false,
        photo: false,
        quantity: 1,
        sale: 0,
        total_price : false,
        price_status : false,
        indexOrder : false,
        index : false ,
        name_order : false,
        isSelectOrder : false,
        dataProductSelect : false
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
        price_total : 0,
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
                let listQuery = {...this.$router.currentRoute._value.query}
                if(listQuery.products != null){
                    let products = qs.parse(this.$router.currentRoute._value.query.products)
                    console.log("products list seledct",products)
                    products = Object.values(products)
                    products.push({
                        quantity : this.numberQuantity,
                        product_slug : this.slug
                    })
                    
                    delete listQuery.products
                    this.$router.push({ query: { "products":qs.stringify(products) , ...listQuery} });
                }
                else {
                    this.$router.push({ query: { "products":qs.stringify([{
                        quantity : this.numberQuantity,
                        product_slug : this.slug
                    }]) , ...listQuery} });
                }
                this.$emit('hideListItemHeart',true)
            }
            else{
                let listQuery = {...this.$router.currentRoute._value.query}
                if(listQuery.products != null){
                    let products = qs.parse(this.$router.currentRoute._value.query.products)
                    console.log("products list seledct",products)
                    products = Object.values(products)
                    products = products.filter(product => {
                        return product.product_slug != this.slug
                    })
                    
                    delete listQuery.products
                    this.$router.push({ query: { "products":qs.stringify(products) , ...listQuery} });
                }
                else {
                    this.$router.push({ query: { "products":qs.stringify({
                        quantity : this.numberQuantity,
                        product_slug : this.slug
                    }) , ...listQuery} });
                }
                console.log("products list seledct",qs.parse(this.$router.currentRoute._value.query.products))
                this.$store.dispatch('cart/actionRemoveSelectedProductInCart', { product_slug: this.slug ,indexOrder : this.indexOrder ,index : this.index });
            }
            this.checkedSelected = ! this.checkedSelected 
        },
        icreasingQuantity(){
            this.numberQuantity += 1
            this.$store.dispatch('cart/actionChangeQuantityProductInCart', { value: 1 , indexOrder : this.indexOrder ,index : this.index });
        },
        decliningQuantity(){
            if(this.numberQuantity > 1){
                this.numberQuantity -=1;
                this.$store.dispatch('cart/actionChangeQuantityProductInCart', { value: -1 , indexOrder : this.indexOrder ,index : this.index });
                this.changeQuantityProductInCart(-1)
            }
            
        },
        nextPageDetailProduct(){
            this.$emit('hideCart')
            this.$router.push('/product/'+ this.slug)
        },
        removeProductInCart(){
            this.$store.dispatch('cart/actionRemoveProductInCart', { product_slug: this.slug ,name_order : this.name_order , indexOrder : this.indexOrder ,index : this.index})
        },
        changeNumberQuantity(){
            if(/^\d+$/.test(this.numberQuantity)){
                if(this.numberQuantity <= 0){
                    this.numberQuantity = 1
                    this.$store.dispatch('cart/actionChangeNumberQuantityProductInCart', { product_slug: this.slug ,name_order : this.name_order , indexOrder : this.indexOrder ,index : this.index,quantity : 1})

                } else {
                    this.$store.dispatch('cart/actionChangeNumberQuantityProductInCart', { product_slug: this.slug ,name_order : this.name_order , indexOrder : this.indexOrder ,index : this.index,quantity : this.numberQuantity})
                }
                
            }else {
                this.numberQuantity = 1
                this.$store.dispatch('cart/actionChangeNumberQuantityProductInCart', { product_slug: this.slug ,name_order : this.name_order , indexOrder : this.indexOrder ,index : this.index,quantity : 1})
            }
        }
    },
    created(){
        this.numberQuantity = this.quantity;
        this.checkedSelected = this.isSelectOrder;
        for (let product of this.dataProductSelect){
            if(product.product_slug == this.slug){
                this.$store.dispatch('cart/actionSelectProductInCart', { product_slug: this.slug ,indexOrder : this.indexOrder ,index : this.index })
                this.checkedSelected = true
            }
        }
        this.price_total = Math.ceil((100 - this.sale) / 100 * this.price)
        this.price_total = new Intl.NumberFormat('vi-VN').format(this.price_total)
    }

})
</script>
<style>
.price-product-cart{
    max-width:100% ;
}
.check-box-cart {
    display:block;
    position:static !important;
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
.info-product-cart .sale-product-category{
    position:relative;
    width:fit-content;
}
.btn-remove-item-in-cart:hover{
    opacity : 1;
}
.text-name-product-cart {
    font-size: 14px;
}
.button-481 {
  max-width:200px;
  max-height:50px;
  border : 1px solid black;
  appearance: none;
  background-color: #FFFFFF;
  box-sizing: border-box;
  color: #000000;
  cursor: pointer;
  display: inline-block;
  font-family: Clarkson,Helvetica,sans-serif;
  font-size: 14px;
  font-weight: 500;
  letter-spacing: 0;
  line-height: 1em;
  margin: 0;
  opacity: 1;
  outline: 0;
  padding: 1.5em 2.2em;
  position: relative;
  text-align: center;
  text-decoration: none;
  text-rendering: geometricprecision;
  text-transform: uppercase;
  transition: opacity 300ms cubic-bezier(.694, 0, 0.335, 1),background-color 100ms cubic-bezier(.694, 0, 0.335, 1),color 100ms cubic-bezier(.694, 0, 0.335, 1);
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  vertical-align: baseline;
  white-space: nowrap;
}

.button-481:before {
  animation: opacityFallbackOut .5s step-end forwards;
  backface-visibility: hidden;
  background-color: #EBEBEB;
  clip-path: polygon(-1% 0, 0 0, -25% 100%, -1% 100%);
  content: "";
  height: 100%;
  left: 0;
  position: absolute;
  top: 0;
  transform: translateZ(0);
  transition: clip-path .5s cubic-bezier(.165, 0.84, 0.44, 1), -webkit-clip-path .5s cubic-bezier(.165, 0.84, 0.44, 1);
  width: 100%;
}

.button-481:hover:before {
  animation: opacityFallbackIn 0s step-start forwards;
  clip-path: polygon(0 0, 101% 0, 101% 101%, 0 101%);
}

.button-481:after {
  background-color: #FFFFFF;
}

.button-481 span {
  z-index: 1;
  position: relative;
  top:-4px;
}
.disable-button {
    max-width:200px;
    max-height:50px;
    border : 1px solid black;
    appearance: none;
    background-color: #FFFFFF;
    box-sizing: border-box;
    color: #000000;
    cursor: pointer;
    display: inline-block;
    font-family: Clarkson,Helvetica,sans-serif;
    font-size: 14px;
    font-weight: 500;
    letter-spacing: 0;
    line-height: 1em;
    margin: 0;
    opacity: 1;
    outline: 0;
    padding: 1.5em 2.2em;
    position: relative;
    text-align: center;
    text-decoration: none;
    text-rendering: geometricprecision;
    text-transform: uppercase;
    transition: opacity 300ms cubic-bezier(.694, 0, 0.335, 1),background-color 100ms cubic-bezier(.694, 0, 0.335, 1),color 100ms cubic-bezier(.694, 0, 0.335, 1);
    user-select: none;
    -webkit-user-select: none;
    touch-action: manipulation;
    vertical-align: baseline;
    white-space: nowrap;
    border-radius: 50%;
    height:25px;
    width:16px;
    cursor:not-allowed !important;
}
.disable-button:hover {
    border:1px solid !important;
}
@media only screen and (max-width: 524px)
{
    .layout-img-product {
        top:10%;
        left:0%;
    }
    .card{
        width: 100%;
        height:fit-content !important;
        padding-top: 15px;
    }
    .button-48 {
        max-width: 60px;
        padding : 5px 15px;
    }
    .button-48 span {
        font-size: 10px !important;
    }
}
</style>