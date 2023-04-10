<template>
    <div class="d-flex flex-column" id="list-comment">
        <div v-for="index in number_comment_load">
            <div :id="`${comments[index].id}`" class="m-4">
                <div class="d-flex">
                    <div class="d-flex">
                        <img  class="img-author-comment" :src="'http://127.0.0.1:8000/'+`${comments[index].user_profile}`" alt="Resized Image"/>
                    </div>
                    <div class="d-flex flex-column">
                        <p class="m-2 mt-3 p-2 px-4 bg-light rounded comment-blog">
                            <p class="text-user-email mb-1"><i><b>{{comments[index].user_email}}</b></i></p>
                            <hr class="my-1">
                             {{comments[index].content}}
                        </p>
                        <div class="d-flex">
                            <p class="mx-2 text-white show-reply" @click="heartComment(comments[index].id)">
                                <span :id="'number-heart-'+`${comments[index].id}`" class="ms-1 me-1">{{comments[index].number_heart}}</span> 
                                <i class="fa-solid fa-heart me-2 text-white"></i> 
                                <i :id="'heart-'+`${comments[index].id}`" :value="comments[index].status_heart_comment == false ? 0 : 1" >
                                    <b v-if="comments[index].status_heart_comment == false">Yêu thích</b>
                                    <b v-if="comments[index].status_heart_comment == true"> Đã yêu thích </b>
                                </i>
                            </p>
                            <p v-if="isCommentChild(comments[index]['id']) == true" class="mx-2 text-white show-reply" :value="`${comments[index]['id']}`" @click="checkCommentChild(comments[index]['id'],comments[index]['level'],null)"> 
                                <i><b class="action-show">
                                Xem
                                    <span class="text-white"> {{comments[index].count_comment_child}} </span>
                                phản hồi
                                </b></i></p>
                        </div>
                        <div class="d-flex">
                            <font-awesome-icon icon="fa-regular fa-comment" class="m-0 ms-4 text-white" />
                            <p class="mx-2 text-white comment-reply" :value="`${comments[index]['id']}`" @click="CommentPost(comments[index]['id'],comments[index].user_email)"> <i><b>Comment</b></i></p>
                        </div>
                    </div>
                </div>
            </div>      
        </div>
        <div v-if="isShowMoreComment" class="text-center" @click="upNumberCommentShow">
            <p class="text-white btn-more-comment">Xem thêm bình luận</p>
        </div>
        <div id="layout-comment">
            <div class="d-flex align-items-center" id="comment-user-blog">
                <div class="d-flex">
                            <img  class="img-author-comment" :src="profilePhoto" alt="Resized Image"/>
                </div>
                <div class="content-comment w-100">
                    <div v-if="userOfCommentSelected != false" class="d-flex align-items-center mb-1">
                        <p class="text-white m-0 ms-3"><b><i>Reply comment user : {{userOfCommentSelected}}</i></b></p>
                        <font-awesome-icon icon="fa-solid fa-xmark" class="ms-3 text-white comment-reply" @click="CancelReplyComment"/>
                    </div>
                    <input type="text" v-model="contentPostComment" class="w-100 text-input-comment">
                </div>
                <font-awesome-icon icon="fa-solid fa-paper-plane" class="m-0 send-icon-comment mx-2 my-2" @click="PostComment"/>
            </div>
        </div>
    </div>
</template>

<script>

import { mapGetters } from 'vuex'
import { CommentApiService,CommentAction } from './../../common/comment.service'
export default {
    name : 'ListComment' ,
    props : {
        listComments : null,
        blogId : ''
    },
    data () {
        return  {
            error : '',
            isShowComment : {},
            isShowInputComment : false,
            isComment : false ,
            userOfCommentSelected : false ,
            profilePhoto : false ,
            commentSelected : false ,
            contentPostComment : '',
            comments : [],
            indexload : 1,
            number_comment_load : 3,
            isShowMoreComment : true,
        }
    },
    computed: {
		...mapGetters('auth', {
			user : 'currentUser',
			authenticated: 'isAuthenticated',
            getProfilePhoto : 'getProfilePhoto'
		})
    },
    methods :{  
        async heartComment(cmt){
            await CommentAction.actionHeartComment({
                params: {
                    comment : cmt
                }
            }).then(response => {
                console.log("post heart",response)
                let heart_comment_current = document.getElementById('heart-'+cmt)
                switch (response.value) {
                    case true:
                        heart_comment_current.innerHTML = '<b> Đã yêu thích </b>';
                        heart_comment_current.setAttribute("value",1)
                        console.log("Đã yêu thích",heart_comment_current)
                        let number_heart_comment_current = document.getElementById('number-heart-'+cmt)
                        
                        number_heart_comment_current.innerHTML = parseInt(number_heart_comment_current.innerHTML) +  1
                        
                        break;
                    case false:
                        heart_comment_current.innerHTML = '<b> Yêu thích </b>';
                        heart_comment_current.setAttribute("value",0)
                        let number_heart_comment_current_1 = document.getElementById('number-heart-'+cmt)
                        number_heart_comment_current_1.innerHTML = parseInt(number_heart_comment_current_1.innerHTML) -  1
                        
                        break;
                }
            })
            
                
        },
        /* ----------------------- METHOD RESET STATUS COMMENT ---------------------- */
        resetStatus(comment_id){
            let comment_current = document.getElementById(this.commentSelected)
                comment_current.setAttribute('class',"")
        },
        /* --------------------- METHOD CANCEL SELECTED COMMENT --------------------- */
        CancelReplyComment () {

            if (this.commentSelected != false){
                let comment_current = document.getElementById(this.commentSelected);
                this.resetStatus(this.commentSelected)
                comment_current.setAttribute('class',"");
            }
            let commentUserBlog = document.getElementById("comment-user-blog")
            let main= document.getElementById('layout-comment')
            main.appendChild(commentUserBlog)
            this.isShowInputComment = false
            this.userOfCommentSelected = false ;
            this.commentSelected = false ;
        },
        /* ------------------------- METHOD SELECTED COMMENT ------------------------ */
        CommentPost (comment_id,user_comment) {
            let commentUserBlog = document.getElementById("comment-user-blog")
            if (this.commentSelected != comment_id && this.commentSelected != false){
                this.resetStatus(comment_id)
            }
            else {
                this.isShowInputComment = ! this.isShowInputComment
            }
            console.log('this.comment_id : ', comment_id)
            let comment_activate = document.getElementById(comment_id)
            if(this.isShowInputComment == true){
                comment_activate.setAttribute('class',"m-4 border border-white")
                this.commentSelected = comment_id
                this.userOfCommentSelected = user_comment

                comment_activate.appendChild(commentUserBlog)
            } else {
                comment_activate.setAttribute('class',"")
                this.userOfCommentSelected = false ;
                this.commentSelected = false ;
                let commentUserBlog = document.getElementById("comment-user-blog")
                let main= document.getElementById('layout-comment')
                main.appendChild(commentUserBlog)
            }
            
        },
        /* ------------------------- METHOD IS COMMENT CHILD ------------------------ */
        isCommentChild(comment){
            for (let value of this.listComments){
                console.log("value.count_comment_child",value.count_comment_child)
                if(value.id == comment && value['count_comment_child'] > 0) {
                    return true;
                }
            }
            return false
        },
        /* ------------------------ METHOD GET COMMENTS CHILD ----------------------- */
        async getCommentChild(comment){
            let json
            await CommentApiService.getCommentChild({
                params: {
                    id : comment
                }
            }).then(response => {
                console.log('response.data.comments',response.data.comments)
                json =  response.data.comments
            })
            return json
        },
        /* ------------------------ METHOD APPEND COMMENT_NEW ----------------------- */
        appendCommentNew(comment,level,commentnew){
            let treeNode = document.getElementById(comment)
            let div_all_comments = document.createElement("div")
            let level_comment = level + 1
            let class_level = "comment-level"
            let id_comment = 'id_comment-'+comment
            div_all_comments.setAttribute('class',"m4 " + class_level)
            div_all_comments.setAttribute('id',id_comment)

            for( let index of commentnew){

                    let div_current_comment = document.createElement("div")
                    div_current_comment.setAttribute('id',index.id)

                    let div_flex_1 = document.createElement("div")
                    div_flex_1.setAttribute('class','d-flex')
                    div_current_comment.appendChild(div_flex_1)

                    let div_flex_1_1 = document.createElement("div")
                    div_flex_1_1.setAttribute('class','d-flex')
                    

                    let img_div_flex_2 = document.createElement("img")
                    img_div_flex_2.setAttribute('class','img-author-comment')
                    img_div_flex_2.setAttribute('src',"http://127.0.0.1:8000/"+index.user_profile)
                    img_div_flex_2.setAttribute('class','img-author-comment')
                    div_flex_1_1.appendChild(img_div_flex_2)

                    let div_flex_1_2 = document.createElement("div")
                    div_flex_1_2.setAttribute('class','d-flex flex-column')

                    let p_div_flex_1_2 = document.createElement("p")
                    p_div_flex_1_2.setAttribute('class','m-2 mt-3 p-2 px-4 bg-light rounded comment-blog')


                    let p_flex_div_flex_1_2 = document.createElement("p")
                    p_flex_div_flex_1_2.setAttribute('class','mx-2 text-white show-reply')

                    let span_p_div_flex_1_2 = document.createElement("span")
                    span_p_div_flex_1_2.setAttribute('class','me-1')
                    span_p_div_flex_1_2.innerText = index.number_heart

                    let icon_p_div_flex_1_2 = document.createElement("i") 
                    icon_p_div_flex_1_2.setAttribute('class','fa-solid fa-heart me-2')
                    let b_aft_i_p_div_flex_1_2 = document.createElement("b")
                    b_aft_i_p_div_flex_1_2.innerText =  "Yêu thích"
                    b_aft_i_p_div_flex_1_2.setAttribute('id','heart-'+index.id)

                    p_flex_div_flex_1_2.appendChild(span_p_div_flex_1_2)
                    p_flex_div_flex_1_2.appendChild(icon_p_div_flex_1_2)
                    p_flex_div_flex_1_2.appendChild(b_aft_i_p_div_flex_1_2)

                    if(index.count_comment_child > 0){
                        let b_aft_b_p_div_flex_1_2 = document.createElement("b")
                        b_aft_b_p_div_flex_1_2.setAttribute('class','ms-3 action-show')
                        b_aft_b_p_div_flex_1_2.innerText =  "Xem " + index.count_comment_child + " phản hồi"
                        b_aft_b_p_div_flex_1_2.addEventListener('click',(event) => {
                            this.checkCommentChild(index.id)
                        })
                        p_flex_div_flex_1_2.appendChild(b_aft_b_p_div_flex_1_2)
                    }
                    
                    /* ----------------------------------- add ---------------------------------- */
                    let p_flex_div_flex_1_3 = document.createElement("div")
                    p_flex_div_flex_1_3.setAttribute('class','mx-2 text-white')
                    let icon_p_div_flex_1_3 = document.createElement("i") 
                    icon_p_div_flex_1_3.setAttribute('class','fa-regular fa-comment me-2') 
                    p_flex_div_flex_1_3.appendChild(icon_p_div_flex_1_3)

                    if(index.level < 6 ){
                        let b_aft_b_p_div_flex_1_3 = document.createElement("b")
                        b_aft_b_p_div_flex_1_3.setAttribute('class','mx-2 text-white comment-reply')
                        b_aft_b_p_div_flex_1_3.innerText =  "Bình luận"
                        b_aft_b_p_div_flex_1_3.addEventListener('click',(event) => {
                            this.CommentPost(index.id,index.user_email)
                        })
                        p_flex_div_flex_1_3.appendChild(b_aft_b_p_div_flex_1_3)
                        }
                    /* --------------------------------- end add -------------------------------- */
                    let p_p_div_flex_1_2 = document.createElement("p")
                    p_p_div_flex_1_2.setAttribute('class','text-user-email mb-1')

                    let i_p_p_div_flex_1_2 = document.createElement("i")
                    let i_b_p_p_div_flex_1_2 = document.createElement("b")
                    i_b_p_p_div_flex_1_2.innerText = index.user_email
                    i_p_p_div_flex_1_2.appendChild(i_b_p_p_div_flex_1_2)
                    
                    let hr_p_div_flex_1_2 = document.createElement("hr")
                    hr_p_div_flex_1_2.setAttribute('class','my-1')
                    
                    let p_p_p_div_flex_1_2 = document.createElement("p")
                    p_p_p_div_flex_1_2.setAttribute('class','m-0')
                    p_p_p_div_flex_1_2.innerText = index['content']
                    

                    p_p_div_flex_1_2.appendChild(i_p_p_div_flex_1_2)
                    p_p_div_flex_1_2.appendChild(hr_p_div_flex_1_2)
                    p_p_div_flex_1_2.appendChild(p_p_p_div_flex_1_2)
                    p_div_flex_1_2.appendChild(p_p_div_flex_1_2)
                    div_flex_1_2.appendChild(p_div_flex_1_2)
                    div_flex_1_2.appendChild(p_flex_div_flex_1_2)
                    div_flex_1_2.appendChild(p_flex_div_flex_1_3)
                    div_flex_1.appendChild(div_flex_1_1)
                    div_flex_1.appendChild(div_flex_1_2)
                    div_all_comments.appendChild(div_current_comment)
                
                
                }
                treeNode.appendChild(div_all_comments)
        },
        /* --------------- METHOD SHOW COMMENT CHILD OF COMMENT PARENT -------------- */
       async checkCommentChild(comment,level,comments) {
            if(comments == null){ 
                var comments = await this.getCommentChild(comment)
            }
            console.log('comments child',comments)
            if(this.isShowComment[comment] == true ) {
                let treeNode = document.getElementById(comment)
                const list_comment = treeNode.querySelectorAll('.comment-level')
                list_comment.forEach(c => c.remove());
                let action_show = treeNode.querySelectorAll('.action-show')
                action_show.forEach(c => c.innerHTML = "Xem phản hồi");
                this.isShowComment[comment] = false
            }
            else{
                this.isShowComment[comment] = true;
                let treeNode = document.getElementById(comment)
                let action_show = treeNode.querySelectorAll('.action-show')
                action_show.forEach(c => c.innerHTML = "Ẩn phản hồi");
                let div_all_comments = document.createElement("div")
                let level_comment = level + 1
                let class_level = "comment-level"
                let id_comment = 'id_comment-'+comment
                div_all_comments.setAttribute('class',"m4 " + class_level)
                div_all_comments.setAttribute('id',id_comment)

                for( let index of comments){

                        let div_current_comment = document.createElement("div")
                        div_current_comment.setAttribute('id',index.id)

                        let div_flex_1 = document.createElement("div")
                        div_flex_1.setAttribute('class','d-flex')
                        div_current_comment.appendChild(div_flex_1)

                        let div_flex_1_1 = document.createElement("div")
                        div_flex_1_1.setAttribute('class','d-flex')
                       

                        let img_div_flex_2 = document.createElement("img")
                        img_div_flex_2.setAttribute('class','img-author-comment')
                        img_div_flex_2.setAttribute('src',"http://127.0.0.1:8000/"+index.user_profile)
                        img_div_flex_2.setAttribute('class','img-author-comment')
                        div_flex_1_1.appendChild(img_div_flex_2)

                        let div_flex_1_2 = document.createElement("div")
                        div_flex_1_2.setAttribute('class','d-flex flex-column')

                        let p_div_flex_1_2 = document.createElement("p")
                        p_div_flex_1_2.setAttribute('class','m-2 mt-3 p-2 px-4 bg-light rounded comment-blog')


                        let p_flex_div_flex_1_2 = document.createElement("p")
                        p_flex_div_flex_1_2.setAttribute('class','mx-2 text-white show-reply')

                        let span_p_div_flex_1_2 = document.createElement("span")
                        span_p_div_flex_1_2.setAttribute('class','me-1')
                        span_p_div_flex_1_2.innerText = index.number_heart

                        let icon_p_div_flex_1_2 = document.createElement("i") 
                        icon_p_div_flex_1_2.setAttribute('class','fa-solid fa-heart me-2')
                        let b_aft_i_p_div_flex_1_2 = document.createElement("b")
                        b_aft_i_p_div_flex_1_2.innerText =  "Yêu thích"
                        b_aft_i_p_div_flex_1_2.setAttribute('id','heart-'+index.id)

                        p_flex_div_flex_1_2.appendChild(span_p_div_flex_1_2)
                        p_flex_div_flex_1_2.appendChild(icon_p_div_flex_1_2)
                        p_flex_div_flex_1_2.appendChild(b_aft_i_p_div_flex_1_2)

                        if(index.count_comment_child > 0){
                            let b_aft_b_p_div_flex_1_2 = document.createElement("b")
                            b_aft_b_p_div_flex_1_2.setAttribute('class','ms-3 action-show')
                            b_aft_b_p_div_flex_1_2.innerText =  "Xem " + index.count_comment_child + " phản hồi"
                            b_aft_b_p_div_flex_1_2.addEventListener('click',(event) => {
                                this.checkCommentChild(index.id)
                            })
                            p_flex_div_flex_1_2.appendChild(b_aft_b_p_div_flex_1_2)
                        }
                        
                        /* ----------------------------------- add ---------------------------------- */
                        let p_flex_div_flex_1_3 = document.createElement("div")
                        p_flex_div_flex_1_3.setAttribute('class','mx-2 text-white')
                        let icon_p_div_flex_1_3 = document.createElement("i") 
                        icon_p_div_flex_1_3.setAttribute('class','fa-regular fa-comment me-2') 
                        p_flex_div_flex_1_3.appendChild(icon_p_div_flex_1_3)

                        if(index.level < 6 ){
                            let b_aft_b_p_div_flex_1_3 = document.createElement("b")
                            b_aft_b_p_div_flex_1_3.setAttribute('class','mx-2 text-white comment-reply')
                            b_aft_b_p_div_flex_1_3.innerText =  "Bình luận"
                            b_aft_b_p_div_flex_1_3.addEventListener('click',(event) => {
                                this.CommentPost(index.id,index.user_email)
                            })
                            p_flex_div_flex_1_3.appendChild(b_aft_b_p_div_flex_1_3)
                            }
                        /* --------------------------------- end add -------------------------------- */
                        let p_p_div_flex_1_2 = document.createElement("p")
                        p_p_div_flex_1_2.setAttribute('class','text-user-email mb-1')

                        let i_p_p_div_flex_1_2 = document.createElement("i")
                        let i_b_p_p_div_flex_1_2 = document.createElement("b")
                        i_b_p_p_div_flex_1_2.innerText = index.user_email
                        i_p_p_div_flex_1_2.appendChild(i_b_p_p_div_flex_1_2)
                        
                        let hr_p_div_flex_1_2 = document.createElement("hr")
                        hr_p_div_flex_1_2.setAttribute('class','my-1')
                        
                        let p_p_p_div_flex_1_2 = document.createElement("p")
                        p_p_p_div_flex_1_2.setAttribute('class','m-0')
                        p_p_p_div_flex_1_2.innerText = index['content']
                        

                        p_p_div_flex_1_2.appendChild(i_p_p_div_flex_1_2)
                        p_p_div_flex_1_2.appendChild(hr_p_div_flex_1_2)
                        p_p_div_flex_1_2.appendChild(p_p_p_div_flex_1_2)
                        p_div_flex_1_2.appendChild(p_p_div_flex_1_2)
                        div_flex_1_2.appendChild(p_div_flex_1_2)
                        div_flex_1_2.appendChild(p_flex_div_flex_1_2)
                        div_flex_1_2.appendChild(p_flex_div_flex_1_3)
                        div_flex_1.appendChild(div_flex_1_1)
                        div_flex_1.appendChild(div_flex_1_2)
                        div_all_comments.appendChild(div_current_comment)
                    
                    
                }
                treeNode.appendChild(div_all_comments)
            }
        },
        /* --------------------------- METHOD POST COMMENT -------------------------- */
        async PostComment(){
            let content = this.contentPostComment 
            let parent = this.commentSelected
            let blog_id = this.blogId

            await CommentAction.actionPostComment({
                content : content ,
                parent : parent,
                blog_id : blog_id,

            }).then(res => {
                console.log("comment post",res)
                if(res.status == 200){
                    if(parent != false){
                        this.appendCommentNew(parent,res.comment.level,[res.comment])
                    }
                    else {
                        this.comments.push(res.comment)
                    }

                }
            })
        },
        upNumberCommentShow(){
            this.indexload += 1
            let number_comment = this.indexload * this.number_comment_load ;
            if(number_comment > this.comments.length){
                this.number_comment_load = (this.comments.length - 1)
                this.isShowMoreComment = false
            }else {
                this.number_comment_load = number_comment
            }
        }
    },
    created () {
        this.profilePhoto = "http://127.0.0.1:8000" + this.getProfilePhoto
        this.isCommentChild("tribgb");
        this.comments = this.listComments
        console.log("list-commet",this.comments)
    }
}
</script>

<style>
.text-input-comment {
    border:0ch;
    border-radius: 15px;
    padding : 5px 10px;
}
.send-icon-comment {
    font-size: 1.5rem;
    color:white;
}
.comment-blog {
    width :fit-content ;
    height : fit-content ;
}
.img-author-comment {
    border-radius: 50%;
    width : 3rem;
    height : 3rem;
    margin: 1rem 1rem;
}
.show-reply:hover {
    cursor :pointer;
    text-decoration: underline;
}
.comment-reply:hover {
    cursor :pointer;
    text-decoration: underline;
}
.comment-level{
    margin-left: 5rem;
}
.comment-level-2 {
    margin-left: 10rem;
}
.text-user-email {
    color : rgba(19, 18, 18,0.8);
}
.btn-more-comment {
    cursor:pointer;
}
.btn-more-comment:hover {
    text-decoration: underline;
}
</style>