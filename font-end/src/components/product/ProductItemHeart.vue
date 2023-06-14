<template> 
<div class="d-flex flex-column align-items-center justify-content-center h-100 infor-item-box border border-2 w-100 bg-white position-relative">
        <div class="h-100 d-flex flex-column align-items-center justify-content-center">
            <img class="img-product-item text-center" :src="'http://127.0.0.1:8000/'+`${photo}`" alt="name">
        </div>
        <div v-if="sale > 0" class="d-flex flex-column sale-product-category" :class="[isShowDetail ? 'ribbon-sale-hide' : 'ribbon-sale' ]">
            <div class="content-sale">
                <p class="m-0 text-content-sale">
                    <span>
                    <font-awesome-icon icon="fa-solid fa-bolt" class="text-danger" />
                    </span> <b>Giảm sốc</b>
                </p>
            </div>
            <div class="text-center">
                <p class="text-content-sale m-0">
                    <span class="text-danger"> lên tới </span>
                    <b class="ms-1">{{sale}} %</b>
                </p>
            </div>
        </div>
        <div :class="[isShowDetail ? 'none-hover-border' : 'hover-border ']" @click="isShowDetailProduct(true)" @mouseover="isShowHoverPrice" @mouseleave="isNoneHoverPrice">

        </div>
        <div class="infor-item-box d-flex flex-column align-items-center justify-content-center" 
            :class="[ isShowDetail ==true ? 'info-product' : isShowDetail == false ? 'hide-infor-product' : 'already-infor-product']"
         >
            <div class="btn-cancel-deltail" @click="isShowDetailProduct(false)">
                <font-awesome-icon icon="fa-solid fa-xmark" class="fs-4 text-dark" />
            </div>
            <div class="d-flex w-100 justify-content-between bg-dark">
                <div class="w-100 shadow"><p class="text-white text-fs-name my-1 text-center">{{name}}</p></div>
            </div>
            <div class="btn btn-dark mt-1" @click="removeHeart">
                <p>Xóa</p>
            </div>
            <div class="d-flex w-100 justify-content-between">
                <div class="mt-1 w-100">
                    <p class="text-price-item-heart my-1 text-center">
                    <span :class="[ sale > 0 ? 'price-no-sale ' : '']" >{{price}}</span>
                    <span v-if="sale > 0" class="ms-2 text-danger">{{Math.ceil((100 - sale) / 100 * price)}}</span> vnđ
                    </p>
                </div>
            </div>
            <a class="btn btn-dark btn-detail-item-heart d-block"  :href="'http://127.0.0.1:8080/product/' + slug"><p>Chi tiết</p></a>
        </div>
    </div>
</template>

<script>
import { mapGetters,mapActions } from 'vuex'
import { useRoute } from 'vue-router';
import { ProductAction} from './../../common/product.service'
export default ({
    name: 'ProductItemHeart',
    props: {
        slug : false,
        name : false,
        price : false,
        photo : false,
        sale : 0,
    },
    setup() {
        const route = useRoute();
        return { route };
    },
    data: () => ({
        isShowDetail : null,
        isHoverPrice : false,
        status_heart : false,
        numberHeart : false ,
        linkDetailProduct : '/'
    }),
    
    methods : {
        nextPageDetailProduct(){
            this.$router.push('/product/'+ this.slug)
        },
        isShowDetailProduct(status){
            this.isShowDetail = status
        },
        isShowHoverPrice(){
            this.isHoverPrice = true;
        },
        isNoneHoverPrice(){
            this.isHoverPrice = false;
        },
        async removeHeart(){
            this.$emit('deleteProductHeart',this.slug)
        }

    },
    created(){
        this.linkDetailProduct = "/product/" + this.slug
    }
    
})
</script>
<style>
.ribbon-sale {
    left : 0%;
    max-width: 100px;
}
.ribbon-sale-hide {
    max-width: 100px;
    left:-100% !important;
    animation-name: ribbonSaleHide;
    animation-duration: 0.5s;
    
}
.text-price-item-heart{
    position:absolute;
    padding: 2px 15px;
    background-color: white;
    bottom:5%;
    font-weight: 300;
    font-size: 16px;
}
.btn-detail-item-heart{
    position:absolute;
    bottom:5%;
    font-weight: 300;
    font-size: 16px;
    right:5%;
    cursor:pointer;
}
.btn-cancel-deltail {
    position:absolute ; 
    top:5%;
    right:5%;
    cursor:pointer;
}
@keyframes hideInforProduct {
    from {
        top:0%;
    }
  to {top:-100%;}
}
.hide-infor-product {
    border:none;
    position:absolute;
    top:-100%;  
    left:0;
    width:100%;
    height:100%;
    background-color: rgba(0, 0, 0, 0.1);
    animation-name: hideInforProduct;
    animation-duration: 0.5s;
}
.already-infor-product {
    position:absolute;
    top:-100%;  
    left:0;
}
.price-no-sale {
    text-decoration:line-through;
    font-weight: 300;
    color:rgb(105, 105, 105)
}
.text-fs-name {
    font-size: 16px;
}
@media only screen and (max-width: 424px) {

}
</style>