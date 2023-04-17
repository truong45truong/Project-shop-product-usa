<template>
   <div class="shadow rounded position-relative px-3 layout-expand-cmmt">
    <div class="d-flex mt-1 justify-content-end btn-hide" @click ='hide'>
        <font-awesome-icon icon="fa-solid fa-xmark" class="text-dark mb-0" />
    </div>
    <p class="text-dark btn-option-expand mt-3"> Báo cáo bình luận</p>
    <p v-if="isAuthentication" class="text-dark btn-option-expand" @click='editComment'> Chỉnh sửa</p>
    <p v-if="isAuthentication" class="text-dark btn-option-expand" @click='deleteComment'> Xóa</p>
   </div>
</template>
<script>
import { mapActions,mapGetters } from 'vuex'
import {CommentAction} from './../../common/comment.service'

export default {
    name: 'OptionExpandComment',
    props: {
        msg:''
    },
    data() {
        return {
            isAuthentication : false,
            comment_id : '',
            content: '',
        } 
    }
    ,
    created() {
        
            
    },
    
    computed: {
        ...mapGetters('auth', {
			get_user         : 'currentUser'
		}),
    },
    methods : {
        hide(){
            this.$emit('hide')
        },
        checkAuthentication(email){
            if ( this.get_user.user == email){
                this.isAuthentication = true
            }else {
                this.isAuthentication = false
            }
            console.log('this.isAuthentication',this.isAuthentication)
        },
        initValue(comment_id,content){
            this.comment_id = comment_id
            this.content = content
        },
        editComment(){
            this.$emit('editComment',this.comment_id,this.content)
            this.$emit('hide')
        },
        async deleteComment(){
            await CommentAction.actionDeleteComment({
                params : {
                    comment_id : this.comment_id,
                }
            }).then(response => {
                if(response.status == 200){
                    this.hide()
                    this.$emit('deleteComment',this.comment_id)
                }
            })
        }

    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.layout-expand-cmmt {
    width:fit-content;
    height:fit-content;
    background-color: white;
}
.btn-hide {
    cursor:pointer;

}
.btn-option-expand {
    cursor:pointer;
    font-size: 15px;
}
.btn-option-expand:hover {
    text-decoration: underline;
}
</style>