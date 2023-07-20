
<template>
    <div v-if="isLogin" class="position-fixed over-bg-login h-100 w-100"></div>
    <menu-header @hideListItemHeart="activeShowListHeart" @hideCart="activeShowCart"
                @hideChangePassword = "activeChangePassword"  />
    <main >
      <div class="d-flex flex-column" :class="[get_is_activate == true ? 'top-action-on-web' : '']" >
        <notice-carefully v-if="get_is_activate" class="m-auto">
        </notice-carefully>
      </div>
              <!-- Error Page -->
          <div class="error">
            <div class="container-floud">
                <div class="col-xs-12 ground-color text-center">
                    <div class="container-error-404">
                        <div class="clip"><div class="shadow"><span class="digit thirdDigit"></span></div></div>
                        <div class="clip"><div class="shadow"><span class="digit secondDigit"></span></div></div>
                        <div class="clip"><div class="shadow"><span class="digit firstDigit"></span></div></div>
                        <div class="msg">OH!<span class="triangle"></span></div>
                    </div>
                    <!-- <img src="./../assets/images/not-found.png" alt="" class=""> -->
                    <h2 class="h1 mt-5">Sorry! Page not found</h2>
                </div>
            </div>
        </div>
        <!-- Error Page -->
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
  
  
  export default {
    name: "ErrorView",
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
      function randomNum()
        {
            "use strict";
            return Math.floor(Math.random() * 9)+1;
        }
            var loop1,loop2,loop3,time=30, i=0, number, selector3 = document.querySelector('.thirdDigit'), selector2 = document.querySelector('.secondDigit'),
                selector1 = document.querySelector('.firstDigit');
            loop3 = setInterval(function()
            {
              "use strict";
                if(i > 40)
                {
                    clearInterval(loop3);
                    selector3.textContent = 4;
                }else
                {
                    selector3.textContent = randomNum();
                    i++;
                }
            }, time);
            loop2 = setInterval(function()
            {
              "use strict";
                if(i > 80)
                {
                    clearInterval(loop2);
                    selector2.textContent = 0;
                }else
                {
                    selector2.textContent = randomNum();
                    i++;
                }
            }, time);
            loop1 = setInterval(function()
            {
              "use strict";
                if(i > 100)
                {
                    clearInterval(loop1);
                    selector1.textContent = 4;
                }else
                {
                    selector1.textContent = randomNum();
                    i++;
                }
            }, time);
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
      ChatBoxLayout
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
  .error .clip .shadow
    {
        height: 180px;  /*Contrall*/
    }
    .error .clip:nth-of-type(2) .shadow
    {
        width: 130px;   /*Contrall play with javascript*/ 
    }
    .error .clip:nth-of-type(1) .shadow, .error .clip:nth-of-type(3) .shadow
    {
        width: 250px; /*Contrall*/
    }
    .error .digit
    {
        width: 150px;   /*Contrall*/
        height: 150px;  /*Contrall*/
        line-height: 150px; /*Contrall*/
        font-size: 120px;
        font-weight: bold;
    }
    .error h2   /*Contrall*/
    {
        font-size: 32px;
    }
    .error .msg /*Contrall*/
    {
        top: -190px;
        left: 30%;
        width: 80px;
        height: 80px;
        line-height: 80px;
        font-size: 32px;
        z-index: -1;
    }
    .error span.triangle    /*Contrall*/
    {
        top: 70%;
        right: 0%;
        border-left: 20px solid #535353;
        border-top: 15px solid transparent;
        border-bottom: 15px solid transparent;
    }


    .error .container-error-404
    {
      margin-top: 10%;
        position: relative;
        height: 250px;
        padding-top: 40px;
    }
    .error .container-error-404 .clip
    {
        display: inline-block;
        transform: skew(-45deg);
    }
    .error .clip .shadow
    {
        
        overflow: hidden;
    }
    .error .clip:nth-of-type(2) .shadow
    {
        overflow: hidden;
        position: relative;
        box-shadow: inset 20px 0px 20px -15px rgba(150, 150, 150,0.8), 20px 0px 20px -15px rgba(150, 150, 150,0.8);
    }
    
    .error .clip:nth-of-type(3) .shadow:after, .error .clip:nth-of-type(1) .shadow:after
    {
        content: "";
        position: absolute;
        right: -8px;
        bottom: 0px;
        z-index: 9999;
        height: 100%;
        width: 10px;
        background: linear-gradient(90deg, transparent, rgba(173,173,173, 0.8), transparent);
        border-radius: 50%;
    }
    .error .clip:nth-of-type(3) .shadow:after
    {
        left: -8px;
    }
    .error .digit
    {
        position: relative;
        top: 8%;
        color: white;
        background: #023346;
        border-radius: 50%;
        display: inline-block;
        transform: skew(45deg);
    }
    .error .clip:nth-of-type(2) .digit
    {
        left: -10%;
    }
    .error .clip:nth-of-type(1) .digit
    {
        right: -20%;
    }.error .clip:nth-of-type(3) .digit
    {
        left: -20%;
    }    
    .error h2
    {
        color: #A2A2A2;
        font-weight: bold;
        padding-bottom: 20px;
    }
    .error .msg
    {
        position: relative;
        z-index: 9999;
        display: block;
        background: #535353;
        color: #A2A2A2;
        border-radius: 50%;
        font-style: italic;
        z-index: -99;
    }
    .error .triangle
    {
        position: absolute;
        z-index: 999;
        transform: rotate(45deg);
        content: "";
        width: 0; 
        height: 0; 
    }

/* Error Page */
@media(max-width: 767px)
{
    /* Error Page */
            .error .clip .shadow
            {
                height: 100px;  /*Contrall*/
            }
            .error .clip:nth-of-type(2) .shadow
            {
                width: 80px;   /*Contrall play with javascript*/ 
            }
            .error .clip:nth-of-type(1) .shadow, .error .clip:nth-of-type(3) .shadow
            {
                width: 100px; /*Contrall*/
            }
            .error .digit
            {
                width: 80px;   /*Contrall*/
                height: 80px;  /*Contrall*/
                line-height: 80px; /*Contrall*/
                font-size: 52px;
            }
            .error h2   /*Contrall*/
            {
                font-size: 24px;
            }
            .error .msg /*Contrall*/
            {
                top: -110px;
                left: 15%;
                width: 40px;
                height: 40px;
                line-height: 40px;
                font-size: 18px;
            }
            .error span.triangle    /*Contrall*/
            {
                top: 70%;
                right: -3%;
                border-left: 10px solid #535353;
                border-top: 8px solid transparent;
                border-bottom: 8px solid transparent;
            }
.error .container-error-404
  {
    height: 150px;
  }
        /* Error Page */
}

/*--------------------------------------------Framework --------------------------------*/

.overlay { position: relative; z-index: 20; } /*done*/
    .ground-color { background: white; }  /*done*/
    .item-bg-color { background: #EAEAEA } /*done*/
    
    /* Padding Section*/
        .padding-top { padding-top: 10px; } /*done*/
        .padding-bottom { padding-bottom: 10px; }   /*done*/
        .padding-vertical { padding-top: 10px; padding-bottom: 10px; }
        .padding-horizontal { padding-left: 10px; padding-right: 10px; }
        .padding-all { padding: 10px; }   /*done*/

        .no-padding-left { padding-left: 0px; }    /*done*/
        .no-padding-right { padding-right: 0px; }   /*done*/
        .no-vertical-padding { padding-top: 0px; padding-bottom: 0px; }
        .no-horizontal-padding { padding-left: 0px; padding-right: 0px; }
        .no-padding { padding: 0px; }   /*done*/
    /* Padding Section*/

    /* Margin section */
        .margin-top { margin-top: 10px; }   /*done*/
        .margin-bottom { margin-bottom: 10px; } /*done*/
        .margin-right { margin-right: 10px; } /*done*/
        .margin-left { margin-left: 10px; } /*done*/
        .margin-horizontal { margin-left: 10px; margin-right: 10px; } /*done*/
        .margin-vertical { margin-top: 10px; margin-bottom: 10px; } /*done*/
        .margin-all { margin: 10px; }   /*done*/
        .no-margin { margin: 0px; }   /*done*/

        .no-vertical-margin { margin-top: 0px; margin-bottom: 0px; }
        .no-horizontal-margin { margin-left: 0px; margin-right: 0px; }

        .inside-col-shrink { margin: 0px 20px; }    /*done - For the inside sections that has also Title section*/ 
    /* Margin section */

    hr
    { margin: 0px; padding: 0px; border-top: 1px dashed #999; }
  </style>