<template>
    <div class="row d-flex">
        <div class="col-sm-3 text-center">
            <h5 class="text-white mb-3 me-2">Instagram</h5>
            <div class="d-flex flex-column align-items-start justify-content-between px-5">
                <p class="text-white title-name m-0 me-2 w-100 text-center">
                    <font-awesome-icon icon="fa-brands fa-instagram" />
                    <span class="ms-2">shop.katie.usa</span>
                </p>
            </div>
        </div>
        <div class="col-sm-3 text-center">
            <h5 class="text-white mb-3 me-2">Twitter</h5>
            <div class="d-flex flex-column align-items-start justify-content-between px-5">
                <p class="text-white title-name m-0 me-2 w-100 text-center">
                    <font-awesome-icon icon="fa-brands fa-twitter" />
                    katieshop.economic@gmail.com
                </p>
            </div>
        </div>
        <div class="col-sm-3 text-center">
            <h5 class="text-white mb-3 me-2">Facebook</h5>
            <div class="d-flex flex-column align-items-start justify-content-between px-5">
                <p class="text-white title-name m-0 me-2 w-100 text-center">
                    <font-awesome-icon icon="fa-brands fa-facebook" />
                    https://www.facebook.com/kateshopusa
                </p>
            </div>
        </div>
        <div class="col-sm-3 text-center">
            <h5 class="text-white mb-3 me-2">Group blog</h5>
            <div class="d-flex flex-column align-items-start justify-content-between px-5">
                <p class="text-white title-name m-0 me-2 w-100 text-center">
                    <font-awesome-icon icon="fa-solid fa-blog" />
                    <span class="ms-2">blogkatieshop.com</span>
                </p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "FollowLayout",
    props: {
        msg : ''
    },
    data : () => ({
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
