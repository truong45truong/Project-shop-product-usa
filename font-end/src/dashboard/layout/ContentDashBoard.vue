
<template>
    <div class="row bg-info mx-2 p-2">
        <div class="col-lg-3">
            <div class="single_analite_content text-white">
                <h4>Thu nhập / năm</h4>
               <p class="">
                số sản phẩm bán ra :  <span class=""> 2000 </span>
               </p>
               <p class=""> Thu nhập </p>
            </div>
        </div>
        <div class="col-lg-3">
            <div class="single_analite_content text-white">
                <h4>thu nhập / tháng</h4>
                <p class="">
                số sản phẩm bán ra :  <span class=""> 2000 </span>
               </p>
               <p class="Thu nhập"> Thu nhập </p>
            </div>
        </div>
        <div class="col-lg-3">
            <div class="single_analite_content text-white">
                <h4>thu nhập / tuần</h4>
                <p class="">
                số sản phẩm bán ra :  <span class=""> 2000 </span>
               </p>
               <p class="Thu nhập"> Thu nhập </p>
            </div>
        </div>
        <div class="col-lg-3">
            <div class="single_analite_content text-white">
                <h4>thu nhập / ngày</h4>
                <p class="">
                số sản phẩm bán ra :  <span class=""> 2000 </span>
               </p>
               <p class="Thu nhập"> Thu nhập </p>
            </div>
        </div>
    </div>
</template>
  
<script>
import { mapGetters } from 'vuex'
import { useRoute } from 'vue-router'


export default {
    name: "ContentDashBoard",
    setup() {
        const route = useRoute();
        return { route };
    },

    data: () => ({

    }),
    components: {
    },
    computed: {
        ...mapGetters('dashboard', {
            get_is_show_layout: 'getIsShowLayout',
        }),
    },
    methods: {

    },
    created() {
    }
}
</script>
<style lang="scss" scoped>
#accordion .panel {
    margin-bottom: 20px;
}

#accordion .panel-heading {
    background-color: #3bb7c1;
    color: #fff;
    text-transform: uppercase;
}
</style>