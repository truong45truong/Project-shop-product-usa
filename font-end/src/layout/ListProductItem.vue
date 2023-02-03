<template>
    <div class="container mt-5 flash-sale-top">
        <div class="row m-3 flash-sale-inside">
            <div class="col-lg-6 my-5 d-flex align-items-center ">
                <font-awesome-icon icon="fa-solid fa-bolt" class="text-white fs-3 me-2" />
                <h3 class="text-white m-0 me-1">Flash Sale:</h3>
                <CountDownFLashSale :date_prop="date_flash_sale" :hour_prop="hour_flash_sale" :mins_prop="mins_flash_sale" :secs_prop="secs_flash_sale"/>
            </div>
            <div class="col-lg-6 my-5 d-flex align-items-center justify-content-end">
                <p class="show-all-product-flash-sale m-0 text-white fs-5">Xem tất cả</p>
                <font-awesome-icon icon="fa-solid fa-arrow-right" class="text-white fs-3 ms-4" />
            </div>
        </div>
        <div class="row mx-3">
            <Carousel :settings="settings" :breakpoints="breakpoints">
                <Slide v-for="item in listProductItem" :key="item" :class="'mx-3 shawdo'">
                    <product-item :slug="item.slug" :photo="item.photo_products[0]" :name="item.name"
                        :price="item.prices[0]"
                    />
                </Slide>
            
                <template #addons>
                    <Pagination />
                    <Navigation />
                </template>
            </Carousel>
        </div>
    </div>
</template>
  
<script>
import { defineComponent } from 'vue'
import { Carousel, Navigation, Slide, Pagination } from 'vue3-carousel'
import { ProductApiService } from './../common/product.service'
import CountDownFLashSale from './../components/other/CountDowmFLashSale.vue'
import ProductItem from './../components/product/ProductItem.vue'
import 'vue3-carousel/dist/carousel.css'
import 'vue3-carousel/dist/carousel.js'
export default ({
    name: 'ListProductItem',
    components: {
        ProductItem,
        Pagination,
        Carousel,
        Slide,
        Navigation,
        CountDownFLashSale
    },
    data: () => ({
        listProductItem : [],
        settings: {
        itemsToShow: 2,
        snapAlign: 'center',
        date_flash_sale : 3,
        hour_flash_sale : 17,
        mins_flash_sale : 30,
        secs_flash_sale : 60,
      },
      // breakpoints are mobile first
      // any settings not specified will fallback to the carousel settings
      breakpoints: {
        400: {
          itemsToShow: 2,
          snapAlign: 'center',
        },
        // 700px and up
        700: {
          itemsToShow: 3,
          snapAlign: 'center',
        },
        // 1024 and up
        1024: {
          itemsToShow: 4,
          snapAlign: 'center',
        },
      },
    }),
    async created(){
        await ProductApiService.get().then(res => {
            let array = []
            for(let item of res.data){
                console.log(item)
                array.push(item)
            }
            this.listProductItem = array
            console.log(this.listProductItem)
        })
    }
})
</script>
<style>
.box-demo {
    height:85%;
    position:relative;
    overflow:hidden
}
.flash-sale-inside {
    background-color: rgb(36,41,47);
}



/* CSS */
.flash-sale-top {
  --b: 3px;   /* border thickness */
  --s: 1em; /* size of the corner */
  --color: #373B44;
  
  padding: calc(.5em + var(--s)) calc(.9em + var(--s));
  color: var(--color);
  --_p: var(--s);
  background:
    conic-gradient(from 90deg at var(--b) var(--b),#0000 90deg,var(--color) 0)
    var(--_p) var(--_p)/calc(100% - var(--b) - 2*var(--_p)) calc(100% - var(--b) - 2*var(--_p));
  transition: .3s linear, color 0s, background-color 0s;
  outline: var(--b) solid #0000;
  outline-offset: .6em;
  font-size: 16px;

  border: 0;

  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
}

.flash-sale-top:hover,
.flash-sale-top:focus-visible{
  --_p: 0px;
  outline-color: var(--color);
  outline-offset: .05em;
}

/* CSS */
.button-56 {
  align-items: center;
  background-color: rgb(230, 181, 23);
  border: 2px solid rgb(230, 181, 23);
  border-radius: 8px;
  box-sizing: border-box;
  color: rgb(230, 181, 23);;
  cursor: pointer;
  display: flex;
  font-family: Inter,sans-serif;
  font-size: 16px;
  height: 48px;
  justify-content: center;
  max-width: 100%;
  padding: 0 25px;
  position:relative;
  text-align: center;
  text-decoration: none;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  z-index: 9;
}

.button-56:after {
  position:absolute;
  background-color: rgb(250, 196, 96);
  border-radius: 8px;
  content: "Xem tất cả";
  color : rgb(14, 13, 12);
  display: block;
  height: 100%;
  left: 0;
  width: 100%;
  top: 0px;
  padding:15px 25px;
  transform: translate(8px, 10px);
  transition: transform .2s ease-out;
  z-index: 99;
}

.button-56:hover:after {
  transform: translate(0, 0);
}

.button-56:after:active {
  background-color: #ffdeda;
  outline: 0;
}

.button-56:hover {
  outline: 0;
}

@media (min-width: 768px) {
  .button-56 {
    padding: 0 40px;
  }
}
.show-all-product-flash-sale{
    font-family: 'Sassy Frass', cursive;
    font-weight: 700;
}

</style>