<template>
    <div v-if="data_src.length <= 3" class="ms-4 mt-2 d-flex w-100 layout-list-media ">
        <div v-for="file, index in data_src" :key="index" class="img-media-comment">
            <img v-if="file.type == 0" class="media-comment px-1"  :src="file.src" :index="index" />
            <video v-if="file.type == 1" :src="file.src" controls></video>
        </div>
    </div>
    <Carousel v-if="data_src.length > 3" class="ms-4 mt-2 layout-list-media" :settings="settings" :breakpoints="breakpoints">
        <Slide v-for="file, index in data_src" :key="index">
            <div class="carousel__item img-media-comment">
                <img v-if="file.type == 0" class="media-comment"  :src="file.src" :index="index" />
                <video v-if="file.type == 1" :src="file.src" controls></video>
            </div>
        </Slide>
        <template #addons>
            <Navigation />
        </template>
    </Carousel>
</template>
<script>
import ImageSendComment from './../../components/blog/ImageSendComment.vue'
import { Carousel, Navigation, Slide, Pagination } from 'vue3-carousel'

export default {
    name: 'ListMediaComment',
    props: {
        msg: String,
        data_files : '',
        comment_id : ''
    },
    emits: ['setPositionMedia'],
    components: {
        ImageSendComment,
        Pagination,
        Carousel,
        Slide,
        Navigation,
    },
    data() {
        return {
            data_src: [],
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
            let media = index.split(":")
            this.data_src.push({ src : "http://127.0.0.1:8000/" + media[0] ,
                                 type : parseInt(media[1])
         })
        }
    },
    mounted(){
        this.$emit('setPositionMedia',this.comment_id)
    },
    methods: {

    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.img-media-comment {
    max-width:8rem;
    height:auto;
}
.media-comment {
    max-width: 8rem;
    height:auto;
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