
<template>
    <div class="row">
        <p class="text-primary"> <span class="text-header-dashboard" @click="backProduct">Sản phẩm </span> >>
            <span class="text-header-dashboard"> Voucher </span>
        </p>
    </div>
    <div class="row">
        <div class="col-sm-3 p-2 d-flex">
            <div class="input-group">
                <div class="form-outline">
                    <input v-model="keySearch" type="search" id="form1" class="form-control" @blur="searchAllVoucherPage"
                        v-on:keyup.enter="searchAllVoucherPage" />
                    <label class="form-label search-dashboard" for="form1">Tìm kiếm</label>
                </div>
                <button type="button" class="btn btn-primary">
                    <i class="fas fa-search"></i>
                </button>
            </div>
        </div>
        <div class="col-sm-3 p-2">
            <button class="btn-add-voucher d-flex p-2 px-4 w-100" @click="showOption(1)"
                :class="{ 'btn-option-activate': get_show_voucher.isShowList }">
                <font-awesome-icon icon="fa-solid fa-list" class="icon-voucher-db  mx-2" />
                <b>Danh sách</b>
            </button>
        </div>
        <div class="col-sm-3 p-2">
            <button class="btn-add-voucher d-flex p-2 px-4 w-100" @click="showOption(2)"
                :class="{ 'btn-option-activate': get_show_voucher.isShowAdd }">
                <font-awesome-icon icon="fa-solid fa-plus" class="icon-voucher-db  mx-2" />
                <b>Thêm voucher</b>
            </button>
        </div>
        <div class="col-sm-3 p-2">
            <button class="btn-add-voucher d-flex p-2 px-4 w-100" @click="showOption(3)"
                :class="{ 'btn-option-activate': get_show_voucher.isShowAddProduct }">
                <font-awesome-icon icon="fa-solid fa-ticket" class="icon-voucher-db  mx-2" />
                <b>Thêm Sản phẩm vào voucher</b>
            </button>
        </div>
        <div class="col-3 p-2 d-flex">
            <p class="m-0"> Mức độ :</p>
            <input v-model="levelVoucher" type="number" class="me-2" @blur="searchAllVoucherPage" v-on:keyup.enter="searchAllVoucherPage">
        </div>
    </div>
    <AddVoucher v-if="get_show_voucher.isShowAdd" />
    <div v-if="get_show_voucher.isShowList" class="row">
        <table class="responstable">

            <tr>
                <th>STT</th>
                <th>Tên Voucher</th>
                <th>Chi tiết </th>
                <th>giảm</th>
                <th> mô tả</th>
                <th> số lượng</th>
                <th> mức độ</th>
                <th> giảm tối đa</th>
                <th> số sản phẩm </th>
                <th> Chọn</th>
            </tr>

            <tr v-for="item, index in dataVoucher" class="tr-product-admin">
                <td @click="showDetailVoucher(item.id)"> {{ index }} </td>
                <td @click="showDetailVoucher(item.id)">{{ item.name }}</td>
                <td @click="showDetailVoucher(item.id)">{{ item.detail }}</td>
                <td @click="showDetailVoucher(item.id)">{{ item.sale }}</td>
                <td @click="showDetailVoucher(item.id)">{{ item.description }}</td>
                <td @click="showDetailVoucher(item.id)">{{ item.quantity }}</td>
                <td @click="showDetailVoucher(item.id)">{{ item.level }}</td>
                <td @click="showDetailVoucher(item.id)">{{ item.limited_price }}</td>
                <td @click="showDetailVoucher(item.id)">{{ item.count_product }}</td>
                <td class="">
                    <button class="button-28" :class="{ 'button-28-selected': checkVoucherSelect(item.id) }" role="button"
                        @click="appendVoucherSelected(item.id)">
                        <span class="text-white" v-if="checkVoucherSelect(item.id)"> Đã chọn </span>
                        <span class="" v-if="!checkVoucherSelect(item.id)"> Chọn </span>
                    </button>
                </td>
            </tr>
        </table>
        <button class="btn btn-dark" @click="delVoucher">
            Xóa
        </button>
    </div>
    <div v-if="get_show_voucher.isShowAddProduct" class="row">
        <table class="responstable">

            <tr>
                <th>STT</th>
                <th>Tên Voucher</th>
                <th>Chi tiết </th>
                <th>giảm</th>
                <th> mô tả</th>
                <th> số lượng</th>
                <th> mức độ</th>
                <th> giảm tối đa</th>
                <th> Chọn</th>
            </tr>

            <tr v-for="item, index in dataVoucherEmpty" class="tr-product-admin">
                <td @click="showDetailVoucher(item.id)"> {{ index }} </td>
                <td @click="showDetailVoucher(item.id)">{{ item.name }}</td>
                <td @click="showDetailVoucher(item.id)">{{ item.detail }}</td>
                <td @click="showDetailVoucher(item.id)">{{ item.sale }}</td>
                <td @click="showDetailVoucher(item.id)">{{ item.description }}</td>
                <td @click="showDetailVoucher(item.id)">{{ item.quantity }}</td>
                <td @click="showDetailVoucher(item.id)">{{ item.level }}</td>
                <td @click="showDetailVoucher(item.id)">{{ item.limited_price }}</td>
                <td class="">
                    <button class="button-28" :class="{ 'button-28-selected': voucherSelected.id == item.id }" role="button"
                        @click="SelectedVoucherAdd(item.id, item.name, item.limited_price, item.level, item.quantity, item.sale)">
                        <span class="text-white" v-if="voucherSelected.id == item.id"> Đã chọn </span>
                        <span class="" v-if="voucherSelected.id != item.id"> Chọn </span>
                    </button>
                </td>
            </tr>
        </table>
        <div v-if="voucherSelected != false" class=" mt-4">
            <p class=""><b>Voucher đã chọn :</b> </p>
            <div class="voucher-selected p-2">
                <p class="text-center m-0 text-white">
                    <b>{{ voucherSelected.name }}</b>
                </p>
                <p class="text-center m-0 text-white">
                    <b>Mức độ : {{ voucherSelected.level }}</b>
                </p>
                <p class="text-center m-0 text-white">
                    <b>Số lượng : {{ voucherSelected.quantity }}</b>
                </p>
            </div>
        </div>
        <div v-if="voucherSelected" class="row mt-4">
            <div class="col-sm-4 p-3">
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
            <div class="col-sm-4 p-3">
                <div class="input-group">
                    <div class="form-outline">
                    <input v-model="numberQuantityProduct" type="number" id="form1" class="form-control" @blur="getProduct"
                        v-on:keyup.enter="getProduct" />
                    <label class="form-label search-dashboard" for="form1">Số  phần từ trong danh sách</label>
                    </div>
                </div>
            </div>
        </div>
        <table v-if="voucherSelected != false" class="responstable">
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
                <td @click="showDetailProduct(item.id)"> {{ ((pageProduct - 1 )*numberQuantityProduct + 1) + index }} </td>
                <td @click="showDetailProduct(item.id)">{{ item.name }}</td>
                <td @click="showDetailProduct(item.id)">{{ item.category_name }}</td>
                <td @click="showDetailProduct(item.id)">{{ item.price }}</td>
                <td @click="showDetailProduct(item.id)">{{ item.sale }}</td>
                <td @click="showDetailProduct(item.id)">{{ item.price_total }}</td>
                <td @click="showDetailProduct(item.id)">{{ item.product_quantity }}</td>

                <td class="">
                    <button class="button-28" :class="{ 'button-28-selected': checkProductSelect(item.id) }" role="button"
                        @click="appendProductSelected(item.id)">
                        <span class="text-white" v-if="checkProductSelect(item.id)"> Đã chọn </span>
                        <span class="text-dark" v-if="!checkProductSelect(item.id)"> Chọn </span>
                    </button>
                </td>
            </tr>
        </table>
        <div v-if="voucherSelected != false" class="container xlarge">
            <div class="pagination">
                <ul class="pagination-ul d-flex">
                    <li v-for="item in arrayPagiProduct">
                        <button class="pagination-btn me-2" :class="{'activate-pagination' : item == pageProduct}"
                        @click="setPageProduct(item)">
                            {{item}}
                        </button>
                    </li>
                </ul>
            </div>
        </div>
        <div v-if="voucherSelected != false" class="row">
            <div class="col-4">
                <button class="btn btn-dark" @click="addProductVoucher">
                    Thêm vào Voucher
                </button>
            </div>
        </div>
    </div>
</template>
  
<script>
import { mapGetters } from 'vuex'
import { useRoute } from 'vue-router'
import { actionAdmin } from './../../common/admin.service'
import AddVoucher from './../component/AddVoucher.vue'
export default {
    name: "ContentVoucher",
    setup() {
        const route = useRoute();
        return { route };
    },

    data: () => ({
        product_selected: [],
        keySearchProduct: '',
        voucher_selected: [],
        keySearch: '',
        dataVoucher: [],
        dataProducts: [],
        voucherSelected: false,
        dataVoucherEmpty: [],
        numberQuantity: 20,
        levelVoucher: 0,
        page: 1,
        pageProduct : 1 ,
        arrayPagiProduct : [],
        numberQuantityProduct : 20,
    }),
    components: {
        AddVoucher
    },
    computed: {
        ...mapGetters('dashboard', {
            get_show_voucher: 'getShowVoucher',
        }),
    },
    methods: {
        showDetailVoucher(voucher_id){
            this.$store.dispatch('dashboard/actionShowVoucher', { type: 4 ,voucher_id })
        },
        async addProductVoucher(){
            await actionAdmin.addProductVoucher({
                params: {
                    voucher_id: this. voucherSelected.id ,
                    products_selected: this.product_selected,
                }
            }).then(res => {
                alert("Thêm sản phẩm vào voucher thành công")
            })
        },
        setPageProduct(page){
            this.pageProduct = page
            this.getProduct()
        },
        setArrayPagiProduct(numberProduct) {
            this.arrayPagiProduct = []
            if ((numberProduct / this.numberQuantityProduct ) > Math.floor(numberProduct / this.numberQuantityProduct ) ){
                let numberPage = Math.floor(numberProduct / this.numberQuantityProduct )
                if (numberPage > 10){
                    this.arrayPagiProduct =  [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , numberPage ]
                }
                else {
                    console.log('Number', numberPage)
                    for (let i = 1 ; i < numberPage ; i = i + 1){
                        this.arrayPagiProduct =  [...this.arrayPagiProduct ,i ]
                    }
                }
            }
            if ((numberProduct / this.numberQuantityProduct ) == Math.floor(numberProduct / this.numberQuantityProduct ) ){
                let numberPage = Math.floor(numberProduct / this.numberQuantityProduct ) - 1
                if (numberPage > 10){
                    this.arrayPagiProduct =  [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , numberPage ]
                }
                else {
                    for (let i = 1 ; i < numberPage ; i = i + 1){
                        this.arrayPagiProduct =  [...this.arrayPagiProduct ,i ]
                    }
                }
            }
        },
        showDetailProduct(product_id){
            this.$store.dispatch('dashboard/actionSelectedDetailProduct' , { product_id : product_id})
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
        async getProduct() {
            await actionAdmin.getAllProductPage({
                params: {
                    page: this.pageProduct,
                    number_quantity: this.numberQuantityProduct,
                }
            }).then(res => {
                this.dataProducts = res.products
                this.setArrayPagiProduct(res.number_product)
            })
        },
        async searchProduct() {
            await actionAdmin.searchProduct({
                params: {
                    key_search: this.keySearch,
                    page: this.pageProduct,
                    number_quantity: this.numberQuantityProduct,
                }
            }).then(res => {
                this.dataProducts = res.products
                this.setArrayPagiProduct(res.number_product)
            })
        },
        appendVoucherSelected(voucher_id) {
            if (this.checkVoucherSelect(voucher_id) == true) {
                this.voucher_selected = this.voucher_selected.filter(val => {
                    return val != voucher_id
                })
            } else {
                this.voucher_selected = [voucher_id, ...this.voucher_selected]
            }
        },
        SelectedVoucherAdd(voucher_id, name, limited_price, level, quantity, sale) {
            if( this.voucherSelected != false  ){
                if(this.voucherSelected.id == voucher_id) {
                    this.voucherSelected = false
                }
            }else
            this.voucherSelected = {
                id: voucher_id,
                name: name,
                limited_price: limited_price,
                level: level,
                quantity: quantity,
                sale: sale
            }
            this.getProduct()
        },
        checkVoucherSelect(voucher_id) {
            for (let item of this.voucher_selected) {
                if (item == voucher_id) return true;
            }
            return false;
        },
        checkVoucherDel(voucher_id, voucher_selected) {
            for (let item of voucher_selected) {
                if (item == voucher_id) return true;
            }
            return false;
        },
        async delVoucher() {
            await actionAdmin.delVoucher({
                params: {
                    vouchers_del: this.voucher_selected,
                }
            }).then(res => {
                this.dataVoucher = this.dataVoucher.filter(voucher => {
                    if (this.checkVoucherDel(voucher.id, res.vouchers_del) == false) {
                        return voucher
                    }
                })
            })
        },
        async searchAllVoucherPage() {
            await actionAdmin.searchAllVoucherPage({
                params: {
                    key_search: this.keySearch,
                    page: this.page,
                    number_quantity: this.numberQuantity,
                    level: this.levelVoucher
                }
            }).then(res => {
                this.dataVoucher = res.vouchers
                this.showOption(1)
            })
        },
        backProduct() {
            this.$store.dispatch('dashboard/actionSelectedLayout', { type: 4 })
        },
        async getVoucher() {
            await actionAdmin.getAllVoucherPage({
                params: {
                    page: this.page,
                    number_quantity: this.numberQuantity,
                    level: this.levelVoucher
                }
            }).then(res => {
                this.dataVoucher = res.vouchers
            })
        },
        showOption(type) {
            this.$store.dispatch('dashboard/actionShowVoucher', { type: type })
            if (type == 3) {
                this.getAllVoucherNoProductPage()
            }
        },
        async getAllVoucherNoProductPage() {
            await actionAdmin.getAllVoucherNoProductPage({
                params: {
                    page: this.page,
                    number_quantity: this.numberQuantity,
                }
            }).then(res => {
                this.dataVoucherEmpty = res.vouchers
            })
        }
    },
    async created() {
        await actionAdmin.getAllVoucherPage({
            params: {
                page: this.page,
                number_quantity: this.numberQuantity,
                level: this.levelVoucher
            }
        }).then(res => {
            this.dataVoucher = res.vouchers
        })
    }
}
</script>
<style lang="scss" scoped>
.pagination-ul {
    list-style: none;
    
}
.pagination-btn {
    width : 3rem;
    height : 3rem;
    border : 1px solid black;
    color  : black;
    background-color: transparent;
}
.activate-pagination {
    border : 1px solid #167F92;
    background-color: #167F92;
    color : white;
}
.voucher-selected {
    background-image: linear-gradient(to right bottom, #ff541e, #ff4835, #fc3d47, #f63657) !important;
    max-width: 500px;
}

.button-28 {
    width: 100px;
    border: 1px solid black;
    border-radius: 10px;
    background-color: transparent;
}

.button-28-selected {
    background-color: black;
}

.button-28:hover {
    border-radius: 0;
}

.text-header-dashboard {
    cursor: pointer;
}

.text-header-dashboard:hover {
    color: rgb(243, 78, 72) !important;
}

.text-aria-admin {
    width: 100% !important;
}

.item-slide-image {
    width: 15rem;
    height: auto;
    overflow: hidden;
}

.btn-add-voucher {
    border: 2px solid black;
    border-radius: 10px;
    background-color: white;
}

.icon-voucher-db {
    font-size: 24px;
    color: rgb(1, 22, 1);
}

.btn-add-voucher:hover {
    border-radius: 0;
    transition: 0.3s;
}

.btn-option-activate {
    background-color: #167F92;
    border: 2px solid #167F92;
    color: white;
}

.btn-option-activate .icon-voucher-db {
    color: white;
}

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


    $main-color: #f0f0f0;
$secondary-color: #1d1f20;

 @mixin display-child($n) {
    @for $i from 2 through $n {
      &:nth-child(#{$i}) {
        a {
          display: inline-block;
        }
      }
    }
 }

</style>