
<template>
    <div v-if="get_show_falshsale.show" class="row">
        <p class="text-primary"> <span class="text-header-dashboard" @click="backProduct">Sản phẩm </span> >>
            <span class="text-header-dashboard"> FlashSale </span>
        </p>
    </div>
    <div class="row">
        <div class="col-sm-3 p-2 d-flex">
            <div class="input-group">
                <div class="form-outline">
                    <input v-model="keySearch" type="search" id="form1" class="form-control" @blur="searchAllVoucherPage"
                        v-on:keyup.enter="searchAllFlashSalePage" />
                    <label class="form-label search-dashboard" for="form1">Tìm kiếm</label>
                </div>
                <button type="button" class="btn btn-primary">
                    <i class="fas fa-search"></i>
                </button>
            </div>
        </div>
        <div class="col-sm-3 p-2">
            <button class="btn-add-voucher d-flex p-2 px-4 w-100" @click="showOption(1)"
                :class="{ 'btn-option-activate': get_show_falshsale.isShowList }">
                <font-awesome-icon icon="fa-solid fa-list" class="icon-voucher-db  mx-2" />
                <b>Danh sách</b>
            </button>
        </div>
        <div class="col-sm-3 p-2">
            <button class="btn-add-voucher d-flex p-2 px-4 w-100" @click="showOption(2)"
                :class="{ 'btn-option-activate': get_show_falshsale.isShowAdd }">
                <font-awesome-icon icon="fa-solid fa-plus" class="icon-voucher-db  mx-2" />
                <b>Thêm flash sale</b>
            </button>
        </div>
        <div class="col-sm-3 p-2">
            <button class="btn-add-voucher d-flex p-2 px-4 w-100" @click="showOption(3)"
                :class="{ 'btn-option-activate': get_show_falshsale.isShowAddProduct }">
                <font-awesome-icon icon="fa-solid fa-ticket" class="icon-voucher-db  mx-2" />
                <b>Thêm Sản phẩm vào flash sale</b>
            </button>
        </div>
    </div>
    <AddFlashSale v-if="get_show_falshsale.isShowAdd" />
    <div v-if="get_show_falshsale.isShowList" class="row">
        <table class="responstable">

            <tr>
                <th>STT</th>
                <th>Tên FlashSale</th>
                <th>Chi tiết </th>
                <th>Số sản phẩm đã chọn</th>
                <th>Chọn </th>
            </tr>

            <tr v-for="item, index in dataFlashSale" class="tr-product-admin">
                <td @click="showDetailFlashSale(item.id)"> {{ index }} </td>
                <td @click="showDetailFlashSale(item.id)">{{ item.name }}</td>
                <td @click="showDetailFlashSale(item.id)">{{ item.note }}</td>
                <td @click="showDetailFlashSale(item.id)">{{ item.count_product }}</td>
                <td class="">
                    <button class="button-28" :class="{ 'button-28-selected': checkFlashSaleSelect(item.id) }" role="button"
                        @click="appendFlashSaleSelected(item.id)">
                        <span class="text-white" v-if="checkFlashSaleSelect(item.id)"> Đã chọn </span>
                        <span class="" v-if="!checkFlashSaleSelect(item.id)"> Chọn </span>
                    </button>
                </td>
            </tr>
        </table>
        <button class="btn btn-dark" @click="delFlashSale">
            Xóa
        </button>
    </div>
    <div v-if="get_show_falshsale.isShowAddProduct" class="row">
        <table class="responstable">

            <tr>
                <th>STT</th>
                <th>Tên FlashSale</th>
                <th>Chi tiết </th>
                <th>giảm</th>
                <th> mô tả</th>
                <th> số lượng</th>
                <th> mức độ</th>
                <th> giảm tối đa</th>
                <th> Chọn</th>
            </tr>

            <tr v-for="item, index in dataFlashSaleEmpty" class="tr-product-admin">
                <td @click="showDetailFlashSale(item.id)"> {{ index }} </td>
                <td @click="showDetailFlashSale(item.id)">{{ item.name }}</td>
                <td @click="showDetailFlashSale(item.id)">{{ item.detail }}</td>
                <td @click="showDetailFlashSale(item.id)">{{ item.sale }}</td>
                <td @click="showDetailFlashSale(item.id)">{{ item.description }}</td>
                <td @click="showDetailFlashSale(item.id)">{{ item.quantity }}</td>
                <td @click="showDetailFlashSale(item.id)">{{ item.level }}</td>
                <td @click="showDetailFlashSale(item.id)">{{ item.limited_price }}</td>
                <td class="">
                    <button class="button-28" :class="{ 'button-28-selected': flashSaleSelected.id == item.id }" role="button"
                        @click="SelectedFlashSaleAdd(item.id, item.name, item.limited_price, item.level, item.quantity, item.sale)">
                        <span class="text-white" v-if="flashSaleSelected.id == item.id"> Đã chọn </span>
                        <span class="" v-if="flashSaleSelected.id != item.id"> Chọn </span>
                    </button>
                </td>
            </tr>
        </table>
        <div class="row">
            <div v-if="flashSaleSelected != false" class="col-sm-6 mt-4">
                <p class=""><b>Voucher đã chọn :</b> </p>
                <div class="voucher-selected p-2">
                    <p class="text-center m-0 text-white">
                        <b>{{ flashSaleSelected.name }}</b>
                    </p>
                </div>
            </div>
            <div class="col-sm-6 mt-4">
                <input v-model="datetimeFinished" type="number" id="form1" class="form-control"/>
                <label class="form-label search-dashboard" for="form1">Số ngày bắt đầu :</label>
            </div>
        </div>

        <div v-if="flashSaleSelected" class="row mt-4">
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
        <table v-if="flashSaleSelected != false" class="responstable">
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
        <div v-if="flashSaleSelected != false" class="container xlarge">
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
        <div v-if="flashSaleSelected != false" class="row">
            <div class="col-4">
                <button class="btn btn-dark" @click="addProductFlashSale">
                    Thêm vào FlashSale
                </button>
            </div>
        </div>
    </div>
</template>
  
<script>
import { mapGetters } from 'vuex'
import { useRoute } from 'vue-router'
import { actionAdmin } from './../../common/admin.service'
import AddFlashSale from './../component/AddFlashSale.vue'
export default {
    name: "ContentFlashSale",
    setup() {
        const route = useRoute();
        return { route };
    },

    data: () => ({
        product_selected: [],
        keySearchProduct: '',
        voucher_selected: [],
        keySearch: '',
        dataFlashSale: [],
        dataProducts: [],
        flashSaleSelected: false,
        dataFlashSaleEmpty: [],
        numberQuantity: 20,
        levelFlashSale: 0,
        page: 1,
        pageProduct : 1 ,
        arrayPagiProduct : [],
        numberQuantityProduct : 20,
        datetimeFinished : 1 ,
    }),
    components: {
        AddFlashSale
    },
    computed: {
        ...mapGetters('dashboard', {
            get_show_falshsale: 'getShowFlashSale',
        }),
    },
    methods: {
        showDetailFlashSale(flash_sale_id){
            this.$store.dispatch('dashboard/actionShowFlashSale', { type: 4 ,flash_sale_id : flash_sale_id })
        },
        async addProductFlashSale(){
            await actionAdmin.addProductFlashSale({
                params: {
                    flash_sale_id: this. flashSaleSelected.id ,
                    products_selected: this.product_selected,
                    datetime_finished : this.datetimeFinished
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
        appendFlashSaleSelected(flash_sale_id) {
            if (this.checkFlashSaleSelect(flash_sale_id) == true) {
                this.voucher_selected = this.voucher_selected.filter(val => {
                    return val != flash_sale_id
                })
            } else {
                this.voucher_selected = [flash_sale_id, ...this.voucher_selected]
            }
        },
        SelectedFlashSaleAdd(flash_sale_id, name,note) {
            if( this.flashSaleSelected != false  ){
                if(this.flashSaleSelected.id == flash_sale_id) {
                    this.flashSaleSelected = false
                }
            }else
            this.flashSaleSelected = {
                id: flash_sale_id,
                name: name,
                note : note
            }
            this.getProduct()
        },
        checkFlashSaleSelect(flash_sale_id) {
            for (let item of this.voucher_selected) {
                if (item == flash_sale_id) return true;
            }
            return false;
        },
        checkFlashSaleDel(flash_sale_id, voucher_selected) {
            for (let item of voucher_selected) {
                if (item == flash_sale_id) return true;
            }
            return false;
        },
        async delFlashSale() {
            await actionAdmin.delFlashSale({
                params: {
                    flash_sales_del: this.voucher_selected,
                }
            }).then(res => {
                this.dataFlashSale = this.dataFlashSale.filter(voucher => {
                    if (this.checkFlashSaleDel(voucher.id, res.flash_sales_del) == false) {
                        return voucher
                    }
                })
            })
        },
        async searchAllFlashSalePage() {
            await actionAdmin.searchAllFlashSalePage({
                params: {
                    key_search: this.keySearch,
                    page: this.page,
                    number_quantity: this.numberQuantity,
                }
            }).then(res => {
                this.dataFlashSale = res.flash_sales
                this.showOption(1)
            })
        },
        backProduct() {
            this.$store.dispatch('dashboard/actionSelectedLayout', { type: 4 })
        },
        async getFlashSale() {
            await actionAdmin.getAllFlashSalePage({
                params: {
                    page: this.page,
                    number_quantity: this.numberQuantity,
                    level: this.levelVoucher
                }
            }).then(res => {
                this.dataFlashSale = res.flash_sales
            })
        },
        showOption(type) {
            this.$store.dispatch('dashboard/actionShowFlashSale', { type: type })
            if (type == 3) {
                this.getAllFlashSaleNoProductPage()
            }
        },
        async getAllFlashSaleNoProductPage() {
            await actionAdmin.getAllFlashSaleNoProductPage({
                params: {
                    page: this.page,
                    number_quantity: this.numberQuantity,
                }
            }).then(res => {
                this.dataFlashSaleEmpty = res.flash_sales
            })
        }
    },
    async created() {
        await actionAdmin.getAllFlashSalePage({
            params: {
                page: this.page,
                number_quantity: this.numberQuantity,
                level: this.levelVoucher
            }
        }).then(res => {
            this.dataFlashSale = res.flash_sales
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