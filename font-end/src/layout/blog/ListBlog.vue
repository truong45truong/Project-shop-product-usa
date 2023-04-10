<template>
    <h1>Thảo luận</h1>
    <div v-for="item, index in data">
        <blog-item :content="item.blog.content" :photo_blogs="item.img" :date_create="item.blog.date_create" 
            :number_comment="item.blog.number_comment" :number_heart="item.blog.number_heart" :status_heart="item.blog.status_heart"
            :title="item.blog.title" :comments="item.comments" :user_id="item.blog.user_id" :key="index" :id='item.blog.id' />
    </div>
</template>
<script>
import BlogItem from './../../components/blog/BlogItem.vue'
import { mapGetters, mapActions } from 'vuex'
import {BlogApiService} from './../../common/blog.service'
export default {
    name: 'ListBlog',
    props: {
        msg: String,
        product_slug : false
    },
    components: {
        BlogItem,
    },
    data() {
        return {
            data: []
        }
    },
    computed: {

    },
    created() {
        this.getData()
    },
    methods: {

        async getData() {
            const params = {
                index : 1

            }
            return await BlogApiService.getBlogProduct({
                params : {
                    product_slug : this.product_slug
                }
            }).then((response) => {
                if (response.data.blogs) {
                    this.data = response.data.blogs
                    console.log("data blog",this.data)
                }
            })
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style></style>