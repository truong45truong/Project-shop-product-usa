<template>
    <div v-if="isDelete == false" class="d-flex flex-row align-items-center w-100 row">
        <div class="col-sm-4 col-6 col-infor-item text-center"><img class="img-cart-market" :src="'http://127.0.0.1:8000/'+`${photo_product}`" alt=""></div>
        <div class="col-lg-6 col-6 col-infor-item name-product-cart d-flex flex-column align-items-center text-center">
            <span class="text-name-product-cart"> {{product_name}}</span>
            <div class="text-price-product-cart"> <b>{{price_total}} vnđ</b> </div>
            <div class="text-price-product-cart"> <b> <span class="text-info">Sale </span> {{product_sale}}%</b> </div>
        </div>

        <div class="col-sm-2 col-infor-item d-flex align-items-center justify-content-around my-3">
            <div class="button-45 w-25 d-flex flex-column align-items-center" @click="removeProductInCart">
                <span class="text-center"><b>Xóa</b></span>
            </div> 
        </div>
    </div>
</template>
  
<script>
import SlideImageProduct from './../other/SlideImageProduct.vue'

export default ({
    name: 'ProductCartInside',
    props: {
        product_slug : '',
        photo_product : '',
        product_name : '',
        product_price: '',
        product_sale : '',
        product_price_total : '',
        product_quantity : 0,
        index : false,
        name_order :''

    },
    data: () => ({
        isShowDetail: false,
        isDelete: false,
        numberQuantity: 1,
        price_total : 0,
    }),
    
    methods: {
        showDetail(){
            this.isShowDetail = ! this.isShowDetail
        },
        selectedProduct(){

        },
        
        nextPageDetailProduct(){
            this.$router.push('/product/'+ this.slug)
        },
        async removeProductInCart(){
            await this.$store.dispatch('cart/actionRemoveProductInCart', { product_slug: this.product_slug ,name_order : this.name_order , indexOrder : 0 ,index : this.index})
            this.isDelete = true
            this.$emit('changePriceTotalOrder',-this.numberQuantity*this.product_price_total,this.product_slug,true,-1)
        }
    },
    created(){
        this.numberQuantity = this.product_quantity;
        this.price_total = Math.ceil((100 - this.product_sale) / 100 * this.product_price)
        this.price_total = new Intl.NumberFormat('vi-VN').format(this.price_total)
    }

})
</script>
<style>

</style>