
<template>
  <main>
    <div class="d-flex flex-column" :class="[get_is_activate == true ? 'top-action-on-web' : '']">
      <notice-carefully v-if="get_is_activate" class="m-auto">
      </notice-carefully>
    </div>
    <menu-header />
    <banner-home />
    <list-product-item-flash-sale />
    <list-product-item />
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
import { mapGetters} from 'vuex'
export default {
  name: "HomeView",
  created() {

  },
  components: {
    MenuHeader,
    BannerHome,
    ListProductItemFlashSale,
    ListProductItem,
    FooterLayout,
    NoticeCarefully
  },
  computed: {
    ...mapGetters('notice', {
      get_is_activate: 'isActivate',
    }),
  },
  methods : {
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