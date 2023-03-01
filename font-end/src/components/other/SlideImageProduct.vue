<template>
     <div class="h-100 d-flex align-items-center justify-content-center layout-img-product shadow col-4" >
            <img v-for=" i in [1,2,3]" class="product-cart-img text-center" :src="'http://127.0.0.1:8000/' + `${photos}`" alt="name" @click="showDetail">
            <font-awesome-icon class="icon-prev-slide" icon="fa-solid fa-circle-chevron-left" />
            <font-awesome-icon class="icon-next-slide" icon="fa-solid fa-circle-chevron-right" />
    </div>
</template>
  
<script>
export default ({
    name: 'SlideImageProduct',
    props : {
        photos : []
    },
    computed: {
        
	},
    methods: {
        backNoticeCarefully() {
            this.cancelNotice
            this.hideNotice
        },
        acceptNoticeCarefully() {
            this.acceptNotice
            this.hideNotice
    
        }
    }
    
})
</script>
<style>
.icon-prev-slide {
    opacity:0.5;
    position:absolute;
    font-size: 20px;
    left:2%;
    cursor:pointer;
}
.icon-prev-slide:hover {
    opacity:1;
}
.icon-next-slide{
    opacity:0.5;
    position:absolute;
    font-size: 20px;
    right:2%;
    cursor:pointer;
}
.icon-next-slide:hover {
    opacity:1;
}
.product-cart-img {
    max-width: 7rem;
    position:absolute;
    max-height: 10rem;
}
.layout-img-product{
    min-width: 9rem;
    min-height: 9rem;
    background-color: #fff;
    border : 1px solid black;
    position:relative;
    top:25%;
    left:5%;
    overflow-x:hidden;
}
</style>