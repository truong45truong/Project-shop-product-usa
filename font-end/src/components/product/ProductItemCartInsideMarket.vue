<template>
    <div class="d-flex flex-column align-items-center justify-content-center h-100 infor-item-box">
        <div class="h-100 d-flex flex-column align-items-center justify-content-center">
            <img class="img-product-item text-center" :src="'http://127.0.0.1:8000'+`${photo.data}`" alt="name">
        </div>
        <div :class="[isShowDetail ? 'ribbon-hide' : 'ribbon']">
            <span>Sale 10%</span>
        </div>
    </div>
    <div v-if="isShowDetail == true" class=" info-product infor-item-box d-flex flex-column align-items-start" @click="isShowProduct">
            <div class="d-flex w-100 justify-content-between">
                <div class="mt-1 w-100"><p class="text-product-cart-inside-market my-1 text-center">{{name}}</p></div>
                <div class="mt-1 w-100"><p class="text-product-cart-inside-market text-danger my-1 text-center">Sale: {{price.sale}} %</p></div>
            </div>
            <div class="d-flex w-100">
                <div class="mt-1 w-100"><p class="text-product-cart-inside-market my-1 text-center">{{ numberProduct}}</p></div>
                <div class="mt-1 w-100"><p class="text-product-cart-inside-market text-dark my-1 text-center">Giá: {{price.price}} vnđ</p></div>
            </div>
            <div class="d-flex w-100">
                <div class="mt-1 w-100"><p class="text-product-cart-inside-market text-white my-1 text-center bg-dark">Tổng : {{price.price * numberProduct}} vnđ</p></div>
            </div>
            <div class="w-100 d-flex justify-content-around">
                <font-awesome-icon class="icon-item-heart-cart fs-2 my-2" icon="fa-regular fa-heart" />
                <button class="button-45 m-0"><p class="m-0 text-btn-product">Xóa</p></button>
            </div>
    </div>
    <div :class="[isShowDetail ? 'none-hover-border' : 'hover-border ']" @click="isShowProduct" @mouseover="isShowHoverPrice" @mouseleave="isNoneHoverPrice">

    </div>
</template>
  
<script>

export default ({
    name: 'ProductItemCartInsideMarket',
    props: {
        slug : false,
        name : false,
        descriptions : false,
        category : false,
        price : false,
        photo : false,
        numberProduct : 1,
    },
    data: () => ({
        isShowDetail : false,
        isHoverPrice : false,
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
        const image = document.getElementsByClassName("img-product-item");
        //image.style.filter = "brightness(0)";
    }
    
})
</script>
<style>
.img-product-item{
    width : 75%;
    height : auto;
}
@keyframes borderHover {
    from {
        border:60px solid rgba(0,0,0,0.2);
    }
  to {border:0px solid rgba(0,0,0,0.01)}
}
.none-hover-border {
    position:absolute;
    width:100%;
    height:100%;
}
.hover-border{
    top:0;
    left:0;
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
    border:none;
    position:absolute;
    top:0;
    left:0;
    background-color: rgba(0, 0, 0, 0.1);
    animation-name: showDetail;
    animation-duration: 0.5s;
}
.text-product-cart-inside-market {
    font-weight : 450;
    color:rgb(221, 122, 0);
}
@keyframes ribbonShow {
    from {
        top:-100%;
        left : 50%;
    }
  to {top:18%;}
}
.ribbon {
    width:100%;
    position: absolute;
    top:18%;
    left:-30%;
    background:#2980b9;
    transform: rotate(-45deg);
    animation-name: ribbonShow;
    animation-duration: 0.5s;
}
@keyframes ribbonHide {
    from {
        top:-30%;
    }
    to {
        top : -100%;
    }
}
.ribbon-hide {
    width:100%;
    position: absolute;
    top:-100%;
    left:-30%;
    background:#2980b9;
    transform: rotate(-45deg);
    animation-name: ribbonHide;
    animation-duration: 0.5s;
}
.ribbon span {
  position: absolute;
  display: block;
  width: 225px;
  padding: 5px 0;
  background-color: #3498db;
  box-shadow: 0 5px 10px rgba(0,0,0,.1);
  color: #fff;
  font: 700 14px/1 'Lato', sans-serif;
  text-shadow: 0 1px 1px rgba(0,0,0,.2);
  text-transform: uppercase;
  text-align: center;
}
.ribbon::before,
.ribbon::after {
  position: absolute;
  top:0;
  left:0;
  z-index: 19999;
  content: '';
  display: block;
  border: 5px solid #2980b9;
}

</style>
