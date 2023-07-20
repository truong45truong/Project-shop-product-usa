<template>
    <div v-if="data_src.length <= 3" class="ms-4 mt-2 d-flex w-100 layout-list-media ">
        <div v-for="file, index in data_src" :key="index" class="img-media-comment">
            <div class="postion-relative px-2">
                <img v-if="file.type == 0" class="media-comment"  :src="file.src" :index="index" />
                <font-awesome-icon icon="fa-solid fa-square-xmark"  class="position-absolute right-50  media-icon-x" @click="removeImg(file.src)" />
            </div>
            <video v-if="file.type == 1" :src="file.src" controls></video>
        </div>
    </div>
    <Carousel v-if="data_src.length > 3" class="ms-4 mt-2 layout-list-media mt-3" :settings="settings" :breakpoints="breakpoints">
        <Slide v-for="file, index in data_src" :key="index">
            <div class="carousel__item img-media-comment">
                <font-awesome-icon icon="fa-solid fa-square-xmark" class="media-icon-x" @click="removeImg(file.src)" />
                <img v-if="file.type == 0" class="media-comment"  :src="file.src" :index="index"/>
            </div>
        </Slide>
        <template #addons>
            <Navigation />
        </template>
    </Carousel>
</template>
<script>
import { Carousel, Navigation, Slide, Pagination } from 'vue3-carousel'
import { URL_PATH_SERVER } from '../../common/constants'
export default {
    name: 'MediaPhotoProductDetail',
    props: {
        data_files : '',
    },
    components: {
        Pagination,
        Carousel,
        Slide,
        Navigation,
    },
    data() {
        return {
            data_src: [],
            URL_PATH_SERVER : URL_PATH_SERVER ,
            settings: {
                itemsToShow: 3,
                snapAlign: 'center',
            },
            // breakpoints are mobile first
            // any settings not specified will fallback to the carousel settings
            breakpoints: {
                // 700px and up
                700: {
                    itemsToShow: 3,
                    snapAlign: 'center',
                },
                // 1024 and up
                1024: {
                    itemsToShow: 3,
                    snapAlign: 'start',
                },
            },

        }
    },
    computed: {
    },
    created() {
        let list_media = this.data_files.split(",")
        for (let index of list_media) {
            this.data_src.push({ src : URL_PATH_SERVER + '/' + index ,
                                 type : 0 })
        }
        
    },
    mounted(){
    },
    methods: {
        removeImg(src_img){
            this.data_src = this.data_src.filter(src => {
                console.log(src)
                return src.src != src_img
            })
            this.$emit('del',src_img)
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.img-media-comment {
    max-width:13rem;
    height:auto;
}
.media-comment {
    max-width: 8rem;
    height:auto;
}
.media-icon-x {
    cursor:pointer;
}
.layout-list-media  {
    max-width: 500px;
    overflow-x: hidden;
}
@media only screen and (max-width: 624px) {
    .img-media-comment {
        max-width: 5rem;
    }
    .media-comment {
        max-width: 5rem;
    }
}
@media only screen and (max-width: 424px) {
    .img-media-comment {
        max-width: 3.5rem;
    }
    .media-comment {
        max-width: 3.5rem;
    }
}
</style>