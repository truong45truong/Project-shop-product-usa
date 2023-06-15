<template>
    <div class="d-flex flex-column align-items-center justify-content-between border content-product-category h-100 position-relative">
      <div v-if="sale > 0" class="d-flex flex-column sale-product-category">
        <div class="content-sale">
          <p class="m-0 text-content-sale">
             <span>
              <font-awesome-icon icon="fa-solid fa-bolt" class="text-danger" />
             </span> <b>Giảm giá</b></p>
        </div>
        <div class="text-center">
          <p class="text-content-sale m-0">
            <span class="text-danger"> lên tới </span>
            <b class="ms-1">{{sale}} %</b>
          </p>
        </div>
      </div>
      <img class="img-product-category text-center" :src="URL_PATH_SERVER + '/' + `${photo}`" alt="name">
      <div class="row">
        <div class="name-product-category">
                  <p class="text-dark mx-2 mb-3">
                      <b>{{ name }}</b>
                  </p>
              </div>
      </div>
      <div class="row">
        <div v-if="sale == 0" class="price-product-category position-relative my-1 ">
            <p class=" m-0 py-1 fw-light"><b>{{price_total }}</b> VNĐ</p>
        </div>
        <div v-if="sale > 0" class="d-flex align-items-center price-sale-product-category mb-2">
          <div class="content-sale">
            <p class="m-0 text-content-sale">
              <b class="text-price_product">{{price_product}} </b></p>
          </div>
          <div class="text-center">
            <p class="text-content-sale m-0">
              <b class="m-0 mx-1">{{price_total}} vnđ</b>
            </p>
          </div>
        </div>
      </div>
      <div class="row">
          <div class="col ">
            <div @click="nextPageDetailProduct" class="d-flex align-items-center btn-product-category  position-relative  mb-2">
              <div class=" layout-detail-card text-center d-flex align-items-center justify-content-center">
                <font-awesome-icon icon="fa-solid fa-angles-right" class="icon-detail-card text-center" />
              </div>
                <p class="m-0 position-absolution w-100 text-content-addcart">
                  <b class="ms-2">Xem chi tiết </b>
                </p>
            </div>
          </div>
      </div>
        <div class="row">
          <div class="col ">
            <div  @click="addToCart" class="d-flex align-items-center btn-product-category position-relative  mb-2">
              <div class=" layout-add-to-card text-center">
                <img class="img-add-to-card" src="./../../assets/icon/orange_shoppictbasket_1484336514.png_512.png" alt="">
              </div>
                <p class="m-0 position-absolution w-100 text-content-addcart">
                  <b>Thêm vào giỏ</b>
                </p>
            </div>
          </div>
        </div>
    </div>
</template>
  
<script>
import { mapGetters } from 'vuex'
import { URL_PATH_SERVER } from '../../common/constants';
export default ({
    name: 'ProductCategory',
    props: {
        photo: false,
        price: false,
        sale: false,
        name: false,
        slug : false,
    },
    components: {
    },
    filters: {
      formatNumber(price) {
        return new Intl.NumberFormat('vi-VN').format(price);
      }
    },
    data: () => ({
      price_total : 0,
      price_product : 0,
      URL_PATH_SERVER : URL_PATH_SERVER ,
    }),
    computed: {
		...mapGetters('auth', {
			get_user: 'currentUser',
			get_authenticated: 'isAuthenticated',
			get_error: 'errorAuthenticated'
		}),
	},
    methods: {
        nextPageDetailProduct(){
            this.$router.push('/product/'+ this.slug)
        },
        addToCart(){
            if (this.get_authenticated == false){
                this.$store.dispatch('auth/actionShowLogin')
            }else {
            this.$store.dispatch('cart/actionAddToCart', {
                    product_slug : this.slug
            })
            this.$store.dispatch('notice/actionTypeNotice',{content : 'Sản phẩm ' + this.name +' vừa dc thêm vào giỏ hàng',type : 'addtocart'})
            this.$store.dispatch('notice/activateShowMenu')
            }
      }
    },
    created() {
      this.price_total = Math.ceil((100 - this.sale) / 100 * this.price)
      this.price_total = new Intl.NumberFormat('vi-VN').format(this.price_total)
      this.price_product = new Intl.NumberFormat('vi-VN').format(this.price)
    }

})
</script>
<style lang="scss">
.img-product-category {
  height : 200px;
  z-index: -1;
}
.img-add-to-card {
  width:30px;
  height:30px;
  

}
.icon-detail-card {
  font-size: 20px !important;
  color:rgb(243, 124, 39);
}
.price-product-category {
    width: fit-content;
    background-color: rgba(190, 190, 190,0.55);
    border-radius: 12px;
    border: 0.5px solid rgb(161, 156, 149);
}
.price-product-category p {
  color:#391300
}
.content-product-category {
    flex-grow: 1 !important;
    height:auto;
    overflow:hiden;
}
.button-4 {
  appearance: none;
  background-color: #FAFBFC;
  border: 1px solid rgba(27, 31, 35, 0.15);
  border-radius: 6px;
  box-shadow: rgba(27, 31, 35, 0.04) 0 1px 0, rgba(255, 255, 255, 0.25) 0 1px 0 inset;
  box-sizing: border-box;
  color: #24292E;
  cursor: pointer;
  display: inline-block;
  font-family: -apple-system, system-ui, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
  font-size: 14px;
  font-weight: 500;
  line-height: 20px;
  list-style: none;
  padding: 6px 16px;
  position: relative;
  transition: background-color 0.2s cubic-bezier(0.3, 0, 0.5, 1);
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  vertical-align: middle;
  white-space: nowrap;
  word-wrap: break-word;
}

.button-4:hover {
  background-color: #F3F4F6;
  text-decoration: none;
  transition-duration: 0.1s;
}

.button-4:disabled {
  background-color: #FAFBFC;
  border-color: rgba(27, 31, 35, 0.15);
  color: #959DA5;
  cursor: default;
}

.button-4:active {
  background-color: #EDEFF2;
  box-shadow: rgba(225, 228, 232, 0.2) 0 1px 0 inset;
  transition: none 0s;
}

.button-4:focus {
  outline: 1px transparent;
}

.button-4:before {
  display: none;
}

.button-4:-webkit-details-marker {
  display: none;
}
.sale-product-category {
  position:absolute;
  right: 0%;
  border : 0.5px solid rgb(251, 192, 65)
}
.content-sale {
  background-color: rgb(251, 192, 65);
  padding:5px;
}
.text-content-sale {
  font-size: 15px;
}
.text-content-sale span {
  font-size: 12px;
}
.price-sale-product-category {
  padding : 0;
  border : 0.5px solid rgb(251, 192, 65)
}
.btn-cart-product-category {
  border :  0.5px solid black;
  padding:0;
}
.content-btn-add-cart {
  background-color:  black;
  height:100% !important;
}
.layout-add-to-card {
  width:60px !important;
  height: 40px !important;
  border : 3px solid rgb(244, 169, 8);
  background-color: white;
  border-radius: 50%;
}
.layout-detail-card {
  width:60px !important;
  height: 40px !important;
  background-color:white;
  border : 3px solid rgb(244, 169, 8);
  border-radius: 50%;
  z-index: 1;
  overflow:hidden;
}
.layout-detail-card .icon-detail-card {
  position:relative;
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
    transform: rotate(7deg);
  }
  50% {
    transform: rotate(-7deg);
  }
  100% {
    transform: rotate(10deg);
  }
}
@keyframes detailMoreRun {
  0% {
    left: -40%;
  }
  100% {
    left: 90%;;
  }
}
.btn-product-category:hover {
  .layout-add-to-card {
    -webkit-animation: 1.5s ease-in-out 0s normal none infinite running swing;
    -moz-animation: 1.5s ease-in-out 0s normal none infinite running swing;
    -o-animation: 1.5s ease-in-out 0s normal none infinite running swing;
    animation: 1.5s ease-in-out 0s normal none infinite running swing;
  }
  .layout-detail-card .icon-detail-card {
    animation: 1s ease-in-out 0s normal none infinite running detailMoreRun;
  }
}
.btn-product-category:active {
  .layout-add-to-card {
    box-shadow: 3px 3px 5px 6px #ccc;
  }
  .layout-detail-card .icon-detail-card {
    box-shadow: 3px 3px 5px 6px #ccc;
  }
}
.btn-product-category  {
  cursor:pointer;
}
.text-price_product {
  text-decoration: line-through;
}
.text-content-addcart {
  position:relative;
  height:fit-content;
  left:-10%;
  padding: 5px 15px ;
  padding-left: 25px;
  padding-right: 10px;
  font-size: 15px;
  color:rgb(39, 39, 39) !important;
  background-color: rgb(244, 169, 8);
  z-index: -1;
  border-radius:  0 15px 15px 0;
}
.text-detail-card {
  color: rgb(243, 124, 39);
}
@media only screen and (max-width: 1024px){
  .button-4  {
    font-size: 14px ;
  }
  .content-sale {
    background-color: rgb(251, 192, 65);
    padding:1px;
  }
  .text-content-sale {
    font-size: 10px;
  }
  .text-content-sale span {
    font-size: 10px;
  }
  .price-product-category p b {
    font-size: 10px;
  }
  .price-product-category {
    font-size: 10px;
  }
  .button-4 {
    padding: 3px;
    font-size: 12px;
  }
  .name-product-category {
    font-size: 13px;
  }
  .name-product-category .mb-3 {
    margin-bottom: 5px !important;
  }
}
@media only screen and (max-width: 624px) {


  .layout-add-to-card,
  .layout-detail-card {
    width:50px !important;
    height: 35px !important;
    border : 3px solid rgb(243, 124, 39);
  }
  .text-content-addcart {

    padding: 3px 10px ;
    padding-left: 20px;
    padding-right: 10px;
    font-size: 11px;
  }
  .img-add-to-card {
    width:25px !important;
    height:25px;
  }
  .button-4  {
    font-size: 14px ;
  }
  .content-sale {
    background-color: rgb(251, 192, 65);
    padding:1px;
  }
  .text-content-sale {
    font-size: 10px;
  }
  .text-content-sale span {
    font-size: 10px;
  }
  .price-product-category p b {
    font-size: 10px;
  }
  .price-product-category {
    font-size: 10px;
  }
  .button-4 {
    padding: 3px;
    font-size: 10px;
  }
  .name-product-category .mb-3 {
    margin-bottom: 5px !important;
  }
}
@media only screen and (max-width: 424px) {
  .button-4  {
    font-size: 11px ;
  }
  .content-sale {
    background-color: rgb(251, 192, 65);
    padding:1px;
  }
  .text-content-sale {
    font-size: 10px;
  }
  .text-content-sale span {
    font-size: 10px;
  }
  .price-product-category p b {
    font-size: 10px;
  }
  .button-4 {
    padding: 3px;
  }
  .name-product-category .mb-3 {
    margin-bottom: 5px !important;
  }
  .name-product-category {
    font-size: 10px;
  }
}
</style>