
<template>
    <div class="row">
        <p class="text-primary"> <span class="text-header-dashboard" @click="backProduct">Sản phẩm </span> >>  
            <span class="text-header-dashboard">Chi tiết sản phẩm</span> </p>
    </div>
    <div class="row m-2 border">
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
      <textarea v-model="descriptionProductCreate" class="form-control text-aria-admin" id="exampleFormControlTextarea1" rows="14"></textarea>
    </div>
    <div class="mb-3">
      <div class="d-flex px-3">
          <label class="ms-2 label-choose-file align-items-center" for="image-post">
              <i class="ms-5 add-image-post me-2">Thêm Ảnh/Video</i>
              <font-awesome-icon icon="fa-regular fa-image" class="icon-image-post-blog fs-4" />
              <input class="ms-1" type="file" id="image-post" ref="imageUpdateDasboard" name="filename" @change="upLoadFileImg"
                multiple />
          </label>           
      </div>
      <Carousel class="mt-4 border" :settings="settings" :breakpoints="breakpoints">
          <Slide v-for="file, index in fileUpload" :key="index">
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
      <MediaPhotoProductDetail @del="delImg" v-if="data_files != ''" :data_files="data_files" />
    </div>
    <div class="btn btn-dark m-2" @click="updateProduct">
      Lưu
    </div>
  </div>
</template>
  
<script>
import { mapGetters } from 'vuex'
import { useRoute } from 'vue-router'
import { actionAdmin } from './../../common/admin.service'
import {CategoryApiService} from './../../common/category.service'
import MediaPhotoProductDetail from './../component/MediaProductDetail.vue'
import { Carousel, Navigation, Slide } from 'vue3-carousel'
import ImageSendComment from './../../components/blog/ImageSendComment.vue'
import { URL_PATH_SERVER } from '../../common/constants'

export default {
    name: "DetailProductAdmin",
    setup() {
        const route = useRoute();
        return { route };
    },

    data: () => ({
        dataCategory : [],
        fileUpload : [],
        nameProductCreate : '',
        categoryProductCreate : '',
        sexProductCreate : '',
        priceProductCreate : '',
        saleProductCreate : '',
        quantityProductCreate : '',
        descriptionProductCreate : '',
        data_file_del : [],
        data_files : '',
        settings: {
            itemsToShow: 5,
            snapAlign: 'center',
        },
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
        Carousel,
        Slide,
        Navigation,
        MediaPhotoProductDetail,
        ImageSendComment
    },
    computed: {
        ...mapGetters('dashboard', {
            get_product_detail: 'getProductDetail',
        }),
    },
    methods: {
        removeFileUpload(index){
            this.fileUpload.splice(index, 1)
            console.log('this.fileUpload',index)
        },
        backProduct(){
            this.$store.dispatch('dashboard/actionSelectedLayout' , { type : 4})
        },
        addCategoryLevel(length){
            let text="";
            for (let i = 0; i < length; i++) {
                text += "---"
            }
            return text
        },
        delImg(src){
            this.data_file_del = [src.replace(URL_PATH_SERVER + '/','') , ...this.data_file_del]
        },
        async updateProduct(){
            await actionAdmin.updateProduct({
                params : {
                    product_id : this.get_product_detail,
                    media_file : this.fileUpload ,
                    name : this.nameProductCreate,
                    category_id : this.categoryProductCreate,
                    sex : this.sexProductCreate,
                    price : this.priceProductCreate,
                    sale : this.saleProductCreate ,
                    quantity : this.quantityProductCreate ,
                    description : this.descriptionProductCreate,
                    media_file_del : this.data_file_del
                }
            }).then(res => {
                console.log(res)
                this.getProduct()

            })
        },
        async getProduct(){
            await actionAdmin.getDetailProduct({
                params : {
                    product_id : this.get_product_detail,
                    category_id : this.categoryProductCreate

                }
            }).then(res => {
                console.log(res)
                this.fileUpload = []
                this.nameProductCreate = res.product[0].name
                this.categoryProductCreate =res.category
                this.sexProductCreate = res.product[0].sex
                this.priceProductCreate = res.product[0].price
                this.saleProductCreate = res.product[0].sale
                this.quantityProductCreate = res.product[0].product_quantity
                this.descriptionProductCreate = res.product[0].description
                this.data_files = res.product[0].file_media_product

            })
        },
        async upLoadFileImg() {
            const files = this.$refs.imageUpdateDasboard.files
            
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
    },
    async created() {
        await CategoryApiService.get().then(res =>{
            this.dataCategory = res.data.category
        })
        await actionAdmin.getDetailProduct({
            params : {
                product_id : this.get_product_detail,
                category_id : this.categoryProductCreate

            }
        }).then(res => {
            this.fileUpload = []
            this.nameProductCreate = res.product[0].name
            this.categoryProductCreate =res.category
            this.sexProductCreate = res.product[0].sex
            this.priceProductCreate = res.product[0].price
            this.saleProductCreate = res.product[0].sale
            this.quantityProductCreate = res.product[0].product_quantity
            this.descriptionProductCreate = res.product[0].description
            this.data_files = res.product[0].file_media_product
            this.data_file_del = []
        })
    }
}
</script>
<style lang="scss" scoped>
.text-header-dashboard {
    cursor : pointer;
}
.text-header-dashboard:hover {
    color :rgb(243, 78, 72) !important;
}
.text-aria-admin {
    width : 100% !important;
}
.item-slide-image {
    width: 15rem;
    height: auto;
    overflow: hidden;
}
</style>