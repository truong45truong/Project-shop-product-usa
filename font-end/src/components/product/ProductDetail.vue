
<template>
    <div class="container detail-product position-relative">
        <div class="w-100 mt-5">
            <div class="bloc">
                <div class="esarfa text-center">
                    <h1>{{ data.name }}</h1>
                </div>
            </div>
        </div>
        <div class="row shadow position-relative">
            <div class="col-sm-4 position-relative">
                <img class="img-detail-product" :src="URL_PATH_SERVER + '/' + `${imgs[0]}`" alt="">
                <div v-if="data.sale > 0" class="promoribon"><br>
                  <img class="img-sale" src="./../../assets/images/sale-product-detail.png" alt="">
                  <p class="text-white m-0">Sale</p>
                  <p class="text-white m-0">
                      {{data.sale}}%
                  </p>
                </div>
                <ListImageProduct :dataImage="imgs" />
            </div>
            <div class="col">
                <div class="d-flex flex-column position-relative">
                  <div class="border p-3 flask-sale-content" v-if="data.sale > 0">
                      <div class="d-flex">
                        <font-awesome-icon icon="fa-solid fa-bolt" class="text-danger" />
                        <p class="ms-2">
                          Flask Sale Còn :
                        </p>
                      </div>
                      <CountDownFLashSale />
                    </div>
                    <p class="m-0 text-content-detail fs-5 text-dark mb-2">
                        Giá : 
                          <span :class="[ data.sale>0 ? 'price-sale' : '']" > {{ data.price }} </span>
                          <span class="ms-2 text-danger" v-if="data.sale > 0"> {{price_total}} </span>
                        vnđ
                    </p>
                    <p class="m-0 fs-5 text-content-detail text-dark mb-2"> Yêu thích : {{ data.count_heart }}
                        <span> <font-awesome-icon icon="fa-solid fa-heart" class="fs-4" /> </span>
                    </p>
                    <div class="d-flex flex-column mb-4">
                        <p class="m-0 text-content-detail fs-5 text-dark mb-2">Mã giảm giá áp dụng cho sản phẩm</p>
                        <div class="btn-select-voucher d-flex justify-content-between py-2 px-4" @click="showSelectedVoucher">
                            <p class="m-0 text-white">Chọn Mã</p>
                            <font-awesome-icon icon="fa-solid fa-angle-down" class="m-0 text-white" />
                        </div>
                        <div v-if="isShowSelectedVoucher" class="content-selected-voucher d-flex flex-column">
                          <div class="mx-3 d-flex align-items-center justify-content-between">
                            <input type="radio">
                            <p class="m-0 me-1 text-white">Giảm 15 k</p>
                          </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="layout-action mt-5 pb-3">
          <div class="row">
            <div class="col-sm-6 mt-3 d-flex flex-column">
              <button class="button-48 m-auto" @click="addToCart">
                <span class="text"> Thêm vào giỏ hàng</span>
              </button>
            </div>
            <div class="col-sm-6 mt-3 d-flex flex-column">
              <button class="button-48 m-auto" @click="nextCheckout">
                <span class="text"> Mua Ngay</span>
              </button>
            </div>
          </div>
        </div>
        <div  class="border mt-5" 
        >
          <div class="row content-descript"
          :class="[ checkShowMoreDescribe == false ? ''  :  showMoreDescribe ? 'more-expand' : 'more-hide' ]" 
          >
            <h4 class="mb-3 mt-1">Mô tả sản phẩm </h4>
            <p class="text-dark text-descript">{{data.description}}</p>
          </div>
          <div v-if="checkShowMoreDescribe" class="bg-dark mt-2 text-center" 
            @click="isShowMoreDecribe"
          >
              <p class="text-white m-0 py-2">Xem thêm
                <font-awesome-icon class="text-" icon="fa-solid fa-angle-down" />
              </p>
          </div>
        </div>
        <div v-if="isLoadComment" class="mt-5 bg-dark shadow">
          <list-comment :listComments= "list_comment" :blogId = "false" :productSlug="route.params.slug" />
        </div>
        <div class="mt-5">
          <!-- <list-blog :product_slug="route.params.slug"/> -->
        </div>
    </div>
</template>
  
<script>
import { useRoute } from 'vue-router';
import { mapGetters } from 'vuex'
import { ProductApiService } from './../../common/product.service'
import {CommentApiService} from './../../common/comment.service'
import CountDownFLashSale from './../other/CountDowmFLashSale.vue'
import ListComment from './../../layout/blog/ListComment.vue'
import ListBlog from './../../layout/blog/ListBlog.vue'
import lzwCompress from 'lzwcompress';
import ListImageProduct from './ListImageProduct.vue'
import { URL_PATH_SERVER } from '../../common/constants';
export default {
    name: "DetailProduct",
    setup() {
        const route = useRoute();
        return { route };
    },
    watch:{
      $route (to, from) {
        (async () => {
          try {
            const response = await ProductApiService.get({
              params: {
                product_slug: this.route.params.slug
              }
            });
            console.log(response);
            this.data = response.data.products[0];
          } catch (error) {
            console.log(error);
          }
        })();
      }
    } ,
    data: () => ({
        data: '',
        isShowSelectedVoucher : false,
        list_comment : false,
        isLoadComment : false,
        checkShowMoreDescribe : false,
        showMoreDescribe : false,
        price_total : 0,
        imgs : '',
        URL_PATH_SERVER : URL_PATH_SERVER ,
    }),
    async created() {
      await ProductApiService.get({
          params: {
              product_slug: this.route.params.slug
          }
      }).then(res => {
          console.log(res)
          this.data = res.data.products[0]
          this.imgs = res.data.products[0].file_media_product.split(',')
      })
      await CommentApiService.getCommentProduct({
        params : {
          product_slug : this.route.params.slug,
          start_limit : 0,
          end_limit : 4,
        }
      }).then(response => {
        console.log('response comment',response)
        this.list_comment = response.data.comments
        this.isLoadComment = true
      })
      this.price_total = Math.ceil((100 - this.data.sale) / 100 * this.data.price)
      this.price_total = new Intl.NumberFormat('vi-VN').format(this.price_total)
    },
    mounted()
    {
      if(window.innerWidth < 624){
        this.checkShowMoreDescribe = true
      }
      window.scrollTo(0, 0);
    },
    components: {
      CountDownFLashSale,
      ListBlog,
      ListComment,
      ListImageProduct
    },
    computed: {
        ...mapGetters('notice', {
            get_is_activate: 'isActivate',
        }),
        ...mapGetters('auth', {
			    get_authenticated: 'isAuthenticated',
		    }),
    },
    methods: {
      showSelectedVoucher(){
        this.isShowSelectedVoucher = !this.isShowSelectedVoucher
      },
      addToCart(){
        if (this.get_authenticated == false){
          this.$emit('login')
        }else {
          this.$store.dispatch('cart/actionAddToCart', {
                product_slug : this.route.params.slug
           })
           this.$store.dispatch('notice/actionTypeNotice',{content : 'Sản phẩm ' + this.data.name +' vừa dc thêm vào giỏ hàng',type : 'addtocart'})
          this.$store.dispatch('notice/activateShowMenu')
        }
      },
      isShowMoreDecribe(){
        this.showMoreDescribe = ! this.showMoreDescribe
      },
      nextCheckout(){
        let inf = JSON.stringify({
          product : {
            slug : this.route.params.slug,
            quantity : 1
          },
        })
        console.log(String(lzwCompress.pack(inf)), this.route.params.slug)
      }
    }
}
</script>
<style lang="scss">
.layout-action {
  background: #333;
}
@keyframes animationSaleDetail {
    from {
        transform: rotate(-20deg) scale(1);
    }

    to {
        transform: rotate(-20deg) scale(1.1);
    }
}

.sale-detail {
    background-color: rgb(211, 71, 71);
}

.bloc {
    width: 100%;
    margin: auto;
}

.esarfa {
    width: 100%;
    background: #333;
    color: #fff;
    position: relative;
    padding: 0 2em;
}

.esarfa:after,
.esarfa:before {
    content: "";
    display: block;
    position: absolute;
    width: 0;
    height: 0;
    top: 100%;
    border-top: 1em solid #999;
    border-right: 1em solid transparent;
    border-left: 1em solid transparent;
    border-bottom: 1em solid transparent;
}

.esarfa:before {
    left: 0;
    border-right: 1em solid #999;
}

.esarfa:after {
    right: 0;
    border-left: 1em solid #999;
}
.flask-sale-content {
  width:fit-content;
}
.detail-product .row {
    margin: 0vw 2rem;
}

.img-detail-product {
    max-width: 100%;
}

.promoribon {
  position:absolute;
  top:0%;
    left:5%;
  width: 65px;
  height:65px;
  -webkit-animation: 3s ease-in-out 0s normal none infinite running swing;
  -moz-animation: 3s ease-in-out 0s normal none infinite running swing;
  -o-animation: 3s ease-in-out 0s normal none infinite running swing;
  animation: 3s ease-in-out 0s normal none infinite running swing;
  -webkit-transform-origin: 100px -71px;
  -moz-transform-origin: 100px -71px;
  -o-transform-origin: 100px -71px;
  transform-origin: 100px -71px;
}
.img-sale {
    position:absolute;
    width:65px;
    height:auto;
}
.promoribon p {
    position:relative;
    top:10%;
    left:25%;
    font-size: 16px;
    font-weight: 600;
}
.btn-select-voucher{
  background-color: #16a085;
  width:200px;
  cursor:pointer;
}
.content-selected-voucher {
  background-color: #227e6b;
  width:200px;
}

.promoribon:after {
  content: '';
  position: absolute;
  top: -80%;
  right:50%;
  width: 2px;
  height: 81px;
  border-radius: 0%;
  background: rgb(255, 94, 0);
  z-index: -99;
}

@-webkit-keyframes swing {
  0% {
    -webkit-transform: rotate(5deg);
  }
  50% {
    -webkit-transform: rotate(-5deg);
  }
  100% {
    -webkit-transform: rotate(5deg);
  }
}

@-moz-keyframes swing {
  0% {
    -moz-transform: rotate(5deg);
  }
  50% {
    -moz-transform: rotate(-5deg);
  }
  100% {
    -moz-transform: rotate(5deg);
  }
}

@-o-keyframes swing {
  0% {
    -o-transform: rotate(5deg);
  }
  50% {
    -o-transform: rotate(-5deg);
  }
  100% {
    -o-transform: rotate(5deg);
  }
}

@keyframes swing {
  0% {
    transform: rotate(5deg);
  }
  50% {
    transform: rotate(-5deg);
  }
  100% {
    transform: rotate(5deg);
  }
}

/* CSS */
.button-48 {
  width:200px;
  appearance: none;
  background-color: #FFFFFF;
  border-width: 0;
  box-sizing: border-box;
  color: #000000;
  cursor: pointer;
  display: inline-block;
  font-family: Clarkson,Helvetica,sans-serif;
  font-size: 14px;
  font-weight: 500;
  letter-spacing: 0;
  line-height: 1em;
  margin: 0;
  opacity: 1;
  outline: 0;
  padding: 1.5em 2.2em;
  position: relative;
  text-align: center;
  text-decoration: none;
  text-rendering: geometricprecision;
  text-transform: uppercase;
  transition: opacity 300ms cubic-bezier(.694, 0, 0.335, 1),background-color 100ms cubic-bezier(.694, 0, 0.335, 1),color 100ms cubic-bezier(.694, 0, 0.335, 1);
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  vertical-align: baseline;
  white-space: nowrap;
}

.button-48:before {
  animation: opacityFallbackOut .5s step-end forwards;
  backface-visibility: hidden;
  background-color: #EBEBEB;
  clip-path: polygon(-1% 0, 0 0, -25% 100%, -1% 100%);
  content: "";
  height: 100%;
  left: 0;
  position: absolute;
  top: 0;
  transform: translateZ(0);
  transition: clip-path .5s cubic-bezier(.165, 0.84, 0.44, 1), -webkit-clip-path .5s cubic-bezier(.165, 0.84, 0.44, 1);
  width: 100%;
}

.button-48:hover:before {
  animation: opacityFallbackIn 0s step-start forwards;
  clip-path: polygon(0 0, 101% 0, 101% 101%, 0 101%);
}

.button-48:after {
  background-color: #FFFFFF;
}

.button-48 span {
  z-index: 1;
  position: relative;
}
.price-sale {
  text-decoration: line-through;
  color:rgb(105, 105, 105);
  font-weight:300;
}
.text-descript {
  white-space: pre-wrap !important;
}
.content-descript {
  white-space: wrap;
  overflow: hidden;
  text-overflow: ellipsis; 
}
.more-hide {
  height:250px;
}
.more-expand {
  height:auto;
}
@media only screen and (max-width: 424px) {
  .button-48 span.text {
    font-size: 11px !important;
  }
  .button-48 {
    width:140px;
    height:20px;  
  }
  .esarfa {
    padding : 0 1rem;
  }
  .esarfa:after,
  .esarfa:before {
      content: "";
      display: block;
      position: absolute;
      width: 0;
      height: 0;
      top: 100%;
      border-top: 0.75em solid #999;
      border-right: 0.75em solid transparent;
      border-left: 0.75em solid transparent;
      border-bottom: 0.75em solid transparent;
  }

  .esarfa:before {
      left: 0;
      border-right: 0.2em solid #999;
  }

  .esarfa:after {
      right: 0;
      border-left: 0.2em solid #999;
  }
  .esarfa h1{
    font-size: 13px;
  }
  .img-sale {
    width:50px;
  }
  .promoribon{
    top:15%;
  }
  .promoribon::after {
    left:35%;
  }
  .text-content-detail,
  .text-content-detail span svg {
      font-size: 12px !important;
  }
  .flask-sale-content {
    padding:10px !important;
    margin-bottom: 10px;
  }
  .detail-product .row {
    margin: 0  1rem;
  }
}
</style>