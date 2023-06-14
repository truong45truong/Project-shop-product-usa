<template>
    <div class="">
        <div class="row d-flex">
            <div class="col-sm-6 text-center">
                <h5 class="text-white tilte-text mb-3 me-2">Về chúng tôi</h5>
                <div class="d-flex flex-column align-items-start justify-content-between px-5">
                    <p class="text-white title-name m-0 me-2 w-100 text-center">Giấy tờ pháp lí kinh doanh</p>
                    <p class="text-white title-name m-0 me-2 w-100 text-center">Lịch sử thành lập</p>
                    <p class="text-white title-name m-0 me-2 w-100 text-center">Nguồn cung cấp hàng hóa</p>
                </div>
            </div>
            <div class="col-sm-6 text-center">
                <h5 class="text-white tilte-text mb-3 me-2">Đảm Bảo</h5>
                <div class="d-flex flex-column align-items-start justify-content-between px-5">
                    <p class="text-white title-name m-0 me-2 w-100 text-center">Sản phẩm</p>
                    <p class="text-white title-name m-0 me-2 w-100 text-center">Chất lượng sản phẩm</p>
                    <p class="text-white title-name m-0 me-2 w-100 text-center">Nhà cung cấp uy tín</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: "IntroduceLayout",
    props: {
        msg: String,
    },
    data : () => ({
        listCateogry : false,
        isShowChild : []
    }),
    async created (){
    },
    methods : {

    }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>S
.title-name{
    word-wrap: none !important;
}
.title-name:hover {
    color: rgb(14, 14, 85) !important;
    cursor:pointer;
}
@keyframes showdowncategory {
    from {
        top:0%
    }
  to {top: 32%;}
}
@keyframes showActionExpandLine {
    from {
        width: 0%;
    }
    to {
        width: 100%;
    }
}
.activate-animation {
    position:absolute;
    top:32%;
    animation-name: showdowncategory;
    animation-duration: 0.5s;
}
@keyframes xoayvong {
  from {
    -webkit-transform:rotate(0deg);
    -moz-transform:rotate(0deg);
    -o-transform:rotate(0deg);
  }
  to {
    -webkit-transform:rotate(360deg);
    -moz-transform:rotate(360deg);
    -o-transform:rotate(360deg);
  }
}
.icon-expand{
    font-size: 14px !important;
    cursor: pointer;
}
.icon-expand:hover {
    animation-name: xoayvong;
    animation-duration: 0.5s;
}
.hr-category{
    width:100%;
    height:2px;
    background-color: white;
}
.activate-expand {
    display :block;
    animation-name: showActionExpandLine;
    animation-duration: 0.5s;
}
.non-activate-expand{
    display:none;
}
</style>
