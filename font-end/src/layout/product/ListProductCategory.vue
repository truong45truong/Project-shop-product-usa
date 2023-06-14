<template>
    <div class="title-list">
        <div class="container">
            <div class="row">
                <p href="" class="fs-1 text-dark title-category"><i>{{category.name}}</i></p>
                <div class="">
                    <p class="text-dark"><i>Các sản phẩm chúng tôi đều có nguồn cung cấp uy tín và chất lượng</i></p>
                    <p class="text-dark">
                        <i>Giấy phép kinh doanh</i>
                        <a class="ms-2" href=""> <i>Tại đây</i></a>
                    </p>
                </div>
            </div>
        </div>
    </div>
    <div class="top-list" id="top-list-filter-sort">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-sm-6 d-flex">
                    <a v-for="item in listCategory" class="mb-2 me-2 title-category" href=""><i>{{item.name}}</i></a>
                </div>
                <div class="col-sm-6 d-flex justify-content-end" id="filter-and-sort">
                    <button class="border border-dark d-flex p-3 btn-filter mt-2" @click="showFilterAndSort"
                        >
                        <p class="text-dark m-0 me-2">Lọc & Xắp xếp</p>
                        <font-awesome-icon icon="fa-solid fa-filter" />
                    </button>
                </div>
            </div>
            <hr>
        </div>
    </div>
    <FilterAndSortLayout v-if="filterAndSort != false" :type=1 @hideFilterAndSort="showFilterAndSort"
     :listCategory="listCategory" :category_applied="route.params.category" :hideProducts=false  />
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

import { Carousel, Navigation, Slide, Pagination } from 'vue3-carousel'
const Sort = new Map();
Sort.set('Tên : A -> Z', "S-1")
Sort.set('Tên : Z -> A','S-2')
Sort.set('Giá : Thấp -> Cao' , 'S-3')
Sort.set('Giá : Cao -> Thấp' , 'S-4')
Sort.set('Đánh giá : Thấp -> Cao' , 'S-5')
Sort.set('Đánh giá : Cao -> Thấp' , 'S-6')
Sort.set('Lượt mua : Thấp -> Cao' , 'S-7')
Sort.set('Lượt mua : Cao -> Thấp' , 'S-8')
const Limits = new Map();
Limits.set('Đánh giá: hơn 3' ,'L-1')
Limits.set('Đánh giá: hơn 4' ,'L-2')
Limits.set('Đánh giá: hơn 5' , 'L-3')
export default {
    name: 'ListProductCategory',
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
        showFilterAndSort() {
            this.filterAndSort = !this.filterAndSort
        },
        handleScroll(event) {
            
            const element = document.getElementById('top-list-filter-sort');
            const scrollPosition = window.scrollY;
            if (scrollPosition >= this.dFixedButtonFilterAndSort) {
                element.classList.add('position-fixed');
                element.classList.add('shadow');
            }else {
                element.classList.remove('position-fixed');
                element.classList.remove('shadow');
            }
        },
        changePage(index){
            let listQuery = {...this.$router.currentRoute._value.query}
            this.$router.push({ query: {...listQuery,...{Page : index}} });
            this.indexPage = index
        },
        async getData(){
            const filter_sort = sessionStorage.getItem('filter_sort');
            let applied = JSON.parse(filter_sort);
            console.log("get data",applied)
            let arrayLimits= new Array()
            let arraySort = new Array()
            let arraySlugCategory = new Array()
            let filter = {
                sorts : false,
                limits : false,
                categories: false
            }
            if(applied.applied.sorts != false){
                console.log(applied.applied.sorts,typeof applied.applied.sorts)
                if(typeof applied.applied.sorts !== 'string' ){
                    for (let item of applied.applied.sorts){
                        let e = Sort.get(item)
                        if(e)
                        arraySort.push(e)
                    }
                    filter.sorts = arraySort
                }else {
                    let e = Sort.get(applied.applied.sorts)
                    if(e)
                    arraySort.push(e)
                    filter.sorts = arraySort
                }
                
            }
            if(applied.applied.limits != false){
                for (let item of applied.applied.limits){
                    let e = Limits.get(item)
                    if(e)
                    arrayLimits.push(e)
                }
                filter.limits = arrayLimits
            }
            if(applied.applied.products != false && applied.applied.products != 'false'){
                for (let item of applied.applied.products){
                    arraySlugCategory.push(item)
                }
                filter.categories = arraySlugCategory
            }
            await ProductAction.actionGetProductCategory({
                params: {
                    category_slug:  this.route.params.category,
                    'filter_sort' :  JSON.stringify(filter.sorts),
                    'filter_limit' :  JSON.stringify(filter.limits),
                    'slug_categories' : JSON.stringify(filter.categories),
                    'up' :applied.applied.up == null ? false : applied.applied.up,
                    'down' :applied.applied.down == null ? false : applied.applied.down,
                }
            }).then(res => {
                if (res.status == 200) {
                    let listQuery = {...this.$router.currentRoute._value.query}

                    if(listQuery.Page != null){
                        console.log('listQuery.Page',listQuery.Page)
                        this.indexPage = listQuery.Page
                    }
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
                }
            })
        }
    },

    async created() {
        for (let i = 1; i <= this.numberProductInPage; i++) {
            this.arrValue.push(i);
        }
        this.category = this.route.params.category
        await CategoryApiService.getCategoryTree({
            params : {
                category_slug :  this.route.params.category
            }
        }).then(response => {
            this.category = response.data.category_main
            this.listCategory = response.data.categories
        })
        console.log("params route" , this.$router.currentRoute._value.query)
        if(this.$router.currentRoute._value.query != null){
            let limits = []
            let products = []
            let sorts = []

            if(typeof this.$router.currentRoute._value.query.limits == 'string'){
                limits.push(this.$router.currentRoute._value.query.limits)
            }
            else {
                if(this.$router.currentRoute._value.query.limits != 'false'
                    || this.$router.currentRoute._value.query.limits != false
                )
                limits = this.$router.currentRoute._value.query.limits
                else 
                limits = false
            }

            if(typeof this.$router.currentRoute._value.query.sorts == 'string'){
                sorts.push(this.$router.currentRoute._value.query.sorts)
            }
            else {
                if(this.$router.currentRoute._value.query.sorts != 'false'
                    || this.$router.currentRoute._value.query.sorts != false
                )
                sorts = this.$router.currentRoute._value.query.sorts
                else 
                sorts = false
            }

            if(typeof this.$router.currentRoute._value.query.products == 'string'){
                products.push(this.$router.currentRoute._value.query.products)
            }
            else {
                if(this.$router.currentRoute._value.query.products != 'false'
                    || this.$router.currentRoute._value.query.products != false
                )
                products = this.$router.currentRoute._value.query.products
                else 
                products = false
            }

            let ValueFilterAndSort = {
                applied : {
                    products : products,
                    sorts : sorts,
                    limits : limits,
                    category : this.$router.currentRoute._value.query.category,
                    up : this.$router.currentRoute._value.query.up,
                    down : this.$router.currentRoute._value.query.down
                }
            }
            sessionStorage.setItem('filter_sort', JSON.stringify(ValueFilterAndSort));
        }
        window.addEventListener('scroll', this.handleScroll);
        const filter_sort = sessionStorage.getItem('filter_sort');
        let applied = JSON.parse(filter_sort);
        if(filter_sort == null){
            let ValueFilterAndSort = {
                applied : {
                    products : false,
                    sorts : false,
                    limits : false,
                    category : this.route.params.category,
                    up: false,
                    down : false
                }
            }
            sessionStorage.setItem('filter_sort', JSON.stringify(ValueFilterAndSort));
        } else {
                if(applied.applied.category != this.route.params.category){
                    let ValueFilterAndSort = {
                    applied : {
                        products : false,
                        sorts : false,
                        limits : false,
                        category : this.route.params.category,
                        up: false,
                        down : false
                    }
                }
                sessionStorage.setItem('filter_sort', JSON.stringify(ValueFilterAndSort));
            }
        }
        await this.getData()
    },
    mounted() {
        const element = document.getElementById('filter-and-sort');
        const rect = element.getBoundingClientRect();
        const y = rect.top;
        this.dFixedButtonFilterAndSort = y
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