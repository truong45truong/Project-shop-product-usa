<template>
   <div class="d-flex flex-column align-items-center justify-content-center h-100 infor-item-box border border-2 w-100">
        <div class="h-100 d-flex flex-column align-items-center justify-content-center">
            <img class="img-product-item text-center" :src="'http://127.0.0.1:8000/'+`${photo}`" alt="name">
        </div>
        <div :class="[isShowDetail ? 'ribbon-hide' : 'ribbon']">
            <span>Sale 10%</span>
        </div>
        <div :class="[isShowDetail ? 'none-hover-border' : 'hover-border ']" @click="isShowProduct" @mouseover="isShowHoverPrice" @mouseleave="isNoneHoverPrice">

        </div>
        <div v-if="isShowDetail == true" class="info-product-item d-flex flex-column align-items-center justify-content-center" @click="isShowProduct">
            <div class="d-flex w-100 my-1">
                <div class="w-100"><p class="text-product-cart-inside-market text-white my-1 text-center bg-dark py-1">Tên : {{name}} vnđ</p></div>
            </div>
            <div class="d-flex w-100 my-1">
                <div class=" w-100"><p class="text-product-cart-inside-market text-white my-1 text-center bg-dark py-1">Giá : {{price}} vnđ</p></div>
            </div>
            <div class="d-flex w-100 my-1">
                <div class="w-100"><p class="text-product-cart-inside-market text-white my-1 text-center bg-dark py-1">Tổng : {{(100 - 10) / 100 * price}} vnđ</p></div>
            </div>
            <div class="w-100 d-flex justify-content-around">
                <button class="button-45 m-0"><p class="m-0 text-btn-product">Thêm vào Giỏ</p></button>
            </div>
        </div>
        <div class="d-flex align-items-center heart-content">
            <span class="text-btn-product fs-4 me-2"> {{hearts}}</span>
            <font-awesome-icon v-if="!status_heart" class="fs-4 my-2" icon="fa-regular fa-heart" />
            <font-awesome-icon v-if="status_heart" class="fs-4 my-2" icon="fa-solid fa-heart" />
        </div>
    </div>
</template>
  
<script>

export default ({
    name: 'ProductItem',
    props: {
        slug : false,
        name : false,
        descriptions : false,
        category : false,
        price : false,
        photo : false,
        status : false,
        hearts : false,
        status : false,
    },
    data: () => ({
        isShowDetail : false,
        isHoverPrice : false,
        status_heart : false,
    }),
    methods : {
        isShowProduct(){
            this.isShowDetail = !this.isShowDetail
        },
        isShowHoverPrice(){
            this.isHoverPrice = true;
        },
        isNoneHoverPrice(){
            this.isHoverPrice = false;
        }
    },
    created(){
        this.status_heart = this.status
    }
    
})
</script>
<style>
.img-product-item{
    width : 100%;
    height : auto;
}
@keyframes borderHover {
    from {
        border:100px solid rgba(0,0,0,0.1);
    }
  to {border:0px solid rgba(0,0,0,0.1)}
}
.none-hover-border {
    position:absolute;
    width:100%;
    height:100%;
}
.hover-border{
    position:absolute;
    top:0%;
    width:100%;
    height:100%;
}
.hover-border:hover {
    animation-name: borderHover;
    animation-duration: 0.5s;
}
@keyframes showDetailItem {
    from {
        top:0;
        right:-100%;
    }
  to {
    top:0;
    right:0%;}
}
.infor-item-box{
    position:relative;
    overflow: hidden;
}
.info-product-item{
    border:none;
    position:absolute;
    width:100%;
    height:100%;
    top:0%;
    right:0%;
    animation-name: showDetailItem;
    animation-duration: 0.5s;
}
.text-product{
    color:rgb(253, 249, 249);
    font-size:larger;
    font-weight: 800;
}
.text-btn-product{
    border:none;
}
.btn-product{
    background-color:brown !important;
    border-color: brown !important;
}
.icon-heart-product {
    color:brown
}
.text-price-product{
    font-size: 14px;
    font-weight: 300;
    margin: 3px 10px;
}
.none-hover-price {
    top:88%;
    left:5%;
}
.hover-price {
    top:80%;
    left:5%;
}
.price-product{
    position:absolute;
    width:fit-content;
    background-color: rgb(241, 236, 236);
}
.icon-item-heart-cart:hover {
    cursor:pointer;
}
.heart-content {
    position:absolute;
    top:0%;
    right:5%;
}
</style>
