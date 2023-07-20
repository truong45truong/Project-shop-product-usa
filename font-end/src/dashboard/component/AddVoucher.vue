
<template>
    <div class="row m-2 border">
      <div class="col-sm-6 mb-3">
        <label for="exampleFormControlInput1" class="form-label">Tên Voucher</label>
        <input v-model="nameVoucherCreate" type="text" class="form-control form-text-area" id="exampleFormControlInput1" placeholder="Nhập tên voucher">
      </div>
      <div class="col-sm-6 mb-3 flex">
        <p class="m-0 ">Mức độ ưu tiên: </p>
        <select v-model="levelVoucherCreate" class="form-control form-text-area" aria-label="Default select example">
          <option :value=0  >Tất cả</option>
          <option :value="1" >Thường xuyên</option>
          <option  :value="2" >Vip</option>
        </select>
      </div>
      <div class="col-sm-4 mb-3 flex">
        <p class="m-0 ">Giảm(%): </p>
        <input v-model="saleVoucherCreate" type="number" class="form-control form-text-area" >
      </div>
      <div class="col-sm-4 mb-3 flex">
        <p class="m-0 ">Số lượng: </p>
        <input v-model="quantityVoucherCreate" type="number" class="form-control form-text-area" >
      </div>
      <div class="col-sm-4 mb-3 flex">
        <p class="m-0 ">Giảm tối đa(.000): </p>
        <input v-model="limitedPriceVoucherCreate" type="number" class="form-control form-text-area" >
      </div>
      <div class="col-sm-6 mb-3">
        <label for="exampleFormControlInput1" class="form-label">Chi tiết Voucher</label>
        <input v-model="detailVoucherCreate" type="text" class="form-control form-text-area" id="exampleFormControlInput1" placeholder="Chi tiết">
      </div>
      <div class="col-sm-6 mb-3">
        <label for="exampleFormControlInput1" class="form-label">Mô tả Voucher</label>
        <input v-model="descriptionVoucherCreate" type="text" class="form-control form-text-area" id="exampleFormControlInput1" placeholder="Mô tả">
      </div>
      <div class="btn btn-dark m-2" @click="createVoucher">
        Thêm Voucher
      </div>
    </div>
  </template>
    
  <script>
  import { mapGetters } from 'vuex'
  import { useRoute } from 'vue-router'
  import { actionAdmin } from './../../common/admin.service'
  export default {
    name: "AddVoucher",
    setup() {
      const route = useRoute();
      return { route };
    },
  
    data: () => ({
      nameVoucherCreate : '',
      detailVoucherCreate : '',
      saleVoucherCreate : 0,
      descriptionVoucherCreate : '',
      quantityVoucherCreate : '',
      levelVoucherCreate : 0,
      limitedPriceVoucherCreate : 0,
    }),
    components: {
    },
    computed: {
      ...mapGetters('dashboard', {
        get_is_show_layout: 'getIsShowLayout',
      }),
    },
    methods: {
      async createVoucher(){
        await actionAdmin.createVoucher({
          params: {
            name : this.nameVoucherCreate ,
            detail : this.detailVoucherCreate ,
            sale : this.saleVoucherCreate ,
            description : this.descriptionVoucherCreate,
            quantity : this.quantityVoucherCreate ,
            level : this.levelVoucherCreate ,
            limited_price : this.limitedPriceVoucherCreate ,
          }
        }).then(res => {
          alert("thêm Voucher thành công")
            this.nameVoucherCreate = ''
            this.detailVoucherCreate = ''
            this.saleVoucherCreate = 0
            this.descriptionVoucherCreate = ''
            this.quantityVoucherCreate = 0
            this.levelVoucherCreate = 0
            this.limitedPriceVoucherCreate = 0
            this.priceVoucherCreate = 0
        })
      },
    },
    async created() {
    },
  }
  </script>
  <style lang="scss" scoped>
  .form-text-area {
    width : 100% !important;
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