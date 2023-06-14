<template>
    <div class="layout-chatbox justify-content-end" :class="[ isShow == false ? '' : 'h-100 w-100 ' ]">
        <div v-if="isShow " class="cancel-show bg-white text-center" @click="hide">
            <b>
                <p>Trở về</p>
            </b>
        </div>
        <div v-if="isShow " class="container h-100 w-100">
            <div class="row">
                <div class="col-sm-6 bg-white p-2">
                    <div class="content-chat">
                        <div class="text-center">
                            Chat với hỗ trợ
                        </div>
                        <div class="d-flex">
                            <div class="d-flex flex-column me-3">
                                <img class="support-avt" src="./../../assets/images/support-chat.png" alt="">
                                <b>Hỗ trợ</b>
                            </div>
                            <div class="my-1">
                                <div class="content-support-text">
                                    <p class="m-0">Chào bạn</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="content-chat-support mt-2">
                        <textarea class="w-100"  placeholder="Nhập nội dung ..." ></textarea>
                    </div>
                </div>
                <div class="col-sm-6 bg-white p-2">
                    <div class="text-center">
                        <p>Tìm kiếm sản phẩm bằng hình ảnh</p>
                    </div>
                    <div class="d-flex px-3">
                        <label class="ms-2 label-choose-file align-items-center" for="image-post">
                            <i class="ms-5 add-image-post me-2">Thêm Ảnh/Video</i>
                            <font-awesome-icon icon="fa-regular fa-image" class="icon-image-post-blog fs-4" />
                            <input class="ms-1" type="file" id="image-post" ref="imagePost" name="filename" @change="uploadFile"
                             multiple />
                        </label>           
                    </div>
                    <div class="text-center mt-2">
                        <p>Tìm kiếm sản phẩm bằng Mô tả</p>
                        <div class="content-chat-support mt-2">
                            <textarea class="w-100"  placeholder="Nhập nội dung ..." ></textarea>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div v-if="isShow == false" class="btn-show-chatbox end shadow" @click="show">
            <div class="d-flex p-2 align-items-center">
                <font-awesome-icon class="text-white" icon="fa-solid fa-angle-up" />
                <p class=" ms-2 text-white m-0">
                     Hỗ trợ mua sắm
                </p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "ChatBoxLayout",
    props: {
        msg : ''
    },
    data : () => ({
        isShow :false,
    }),
    async created (){
    },
    methods : {
        show(){
            this.isShow = true;
        },
        hide (){
            this.isShow = false
        }
    }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.layout-chatbox {
    position:fixed;
    bottom : 0;
    z-index: 9999;
    background-color: rgba(12, 12, 12,0.4);
}
.btn-show-chatbox {
    cursor:pointer;
    right:0%;
    max-width: 200px;
    background-color: rgb(17, 17, 17);
}
.img-employee {
    max-width:200px;
}
.content-support-text{
    padding : 15px;
    border: 1px solid black;
    width:fit-content;
    border-radius: 20px;
}
.support-avt {
    max-width: 50px;
}
.label-choose-file {
    cursor: pointer;
}
#image-post {
    display:none;
}
</style>
