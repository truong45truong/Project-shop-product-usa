
<template>
    <div class="row m-2 border">
      <div class="col-sm-6 mb-3">
        <label for="exampleFormControlInput1" class="form-label">Tên Flash Sale</label>
        <input v-model="nameVoucherCreate" type="text" class="form-control form-text-area" id="exampleFormControlInput1" placeholder="Nhập tên flash sale">
      </div>
      <div class="col-sm-6 mb-3 flex">
        <label for="exampleFormControlInput1" class="form-label">Chi tiết</label>
        <input v-model="noteFlashSaleCreate" type="text" class="form-control form-text-area" placeholder="Nhập chi tiết" >
      </div>
      
      <div class="btn btn-dark m-2" @click="createFlashSale">
        Thêm Flash Sale
      </div>
    </div>
  </template>
    
  <script>
  import { mapGetters } from 'vuex'
  import { useRoute } from 'vue-router'
  import { actionAdmin } from './../../common/admin.service'
  export default {
    name: "AddFlashSale",
    setup() {
      const route = useRoute();
      return { route };
    },
  
    data: () => ({
      nameVoucherCreate : '',
      noteFlashSaleCreate : '',
    }),
    components: {
    },
    computed: {
      ...mapGetters('dashboard', {
        get_is_show_layout: 'getIsShowLayout',
      }),
    },
    methods: {
      async createFlashSale(){
        await actionAdmin.createFlashSale({
          params: {
            name : this.nameVoucherCreate ,
            note : this.noteFlashSaleCreate ,
          }
        }).then(res => {
          alert("thêm Voucher thành công")
            this.nameFlashSaleCreate = ''
            this.noteFlashSaleCreate = ''
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