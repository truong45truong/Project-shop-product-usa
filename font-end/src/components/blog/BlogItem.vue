<template>
    <div class="blog-tem shadow rounded">
        <div class="d-flex flex-column">
            <div class="mx-5 my-3 d-flex justify-content-between">
                <div class="d-flex">
                    <!-- <img  class="img-author" :src="user_id.photo" alt="Resized Image"/>
                    <div>
                        <p class="ms-3 text-white"><b>{{user_id.email}}</b></p>
                        <p class="ms-3 text-white"><i>{{date_create}}</i></p>
                    </div> -->
                </div>
                <div class="">
                    <a class="fs-1 text-white action-blog" href="">...</a>
                </div>
            </div>
            <hr class=" m-0 mb-2"/>
            <div>
                <h5 class="text-white mx-5">{{ title }}</h5>
                <p class="text-white mx-5 d-block break-lines" v-bind:class="{'content-blog-hide' : !isShow}" id="contentBlog">{{content }}</p>
                <p v-if="!isShow" class="text-white mx-5 d-block break-lines mb-2 btn-action" @click="setMore()"><i><b>Xem thêm</b></i></p>
                <p v-if="isShow" class="text-white mx-5 d-block break-lines mb-2 btn-action" @click="setMore()"><i><b>Ẩn bớt</b></i></p>
            </div>
        </div>
        <Carousel :settings="settings" :breakpoints="breakpoints" :wrap-around="true">
            <Slide v-for="image in data_src" :key="image">
                <img v-if="!image.type" class="img-slide" :src="image.src" alt="Resized Image"/>
                <video v-if="image.type" class="img-slide" :src="image.src" controls></video>
            </Slide>

            <template #addons>
                <Navigation  class="slide-width" />
            </template>
        </Carousel>
        <div class="d-flex justify-content-between">
            <div class="icon-activate ms-5 my-2 d-flex">
                <p class="me-2 m-0 btn-heart-blog" @click="heartBlog">
                    <span><b class="text-white me-1">{{hearts_lenght}} </b></span>
                    <span v-if="isHeart">Đã yêu thích </span>
                    <span v-if="isHeart == false">Yêu thích</span>
                </p>
                <font-awesome-icon icon="fa-solid fa-heart" />
            </div>
            <div class="icon-activate my-2 d-flex">
                <p class="me-2 m-0"> 
                    <span><b class="text-white me-1">{{comments_length}}</b></span>
                    Bình luận 
                </p>
                <font-awesome-icon icon="fa-solid fa-comment" />
            </div>
            <div class="icon-activate me-5 my-2 d-flex">
                <p class="me-2 m-0">Chia sẻ</p>
                <font-awesome-icon icon="fa-solid fa-share" />
            </div>
        </div>
        <hr class="m-0 mb-1"/>
        <list-comment :listComments = "comments" :blogId = "id" :productSlug="false"/>
    </div>
</template>
<script>
import { Carousel, Navigation, Slide } from 'vue3-carousel'
import ListComment from './../../layout/blog/ListComment.vue'
import {blogAction} from './../../common/blog.service'
import { URL_PATH_SERVER } from './../../common/constants'
export default {
    name: 'BlogItem',
    props: {
        id : '' ,
        img: '',
        content: '',
        title: '',
        user_id: '',
        comments: [],
        photo_blogs: [],
        date_create : '',
        number_heart: 0,
        number_comment : 0,
        status_heart : false,
    },
    data() {
        return {
            postBody: '',
            data_src: [],
            data_content : '',
            isShow : true,
            settings: {
                itemsToShow: 3,
                snapAlign: 'center',
            },
            isHeart:false,
            hearts_lenght : 0,
            comment_lenght: 0,
            // breakpoints are mobile first
            // any settings not specified will fallback to the carousel settings
            breakpoints: {
                400: {
                itemsToShow: 1,
                snapAlign: 'center',
                },
                // 700px and up
                700: {
                itemsToShow: 2,
                snapAlign: 'center',
                },
                // 1024 and up
                1024: {
                itemsToShow: 3,
                snapAlign: 'center',
                },
            },
        } 
    }
    ,
    created() {
        console.log("comments",this.comments)

        this.isHeart = this.status_heart
        if(this.status_heart == null){
            this.isHeart = false
        }
        this.hearts_lenght = this.number_heart
        this.comments_length = this.number_comment
        let list_photo = this.photo_blogs.split(",")
        for (let index of list_photo) {
            let media = index.split(":")
            this.data_src.push({ src : URL_PATH_SERVER + '/' + media[0] ,
                                 type : parseInt(media[1])
         })
        }
        if( document.getElementById('contentBlog') > 300)
            {
                this.isShow = true
            } else { this.isShow = false}
            
    },
    components: {
        Carousel,
        Slide,
        Navigation,
        ListComment
    },
    methods : {
        setMore(){
            console.log(this.isShow)
            this.isShow= ! this.isShow
        }
        ,
        async heartBlog(){
            this.isHeart = ! this.isHeart
            if(this.isHeart == false){
                this.hearts_lenght -= 1
            }else {
                this.hearts_lenght += 1
            }
            await blogAction.actionHeartBlog({
                params : {
                    blog_id : this.id
                }
            }).then(res => {
                console.log("heart blog",res)
            })
        }

    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.blog-tem {
    background-color: rgb(33, 37, 41);
    margin: 5rem 0;
}
.img-slide {
    width : 100%;
    height : auto;
}
.icon-activate{
    font-size: 1.5rem;
    color:white;
}
.carousel__icon {
    color:rgba(255, 255, 255,0.65);
    font-size:2rem;
}

.img-author{
    width:75px;
    height:75px;
    border-radius: 50%;
}
.action-blog {
    margin:auto;
    text-decoration:none;
}
.break-lines {
    white-space: pre-line;
}
.content-blog-hide {
    white-space: wrap; 
    height: 5rem; 
    overflow: hidden;
    text-overflow: ellipsis; 
}
.btn-action:hover {
    cursor:pointer;
    text-decoration:underline;
    color:rgb(49, 132, 180) !important;
}
.comment-blog {
    margin-right: 0;
}
.carousel__prev,
.carousel__next {
  background-color: rgb(36,41,47);
  color: white;
  font-size: 14px;
  padding: 2px 4px;
  border: 1px solid rgb(36,41,47);
  border-radius: 5px;
  margin-right: 8px;
  border-radius: 50%;
}
.btn-heart-blog {
    cursor:pointer;
}
.btn-heart-blog:hover {
    text-decoration: underline;
}
</style>