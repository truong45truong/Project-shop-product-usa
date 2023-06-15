<template>
    <div class="d-flex flex-column align-items-center justify-content-center h-100 infor-item-box border border-2 w-100">
        <div class="h-100 d-flex flex-column align-items-center justify-content-center">
            <img class="img-product-item text-center" :src="URL_PATH_SERVER + '/'+`${photo}`" alt="name">
        </div>
        <div :class="[isShowDetail ? 'none-hover-border' : 'hover-border ']" @click="isShowProduct" @mouseover="isShowHoverPrice" @mouseleave="isNoneHoverPrice">

        </div>
        <div :class="[isShowDetail ? 'ribbon-hide' : 'ribbon']">
            <span>Sale 10%</span>
        </div>
        <div v-if="isShowDetail == true" class="info-product infor-item-box d-flex flex-column align-items-center justify-content-center">
            <div class="btn-cancel-product-detail" @click="isShowProduct">
                <font-awesome-icon icon="fa-solid fa-xmark" class="fs-4 btn-cancel text-dark" />
            </div>
            <div class="d-flex w-100 justify-content-between">
                <div class="mt-1 w-100"><p class="text-product-cart-inside-market my-1 text-center">{{name}}</p></div>
                <div class="mt-1 w-100"><p class="text-product-cart-inside-market text-danger my-1 text-center">Sale: {{sale}} %</p></div>
            </div>
            <div class="d-flex w-100">
                <div class="mt-1 w-100"><p class="text-product-cart-inside-market my-1 text-center" v-if="numberProduct" >{{ numberProduct}}</p></div>
                <div class="mt-1 w-100"><p class="text-product-cart-inside-market text-dark my-1 text-center">Giá: {{price}} vnđ</p></div>
            </div>
            <div class="d-flex w-100" v-if="numberProduct" >
                <div class="mt-1 w-100"><p class="text-product-cart-inside-market text-white my-1 text-center bg-dark">Tổng : {{price * numberProduct}} vnđ</p></div>
            </div>
            <div class="w-100 d-flex justify-content-around">
                <button class="button-45 m-0"><p class="m-0 text-btn-product">Thêm vào giỏ</p></button>
                <button class="button-45 m-0"><p class="m-0 text-btn-product" @click="nextPageDetailProduct">Chi tiết</p></button>
            </div>
        </div>
    </div>
</template>
  
<script>
import { URL_PATH_SERVER } from '../../common/constants';
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
        sale: false
    },
    data: () => ({
        isShowDetail : false,
        isHoverPrice : false,
        status_heart : false,
        URL_PATH_SERVER : URL_PATH_SERVER ,
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
        },
        nextPageDetailProduct(){
            this.$router.push('/product/'+ this.slug)
        },
    },
    
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
.infor-item-box{
    position:relative;
    overflow: hidden;
}
.none-hover-border {
    position:absolute;
    width: calc(100% - 15px);
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
    width:100%;
    height:100%;
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
    left:-36%;
    background:#2980b9;
    transform: rotate(-45deg);
    animation-name: ribbonShow;
    animation-duration: 0.5s;
}
@keyframes ribbonHide {
    from {
        top:18%;
        left:-36%
    }
    to {
        top : 95%;
        left: -95%;
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
    animation-duration: .5s;
}
.ribbon-hide span ,
.ribbon span {
  position: absolute;
  display: block;
  width: 100%;
  padding: 5px 0;
  background-color: #3498db;
  box-shadow: 0 5px 10px rgba(0,0,0,.1);
  color: #fff;
  font: 700 14px/0.5vw 'Lato', sans-serif;
  font-size: 0.925vw;
  text-shadow: 0 1px 1px rgba(0,0,0,.2);
  text-transform: uppercase;
  text-align: center;
}

</style>
