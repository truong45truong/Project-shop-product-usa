<template>
    <div class="d-flex align-items-center justify-content-center h-100 w-100 position-relative row">
        <div class="col-sm-6">
            <div class="d-flex w-100 justify-content-around">
                <slide-image-product class="position-sticky"  :photos="photo"/>
                <div class="ms-4 d-flex flex-column align-items-center position-sticky">
                    <div class=" px-1 mt-2">
                        <p class="my-0 text-center text-dark" :class="[ sale > 0 ? 'price-have-sale fw-lighter' : 'fw-bolder ']">{{ price }} vnđ</p>
                    </div>
                    <div class="name-product-in-cart d-flex w-100 justify-content-between">
                        <div class="mt-1 w-100">
                            <p class="m-0 text-dark text-center fw-bolder">{{ name }}</p>
                        </div>
                    </div>
                    <div class=" px-1 mt-2">
                        <p v-if="sale > 0" class="my-0 text-center text-sale-product-order fw-bolder">Sale: {{sale}}%</p>
                    </div>
                    <div v-if="sale > 0" class=" px-1 mt-2">
                        <p class="my-0 text-center text-sale-product-order fw-bolder">{{total_price}}</p>
                    </div>
                </div>
            </div>
        </div>
        <div class="d-flex justify-content-around my-2 col-sm-2">
                <div class="w-25 text-center">
                    <div class="button-35 btn-down m-auto" @click="decliningQuantity">-</div>
                </div>
                <input v-model="numberQuantity" type="number" class="input-quantity-product w-50 text-center">
                <div class="w-25 text-center">
                    <div class="button-35" @click="icreasingQuantity">+</div>
                </div>
        </div>
        <div class="col-sm-3 d-flex flex-column align-items-center">
            <h5>voucher</h5>
            <p v-if="voucher_activate == false" class="m-0 text-danger">Chưa đủ điều kiện</p>
            <p v-if="voucher_activate != false" class="m-0 text-danger"> Đủ điều kiện</p>
        </div>
        <div class="col">
            <h5 class="mb-1 text-danger"><b>Tổng</b></h5>
            <b>
                <p v-if="voucher_activate != false" class="m-0 text-danger"> {{price_after_voucher*numberQuantity}}</p>
            </b>
            <b>
                <p v-if="voucher_activate == false" class="m-0 text-danger"> {{total_price*numberQuantity}}</p>
            </b>
            <h5 class="m-0 btn-remove-item-in-cart" @click="removeProduct">Xóa</h5>
        </div>
    </div>
</template>
  
<script>
import SlideImageProduct from './../other/SlideImageProduct.vue'
import {mapGetters } from 'vuex'
export default ({
    name: 'ProductOrder',
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
        voucher_activate : false,
        price_after_voucher : false
    },
    components: {
      SlideImageProduct
    },
    data: () => ({
        isShowDetail: false,
        isHoverPrice: false,
        status_heart: false,
        checkedSelected : false,
        numberQuantity: 1,
    }),
    computed: {
        ...mapGetters('notice', {
			get_type         : 'isType',
			get_content: 'isContent',
            get_accept : 'isAccept'
		}),
	},
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
            this.$store.dispatch('cart/actionChangeQuangtityProductInOrder', { 
                product_slug: this.slug ,indexOrder : this.indexOrder ,
                index : this.index  , value : 1
            })
        },
        decliningQuantity(){
            if(this.numberQuantity > 1){
                this.numberQuantity -=1
                this.$store.dispatch('cart/actionChangeQuangtityProductInOrder', { 
                    product_slug: this.slug ,indexOrder : this.indexOrder ,
                    index : this.index ,value : -1
                })
            }
        },
        removeProduct(){
            this.$store.dispatch('notice/actionTypeNotice',{content : 'Bạn có muốn xóa sản phẩm : ' +this.name,type : 'Xóa'})
            
            return new Promise((resolve) => {
                this.$store.dispatch('notice/activateShow')
                const checkValue = () => {
                    if (this.get_accept === true) {
                        this.$store.dispatch('cart/actionRemoveSelectedProductInCart', { product_slug: this.slug ,indexOrder : this.indexOrder ,index : this.index });      
                        
                        resolve();
                    }
                    if(this.get_accept === false || this.get_accept === true){
                        this.$store.dispatch('notice/actionComplete')
                    }
                    else {
                        setTimeout(checkValue, 500);
                    }
                };

                checkValue();
            });
        }
    },
    created(){
        this.numberQuantity = this.numberProduct
    }

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
.text-sale-product-order{
    color:rgb(255, 51, 0);
    opacity:1;
}
.price-have-sale {
    text-decoration:line-through;
}
</style>