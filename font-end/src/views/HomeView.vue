
<template>
  <div v-if="isLogin" class="position-fixed over-bg-login h-100 w-100"></div>
  <menu-header @hideListItemHeart="activeShowListHeart" @hideCart="activeShowCart"
              @hideChangePassword = "activeChangePassword"  />
  <main >
    <div class="d-flex flex-column" :class="[get_is_activate == true ? 'top-action-on-web' : '']" >
      <notice-carefully v-if="get_is_activate" class="m-auto">
      </notice-carefully>
    </div>
    <banner-home />
    <list-product-item-flash-sale ref="list_product_item_flash_sal" class=" mb-5" />
    <list-product-item ref="list_product_item mb-5" />
    <div class="container list-product-layout flash-sale-top mt-5 p-5">
      <div class="row p-5 bg-dark">
        <div class="d-flex align-items-center">
          <font-awesome-icon icon="fa-solid fa-bag-shopping" class="text-white icon-recommend" />
          <h5 class="text-white m-0 mx-3"> <b>Dành cho bạn </b></h5>
        </div>
      </div>
      <product-recommend />
    </div>
    <list-item-heart v-if="isShowListHeart" class="h-100" @hideListItemHeart="activeShowListHeart" @removeProductHeart="fromHomeViewChangeStatutsHeart"
    :isShowComponent="isShowListHeart"
    />
    <shopping-cart-layout v-if="isShowCart" class="h-100" @hideCart="activeShowCart" 
    :isShowComponent="isShowCart" />
    <notice-menu />
  </main>
  <footer-layout />
  <change-password @hide = "activeChangePassword" v-if="isShowChangePassword" />
  <chat-box-layout />
</template>

<script>

import MenuHeader from "../layout/main/MenuHeader.vue";
import BannerHome from "../layout/others/BannerHome.vue"
import ListProductItemFlashSale from "../layout/product/ListProductItemFlashSale.vue"
import FooterLayout from '../layout/main/FooterLayour.vue'
import ListProductItem from '../layout/product/ListProductItem.vue'
import NoticeCarefully from './../components/other/NoticeCarefully.vue'
import ListItemHeart from '../layout/product/ListItemHeart.vue'
import ShoppingCartLayout from '../layout/cart/ShoppingCartLayout.vue'
import ChangePassword from './../components/login/ChangePassword.vue'
import FilterAndSortLayout from './../layout/others/FilterAndSortLayout.vue'
import NoticeMenu from './../components/other/NoticeMenu.vue'
import ChatBoxLayout from './../layout/chatbox/ChatBoxLayout.vue'
import { mapGetters} from 'vuex'
import {useRoute} from 'vue-router'
import {DOMAIN} from './../common/constants'
import ProductRecommend from './../layout/product/ProductRecommend.vue'

export default {
  name: "HomeView",
  setup() {
        const route = useRoute();
        return { route };
  },
  async created() {
    if (this.get_authenticated) {
      await this.$store.dispatch('heart/actionGetData')
      if (this.get_is_data_cart == false) {
        await this.$store.dispatch('cart/actionGetData')
        if(this.$router.currentRoute._value.query.nextCart == 'true'){
            this.activeShowCart(true)
        } else 
        if(this.$router.currentRoute._value.query.nextHeart == 'true'){
          this.activeShowListHeart(true)
        }
      }
    }else {
      if(this.$router.currentRoute._value.query.nextCart == 'true'){
        console.log("this.$router",this.route.query)
        this.$router.push({ name : 'sign-in' , query : {
          nextPage : String(window.location.href).replace(DOAMIN,'')
        }})
      }
    }
  },
  data: () => ({
    isShowListHeart : null,
    isShowCart : null,
    isShowChangePassword : null ,
    }),
  components: {
    MenuHeader,
    BannerHome,
    ListProductItemFlashSale,
    ListProductItem,
    FooterLayout,
    NoticeCarefully,
    ListItemHeart,
    ShoppingCartLayout,
    ChangePassword,
    NoticeMenu,
    ChatBoxLayout,
    ProductRecommend
  },
  computed: {
    ...mapGetters('notice', {
      get_is_activate: 'isActivate',
      get_activate_menu : 'isActivateMenu'
    }),
    ...mapGetters('cart', {
      get_is_data_cart: 'getIsHaveData',
      get_data : 'getData',
    }),
    ...mapGetters('auth', {
			get_authenticated: 'isAuthenticated',
      isLogin : 'isShowLogin',

		}),
  },
  methods : {
    activeShowListHeart( status ){
      if (this.get_authenticated != true) {
        this.$store.dispatch('notice/actionTypeNotice', { content: 'Đăng nhập để vào yêu thích', type: 'addtocart' })
        this.$store.dispatch('notice/activateShowMenu')
      } else {
        if(status == false){
            let listQuery = {...this.$router.currentRoute._value.query}
            console.log('listQuery',listQuery)
            delete listQuery.nextHeart
            this.$router.push({ query: {...listQuery} });
          }
          this.isShowListHeart = status;
      }
    },
    fromHomeViewChangeStatutsHeart(product_slug){
      const listProductItem = this.$refs.list_product_item;
      listProductItem.changeStatusHeartProduct(product_slug);
    },
    activeShowCart( status ){
      if(this.get_authenticated != true){
        this.$store.dispatch('notice/actionTypeNotice',{content : 'Đăng nhập để vào giỏ hàng',type : 'addtocart'})
        this.$store.dispatch('notice/activateShowMenu')
      } else {
        if(status == false){
            let listQuery = {...this.$router.currentRoute._value.query}
            console.log('listQuery',listQuery)
            delete listQuery.nextCart
            this.$router.push({ query: {...listQuery} });
          }
        this.isShowCart = status;
      }
    },
    activeChangePassword( status ){
      this.isShowChangePassword = status;
    },
    handleScroll(event) {
      // add your scroll event handling code here
    }
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
.over-bg-login  {
  background-color: rgba(0, 0, 0,0.4);
  z-index: 999;
}
.icon-recommend {
  font-size: 24px;
}
</style>