<template>
    <div class="d-flex flex-column" id="list-comment">
        <div v-for="index in comments" :id="`${index.id}`" class="m-4 position-relative" :key="index.id">
            <div class="d-flex container-comment">
                <div class="d-flex flex-column layout-avatar">
                    <img v-if="index.user_profile != null" class="img-author-comment" 
                        :src="'http://127.0.0.1:8000/' + `${index.user_profile}`"
                        alt="Resized Image" 
                    />
                    <img v-if="index.user_profile == null" class="img-author-comment" 
                        src="./../../assets/images/user.png"
                        alt="Resized Image" 
                    />
                </div>
                <div class="d-flex flex-column" :id="'container-cmt-'+index.id">
                    <p class="m-2 mt-3 p-2 px-4 bg-light rounded comment-blog">
                    <p class="text-user-email mb-1"><i><b>{{ index.user_email }}</b></i></p>
                    <hr class="my-1">
                    <p :id="'content-cmt-' + `${index.id}`">{{ index.content }}</p>
                    </p>
                    <div class="d-flex">
                        <p class="mx-2 text-white show-reply" @click="heartComment(index.id)">
                            <span :id="'number-heart-' + `${index.id}`" class="ms-1 me-1">{{
                                index.number_heart }}</span>
                            <i class="fa-solid fa-heart me-2 text-white"></i>
                            <i :id="'heart-' + `${index.id}`"
                                :value="index.status_heart_comment == false ? 0 : 1">
                                <b v-if="index.status_heart_comment == false">Yêu thích</b>
                                <b v-if="index.status_heart_comment == true"> Đã yêu thích </b>
                            </i>
                        </p>
                        <p v-if="isCommentChild(index['id']) == true" class="mx-2 text-white show-reply"
                            :value="`${index['id']}`"
                            @click="checkCommentChild(index['id'], index['level'], null)">
                            <i><b class="action-show">
                                    Xem
                                    <span class="text-white"> {{ index.count_comment_child }} </span>
                                    phản hồi
                                </b></i>
                        </p>
                    </div>
                    <p v-if="index.comment_is_edit != null" class="text-white edit-text"
                        :id="'edit-datetime-' + `${index.id}`">
                        Chỉnh sửa : {{ converDatime(index.comment_is_edit )}}
                    </p>
                    <p v-if="index.comment_is_edit == null" class="text-white edit-text"
                        :id="'edit-datetime-' + `${index.id}`">
                        Ngày đăng : {{ converDatime(index.date_create )}}
                    </p>
                    <div class="d-flex">
                        <font-awesome-icon icon="fa-regular fa-comment" class="m-0 ms-4 text-white" />
                        <p class="mx-2 text-white comment-reply" :value="`${index['id']}`"
                            @click="CommentPost(index['id'], index.user_email)">
                            <i><b>Trả lời</b></i>
                        </p>
                    </div>
                    <ListMediaComment v-if="index.file_media_comment != null" 
                    :data_files ="index.file_media_comment"  />
                </div>
                <div class="">
                    <button class="text-white btn-option-comment text-center position-relative mt-3"
                        @click="isShowOptionExpand(index['id'], index.user_email, index.content)">
                        <p class="mb-2 text-absolute position-absolute">...</p>
                    </button>
                </div>
            </div>
        </div>
        
        <div  v-if="comments.length > 0" class="text-center" >
            <p class="text-white btn-more-comment" v-if="isShowMoreComment" @click="upNumberCommentShow">Xem thêm bình luận</p>
            <p class="text-white " v-if="!isShowMoreComment" >Đã hiển thị tất cả bình luận</p>
            
        </div>
        <div v-if="comments.length == 0" class="text-center">
            <p class="my-4 text-white">Chưa có bình luận cho sản phẩm này</p>
        </div>
        <div id="layout-comment">
            <div class="bg-white mt-2" id="comment-user-blog">
                <div class="d-flex  w-100">
                    <div class="d-flex">
                        <img v-if="authenticated" class="img-author-comment" :src="profilePhoto" alt="Resized Image" />
                    </div>
                    <div class="content-comment w-100">
                        <div v-if="userOfCommentSelected != false" class="d-flex align-items-center justify-content-between mb-1">
                            <p class="text-dark m-0 ms-3"><b><i class="text-reply">Trả lời bình luận : {{ userOfCommentSelected }}</i></b></p>
                            <font-awesome-icon icon="fa-solid fa-xmark" class="ms-3 text-dark cancel-btn me-3"
                                @click="CancelReplyComment" />
                        </div>
                        <textarea v-model="contentPostComment" placeholder="Viết bình luận ..."
                            class="w-100 text-input-comment" v-on:keyup.enter="PostComment">
                        </textarea>
                    </div>
                </div>
                <div class="d-flex justify-content-between">
                    <div class="d-flex px-3">
                        <label class="ms-2 label-choose-file align-items-center" for="image-post">
                            <i class="ms-5 add-image-post me-2">Thêm Ảnh/Video</i>
                            <font-awesome-icon icon="fa-regular fa-image" class="icon-image-post-blog fs-4" />
                            <input class="ms-1" type="file" id="image-post" ref="imagePost" name="filename" @change="uploadFile"
                             multiple />
                        </label>           
                    </div>
                    <div class="d-flex align-items-center" @click="PostComment">
                        <p class="show-reply mb-0 me-2" >Bình luận</p>
                        <font-awesome-icon icon="fa-solid fa-paper-plane" class="m-0 send-icon-comment text-dark mx-2 my-2"
                             />
                    </div>
                </div>
                <div class="" v-if="authenticated == false">
                    <!-- Gutter g-1 -->
                    <div class="row g-1">
                        <div class="col-sm-6">
                            <!-- Name input -->
                            <div class="form-outline d-flex justify-content-center">
                                <label class="form-label" for="form9Example1"
                                >Tên
                                    <input v-model="inforCustomer.name" type="text" id="form9Example1" 
                                    class="form-control" :class="[inforCustomer.error.name == true ? 'boder border-danger' : '']" />
                                </label>
                            </div>
                        </div>
                        <div class="col-sm-6">
                            <!-- Email input -->
                            <div class="form-outline  d-flex justify-content-center">
                                <label class="form-label" for="form9Example2">Địa chỉ Email
                                    <input v-model="inforCustomer.email" type="email" id="form9Example2" 
                                    class="form-control"  :class="[inforCustomer.error.email == true ? 'boder border-danger' : '']" />
                                </label>
                                
                            </div>
                        </div>
                        <div class="col-sm-6">
                            <!-- Name input -->
                            <div class="justify-content-center text-center">
                                <div class="d-flex justify-content-center">
                                    <input v-model="inforCustomer.sex" type="radio" id="contactChoice1" name="contact"
                                    :value="true" :class="[inforCustomer.error.sex == true ? 'boder border-danger' : '']" />
                                    <label for="contactChoice1" class="ms-1">Anh</label>
                                    <input v-model="inforCustomer.sex" type="radio" id="contactChoice2" class="ms-4" name="contact"
                                    :value="false" :class="[inforCustomer.error.sex == true ? 'boder border-danger' : '']" />
                                    <label for="contactChoice2" class="ms-1">Chị</label>
                                </div>
                                <p v-if="inforCustomer.error.sex" class="text-danger">Chọn Anh/Chị</p>
                            </div>
                        </div>
                        <div class="col-sm-6">
                            <!-- Email input -->
                            <div class="form-outline  d-flex justify-content-center">
                                <label class="form-label" for="form9Example2">Số điện thoại
                                    <input v-model="inforCustomer.phoneNumber" type="email" id="form9Example2" 
                                    class="form-control"  :class="[inforCustomer.error.phoneNumber == true ? 'boder border-danger' : '']" />
                                </label>
                            </div>
                        </div>
                    </div>
                </div>
                <Carousel class="mt-4" :settings="settings" :breakpoints="breakpoints">
                    <Slide v-for="file, index in fileUpload" :key="index">
                        <div class="carousel__item item-slide-image">
                            <ImageSendComment v-if="file.isImage"  :data="file.data" :index="index" 
                            @removeFileUpload="removeFileUpload" />
                            <video v-if="file.isVideo" :src="file.videoSrc" controls></video>
                        </div>
                    </Slide>

                    <template #addons>
                        <Navigation v-if="fileUpload.length > 5" />
                    </template>
                </Carousel>
            </div>
            <div id="layout-edit-comment">
                <EditComment ref="editComment" id="edit-comment-object" @hide="hideEditComment" @upload="uploadEditComment"
                    :class="[isEditComment == false ? 'd-none' : 'show-edit-comment mt-2']" />
            </div>
            <div id="layout-option-expand">
                <OptionExpandComment ref="optionExpandComment" @hide="hideOptionExpand" @editComment="editComment"
                    @deleteComment="deleteComment" id="option-expand-cmt"
                    :class="[isOptionExpand == false ? 'hide-option-expand' : 'show-option-expand']" />
            </div>
        </div>
        <div id="list-media-comment-child" class="d-non">
            <div v-for="item in listMediaCommentChild" :id="'media-cmt-'+ item.id" class="d-inline" >
                <ListMediaComment :data_files ="item.file_media_comment" :comment_id="item.id" 
                @setPositionMedia="setPositionMedia"
                />
            </div>
        </div>
    </div>
</template>

<script>

import { mapGetters } from 'vuex'
import { CommentApiService, CommentAction } from './../../common/comment.service'
import { Carousel, Navigation, Slide } from 'vue3-carousel'
import ImageSendComment from './../../components/blog/ImageSendComment.vue'
import OptionExpandComment from './../../components/blog/OptionExpandComment.vue'
import EditComment from './../../components/blog/EditComment.vue'
import ListMediaComment from './ListMediaComment.vue'
export default {
    name: 'ListComment',
    props: {
        listComments: null,
        blogId: '',
        productSlug : false,
    },
    data() {
        return {
            listMediaCommentChild : [],
            error: '',
            showComment: {
                value: [],
                isShow : {}
            },
            expand_line_resize : 16,
            commentComponent : '',
            optionExpandCmt : '',
            editCommentCoponent: '',
            isShowInputComment: false,
            isComment: false,
            userOfCommentSelected: false,
            profilePhoto: false,
            commentSelected: false,
            contentPostComment: '',
            comments: [],
            indexload: 4,
            number_comment_load: 10,
            isShowMoreComment: true,
            isOptionExpand: false,
            isEditComment: false,
            fileUpload: [],
            inforCustomer : {
                sex : null,
                phoneNumber : '',
                name : '',
                email : '',
                error : {
                    email : false,
                    phoneNumber : false,
                    sex : false,
                    name : false,
                }
            },
            settings: {
                itemsToShow: 5,
                snapAlign: 'center',
            },
            // breakpoints are mobile first
            // any settings not specified will fallback to the carousel settings
            breakpoints: {
                // 700px and up
                700: {
                    itemsToShow: 3.5,
                    snapAlign: 'center',
                },
                // 1024 and up
                1024: {
                    itemsToShow: 5,
                    snapAlign: 'start',
                },
            },
        }
    },
    components: {
        OptionExpandComment,
        EditComment,
        Carousel,
        Slide,
        Navigation,
        ImageSendComment,
        ListMediaComment
    },
    computed: {
        ...mapGetters('auth', {
            user: 'currentUser',
            authenticated: 'isAuthenticated',
            getProfilePhoto: 'getProfilePhoto'
        })
    },
    methods: {
        hideOptionExpand() {
            this.isOptionExpand = false
        },
        async heartComment(cmt) {
            await CommentAction.actionHeartComment({
                params: {
                    comment: cmt
                }
            }).then(response => {
                console.log("post heart", response)
                let heart_comment_current = document.getElementById('heart-' + cmt)
                switch (response.value) {
                    case true:
                        heart_comment_current.innerHTML = '<b> Đã yêu thích </b>';
                        heart_comment_current.setAttribute("value", 1)
                        console.log("Đã yêu thích", heart_comment_current)
                        let number_heart_comment_current = document.getElementById('number-heart-' + cmt)

                        number_heart_comment_current.innerHTML = parseInt(number_heart_comment_current.innerHTML) + 1

                        break;
                    case false:
                        heart_comment_current.innerHTML = '<b> Yêu thích </b>';
                        heart_comment_current.setAttribute("value", 0)
                        let number_heart_comment_current_1 = document.getElementById('number-heart-' + cmt)
                        number_heart_comment_current_1.innerHTML = parseInt(number_heart_comment_current_1.innerHTML) - 1

                        break;
                }
            })


        },
        /* ----------------------- METHOD RESET STATUS COMMENT ---------------------- */
        CancelReplyComment() {

            if (this.commentSelected != false) {
                let comment_current = document.getElementById(this.commentSelected);
            }
            let commentUserBlog = document.getElementById("comment-user-blog")
            let main = document.getElementById('layout-comment')
            main.appendChild(commentUserBlog)
            this.isShowInputComment = false;
            this.userOfCommentSelected = false;
            this.commentSelected = false;
            this.contentPostComment = '';
            this.inforCustomer = {
                sex : null,
                phoneNumber : '',
                name : '',
                email : '',
                error : {
                    email : false,
                    phoneNumber : false,
                    sex : false,
                    name : false,
                }
            }
        },
        /* ------------------------- METHOD SELECTED COMMENT ------------------------ */
        CommentPost(comment_id, user_comment) {
            this.checkIsComment()
            this.hideEditComment()
            let commentUserBlog = document.getElementById("comment-user-blog")
            if (this.commentSelected != comment_id && this.commentSelected != false) {
            }
            else {
                this.isShowInputComment = !this.isShowInputComment
            }
            console.log('this.comment_id : ', comment_id)
            let comment_activate = document.getElementById(comment_id)
            if (this.isShowInputComment == true) {
                this.commentSelected = comment_id
                this.userOfCommentSelected = user_comment

                comment_activate.appendChild(commentUserBlog)
            } else {
                this.userOfCommentSelected = false;
                this.commentSelected = false;
                let commentUserBlog = document.getElementById("comment-user-blog")
                let main = document.getElementById('layout-comment')
                main.appendChild(commentUserBlog)
            }

        },
        /* ------------------------- METHOD IS COMMENT CHILD ------------------------ */
        isCommentChild(comment) {
            for (let value of this.listComments) {
                if (value.id == comment && value['count_comment_child'] > 0) {
                    return true;
                }
            }
            return false
        },
        /* ------------------------ METHOD GET COMMENTS CHILD ----------------------- */
        async getCommentChild(comment) {
            console.log("getCommentChild start")

            let json
            await CommentApiService.getCommentChild({
                params: {
                    id: comment
                }
            }).then(response => {
                json = response.data.comments
                this.showComment.value[comment] = response.data.comments
            })
            return json
            console.log("getCommentChild end")

        },
        /* ------------------------ METHOD APPEND COMMENT_NEW ----------------------- */
        appendCommentNew(comment, level, commentnew) {
            console.log("appendCommentNew start level",level)
            if(this.showComment.isShow[comment] == true){
                let treeNode = document.getElementById(comment)
                let action_show = treeNode.querySelectorAll('.action-show')
                action_show.forEach(c => c.innerHTML = "Xem phản hồi");
                this.showComment.isShow[comment] = false
            }
            if( !(comment in this.showComment.value)){
                this.checkCommentChild(comment,level,null)
            } else {
                this.showComment.value[comment].push(commentnew)
                this.checkCommentChild(comment,level,this.showComment.value[comment])
            }
            console.log("appendCommentNew end")

            // this.CancelReplyComment()
        },
        converDatime(dateString) {
                        const date = new Date(Date.parse(dateString));

                        const year = date.getFullYear();
                        const month = date.getMonth() + 1; // Tháng bắt đầu từ 0 nên cần +1
                        const day = date.getDate();
                        const hours = date.getHours();
                        const minutes = date.getMinutes();
                        const seconds = date.getSeconds();

                        return `${day}/${month}/${year} ${hours}:${minutes}:${seconds}`;
        },
        addLineComment(cmt){
            console.log("addLineComment start")
            let cmt_main = document.getElementById(cmt)
            let d_flex = cmt_main.querySelector('.d-flex')
            let d_flex_d_flex = d_flex.querySelector('.d-flex')
            if(d_flex_d_flex.querySelector('.line-up') == null){
                let line_up = document.createElement('div')
                line_up.setAttribute('class', "line-up")
                d_flex_d_flex.appendChild(line_up)
            }
            if(d_flex_d_flex.querySelector('.line-50') == null){
                let line_50 = document.createElement('div')
                line_50.setAttribute('class', "line-50")
                d_flex_d_flex.appendChild(line_50)
            }  
            console.log("addLineComment end")
        },
        removeLineComment(cmt){
            let cmt_main = document.getElementById(cmt)
            let d_flex = cmt_main.querySelector('.d-flex')
            let d_flex_d_flex = d_flex.querySelector('.d-flex')
            let line_up = d_flex_d_flex.querySelector('.line-up')
            let line_50 = d_flex_d_flex.querySelector('.line-50')

            if(line_up != null){
                line_up.remove()
            }
            if(line_50 != null){
                line_50.remove()
            }

        },
        /* --------------- METHOD SHOW COMMENT CHILD OF COMMENT PARENT -------------- */
        async checkCommentChild(comment, level, comments) {
            console.log("check comment start")
            if (comments == null) {
                var comments = await this.getCommentChild(comment)
            }
            var len_comment =  comments.legnth
            let treeNode = document.getElementById(comment)
            const list_comment = treeNode.querySelectorAll('.comment-level')
            list_comment.forEach(c => c.remove());
            if (this.showComment.isShow[comment] == true) {
                let action_show = treeNode.querySelectorAll('.action-show')
                action_show.forEach(c => c.innerHTML = "Xem phản hồi");
                this.showComment.isShow[comment] = false
                this.removeLineComment(comment)
            }
            else {
                this.showComment.isShow[comment] = true;
                let treeNode = document.getElementById(comment)
                let treeNodeChild = treeNode.children[1]
                let action_show = treeNode.querySelectorAll('.action-show')
                action_show.forEach(c => c.innerHTML = "Ẩn phản hồi");
                let div_all_comments = document.createElement("div")
                console.log(treeNode)
                treeNode.insertBefore(div_all_comments, treeNodeChild);
                // treeNode.appendChild(div_all_comments);

                let level_comment = level + 1
                let class_level = "comment-level"
                let id_comment = 'id_comment-' + comment
                div_all_comments.setAttribute('class', "m4 " + class_level)
                div_all_comments.setAttribute('id', id_comment)
                
                this.addLineComment(comment)
                let  cmt_end 
                for (let index of comments) {
                    var div_current_comment = document.createElement("div")
                    div_current_comment.setAttribute('id', index.id)
                    div_current_comment.setAttribute('class', "position-relative")
                    
                    cmt_end = div_current_comment
                    let div_flex_1 = document.createElement("div")
                    div_flex_1.setAttribute('class', 'd-flex container-comment w-100')
                    div_current_comment.appendChild(div_flex_1)
                    let line_canvas = document.createElement('div')
                    line_canvas.setAttribute('class', "line-number-child-comment")
                    div_current_comment.appendChild(line_canvas)

                    let div_flex_1_1 = document.createElement("div")
                    div_flex_1_1.setAttribute('class', 'd-flex flex-column')

                    let div_line = document.createElement('div')
                    div_line.setAttribute('class', 'line-comment-child')
                    div_flex_1_1.appendChild(div_line)

                    let img_div_flex_2 = document.createElement("img")
                    img_div_flex_2.setAttribute('class', 'img-author-comment')
                    if(index.user_profile != null) {
                        img_div_flex_2.setAttribute('src', "http://127.0.0.1:8000/" + index.user_profile)

                    }else {
                        img_div_flex_2.setAttribute('src', "/src/assets/images/user.png")
                    }
                    img_div_flex_2.setAttribute('class', 'img-author-comment')
                    div_flex_1_1.appendChild(img_div_flex_2)

                    let div_flex_1_2 = document.createElement("div")
                    div_flex_1_2.setAttribute('class', 'd-flex flex-column content-comment')
                    div_flex_1_2.setAttribute('id', 'container-cmt-' + index.id)

                    let p_div_flex_1_2 = document.createElement("p")
                    p_div_flex_1_2.setAttribute('class', 'm-2 mt-3 p-2 px-4 bg-light rounded comment-blog')

                    let flex_div_flex_1_2 = document.createElement("div")
                    flex_div_flex_1_2.setAttribute('class', 'd-flex')

                    let p_flex_div_flex_1_2 = document.createElement("p")
                    p_flex_div_flex_1_2.setAttribute('class', 'mx-2 text-white show-reply')
                    let p_span_p_div_flex_1_2 = document.createElement("p")
                    p_span_p_div_flex_1_2.setAttribute('class', 'mx-2 text-white show-reply')

                    flex_div_flex_1_2.appendChild(p_span_p_div_flex_1_2)
                    flex_div_flex_1_2.appendChild(p_flex_div_flex_1_2)
                
                    let span_p_div_flex_1_2 = document.createElement("span")
                    p_span_p_div_flex_1_2.addEventListener('click', (event) => {
                        this.heartComment(index.id)
                    })
                    span_p_div_flex_1_2.setAttribute('class', 'me-1')
                    span_p_div_flex_1_2.setAttribute('id', 'number-heart-' + index.id)
                    if (index.status_heart_comment == false || index.status_heart_comment == null) {
                        span_p_div_flex_1_2.setAttribute('value', 0)
                    } else {
                        span_p_div_flex_1_2.setAttribute('value', 1)
                    }
                    span_p_div_flex_1_2.innerText = index.number_heart

                    let icon_p_div_flex_1_2 = document.createElement("i")
                    icon_p_div_flex_1_2.setAttribute('class', 'fa-solid fa-heart me-2')
                    let b_aft_i_p_div_flex_1_2 = document.createElement("b")
                    if (index.status_heart_comment == false || index.status_heart_comment == null) {
                        b_aft_i_p_div_flex_1_2.innerText = "Yêu thích"
                    } else {
                        b_aft_i_p_div_flex_1_2.innerText = "Đã Yêu thích"
                    }

                    b_aft_i_p_div_flex_1_2.setAttribute('id', 'heart-' + index.id)

                    p_span_p_div_flex_1_2.appendChild(span_p_div_flex_1_2)
                    p_span_p_div_flex_1_2.appendChild(icon_p_div_flex_1_2)
                    p_span_p_div_flex_1_2.appendChild(b_aft_i_p_div_flex_1_2)
                    // 

                    if (index.count_comment_child > 0) {
                        let b_aft_b_p_div_flex_1_2 = document.createElement("b")
                        b_aft_b_p_div_flex_1_2.setAttribute('class', 'ms-3 action-show')
                        b_aft_b_p_div_flex_1_2.innerText = "Xem " + index.count_comment_child + " phản hồi"
                        b_aft_b_p_div_flex_1_2.addEventListener('click', (event) => {
                            this.checkCommentChild(index.id,index.level , null)
                        })
                        p_flex_div_flex_1_2.appendChild(b_aft_b_p_div_flex_1_2)
                        this.showComment.isShow[index.id] = false
                    }

                    /* ----------------------------------- add ---------------------------------- */
                    let p_flex_div_flex_1_3 = document.createElement("div")
                    p_flex_div_flex_1_3.setAttribute('class', 'mx-2 text-white')
                    let icon_p_div_flex_1_3 = document.createElement("i")
                    icon_p_div_flex_1_3.setAttribute('class', 'fa-regular fa-comment me-2')
                    p_flex_div_flex_1_3.appendChild(icon_p_div_flex_1_3)

                    if (index.level < 6) {
                        let b_aft_b_p_div_flex_1_3 = document.createElement("b")
                        b_aft_b_p_div_flex_1_3.setAttribute('class', 'mx-2 text-white comment-reply')
                        b_aft_b_p_div_flex_1_3.innerText = "Trả lời"
                        b_aft_b_p_div_flex_1_3.addEventListener('click', (event) => {
                            this.CommentPost(index.id, index.user_email)
                        })
                        p_flex_div_flex_1_3.appendChild(b_aft_b_p_div_flex_1_3)
                    }
                    /* --------------------------------- end add -------------------------------- */
                    let p_p_div_flex_1_2 = document.createElement("p")
                    p_p_div_flex_1_2.setAttribute('class', 'text-user-email mb-1')

                    let i_p_p_div_flex_1_2 = document.createElement("i")
                    let i_b_p_p_div_flex_1_2 = document.createElement("b")
                    i_b_p_p_div_flex_1_2.innerText = index.user_email
                    i_p_p_div_flex_1_2.appendChild(i_b_p_p_div_flex_1_2)

                    let hr_p_div_flex_1_2 = document.createElement("hr")
                    hr_p_div_flex_1_2.setAttribute('class', 'my-1')

                    let p_p_p_div_flex_1_2 = document.createElement("p")
                    p_p_p_div_flex_1_2.setAttribute('class', 'm-0')
                    p_p_p_div_flex_1_2.setAttribute('id', 'content-cmt-' + index.id)
                    p_p_p_div_flex_1_2.innerText = index.content

                    let media_cmt = false
                    if(index.file_media_comment != null){
                        if(this.listMediaCommentChild.length == 0){
                            media_cmt = {
                                    id : index.id,
                                    file_media_comment : index.file_media_comment
                                }
                        }else {
                            this.listMediaCommentChild.filter( item => {
                                if(item.id != index.id){
                                    media_cmt = {
                                        id : index.id,
                                        file_media_comment : index.file_media_comment
                                    }
                                }
                            } )
                        }
                        if(media_cmt != false){
                            this.listMediaCommentChild.push(media_cmt)

                        }
                    }

                    let flex_div = document.createElement('div')
                    let flex_div_button = document.createElement('button')
                    flex_div_button.addEventListener('click', (event) => {
                        this.isShowOptionExpand(index.id, index.user_email, index.content)
                    })
                    flex_div_button.setAttribute('class', 'text-white btn-option-comment text-center position-relative mt-3')
                    let flex_div_button_p = document.createElement('p')
                    flex_div_button_p.innerText = "..."
                    flex_div_button_p.setAttribute('class', 'mb-2 text-absolute position-absolute')
                    flex_div_button.appendChild(flex_div_button_p)
                    flex_div.appendChild(flex_div_button)


                    var flex_flex_2_p = document.createElement('p')
                    flex_flex_2_p.setAttribute('class', 'text-white edit-text')
                    flex_flex_2_p.setAttribute('id', 'edit-datetime-' + index.id)
                    if (index.comment_is_edit != null) {
                        flex_flex_2_p.innerText = "Chỉnh sửa : " + this.converDatime(index.comment_is_edit)
                    } else {
                        flex_flex_2_p.innerText = "Ngày đăng : " + this.converDatime(index.date_create)
                    }

                    p_p_div_flex_1_2.appendChild(i_p_p_div_flex_1_2)
                    p_p_div_flex_1_2.appendChild(hr_p_div_flex_1_2)
                    p_p_div_flex_1_2.appendChild(p_p_p_div_flex_1_2)
                    p_div_flex_1_2.appendChild(p_p_div_flex_1_2)
                    div_flex_1_2.appendChild(p_div_flex_1_2)
                    div_flex_1_2.appendChild(flex_div_flex_1_2)
                    div_flex_1_2.appendChild(flex_flex_2_p)
                    div_flex_1_2.appendChild(p_flex_div_flex_1_3)
                    div_flex_1.appendChild(div_flex_1_1)
                    div_flex_1.appendChild(div_flex_1_2)
                    div_flex_1.appendChild(flex_div)
                    div_all_comments.appendChild(div_current_comment)
                }
                let line_canvas = cmt_end.querySelector('.line-number-child-comment')
                let img_au = cmt_end.querySelector('.img-author-comment')
                var style = window.getComputedStyle(img_au);

                var height = parseInt(style.getPropertyValue('height'));
                line_canvas.style.height = height/2 + this.expand_line_resize + "px"
            }
            console.log("check comment child end")
        },
        /* --------------------------- METHOD POST COMMENT -------------------------- */
        async PostComment() {
            console.log("PostComment start")
            if (this.contentPostComment != '' && this.blogId != false) {
                let content = this.contentPostComment
                let parent = this.commentSelected
                let blog_id = this.blogId
                await CommentAction.actionPostCommentBlog({
                    content: content,
                    parent: parent,
                    blog_id: blog_id,
                    files : this.fileUpload
                }).then(res => {
                    if (res.status == 200) {
                        delete this.showComment.value[parent]
                        if (parent != false) {
                            console.log("comment post with parent", res)
                            this.appendCommentNew(parent, res.comment.level, res.comment)
                            this.contentPostComment = ''
                            this.fileUpload = []
                        }
                        else {
                            console.log("comment post no parent", res)
                            this.comments.unshift(res.comment)
                            this.appendListMediaNew(res.comment.id,res.comment.file_media_comment)
                            this.contentPostComment = ''
                            this.fileUpload = []
                        }

                    }
                })
            }
            if (this.contentPostComment != '' && this.productSlug != false) {
                let content = this.contentPostComment
                let parent = this.commentSelected
                let product_slug = this.productSlug
                let infor_customer = null
                if(this.authenticated == false){
                    infor_customer = this.checkDataComment()
                    if(infor_customer == null){
                        return 
                    }
                }
                await CommentAction.actionPostCommentProduct({
                    content: content,
                    parent: parent,
                    product_slug: product_slug,
                    files : this.fileUpload,
                    infor_customer : infor_customer
                }).then(res => {
                    console.log("comment post", res)
                    if (res.status == 200) {
                        delete this.showComment.value[parent]
                        if (parent != false) {
                            this.appendCommentNew(parent, res.comment.level-1, [res.comment])
                            this.contentPostComment = ''
                            this.fileUpload = []
                        }
                        else {

                            this.comments = [res.comment,...this.comments]
                            this.contentPostComment = ''
                            this.fileUpload = []
                            document.getElementById('list-comment').scrollIntoView()
                        }

                    }
                })
            }
            console.log("PostComment end")

        },
        async upNumberCommentShow() {
            await CommentApiService.getCommentProduct({
                params : {
                product_slug : this.productSlug,
                start_limit : this.indexload,
                end_limit : this.number_comment_load,
                }
            }).then(response => {
                if(this.number_comment_load > response.data.comments.length){
                    this.comments  = [...this.comments,...response.data.comments]
                    this.isShowMoreComment = false
                }else {
                    this.indexload += this.number_comment_load
                    this.comments  = [...this.comments,...response.data.comments]
                    console.log("this.comments",this.comments)
                }
                
            })
        },
        isShowOptionExpand(cmt, email_user, content) {
            this.checkIsOptionExpandCmt()
            this.isOptionExpand = true;
            this.getObjectOptionExpand(cmt)
            this.$refs.optionExpandComment.checkAuthentication(email_user)
            this.$refs.optionExpandComment.initValue(cmt, content)
        },
        getObjectOptionExpand(cmt) {
            let objectOptionExpand = document.getElementById('option-expand-cmt')
            let object = document.getElementById(cmt)
            let subObj = object.querySelector(".d-flex");
            subObj.append(objectOptionExpand)
        },
        editComment(comment_id, content) {
            this.checkIsEditComment()
            this.CancelReplyComment()
            this.isEditComment = true
            this.$refs.editComment.initValue(comment_id, content)
            let objectOptionExpand = document.getElementById('edit-comment-object')
            let object = document.getElementById(comment_id)
            object.append(objectOptionExpand)
        },
        hideEditComment() {
            this.isEditComment = false
        },
        uploadEditComment(cmt, contentEdit, dateTimeEdit) {
            let commentEdit = document.getElementById("content-cmt-" + cmt)
            commentEdit.innerHTML = contentEdit
            let editDatime = document.getElementById('edit-datetime-' + cmt)
            if (editDatime != null) {
                editDatime.innerHTML = "Chỉnh sửa : " + this.converDatime(dateTimeEdit)
            } else {
                let containerCmt = document.getElementById('container-cmt-' + cmt)
                let beforeChild = containerCmt.children[2]
                let editDatimeNew = document.createElement('p')
                editDatimeNew.setAttribute('class', 'text-white')
                editDatimeNew.setAttribute('id', 'edit-datetime-' + cmt)
                editDatimeNew.innerHTML = "Chỉnh sửa : " + this.converDatime(dateTimeEdit)
                containerCmt.insertBefore(editDatimeNew, beforeChild);
            }
        },
        cancelEditComment() {
            let editComment = document.getElementById('edit-comment-object')
            let main = document.getElementById('layout-comment')
            let optionExpand = document.getElementById('option-expand-cmt')
            main.appendChild(editComment)
            main.appendChild(optionExpand)
        },
        deleteComment(cmt) {
            this.CancelReplyComment()
            this.cancelEditComment()
            
            this.comments = this.comments.filter( comment => {
                if(comment.id == cmt && comment.id > 0){
                    let commet_delete = document.getElementById(cmt)
                    commet_delete.remove()

                }
                return comment.id != cmt
            })
        },
        /* -------------------------- upload file selected -------------------------- */
        async uploadFile() {
            const files = this.$refs.imagePost.files
            for (let i = 0; i < files.length; i++) {
                const file = files[i]
                const dataUrl = await new Promise((resolve) => {
                    const reader = new FileReader()
                    reader.onload = () => resolve(reader.result)
                    reader.readAsDataURL(file)
                })

                if (file.type.startsWith('image/')) {
                    this.fileUpload.push({
                        data: dataUrl,
                        isImage: true,
                        isVideo: false
                    })
                }

                if (file.type.startsWith('video/')) {
                    this.fileUpload.push({
                        data: dataUrl,
                        isVideo: true,
                        isImage: false,
                        videoSrc: URL.createObjectURL(file)
                    })
                }
            }
        },
        removeFileUpload(index){
            this.fileUpload.splice(index, 1)
            console.log('this.fileUpload',index)
        },
        setPositionMedia(cmt){
            let cmt_main = document.getElementById(cmt)
            let d_flex = cmt_main.querySelector('.d-flex')
            let beforeChild = cmt_main.children[2]
            let media_cmt = document.getElementById("media-cmt-"+cmt)
            cmt_main.insertBefore(media_cmt, beforeChild);
        },
        checkDataComment(){
            const pattern = /^(\+84|0)\d{9}$/;
            if (pattern.test(this.inforCustomer.phoneNumber) == false
                || this.inforCustomer.phoneNumber == '') {
                this.inforCustomer.error.phoneNumber = true
            }else {
                this.inforCustomer.error.phoneNumber = false
            }
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
			if(emailRegex.test(this.inforCustomer.email) == false 
                || this.inforCustomer.email == ''){
				this.inforCustomer.error.email = true
			}else {
				this.inforCustomer.error.email = false
			}
            if(this.inforCustomer.name == ''){
                this.inforCustomer.error.name = true
            } else {
                this.inforCustomer.error.name = false
            }
            if(this.inforCustomer.sex == null ){
                this.inforCustomer.error.sex = true
            } else {
                this.inforCustomer.error.sex = false
            }
            if( 
                this.inforCustomer.error.phoneNumber == true
                || this.inforCustomer.error.name == true
                || this.inforCustomer.error.email == true
                || this.inforCustomer.error.sex == true
            ) return null
            let result = "phone: "+this.inforCustomer.phoneNumber + "\n"
                    + "email: "+ this.inforCustomer.email + "\n"
                    + "name: "+ this.inforCustomer.name + "\n"
                    + "sex: "+ this.inforCustomer.sex + "\n"
            return result
                    

        },
        checkIsComment(){
            if (document.getElementById('comment-user-blog') == null){
                document.getElementById('layout-comment').appendChild(this.commentComponent)
            }
        },
        checkIsOptionExpandCmt(){
            if(document.getElementById('option-expand-cmt') == null){
                document.getElementById('layout-option-expand').appendChild(this.optionExpandCmt)
            }
        },
        checkIsEditComment(){
            if(document.getElementById('edit-comment-object') == null){
                document.getElementById('layout-edit-comment').appendChild(
                    this.editCommentCoponent
                )
            }
        }
    },
    created() {
        this.profilePhoto = "http://127.0.0.1:8000" + this.getProfilePhoto
        this.comments = this.listComments
    },
    mounted(){
        this.commentComponent = document.getElementById('comment-user-blog')
        this.optionExpandCmt = document.getElementById('option-expand-cmt')
        this.editCommentCoponent = document.getElementById('edit-comment-object')
        if(window.innerWidth < 624) this.expand_line_resize = 26
        window.addEventListener('resize',() => {
            console.log('window.innerWidth',window.innerWidth)
            if(window.innerWidth < 624)
            this.expand_line_resize = 24
            else {
                this.expand_line_resize = 16
            }
        })
    }
}
</script>

<style>
.text-input-comment {
    border: none !important;
    padding: 5px 10px;
    margin-top: 15px;
}


.send-icon-comment {
    font-size: 1.5rem;
    color: white;
    cursor: pointer;
}

.comment-blog {
    width: fit-content;
    height: fit-content;
}

.img-author-comment {
    background-color: white;
    border-radius: 50%;
    width: 3rem;
    height: 3rem;
    margin: 1rem 1rem;
    margin-bottom: 0;
}

.show-reply:hover {
    cursor: pointer;
    text-decoration: underline;
}

.comment-reply:hover {
    cursor: pointer;
    text-decoration: underline;
}

.comment-level {
    margin-left: 5rem;
}

.comment-level-2 {
    margin-left: 10rem;
}

.text-user-email {
    color: rgba(19, 18, 18, 0.8);
}

.btn-more-comment {
    cursor: pointer;
}

.btn-more-comment:hover {
    text-decoration: underline;
}

.btn-option-comment {
    border: none;
    background-color: transparent;
    font-size: 30px;
}

.hide-option-expand {
    display: none;
}

.text-absolute {
    z-index: 999;
}
.cancel-btn {
    cursor:pointer;
}

@keyframes showActivate {
    0% {
        opacity: 1;
        display: block;
    }

    100% {
        opacity: 0;
        display: none;
    }
}

.show-option-expand {
    display: block;
    z-index: 999;
}

.item-slide-image {
    width: 9rem;
    height: auto;
    overflow: hidden;
}

.img-slide {
    height: 4rem;
    width: auto;
    margin: -2rem
}
#image-post {
    display:none;
}
.label-choose-file {
    cursor: pointer;
}
.boder-left-css {
    border :1px !important;
    border-left-style: dotted;
    border-left: thick rgb(255, 255, 255) !important;
}
.line-up{
    width:2px;
    height:100%;
    background-color: rgb(172, 171, 171);
    position:relative;
    left:50%;
}
.line-50{
    width:53%;
    height:3px;
    background-color: rgb(172, 171, 171);
    position:relative;
    left:50%;
}
.line-comment-child {
    width:1rem;
    height:3px;
    background-color: rgb(172, 171, 171);
    position:relative;
    top:2.5rem;
}
.line-number-child-comment {
    width:2px;
    height:100%;
    position:absolute;
    left:0%;
    top:0%;
    background-color: rgb(172, 171, 171);
}
.container-comment {
    width:100% !important;
    justify-content:flex-start !important;
}
@media only screen and (max-width: 624px)
{   
    .img-author-comment {
        width:35px;
        height:35px;
    }

  .text-user-email i b{
    font-size: 14px;
  }
  .layout-list-media {
    margin-left: 5px !important;
  }
  .comment-blog {
    padding:5px 10px !important;
  }
  .comment-blog  p {
    font-size: 13px;
  }
  .show-reply {
    font-size: 13px;
    width:100%;
  }
  .edit-text {
    font-size: 13px;
  }
  .comment-reply {
    width:100%;
  }
  .fa-comment {
    margin-left: 10px !important;
  }
  .comment-reply i b {
    font-size: 13px;
  }
  .svg-inline--fa  {
    font-size: 13px;
  }
  .comment-level {
    margin-left:4.2rem;
  }
  .layout-avatar {
    justify-content:start;
  }
  .content-comment {
    width:700px;
  }
  .text-reply {
    font-size: 13px;
    width: 100%;
  }
  .add-image-post {
    font-size: 13px;
  }
}
</style>