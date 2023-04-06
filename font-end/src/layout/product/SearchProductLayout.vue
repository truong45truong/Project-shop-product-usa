<template>
    <div class="layout-list-product-search bg-white mt-2 w-100 border border-1">
        <div v-if="data != false" class="container w-100">
            <div  class="row">
                <div class="col-sm-6 text-center">
                    <h5 class="text-dark my-3"><i><b>Danh mục</b></i></h5>
                    <div v-if="data != false" v-for=" item in categories" class="mt-2 d-flex">
                        <router-link class="text-dark text-start w-100 search-category" :to="{ name: 'products-search', params: { key_search: key_search } , query : { category : item.slug } }">{{item.name}}</router-link>
                        <p class="text-end">{{item.number_product}}</p>
                    </div>
                    <div v-if="categories.length == 0" class="mt-2">
                        <h5 class="text-danger">Không có danh mục cần tìm</h5>
                    </div>
                </div>
                <div class="col-sm-6 text-center">
                    <h5 class="text-dark my-3" ><b><i>Sản phẩm tìm kiếm : {{key_search}}</i></b></h5>
                    <div v-if="data != false" v-for=" item in data" class="mt-2">
                        <ProductSearch :slug="item.slug"  :photo="item.data" 
                            :name="item.name" :price="item.price" :sale="item.sale"
                        />  
                    </div>
                </div>
            </div>
            <button class="btn-click-all">
                <router-link class="text-dark text-start w-100" :to="{ name: 'products-search', params: { key_search: key_search } , query : { category : 'All'} }">
                    <h5 class="search-category"><b><i class="search-category">Xem tất cả kết quả</i></b></h5>
                </router-link>
            </button>
        </div>
        <b v-if="data == false" class="text-center">
            <i>
                <p class="my-3 text-danger">Không tìm thấy kết quả nào</p>
            </i>
        </b>
    </div>
</template>

<script>
import { ProductAction,ProductApiService } from './../../common/product.service'
import ProductSearch from './../../components/product/ProductSearch.vue'
export default {
    name: 'SearchProductLayout',
    props : {
        key_search :  {
            type: String,
            required: true,
        },
    },
    components: {
        ProductSearch
    },
    data: () => ({
        data : false,
        categories : false, 
    }),
    methods: {
        
    },
    watch: {
         key_search: async function(newValue) {
            if(newValue != ""){
                await ProductApiService.searchProduct({
                    params : {
                        key_search : newValue,
                        limit_search : 4
                    }
                }).then(response => {
                    if(response.data.products.length == 0){
                        this.data = false
                        this.categories = false
                    }else{
                        this.data = response.data.products
                        this.categories = response.data.number_product_in_category
                        console.log('this.categories ',this.categories )
                    }
                })
            }
        },
    },
    async created() {
        if(this.key_search != false){
            await ProductApiService.searchProduct({
                params : {
                    key_search : this.key_search,
                    limit_search : 4
                }
            }).then(response => {
                if(response.data.products.length == 0){
                        this.data = false
                        this.categories = false
                    }else{
                        this.data = response.data.products
                        this.categories = response.data.number_product_in_category
                }
            })
        }
    },
    mounted() {
    },
}

</script>
<style>
.layout-list-product-search{
    position:absolute;
    max-width: 700px;
    right:0%;
}
.btn-click-all {
    background-color: white;
    border : none;
    text-decoration: underline;
}
.btn-click-all :hover {
    color:rgb(70, 69, 69)
}
.btn-see-more {
    background-color: white;
    border : 1.5px solid black;
    max-width: 200px;
}
.page-list-product .carousel__slide{
    width:100px !important;
}
.active-page {
    background-color:black;
    border: 3.5px solid rgb(177, 177, 177);
    color:white;
}
.search-category:hover {
    text-decoration: none !important;
}
</style>