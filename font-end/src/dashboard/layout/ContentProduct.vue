
<template>
  <div class="row mx-2 p-2">
    <div class="col-lg-3">
      <div class="single_analite_content text-dark text-center" :class="{ 'click-option-product': isShowWareHouse }"
        @click="selectedContent(1)">
        <font-awesome-icon icon="fa-solid fa-warehouse" class="my-3 icon-product-db"
          :class="{ 'icon-option-product': isShowWareHouse }" />
        <b>
          <p class="m-2 pb-5" :class="{ 'text-option-product': isShowWareHouse }">
            Xem sản phẩm trong kho
          </p>
        </b>
      </div>
    </div>
    <div class="col-lg-3">
      <div class="single_analite_content text-dark text-center" :class="{ 'click-option-product': isShowAddProduct }"
        @click="selectedContent(2)">
        <font-awesome-icon icon="fa-solid fa-plus" class="my-3 icon-product-db"
          :class="{ 'icon-option-product': isShowAddProduct }" />
        <b>
          <p class="m-2 pb-5" :class="{ 'text-option-product': isShowAddProduct }">
            Thêm sản phẩm
          </p>
        </b>
      </div>
    </div>
    <div class="col-lg-3">
      <div class="single_analite_content text-dark text-center" :class="{ 'click-option-product': isShowAddVoucher }"
        @click="selectedContent(3)">
        <font-awesome-icon icon="fa-solid fa-ticket" class="my-3 icon-product-db"
          :class="{ 'icon-option-product': isShowAddVoucher }" />
        <b>
          <p class="m-2 pb-5" :class="{ 'text-option-product': isShowAddVoucher }">
            Voucher sản phẩm
          </p>
        </b>
      </div>
    </div>
    <div class="col-lg-3">
      <div class="single_analite_content text-dark text-center" :class="{ 'click-option-product': isShowAddFlashSale }"
        @click="selectedContent(4)">
        <font-awesome-icon icon="fa-solid fa-bolt-lightning" class="my-3 icon-product-db"
          :class="{ 'icon-option-product': isShowAddFlashSale }" />
        <b>
          <p class="m-2 pb-5" :class="{ 'text-option-product': isShowAddFlashSale }">
            flash sale
          </p>
        </b>
      </div>
    </div>
  </div>
  <div v-if="isShowWareHouse" class="row">
    <div class="p-3">
      <div class="input-group">
        <div class="form-outline">
          <input v-model="keySearch" type="search" id="form1" class="form-control" @blur="searchProduct"
            v-on:keyup.enter="searchProduct" />
          <label class="form-label search-dashboard" for="form1">Tìm kiếm</label>
        </div>
        <button type="button" class="btn btn-primary">
          <i class="fas fa-search"></i>
        </button>
      </div>
    </div>
  </div>
  <div v-if="isShowWareHouse" class="row">
    <table class="responstable">

      <tr>
        <th>STT</th>
        <th>Tên sản phẩm</th>
        <th>danh mục</th>
        <th>giá</th>
        <th> giảm giá</th>
        <th> tổng giá</th>
        <th> số lượng</th>
        <th> Chọn</th>
      </tr>

      <tr v-for="item, index in dataProducts" class="tr-product-admin">
        <td @click="showDetailProduct(item.id)"> {{ index }} </td>
        <td @click="showDetailProduct(item.id)">{{ item.name }}</td>
        <td @click="showDetailProduct(item.id)">{{ item.category_name }}</td>
        <td @click="showDetailProduct(item.id)">{{ item.price }}</td>
        <td @click="showDetailProduct(item.id)">{{ item.sale }}</td>
        <td @click="showDetailProduct(item.id)">{{ item.price_total }}</td>
        <td @click="showDetailProduct(item.id)">{{ item.product_quantity }}</td>

        <td class="">
          <button class="button-28" :class="{ 'button-28-selected': checkProductSelect(item.id) }" role="button"
            @click="appendProductSelected(item.id)">
            <span class="" v-if="checkProductSelect(item.id)"> Đã chọn </span>
            <span class="" v-if="!checkProductSelect(item.id)"> Chọn </span>
          </button>
        </td>
      </tr>
    </table>
    <button class="btn btn-dark" @click="delProduct">
      Xóa
    </button>
  </div>
  <div v-if="isShowAddProduct" class="row m-2 border">
    <div class="col-sm-4 mb-3">
      <label for="exampleFormControlInput1" class="form-label">Tên sản phẩm</label>
      <input v-model="nameProductCreate" type="email" class="form-control" id="exampleFormControlInput1" placeholder="Nhập tên">
    </div>
    <div class="col-sm-4 mb-3 flex">
      <p class="m-0 ">Danh mục: </p>
      <select v-model="categoryProductCreate" class="form-control" aria-label="Default select example">
        <option value="0" selected>Chọn danh mục</option>
        <option v-for="item in dataCategory" :value="item.id" :class="{'text-primary' : item.level==0}" > <span > {{addCategoryLevel(item.level)}} </span> {{ item.name}}</option>
      </select>
    </div>
    <div class="col-sm-4 mb-3 flex">
      <p class="m-0 ">Giới tính: </p>
      <select v-model="sexProductCreate" class="form-control" aria-label="Default select example">
        <option value="ALL" selected>Chọn giới tính</option>
        <option :value=0  >Tất cả</option>
        <option :value="1" >Nam</option>
        <option  :value="2" >Nữ</option>
      </select>
    </div>
    <div class="col-sm-4 mb-3 flex">
      <p class="m-0 ">Giá thực: </p>
      <input v-model="priceProductCreate" type="number" class="form-control" >
    </div>
    <div class="col-sm-4 mb-3 flex">
      <p class="m-0 ">Giảm giá: </p>
      <input v-model="saleProductCreate" type="number" class="form-control" >
    </div>
    <div class="col-sm-4 mb-3 flex">
      <p class="m-0 ">Số lượng: </p>
      <input v-model="quantityProductCreate" type="number" class="form-control" >
    </div>
    <div class="mb-3 text-aria-admin">
      <label for="exampleFormControlTextarea1" class="form-label">Mô tả</label>
      <textarea v-model="descriptionProductCreate" class="form-control text-aria-admin" id="exampleFormControlTextarea1" rows="4"></textarea>
    </div>
    <div class="mb-3">
      <div class="d-flex px-3">
          <label class="ms-2 label-choose-file align-items-center" for="image-post">
              <i class="ms-5 add-image-post me-2">Thêm Ảnh/Video</i>
              <font-awesome-icon icon="fa-regular fa-image" class="icon-image-post-blog fs-4" />
              <input class="ms-1" type="file" id="image-post" ref="imagePostDasboard" name="filename" @change="upLoadFileImg"
                multiple />
          </label>           
      </div>
      <Carousel class="mt-4 border" :settings="settings" :breakpoints="breakpoints">
          <Slide v-for="file, index in fileUpload" :key="index">
            {{index}}
              <div class="carousel__item item-slide-image">
                  <ImageSendComment v-if="file.isImage"  :data="file.data" :index="index" 
                  @removeFileUpload="removeFileUpload" />
                  <video v-if="file.isVideo" :src="file.videoSrc" controls></video>
              </div>
          </Slide>

          <template #addons>
              <Navigation v-if="fileUpload.length > 5" />
          </template>
      </Carousel>
    </div>
    <div class="btn btn-dark m-2" @click="createProduct">
      Thêm sản phẩm
    </div>
  </div>
</template>
  
<script>
import { mapGetters } from 'vuex'
import { useRoute } from 'vue-router'
import { actionAdmin } from './../../common/admin.service'
import {CategoryApiService} from './../../common/category.service'
import ListMediaComment from './../../layout/blog/ListMediaComment.vue'
import { Carousel, Navigation, Slide } from 'vue3-carousel'
import ImageSendComment from './../../components/blog/ImageSendComment.vue'
export default {
  name: "ContentProduct",
  setup() {
    const route = useRoute();
    return { route };
  },

  data: () => ({
    pageProduct: 1,
    numberQuantityPage: 20,
    dataProducts: [],
    product_selected: [],
    keySearch: '',
    isShowWareHouse: true,
    isShowAddProduct: false,
    isShowAddVoucher: false,
    isShowAddFlashSale: false,
    dataCategory : [],
    fileUpload : [],
    nameProductCreate : '',
    categoryProductCreate : '',
    sexProductCreate : '',
    priceProductCreate : '',
    saleProductCreate : '',
    quantityProductCreate : '',
    descriptionProductCreate : '',
    settings: {
                itemsToShow: 5,
                snapAlign: 'center',
            },
            // breakpoints are mobile first
            // any settings not specified will fallback to the carousel settings
            breakpoints: {
                // 700px and up
                700: {
                    itemsToShow: 3.5,
                    snapAlign: 'center',
                },
                // 1024 and up
                1024: {
                    itemsToShow: 5,
                    snapAlign: 'start',
                },
            },
  }),
  components: {
    ListMediaComment,
    Carousel,
    Slide,
    Navigation,
    ImageSendComment,
  },
  computed: {
    ...mapGetters('dashboard', {
      get_is_show_layout: 'getIsShowLayout',
    }),
  },
  methods: {
    removeFileUpload(index){
        this.fileUpload.splice(index, 1)
        console.log('this.fileUpload',index)
    },
    selectedContent(type) {
      switch (type) {
        case 1:
          this.isShowWareHouse = true
          this.isShowAddProduct = false
          this.$store.dispatch('dashboard/hideVoucher')
          this.isShowAddFlashSale = false
          break;
        case 2:
          this.isShowWareHouse = false
          this.isShowAddProduct = true
          this.$store.dispatch('dashboard/hideVoucher')
          this.isShowAddFlashSale = false
          break;
        case 3:
          this.isShowWareHouse = false
          this.isShowAddProduct = false
          this.$store.dispatch('dashboard/actionShowVoucher' , { type : 1})
          this.isShowAddFlashSale = false
          break;
        case 4:
          this.isShowWareHouse = false
          this.isShowAddProduct = false
          this.$store.dispatch('dashboard/actionShowFlashSale' , { type : 1})
          break;

        default:
          this.isShowWareHouse = true
          this.isShowAddProduct = false
          this.$store.dispatch('dashboard/hideVoucher')
          this.isShowAddFlashSale = false
          break;
      }
    },
    appendProductSelected(product_id) {
      if (this.checkProductSelect(product_id) == true) {
        this.product_selected = this.product_selected.filter(val => {
          return val != product_id
        })
      } else {
        this.product_selected = [product_id, ...this.product_selected]
      }
    },
    checkProductSelect(product_id) {
      for (let item of this.product_selected) {
        if (item == product_id) return true;
      }
      return false;
    },
    checkProductDel(product_id, product_selected) {
      for (let item of product_selected) {
        if (item == product_id) return true;
      }
      return false;
    },
    async delProduct() {
      await actionAdmin.delProduct({
        params: {
          products_del: this.product_selected,
        }
      }).then(res => {
        this.dataProducts = this.dataProducts.filter(product => {
          if (this.checkProductDel(product.id, res.products_del) == false) {
            return product
          }
        })
      })
    },
    async searchProduct() {
      await actionAdmin.searchProduct({
        params: {
          key_search: this.keySearch,
          page: this.pageProduct,
          number_quantity: this.numberQuantityPage
        }
      }).then(res => {
        this.dataProducts = res.products
      })
    },
    addCategoryLevel(length){
      let text="";
      for (let i = 0; i < length; i++) {
        text += "---"
      }
      return text
    },
    async upLoadFileImg() {
        const files = this.$refs.imagePostDasboard.files
        
        for (let i = 0; i < files.length; i++) {
            const file = files[i]
            console.log(file)
            const dataUrl = await new Promise((resolve) => {
                const reader = new FileReader()
                reader.onload = () => resolve(reader.result)
                reader.readAsDataURL(file)
            })

            if (file.type.startsWith('image/')) {
                this.fileUpload.push({
                    data: dataUrl,
                    isImage: true,
                    isVideo: false
                })
            }

            if (file.type.startsWith('video/')) {
                this.fileUpload.push({
                    data: dataUrl,
                    isVideo: true,
                    isImage: false,
                    videoSrc: URL.createObjectURL(file)
                })
            }
        }
    },
    async createProduct(){
      await actionAdmin.createProduct({
        params: {
          media_file : this.fileUpload ,
          name : this.nameProductCreate,
          category_id : this.categoryProductCreate,
          sex : this.sexProductCreate,
          price : this.priceProductCreate,
          sale : this.saleProductCreate ,
          quantity : this.quantityProductCreate ,
          description : this.descriptionProductCreate,
        }
      }).then(res => {
        alert("thêm sản phẩm thành công")
        this.fileUpload = []
        this.nameProductCreate = ''
        this.categoryProductCreate =''
        this.sexProductCreate =''
        this.priceProductCreate =''
        this.saleProductCreate = ''
        this.quantityProductCreate = ''
        this.descriptionProductCreate =''
      })
    },
    showDetailProduct(product_id){
      this.$store.dispatch('dashboard/actionSelectedDetailProduct' , { product_id : product_id})
    }
  },
  async created() {
    await actionAdmin.getAllProductPage({
      params: {
        page: this.pageProduct,
        number_quantity: this.numberQuantityPage
      }
    }).then(res => {
      this.dataProducts = res.products
    }),
    await CategoryApiService.get().then(res =>{
      this.dataCategory = res.data.category
    }
    )
  },
}
</script>
<style lang="scss" scoped>
$table-breakpoint: 480px;
$table-background-color: #FFF;
$table-text-color: #024457;
$table-outer-border: 1px solid #167F92;
$table-cell-border: 1px solid #D9E4E6;

// Extra options for table style (parse these arguments when including your mixin)
$table-border-radius: 10px;
$table-highlight-color: #EAF3F3;
$table-header-background-color: #167F92;
$table-header-text-color: #FFF;
$table-header-border: 1px solid #FFF;

// The Responstable mixin

@mixin responstable($breakpoint: $table-breakpoint,
  $background-color: $table-background-color,
  $text-color: $table-text-color,
  $outer-border: $table-outer-border,
  $cell-border: $table-cell-border,
  $border-radius: none,
  $highlight-color: none,
  $header-background-color: $table-background-color,
  $header-text-color: $table-text-color,
  $header-border: $table-cell-border) {

  .responstable {
    margin: 1em 0;
    width: 100%;
    overflow: hidden;
    background: $background-color;
    color: $text-color;
    border-radius: $border-radius;
    border: $outer-border;

    tr {
      border: $cell-border;

      &:nth-child(odd) {
        // highlight the odd rows with a color
        background-color: $highlight-color;
      }
    }

    th {
      display: none; // hide all the table header for mobile
      border: $header-border;
      background-color: $header-background-color;
      color: $header-text-color;
      padding: 1em;

      &:first-child {
        // show the first table header for mobile
        display: table-cell;
        text-align: center;
      }

      &:nth-child(2) {
        // show the second table header but replace the content with the data-th from the markup for mobile
        display: table-cell;

        span {
          display: none;
        }

        &:after {
          content: attr(data-th);
        }
      }

      @media (min-width: $breakpoint) {
        &:nth-child(2) {

          // hide the data-th and show the normal header for tablet and desktop
          span {
            display: block;
          }

          &:after {
            display: none;
          }
        }
      }
    }

    td {
      display: block; // display the table data as one block for mobile
      word-wrap: break-word;
      max-width: 7em;

      &:first-child {
        display: table-cell; // display the first one as a table cell (radio button) for mobile
        text-align: center;
        border-right: $cell-border;
      }

      @media (min-width: $breakpoint) {
        border: $cell-border;
      }
    }

    th,
    td {
      text-align: left;
      margin: .5em 1em;

      @media (min-width: $breakpoint) {
        display: table-cell; // show the table as a normal table for tablet and desktop
        padding: 1em;
      }
    }
  }
}

@include responstable($border-radius: $table-border-radius,
  $highlight-color: $table-highlight-color,
  $header-background-color: $table-header-background-color,
  $header-text-color: $table-header-text-color,
  $header-border: $table-header-border);

.custom-btn {
  padding: 20px;
  background-color: transparent;
  border: none
}

.single_analite_content {
  border-radius: 15px;
  background: linear-gradient(315deg, #8eebe6 0%, #bae6ec 74%);
  cursor: pointer;
}

.icon-product-db {
  font-size: 36px;
}

body {
  padding: 0 2em;
  font-family: Arial, sans-serif;
  color: #024457;
  background: #f2f2f2;
}

h1 {
  font-family: Verdana;
  font-weight: normal;
  color: #024457;

  span {
    color: #167F92;
  }
}
.tr-product-admin {
  cursor:pointer;
}
.item-slide-image {
    width: 15rem;
    height: auto;
    overflow: hidden;
}
/* CSS */
.button-28 {
  appearance: none;
  background-color: transparent;
  border: 2px solid #1A1A1A;
  border-radius: 15px;
  box-sizing: border-box;
  color: #3B3B3B;
  cursor: pointer;
  display: inline-block;
  font-family: Roobert, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
  font-size: 16px;
  font-weight: 600;
  line-height: normal;
  margin: 0;
  min-height: 60px;
  min-width: 0;
  outline: none;
  padding: 16px 24px;
  text-align: center;
  text-decoration: none;
  transition: all 300ms cubic-bezier(.23, 1, 0.32, 1);
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  width: 100%;
  will-change: transform;
}

.button-28-selected {
  border: 2px solid white;
  background-color: #1A1A1A;
  color: white;
}

.button-28:disabled {
  pointer-events: none;
}
.text-aria-admin {
  width:100% !important;
}
.button-28:hover {
  color: #fff;
  background-color: #1A1A1A;
  box-shadow: rgba(0, 0, 0, 0.25) 0 8px 15px;
  transform: translateY(-2px);
}

.button-28:active {
  box-shadow: none;
  transform: translateY(0);
}

/* 12 */
.custom-btn {
  width: 230px;
  height: 50px;
  color: #fff;
  border-radius: 5px;
  padding: 10px 25px;
  font-family: 'Lato', sans-serif;
  font-weight: 500;
  background: transparent;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  display: inline-block;
  box-shadow: inset 2px 2px 2px 0px rgba(255, 255, 255, .5),
    7px 7px 20px 0px rgba(0, 0, 0, .1),
    4px 4px 5px 0px rgba(0, 0, 0, .1);
  outline: none;
}

.btn-12 {
  position: relative;
  right: 20px;
  bottom: 20px;
  border: none;
  box-shadow: none;
  width: 230px;
  height: 50px;
  line-height: 42px;
  -webkit-perspective: 230px;
  perspective: 230px;
}

.btn-12 span {
  background: rgb(0, 172, 238);
  background: linear-gradient(0deg, rgba(0, 172, 238, 1) 0%, rgba(2, 126, 251, 1) 100%);
  display: block;
  position: absolute;
  width: 230px;
  height: 50px;
  box-shadow: inset 2px 2px 2px 0px rgba(255, 255, 255, .5),
    7px 7px 20px 0px rgba(0, 0, 0, .1),
    4px 4px 5px 0px rgba(0, 0, 0, .1);
  border-radius: 5px;
  margin: 0;
  text-align: center;
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
  -webkit-transition: all .3s;
  transition: all .3s;
}

.btn-12 span:nth-child(1) {
  box-shadow:
    -7px -7px 20px 0px #fff9,
    -4px -4px 5px 0px #fff9,
    7px 7px 20px 0px #0002,
    4px 4px 5px 0px #0001;
  -webkit-transform: rotateX(90deg);
  -moz-transform: rotateX(90deg);
  transform: rotateX(90deg);
  -webkit-transform-origin: 50% 50% -20px;
  -moz-transform-origin: 50% 50% -20px;
  transform-origin: 50% 50% -20px;
}

.btn-12 span:nth-child(2) {
  -webkit-transform: rotateX(0deg);
  -moz-transform: rotateX(0deg);
  transform: rotateX(0deg);
  -webkit-transform-origin: 50% 50% -20px;
  -moz-transform-origin: 50% 50% -20px;
  transform-origin: 50% 50% -20px;
}

.btn-12:hover span:nth-child(1) {
  box-shadow: inset 2px 2px 2px 0px rgba(255, 255, 255, .5),
    7px 7px 20px 0px rgba(0, 0, 0, .1),
    4px 4px 5px 0px rgba(0, 0, 0, .1);
  -webkit-transform: rotateX(0deg);
  -moz-transform: rotateX(0deg);
  transform: rotateX(0deg);
}

.btn-12:hover span:nth-child(2) {
  box-shadow: inset 2px 2px 2px 0px rgba(255, 255, 255, .5),
    7px 7px 20px 0px rgba(0, 0, 0, .1),
    4px 4px 5px 0px rgba(0, 0, 0, .1);
  color: transparent;
  -webkit-transform: rotateX(-90deg);
  -moz-transform: rotateX(-90deg);
  transform: rotateX(-90deg);
}

.click-option-product {
  background: linear-gradient(0deg, rgba(0, 172, 238, 1) 20%, rgba(2, 126, 251, 1) 80%);
}

.icon-option-product {
  color: #D9E4E6
}

.text-option-product {
  color: #D9E4E6
}</style>