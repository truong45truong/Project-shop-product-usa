<template>
    <div class="d-flex flex-column align-items-center justify-content-between border  layout-product-search" @click="nextPageDetailProduct">
        <div class="row">
            <div class="col-6">
                    <img class="img-product-item text-center" :src="URL_PATH_SERVER + '/' + `${photo}`" alt="name">
                </div>
            <div class="col-6 d-flex flex-column align-items-center justify-content-center">
                <div class="text-center">
                    <p class="text-dark text-name mx-2 mb-3">
                        <b>{{ name }}</b>
                    </p>
                </div>
                <div class="mx-2">
                    <p class="text-dark text-name m-0">{{ price }} VNĐ</p>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script>
import { URL_PATH_SERVER } from '../../common/constants';
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
        URL_PATH_SERVER : URL_PATH_SERVER ,
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
.layout-product-search .text-name {
    font-size: 13px;
}
@media only screen and (max-width: 575px) {
    .layout-product-search .img-product-item {
        max-width: 100px;
    }
}
</style>