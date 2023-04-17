<template>
    <div class="container position-relative mt-3">
        <div class="row bg-dark">
          <div class="col-4">
            <p class="text-white m-0 text-center">
              Mã :
              <span> {{name}} </span>
            </p>
          </div>
          <div class="col-4">
            <p class="text-white m-0 text-center">
              Ngày tạo :
              <span> {{datetime}} </span>
            </p>
          </div>
          <div class="col-4">
            <p class="text-white m-0 text-center">
              Tổng tiền :
              <span> {{total_price}} </span>
            </p>
          </div>
        </div>
        <div class="container-cart d-flex justify-content-center row m-0">
          <div v-for="product,index in products" class="card col-lg-6 mt-1">
              <product-cart
                :slug ="product.product_slug" :name="product.product_name"
                :category="product.category_name" :photo="product.photo_product"
                :price="product.product_price" :sale='product.product_sale'
                :total_price="product.product_price_total" :price_status="product.product_price_status"
                :indexOrder="indexOrder" :index="index" :quantity="product.product_quantity"
                :name_order = "name" :isSelectOrder ="product.isSelectOrder" @hideCart="hideCart"
              />
          </div>
        </div>
      </div>
</template>
  
<script>
import ProductCart from './../product/ProductCart.vue'
export default ({
    name: 'CartOrder',
    props: {
        name: '',
        datetime: '',
        receiver: '',
        address_receiver: '',
        phone_receiver: '',
        status: false,
        note: '',
        logs: '',
        total_price: '',
        cancel: false,
        request_cancel: false,
        transport: false,
        products: false,
        indexOrder: false
    },
    components : {
      ProductCart,
    },
    computed: {

    },
    methods: {
      removeProductInCart(){
        this.$store.dispatch('cart/actionRemoveProductInCart', {
                product_slug :"empty"
            })
      },
      hideCart(){
        this.$emit('hideCart')
      }
    }

})
</script>
<style lang="scss">
.container-cart {
  width: 100%;
  margin: 0;
  position: relative;
  transition: 0.3s;

  .card {
    max-width:100%;
    margin-bottom: 4rem;;
    border-radius: 0.4rem;
    position: relative;
    transition: 0.3s;
    transform: scaleX(1);

    // &:hover {
    //   transform: scale(1.5);
    //   z-index: 9999;
    // }
  }

}
@media only screen and (max-width: 524px)
{
  .col-4 p {
    font-size: 13px;
  }
}
</style>