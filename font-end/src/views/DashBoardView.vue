
<template>
  <div v-if="!get_authenticated" class="position-fixed h-100 w-100">
    <LoginDashBoard @login="login" />
  </div>
  <div v-if="get_authenticated" id="viewport">
    <!-- Sidebar -->
    <MenuDashBoard />
    <!-- Content -->
    <div id="content" class="p-5">
      <ContentDashBoard v-if="get_is_show_layout.isShowDashboard" />
      <ContentUser v-if="get_is_show_layout.isShowUser" />
      <ContentProduct v-if="get_is_show_layout.isShowProduct" />
      <DetailProductAdmin v-if="get_is_show_detail_product" />
      <ContentVoucher v-if="get_show_voucher.show" />
      <ContentDetailVoucher v-if="get_show_voucher.isShowDetail"  />
      <ContentFlashSale v-if="get_show_flash_sale.show" />
      <DetailFlashSale v-if="get_show_flash_sale.isShowDetail" />
      <ContentOrder v-if="get_is_show_layout.isShowOrder" />
    </div>
  </div>
</template>
  
<script>
import { mapGetters } from 'vuex'
import { useRoute } from 'vue-router'
import MenuDashBoard from './../dashboard/layout/Menu.vue'
import ContentDashBoard from './../dashboard/layout/ContentDashBoard.vue'
import LoginDashBoard from './../dashboard/component/LoginDashBoard.vue'
import ContentUser from './../dashboard/layout/ContentUser.vue'
import ContentProduct from './../dashboard/layout/ContentProduct.vue'
import DetailProductAdmin from './../dashboard/layout/DetailProductAdmin.vue'
import ContentVoucher from './../dashboard/layout/ContentVoucher.vue'
import ContentDetailVoucher from './../dashboard/layout/ContentDetailVoucher.vue'
import ContentFlashSale from './../dashboard/layout/ContentFlashSale.vue'
import DetailFlashSale from './../dashboard/layout/DetailFlashSale.vue'
import ContentOrder from './../dashboard/layout/ContentOrder.vue'
export default {
  name: "DashBoardView",
  setup() {
    const route = useRoute();
    return { route };
  },
  async created() {
  },
  data: () => ({
  }),
  components: {
    MenuDashBoard,
    ContentDashBoard,
    LoginDashBoard,
    ContentUser,
    ContentProduct,
    DetailProductAdmin,
    ContentVoucher,
    ContentDetailVoucher,
    ContentFlashSale,
    DetailFlashSale,
    ContentOrder
  },
  computed: {
    ...mapGetters('notice', {
      get_is_activate: 'isActivate',
      get_activate_menu: 'isActivateMenu'
    }),
    ...mapGetters('dashboard', {
      get_is_show_layout: 'getIsShowLayout',
      get_is_show_detail_product : 'getIsShowDetailProduct' ,
      get_show_voucher : 'getShowVoucher' ,
      get_show_flash_sale : 'getShowFlashSale'
    }),
    ...mapGetters('auth', {
      get_authenticated: 'isAuthenticated',
      isLogin: 'isShowLogin',

    }),
  },
  methods: {
    async login(username, password) {
      return await this.$store.dispatch('auth/login', { username: username, password: password }).then((res) => {
        if (this.get_authenticated == true) {
          this.isAuthenticated = true;
          this.isShowLogin = false;
        }
      }).catch(error => {
        console.error("error", error);
      })
    },
  }
}
</script>
<style lang="scss">
#viewport {
  padding-left: 250px;
  -webkit-transition: all 0.5s ease;
  -moz-transition: all 0.5s ease;
  -o-transition: all 0.5s ease;
  transition: all 0.5s ease;
}

#content {
  width: 100%;
  position: relative;
  margin-right: 0;
}

/* Sidebar Styles */

#sidebar {
  z-index: 1000;
  position: fixed;
  left: 250px;
  width: 250px;
  height: 100%;
  margin-left: -250px;
  overflow-y: auto;
  background: #167F92; 
  -webkit-transition: all 0.5s ease;
  -moz-transition: all 0.5s ease;
  -o-transition: all 0.5s ease;
  transition: all 0.5s ease;
}

#sidebar header {
  background: #002329;
  font-size: 20px;
  line-height: 52px;
  text-align: center;
}

#sidebar header a {
  color: #fff;
  display: block;
  text-decoration: none;
}

#sidebar header a:hover {
  color: #fff;
}


#sidebar .nav a {
  background: none;
  border-bottom: 1px solid #132f31;
  color: #CFD8DC;
  font-size: 14px;
  padding: 16px 24px;
}

#sidebar .nav a:hover {
  background: none;
  color: #ECEFF1;
}

#sidebar .nav a i {
  margin-right: 16px;
}

.search-dashboard {
  position: absolute;
  bottom: 70%;
}
</style>