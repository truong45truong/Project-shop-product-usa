
<template>
  <main>
    <div class="d-flex flex-column" :class="[get_is_activate == true ? 'top-action-on-web' : '']">
      <notice-carefully v-if="get_is_activate" class="m-auto">
      </notice-carefully>
    </div>
    <menu-header ref="menuHeader" @hideListItemHeart="activeShowListHeart" @hideCart="activeShowCart" />
    <detail-product @login=showLogin />
    <list-item-heart v-if="isShowListHeart" class="h-100" @hideListItemHeart="activeShowListHeart"
      @removeProductHeart="fromHomeViewChangeStatutsHeart" :isShowComponent="isShowListHeart" />
    <shopping-cart-layout v-if="isShowCart" class="h-100" @hideCart="activeShowCart" :isShowComponent="isShowCart" />
    <footer-layout />
  </main>
</template>
  
<script>
import MenuHeader from "../layout/main/MenuHeader.vue";
import FooterLayout from '../layout/main/FooterLayour.vue'
import NoticeCarefully from './../components/other/NoticeCarefully.vue'
import ListItemHeart from '../layout/product/ListItemHeart.vue'
import ShoppingCartLayout from '../layout/cart/ShoppingCartLayout.vue'
import DetailProduct from './../components/product/ProductDetail.vue'
import { mapGetters } from 'vuex'
export default {
  name: "DetailProductView",
  async created() {
    if (this.get_authenticated) {
      await this.$store.dispatch('heart/actionGetData')
      if (this.get_is_data_cart == false) {
        await this.$store.dispatch('cart/actionGetData')
      }
    }
  },
  mounted(){
    console.log(this.$refs.menuHeader.isShowLogin)
  },
  data: () => ({
    isShowListHeart: null,
    isShowCart: null,
    isShowLogin : false,
  }),
  components: {
    MenuHeader,
    FooterLayout,
    NoticeCarefully,
    DetailProduct,
    ListItemHeart,
    ShoppingCartLayout,
  },
  computed: {
    ...mapGetters('notice', {
      get_is_activate: 'isActivate',
    }),
    ...mapGetters('cart', {
      get_is_data_cart: 'getIsHaveData',
      get_data: 'getData',
    }),
    ...mapGetters('auth', {
			get_authenticated: 'isAuthenticated',
		}),
  },
  methods: {
    activeShowListHeart(status) {
      this.isShowListHeart = status;
    },
    fromHomeViewChangeStatutsHeart(product_slug) {
      const listProductItem = this.$refs.list_product_item;
      listProductItem.changeStatusHeartProduct(product_slug);
    },
    activeShowCart(status) {
      if (this.get_authenticated != true) {
        this.$store.dispatch('notice/actionTypeNotice', { content: 'Đăng nhập để vào giỏ hàng', type: 'addtocart' })
        this.$store.dispatch('notice/activateShowMenu')
      } else {
        this.isShowCart = status;
      }
    },
    showLogin(){
      this.$refs.menuHeader.isShowLogin = true
    }
  }
}
</script>
<style>
</style>