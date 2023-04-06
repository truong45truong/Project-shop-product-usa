<template>
    <div class="d-flex flex-column align-items-center justify-content-between border content-product-category h-100 ">
        <img class="img-product-item text-center" :src="'http://127.0.0.1:8000/' + `${photo}`" alt="name">
        <div class="row">
            <div class="col-sm-6">
                <div class="name-product-category">
                    <p class="text-dark mx-2 mb-3">
                        <b>{{ name }}</b>
                    </p>
                </div>
                <div class="price-product-category mx-2">
                    <p class="text-dark m-0 py-1 px-2 fw-light mb-2">{{ price }} VNĐ</p>
                </div>
                <div class="">
                    <p class="mx-2">
                        Yêu thích
                        <font-awesome-icon icon="fa-regular fa-heart" />
                    </p>
                </div>
                <div class="">
                    <p class="mx-2">
                        Sô lượng Yêu thích 3
                        <font-awesome-icon icon="fa-regular fa-heart" />
                    </p>
                </div>
            </div>
            <div class="col-sm-6">
                <button class="mb-2  button-4" @click="nextPageDetailProduct">
                    Xem chi tiết
                </button>
                <button class="mb-2  button-4" @click="addToCart">
                    Thêm vào giỏ
                </button>
                <button class="mb-2  button-4">
                    Mua ngay
                </button>
            </div>
        </div>
    </div>
</template>
  
<script>
import { mapGetters } from 'vuex'
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
    data: () => ({

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
            this.$store.dispatch('notice/actionTypeNotice',{content : 'Sản phẩm vừa dc thêm vào giỏ hàng',type : 'addtocart'})
            this.$store.dispatch('notice/activateShowMenu')
            }
      }
    },
    created() {
    }

})
</script>
<style>
.price-product-category {
    width: fit-content;
    background-color: rgb(240, 240, 240);
}
.content-product-category {
    flex-grow: 1 !important;
    height:auto;
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
</style>