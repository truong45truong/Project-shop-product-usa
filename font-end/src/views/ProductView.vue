
<template>
    <main>
      <div v-if="isLogin" class="position-fixed over-bg-login h-100 w-100"></div>

      <div class="d-flex flex-column" :class="[get_is_activate == true ? 'top-action-on-web' : '']">
        <notice-carefully v-if="get_is_activate" class="m-auto">
        </notice-carefully>
      </div>
      <menu-header ref="menuHeader" @hideListItemHeart="activeShowListHeart" @hideCart="activeShowCart" 
      @hideChangePassword = "activeChangePassword" />
      <list-product-category />
      <list-item-heart v-if="isShowListHeart" class="h-100" @hideListItemHeart="activeShowListHeart"
        @removeProductHeart="fromHomeViewChangeStatutsHeart" :isShowComponent="isShowListHeart" />
      <shopping-cart-layout v-if="isShowCart" class="h-100" @hideCart="activeShowCart" :isShowComponent="isShowCart" />
      <notice-menu />
      <footer-layout />
      <change-password @hide = "activeChangePassword" v-if="isShowChangePassword" />
    </main>
  </template>
    
  <script>
  import MenuHeader from "../layout/main/MenuHeader.vue";
  import FooterLayout from '../layout/main/FooterLayour.vue';
  import NoticeCarefully from './../components/other/NoticeCarefully.vue';
  import ListItemHeart from '../layout/product/ListItemHeart.vue';
  import ShoppingCartLayout from '../layout/cart/ShoppingCartLayout.vue';
  import ListProductCategory from './../layout/product/ListProductCategory.vue';
  import ChangePassword from './../components/login/ChangePassword.vue'
  import NoticeMenu from './../components/other/NoticeMenu.vue'
  import {DOMAIN} from './../common/constants'
  import { mapGetters } from 'vuex';
  export default {
    name: "ProductView",
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
        this.$router.push({ name : 'sign-in' , query : {
          nextPage : String(window.location.href).replace(DOMAIN,'')
        }})
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
      isShowChangePassword : null ,
    }),
    components: {
      MenuHeader,
      FooterLayout,
      NoticeCarefully,
      ListItemHeart,
      ShoppingCartLayout,
      ListProductCategory,
      ChangePassword,
      NoticeMenu
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
          isLogin : 'isShowLogin',

      }),
    },
    methods: {
      activeShowListHeart(status) {
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
      fromHomeViewChangeStatutsHeart(product_slug) {
        const listProductItem = this.$refs.list_product_item;
        listProductItem.changeStatusHeartProduct(product_slug);
      },
      activeShowCart(status) {
        if (this.get_authenticated != true) {
          this.$store.dispatch('notice/actionTypeNotice', { content: 'Đăng nhập để vào giỏ hàng', type: 'addtocart' })
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
      showLogin(){
        this.$refs.menuHeader.isShowLogin = true
      },
      activeChangePassword( status ){
        this.isShowChangePassword = status;
      },
    }
  }
  </script>
  <style>
  .over-bg-login  {
  background-color: rgba(0, 0, 0,0.4);
  z-index: 999;
}

  </style>