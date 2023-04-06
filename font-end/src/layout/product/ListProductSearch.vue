<template>
    <div class="title-list">
        <div class="container">
            <div class="row">
                <p href="" class="fs-1 text-dark title-category">Tìm kiếm cho: <i>{{keySearch}}</i></p>
                <div class="">
                    <p class="text-dark"><i>Các sản phẩm chúng tôi đều có nguồn cung cấp uy tín và chất lượng</i></p>
                    <p class="text-dark">
                        <i>Danh mục : </i>
                        <a class="ms-2" href=""> <i>{{listCategorySearch}}</i></a>
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
    <FilterAndSortLayout v-if="filterAndSort != false" @hideFilterAndSort="showFilterAndSort" :type=2 :listCategory="listCategory" 
    :key_search="keySearch" :hideProducts=true />
    <div class="bottom-list">
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
import { ProductApiService } from './../../common/product.service'
import ProductCategory from './../../components/product/ProductCategory.vue'
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
    name: 'ListProductSearch',
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
            this.listCategorySearch = this.route.query.category
            this.checkFilterSort()
            this.getData()
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
        keySearch : '',
        listCategorySearch : '',
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
        changePage(index){
            this.indexPage = index
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
        checkFilterSort(){
            const filter_sort = sessionStorage.getItem('filter_sort');
            let applied = JSON.parse(filter_sort);
            if(filter_sort == null){
                let ValueFilterAndSort = {
                    applied : {
                        products : false,
                        sorts : false,
                        limits : false,
                        category : this.route.query.category,
                        up: false,
                        down : false
                    }
                }
                sessionStorage.setItem('filter_sort', JSON.stringify(ValueFilterAndSort));
            } else {
                    if(applied.applied.category != this.route.query.category){
                        let ValueFilterAndSort = {
                        applied : {
                            products : false,
                            sorts : false,
                            limits : false,
                            category : this.route.query.category,
                            up: false,
                            down : false
                        }
                    }
                    sessionStorage.setItem('filter_sort', JSON.stringify(ValueFilterAndSort));
                }
            }
        },
        async getData(){
            const filter_sort = sessionStorage.getItem('filter_sort');
            let applied = JSON.parse(filter_sort);
            let arrayLimits= new Array()
            let arraySort = new Array()
            let arraySlugCategory = new Array()
            let filter = {
                sorts : false,
                limits : false,
                categories: false
            }
            if(applied.applied.sorts != false){
                
                for (let item of applied.applied.sorts){
                    let e = Sort.get(item)
                    if(e)
                    arraySort.push(e)
                }
                filter.sorts = arraySort
            }
            if(applied.applied.limits != false){
                for (let item of applied.applied.limits){
                    let e = Limits.get(item)
                    if(e)
                    arrayLimits.push(e)
                }
                filter.limits = arrayLimits
            }
            if(applied.applied.products != false){
                for (let item of applied.applied.products){
                    arraySlugCategory.push(item)
                }
                filter.categories = arraySlugCategory
            }
            await ProductApiService.searchProductCategory({
                params : {
                    key_search : this.keySearch = this.route.params.key_search,
                    categories_slug :this.route.query.category == 'All' ? true : this.route.query.category,
                    'filter_sort' :  JSON.stringify(filter.sorts),
                    'filter_limit' :  JSON.stringify(filter.limits),
                    'up' : applied.applied.up == null ? false : applied.applied.up,
                    'down' : applied.applied.down == null ? false : applied.applied.down,
                    limit_search : false
                }
            }).then(response => {
                if(response.data.products.length == 0){
                    this.data = false
                }else{
                    this.data = response.data.products
                    if( this.data.length > this.numberProductInPage){
                        this.paginate = false
                        this.indexPage = 1;

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
                console.log('search category',response)
            })
        }
    },

    async created() {
        this.keySearch = this.route.params.key_search
        this.listCategorySearch = this.route.query.category
       
        window.addEventListener('scroll', this.handleScroll);
        this.checkFilterSort()
        console.log(this.route.query,Sort)
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
</style>