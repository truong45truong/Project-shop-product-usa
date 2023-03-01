
<template>
  <main>
    <div class="d-flex flex-column" :class="[get_is_activate == true ? 'top-action-on-web' : '']">
      <notice-carefully v-if="get_is_activate" class="m-auto">
      </notice-carefully>
    </div>
    <menu-header @hideListItemHeart="activeShowListHeart" @hideCart="activeShowCart"/>
    <banner-home />
    <list-product-item-flash-sale ref="list_product_item_flash_sale" />
    <list-product-item ref="list_product_item" />
    <list-item-heart v-if="isShowListHeart" class="h-100" @hideListItemHeart="activeShowListHeart" @removeProductHeart="fromHomeViewChangeStatutsHeart"
    :isShowComponent="isShowListHeart"
    />
    <shopping-cart-layout v-if="isShowCart" class="h-100" @hideCart="activeShowCart" 
    :isShowComponent="isShowCart" />
    <footer-layout />
  </main>
</template>

<script>

import MenuHeader from "../layout/MenuHeader.vue";
import BannerHome from "./../layout/BannerHome.vue"
import ListProductItemFlashSale from "../layout/ListProductItemFlashSale.vue"
import FooterLayout from './../layout/FooterLayour.vue'
import ListProductItem from './../layout/ListProductItem.vue'
import NoticeCarefully from './../components/other/NoticeCarefully.vue'
import ListItemHeart from './../layout/ListItemHeart.vue'
import ShoppingCartLayout from './../layout/ShoppingCartLayout.vue'
import { mapGetters} from 'vuex'
export default {
  name: "HomeView",
  async created() {
    if(this.get_authenticated){
      await this.$store.dispatch('heart/actionGetData')
    if (this.get_is_data_cart == false) {
      await this.$store.dispatch('cart/actionGetData')
    }
    }
  },
  data: () => ({
    isShowListHeart : null,
    isShowCart : null,
    }),
  components: {
    MenuHeader,
    BannerHome,
    ListProductItemFlashSale,
    ListProductItem,
    FooterLayout,
    NoticeCarefully,
    ListItemHeart,
    ShoppingCartLayout
  },
  computed: {
    ...mapGetters('notice', {
      get_is_activate: 'isActivate',
    }),
    ...mapGetters('cart', {
      get_is_data_cart: 'getIsHaveData',
      get_data : 'getData',
    }),
    ...mapGetters('auth', {
			get_authenticated: 'isAuthenticated',
		}),
  },
  methods : {
    activeShowListHeart( status ){
      this.isShowListHeart = status;
    },
    fromHomeViewChangeStatutsHeart(product_slug){
      const listProductItem = this.$refs.list_product_item;
      listProductItem.changeStatusHeartProduct(product_slug);
    },
    activeShowCart( status ){
      this.isShowCart = status;
    },

  }
}
</script>
<style>
.top-action-on-web {
  align-items: center;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 99999;
}

</style>