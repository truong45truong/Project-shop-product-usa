<template>
  <div id="shopping-cart">
    <div class="d-flex icon-cancel-list-heart justify-content-end">
      <font-awesome-icon @click="$emit('hideCart', false)" icon="fa-solid fa-xmark" class="m-3" />
    </div>
    <div class="header-shopping-cart">
      <h2 class="title-cart ms-5">Giỏ hàng</h2>
    </div>
    <div class="layout-order-cart">
      <cart-order v-for="order,index in listOrder" :name="order.order.name" :datetime="order.order.datetime"
        :receiver="order.order.receiver" :address_receive="order.order.address_receiver"
        :phone_receiver="order.order.phone_receiver" :status="order.order.status" :note="order.order.note"
        :logs="order.order.logs" :cancel="order.order.cancel" :total_price="order.order.total_price"
        :request_cancel="order.order.request_cancel" :transport="order.transport" :products="order.products" 
        :indexOrder="index"
         />
    </div>
    <div class="h-100">
     <order-selected-product />
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import CartOrder from '../../components/cart/CartOrder.vue'
import OrderSelectedProduct from '../../components/cart/OrderSelectedProduct.vue'
export default {
  name: "ShoppingCartLayout",
  async created() {
      this.listOrder = this.get_data;
      console.log(this.listOrder)
    
  },
  data: () => ({
    listOrder: [],
    isShowDetailTotalSelectProduct : false
  }),
  components: {
    CartOrder,
    OrderSelectedProduct,
  },
  computed: {
    ...mapGetters('cart', {
      get_is_data_cart: 'getIsHaveData',
      get_data : 'getData',
    }),
  },
  methods: {
    showDetailTotalSelectedProduct(){
      this.isShowDetailTotalSelectProduct = ! this.isShowDetailTotalSelectProduct
    }
  }
}
</script>

<style lang="scss">
#shopping-cart {
  position:fixed;
  width: 100%;
  height: 100%;
  background-image: linear-gradient(to bottom, rgb(255, 255, 255), rgb(197, 195, 195), rgb(148, 148, 148));
  top: 0;
  right: 0%;
  z-index: 999;
  animation-name: showListItemHeart;
  animation-duration: .75s;
  overflow-y: scroll;
  overflow-x:hidden;
}

$font: 'Poppins', sans-serif;

::selection {
  background-color: #C3CFE2;
}

.layout-order-cart {
  position: relative;
  height:65%;
}
.layout-order-cart::-webkit-scrollbar {
  display: none;
}
#shopping-cart::-webkit-scrollbar {
  display: none;
}
.title-cart {
  text-transform: uppercase;
  background: linear-gradient(to right, #30CFD0 0%, #330867 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;

  font: {
    size: 7vh;
    family: $font;
    weight: 800;
  }

  ;
}
</style>