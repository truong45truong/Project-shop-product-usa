<template>
    <div class="d-flex flex-column">
        <img class="img-product-item" :src="'http://127.0.0.1:8000'+`${photo.data}`" alt="name">
    </div>
    <div v-if="isShowDetail == true" class="info-product d-flex flex-column align-items-center">
            <p class="text-product">{{name}}</p>
            <font-awesome-icon class="icon-heart-product fs-2 my-2" icon="fa-regular fa-heart" />
            <button class="btn btn-dark btn-product m-0"><p class="m-0 text-btn-product">Mua Ngay</p></button>
    </div>
    <div :class="[isShowDetail ? 'none-hover-border' : 'hover-border']" @click="isShowProduct" @mouseover="isShowHoverPrice" @mouseleave="isNoneHoverPrice">

    </div>
    <div class="price-product shadow-sm" :class="[isHoverPrice == false  ? 'none-hover-price' : 'hover-price']">
        <p class="text-price-product">{{price.price}} VNĐ</p>
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
        photo : false
    },
    data: () => ({
        isShowDetail : false,
        isHoverPrice : false,
    }),
    methods : {
        isShowProduct(){
            console.log(this.isShowDetail)
            this.isShowDetail = !this.isShowDetail
        },
        isShowHoverPrice(){
            this.isHoverPrice = true;
        },
        isNoneHoverPrice(){
            his.isHoverPrice = false;
        }
    },
    created(){
        console.log(this.photo)
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
    width:100%;
    height:100%;
}
.hover-border:hover {
    animation-name: borderHover;
    animation-duration: 0.5s;
}
@keyframes showDetail {
    from {
        top:-100%;
    }
  to {top:0%;}
}
.info-product{
    border:20px solid rgba(43, 26, 0, 0);
    position:absolute;
    overflow:hidden;
    width:100%;
    height:100%;
    background-color: rgba(43, 26, 0, 0.3);
    animation-name: showDetail;
    animation-duration: 0.5s;
}
.text-product{
    color:#F56A79;
    font-size:larger;
    font-weight: 800;
}
.text-btn-product{
    border:none;
}
.btn-product{
    background-color:#F56A79 !important;
    border-color: #F56A79 !important;
}
.icon-heart-product {
    color:#F56A79
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

</style>