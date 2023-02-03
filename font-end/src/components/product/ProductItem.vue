<template>
    <div class="d-flex flex-column">
        <img class="img-product-item" :src="'http://127.0.0.1:8000'+`${photo.data}`" alt="name">
    </div>
    <div v-if="isShowDetail == true" class="info-product d-flex flex-column align-items-start">
            <div class="d-flex w-100 card-sale">
                <div class="triangle_left"></div>
                <div class="rectangle mt-3"><p class="text-product my-1">{{name}}</p></div>
                <div class="pacman mt-3"></div>
            </div>
            <div class="d-flex w-100 card-price">
                <div class="triangle_left"></div>
                <div class="rectangle mt-3"><p class="text-product my-1">{{price.price}} VNĐ</p></div>
                <div class="pacman mt-3"></div>
            </div>
            <font-awesome-icon class="icon-heart-product fs-2 my-2" icon="fa-regular fa-heart" />
            <button class="btn btn-dark btn-product m-0"><p class="m-0 text-btn-product">Mua Ngay</p></button>
    </div>
    <div :class="[isShowDetail ? 'none-hover-border' : 'hover-border ']" @click="isShowProduct" @mouseover="isShowHoverPrice" @mouseleave="isNoneHoverPrice">

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
            this.isHoverPrice = false;
        }
    },
    created(){
        console.log(this.photo)
        const image = document.getElementsByClassName("img-product-item");
        //image.style.filter = "brightness(0)";
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
    border:none;
    position:absolute;
    width:100%;
    height:100%;
    background-color: rgba(0, 0, 0, 0.3);
    animation-name: showDetail;
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
.rectangle {
    position:relative;
    width: 40%;
    height:fit-content;
    background: brown;
}
.triangle_left {
    position:absolute;
    top:30%;
    left : -12.4%;
    border-top: 1.563rem solid transparent;
    border-right: 2.5rem solid brown;
    border-bottom: 1.563rem solid transparent;
    z-index:-1;
}
.pacman {
    height:35px;
    border-right: 0.813rem solid transparent;
    border-top: 1.156rem solid brown;
    border-left: 0.813rem solid brown;
    border-bottom: 1.156rem solid brown;
}
.card-sale {
    position:relative;
}
.card-price {
    position:relative;
}
.card-price .pacman {
    border-top: 1.156rem solid rgb(16, 167, 187);
    border-left: 0.813rem solid rgb(16, 167, 187);
    border-bottom: 1.156rem solid rgb(16, 167, 187);
}
.card-price .rectangle {
    background :  rgb(16, 167, 187);
}
.card-price .triangle_left {
    border-right: 2.5rem solid  rgb(16, 167, 187);;
}
</style>


<!-- /* CSS */
.button-56 {
  align-items: center;
  background-color: #fee6e3;
  border: 2px solid #111;
  border-radius: 8px;
  box-sizing: border-box;
  color: #111;
  cursor: pointer;
  display: flex;
  font-family: Inter,sans-serif;
  font-size: 16px;
  height: 48px;
  justify-content: center;
  line-height: 24px;
  max-width: 100%;
  padding: 0 25px;
  position: relative;
  text-align: center;
  text-decoration: none;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
}

.button-56:after {
  background-color: #111;
  border-radius: 8px;
  content: "";
  display: block;
  height: 48px;
  left: 0;
  width: 100%;
  position: absolute;
  top: -2px;
  transform: translate(8px, 8px);
  transition: transform .2s ease-out;
  z-index: -1;
}

.button-56:hover:after {
  transform: translate(0, 0);
}

.button-56:active {
  background-color: #ffdeda;
  outline: 0;
}

.button-56:hover {
  outline: 0;
}

@media (min-width: 768px) {
  .button-56 {
    padding: 0 40px;
  }
} -->