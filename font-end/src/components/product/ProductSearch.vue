<template>
    <div class="d-flex flex-column align-items-center justify-content-between border  layout-product-search" @click="nextPageDetailProduct">
        <div class="row">
            <div class="col-sm-6">
                    <img class="img-product-item text-center" :src="'http://127.0.0.1:8000/' + `${photo}`" alt="name">
                </div>
            <div class="col-sm-6 d-flex flex-column align-items-center justify-content-center">
                <div class="text-center">
                    <p class="text-dark mx-2 mb-3">
                        <b>{{ name }}</b>
                    </p>
                </div>
                <div class="mx-2">
                    <p class="text-dark m-0">{{ price }} VNĐ</p>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script>
import { mapGetters } from 'vuex'
export default ({
    name: 'ProductSearch',
    props: {
        photo: false,
        price: false,
        sale: false,
        name: false,
        slug : false,
    },

    data: () => ({

    }),

    methods: {
        nextPageDetailProduct(){
            this.$router.push('/product/'+ this.slug)
        },
    },
    created() {
    }

})
</script>
<style>
.layout-product-search{
    height:120px;
    cursor:pointer;
}
</style>