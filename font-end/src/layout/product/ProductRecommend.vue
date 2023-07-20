<template>
    <div class="bottom-list">
        <div class="container"  v-if="data.length == 0">
            <div class="d-flex flex-column align-items-center">
                <img src="./../../assets/images/noproductfound.png" class="img-no-product my-2" alt="">
            </div>
            <h3 class="text-dark text-center">
                Hiện tại không có sản phẩm nào 
            </h3>
        </div>
        <div v-if="data != false" class="container">
            <div v-if="paginate != false && data" class="row">
                <div v-for="item,index in data" class="col-lg-3 col-sm-4 col-6  mt-4">
                    <ProductCategory v-if="index >= (indexPage-1)*numberProductInPage && index < (indexPage)*numberProductInPage " 
                        :photo="item.data" :price="item.price" :sale="item.sale" 
                        :name="item.name"
                        :slug="item.slug" />
                </div>
            </div>

            <div v-if="paginate == false" class="row">
                <div v-for="item in data" class="col-lg-3 col-sm-4 col-6  mt-4">
                    <ProductCategory :photo="item.data" :price="item.price" :sale="item.sale" :name="item.name"
                        :slug="item.slug" />
                </div>
            </div>

            <div v-if="paginate > 14" class="page-list-product mt-4">
                <Carousel :settings="settings" :breakpoints="breakpoints">
                    <Slide v-for="slide in arrPaginate" :key="slide">
                        <div class="carousel__item">
                            <button class="btn-see-more px-3 py-2 text-center" >
                                {{slide}}
                            </button>
                        </div>
                    </Slide>         
                    <template #addons>
                        <Navigation />
                    </template>
                </Carousel>
            </div>
            <div v-if="paginate <= 14 && paginate != false" class="d-flex justify-content-center mt-4">
                <button v-for="index in arrPaginate" class="btn-see-more px-3 py-2 text-center mx-2" 
                :class="[ index == indexPage ? 'active-page' :'' ]" @click="changePage(index)"
                >
                    {{index}}
                </button>
            </div>
        </div>

    </div>
</template>

<script>
import { useRoute } from 'vue-router';
import FilterAndSortLayout from './../others/FilterAndSortLayout.vue'
import { ProductAction } from './../../common/product.service'
import ProductCategory from './../../components/product/ProductCategory.vue'
import {CategoryApiService} from './../../common/category.service'
import {ActionHistory} from './../../common/historyAction.service'
import { Carousel, Navigation, Slide, Pagination } from 'vue3-carousel'
export default {
    name: 'ProductRecommend',
    components: {
        FilterAndSortLayout,
        ProductCategory,
        Pagination,
        Carousel,
        Slide,
        Navigation,
    },
    watch:{
        $route (to, from){
            let listQuery = {...this.$router.currentRoute._value.query}
            if(listQuery.Page != null){
                this.indexPage = listQuery.Page
            }else {
                this.getData()
            }
        }
    } ,
    setup() {
        const route = useRoute();
        return { route };
    },
    data: () => ({
        listCategory : [],
        category : '',
        filterAndSort: false,
        data: false,
        dFixedButtonFilterAndSort : 0,
        paginate : false,
        indexPage: 1,
        numberProductInPage : 12,
        arrPaginate : [],
        arrValue : [],
        // carousel settings
        settings: {
            itemsToShow: 12,
            snapAlign: 'center',
        },
        // breakpoints are mobile first
        // any settings not specified will fallback to the carousel settings
        breakpoints: {
            400: {
            itemsToShow: 4,
            snapAlign: 'center',
            },
            // 700px and up
            700: {
            itemsToShow: 4,
            snapAlign: 'center',
            },
            // 1024 and up
            1024: {
            itemsToShow: 6,
            snapAlign: 'center',
            },
        },
    }),
    methods: {
        changePage(index){
            let listQuery = {...this.$router.currentRoute._value.query}
            this.$router.push({ query: {...listQuery,...{Page : index}} });
            this.indexPage = index
        },
        async getData(){
            await ActionHistory.getProductRecommend().then(res => {
                this.data = res.products 
                if( this.data.length > this.numberProductInPage){
                        this.paginate = false

                        let naturalPart = Math.floor(this.data.length / this.numberProductInPage)
                        let remainder = this.data.length - naturalPart*this.numberProductInPage

                        if( remainder > 0 ){
                            this.paginate = naturalPart + 1
                        }else {
                            this.paginate = naturalPart
                        }
                        
                        const arrPaginate = [];

                        for (let i = 1; i <= this.paginate; i++) {
                            arrPaginate.push(i);
                        }
                        this.arrPaginate = arrPaginate
                    }else {
                        this.paginate = false
                    }
            })
        }
    },

    async created() {
        await ActionHistory.getProductRecommend().then(res => {
                this.data = res.products 
                if( this.data.length > this.numberProductInPage){
                        this.paginate = false

                        let naturalPart = Math.floor(this.data.length / this.numberProductInPage)
                        let remainder = this.data.length - naturalPart*this.numberProductInPage

                        if( remainder > 0 ){
                            this.paginate = naturalPart + 1
                        }else {
                            this.paginate = naturalPart
                        }
                        
                        const arrPaginate = [];

                        for (let i = 1; i <= this.paginate; i++) {
                            arrPaginate.push(i);
                        }
                        this.arrPaginate = arrPaginate
                    }else {
                        this.paginate = false
                    }
            })
    },
    mounted() {
    },
}

</script>
<style>
.title-category {
    text-decoration: none;
}
.img-no-product {
    max-width:500px !important;
}
.btn-filter {
    background-color: white;
}

.row {
    display: flex;
}

.col {
    flex-grow: 1;
}
#top-list-filter-sort {
    width:100%;
    top : 0%;
    background-color: white;
    z-index: 9;
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
</style>