<template>
    <Carousel :settings="settings" :breakpoints="breakpoints">
      <Slide v-for="slide in slides" :key="slide">
        <div class="carousel__item">
            <img class="banner-image" :src="slide.src" alt="">
        </div>
      </Slide>
  
      <template #addons>
        <Pagination />
        <Navigation />
      </template>
    </Carousel>
  </template>
  
  <script>
  import { defineComponent } from 'vue'
  import { Carousel, Navigation, Slide, Pagination } from 'vue3-carousel'
  import {actionNew} from '../../common/new.service'
  import banner1 from '@/assets/images/banner-1-1.jpg';
  import banner2 from '@/assets/images/banner-1-1.jpg';
  import 'vue3-carousel/dist/carousel.css'
    import 'vue3-carousel/dist/carousel.js'
  export default defineComponent({
    name: 'BannerHome',
    components: {
      Pagination,
      Carousel,
      Slide,
      Navigation,
    },
    data: () => ({
        slides: [
          { src : banner1 },
          { src : banner2}
        ],
      // carousel settings
      settings: {
        itemsToShow: 3,
        snapAlign: 'center',
      },
      // breakpoints are mobile first
      // any settings not specified will fallback to the carousel settings
      breakpoints: {
        400: {
          itemsToShow: 3,
          snapAlign: 'center',
        },
        // 700px and up
        700: {
          itemsToShow: 3,
          snapAlign: 'center',
        },
        // 1024 and up
        1024: {
          itemsToShow: 3,
          snapAlign: 'center',
        },
      },
    }),
    async created(){
      await actionNew.get_new().then(res => {
        let array =[]
        for (let slide of res.data){
          array.push({src : 'http://127.0.0.1:8000' + slide.photo_news[0].data})
        }
        this.slides = array
      })
    }
  })
  </script>
  <style>
.banner-image{
    max-width:100%;
    height:auto;
}
</style>