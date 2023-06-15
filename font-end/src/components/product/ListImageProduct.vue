<template>
    <Carousel :settings="settings" :breakpoints="breakpoints">
        <Slide v-for="slide in dataImage" :key="slide">
            <div class="carousel__item">
                <img class="slide-dp-image" :src="URL_PATH_SERVER + '/' + `${slide}`" alt="">
            </div>
        </Slide>
    
        <template #addons>
            <Pagination />
            <Navigation />
        </template>
    </Carousel>
</template>
    
<script>
import { Carousel, Navigation, Slide, Pagination } from 'vue3-carousel'
import { URL_PATH_SERVER } from '../../common/constants';
export default ({
    name: 'ListImageProduct',
    props: {
        dataImage : []
    },
    components: {
      Pagination,
      Carousel,
      Slide,
      Navigation,
    },
    data: () => ({
        settings: {
            itemsToShow: 2,
            snapAlign: 'center',
        },
        URL_PATH_SERVER : URL_PATH_SERVER ,

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
            itemsToShow: 3,
            snapAlign: 'center',
            },
        },
    }),
    methods: {

    },
    created(){
      
    }

})
</script>
<style>
.slide-dp-image {
    max-width: 100%;
    height: 100%;   
}
</style>