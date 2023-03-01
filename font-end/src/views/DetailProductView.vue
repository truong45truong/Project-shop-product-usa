
<template>
    <main>
      <div class="d-flex flex-column" :class="[get_is_activate == true ? 'top-action-on-web' : '']">
        <notice-carefully v-if="get_is_activate" class="m-auto">
        </notice-carefully>
      </div>
      <menu-header @hideListItemHeart="activeShowListHeart" />
      <detail-product />
      <footer-layout />
    </main>
  </template>
  
  <script>
  
  import MenuHeader from "../layout/MenuHeader.vue";
  import FooterLayout from './../layout/FooterLayour.vue'
  import NoticeCarefully from './../components/other/NoticeCarefully.vue'
  import DetailProduct from './../components/product/ProductDetail.vue'
  import { mapGetters} from 'vuex'
  export default {
    name: "DetailProductView",
    created() {
  
    },
    data: () => ({
      }),
    components: {
      MenuHeader,
      FooterLayout,
      NoticeCarefully,
      DetailProduct,
    },
    computed: {
      ...mapGetters('notice', {
        get_is_activate: 'isActivate',
      }),
    },
    methods : {
      activeShowListHeart( status ){
        this.isShowListHeart = status;
      },
      fromHomeViewChangeStatutsHeart(product_slug){
        const listProductItem = this.$refs.list_product_item;
        listProductItem.changeStatusHeartProduct(product_slug);
      }
    }
  }
  </script>
  <style>

  
  </style>