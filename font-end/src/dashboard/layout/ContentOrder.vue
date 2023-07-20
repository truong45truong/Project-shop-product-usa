
<template>
    <div class="row mx-2 p-2">
        <div class="col-lg-3">
            <div class="single_analite_content text-dark text-center"
                :class="{ 'click-option-product': isShowOrderRequest }" @click="selectedContent(1)">
                <font-awesome-icon icon="fa-solid fa-warehouse" class="my-3 icon-product-db"
                    :class="{ 'icon-option-product': isShowOrderRequest }" />
                <b>
                    <p class="m-2 pb-5" :class="{ 'text-option-product': isShowOrderRequest }">
                        Danh sách Đơn hàng yêu cầu
                    </p>
                </b>
            </div>
        </div>
        <div class="col-lg-3">
            <div class="single_analite_content text-dark text-center"
                :class="{ 'click-option-product': isShowOrderConfirm }" @click="selectedContent(2)">
                <font-awesome-icon icon="fa-solid fa-plus" class="my-3 icon-product-db"
                    :class="{ 'icon-option-product': isShowOrderConfirm }" />
                <b>
                    <p class="m-2 pb-5" :class="{ 'text-option-product': isShowOrderConfirm }">
                        Danh sách đơn hàng đã xác nhận
                    </p>
                </b>
            </div>
        </div>
        <div class="col-lg-3">
            <div class="single_analite_content text-dark text-center" :class="{ 'click-option-product': isShowOrderPayed }"
                @click="selectedContent(3)">
                <font-awesome-icon icon="fa-solid fa-ticket" class="my-3 icon-product-db"
                    :class="{ 'icon-option-product': isShowOrderPayed }" />
                <b>
                    <p class="m-2 pb-5" :class="{ 'text-option-product': isShowOrderPayed }">
                        Danh sách đơn hàng đã thanh toán
                    </p>
                </b>
            </div>
        </div>
        <div class="col-lg-3">
            <div class="single_analite_content text-dark text-center" :class="{ 'click-option-product': isShowAllOrder }"
                @click="selectedContent(4)">
                <font-awesome-icon icon="fa-solid fa-bolt-lightning" class="my-3 icon-product-db"
                    :class="{ 'icon-option-product': isShowAllOrder }" />
                <b>
                    <p class="m-2 pb-5" :class="{ 'text-option-product': isShowAllOrder }">
                        Tất cả đơn hàng
                    </p>
                </b>
            </div>
        </div>
    </div>
    <div v-if="isShowOrderRequest" class="row">
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
    <div v-if="photo_qrcode != false" class="d-flex flex-column align-items-center">
        <h3 class="my-3">Qr code</h3>
        <img class="img-product-item text-center" :src="'http://127.0.0.1:8000' +`${photo_qrcode}`" alt="name">
    </div>
    <div v-if="isShowOrderRequest" class="row">
        <table class="responstable">

            <tr>
                <th>STT</th>
                <th>Người mua</th>
                <th>Ngày tạo</th>
                <th>Người nhận</th>
                <th> Địa chỉ nhận</th>
                <th> Số điện thoại</th>
                <th> Ghi chú</th>
                <th> Thanh toán</th>
                <th> ĐVVC</th>
                <th> Chọn</th>
                <th> Qr </th>
            </tr>

            <tr v-for="item, index in dataOrderRequest" class="tr-product-admin">
                <td @click="showDetailProduct(item.id)"> {{ index }} </td>
                <td @click="showDetailProduct(item.id)">{{ item.user_email }}</td>
                <td @click="showDetailProduct(item.id)">{{ item.datetime }}</td>
                <td @click="showDetailProduct(item.id)">{{ item.receiver }}</td>
                <td @click="showDetailProduct(item.id)">{{ item.address_receiver }}</td>
                <td @click="showDetailProduct(item.id)">{{ item.phone_receiver }}</td>
                <td @click="showDetailProduct(item.id)">{{ item.note }}</td>
                <td @click="showDetailProduct(item.id)">{{ item.total_price }}</td>
                <td @click="showDetailProduct(item.id)">{{ item.transport_name }}</td>

                <td class="">
                    <button class="button-28" :class="{ 'button-28-selected': checkOrderSelect(item.id) }" role="button"
                        @click="appendOrderSelected(item.id)">
                        <span class="" v-if="checkOrderSelect(item.id)"> Đã chọn </span>
                        <span class="" v-if="!checkOrderSelect(item.id)"> Chọn </span>
                    </button>
                </td>
                <td> 
                    <button v-if="item.qr_code_id" class="button-28" @click="setImgQrcode(item.qr_code_id.qrcode)">
                        QrCode
                    </button>
                    <p v-if="item.qr_code_id == null " class="m-0">
                        Không có
                    </p>
                </td>
            </tr>
        </table>
        <div class="row">
            <div class="col-sm-4 p-2">
                <button class="btn btn-dark" @click="confirmOrder">
                    Xác nhận đơn
                </button>
            </div>
            <div class="col-sm-4 p-2">
                <button class="btn btn-dark" @click="cancelOrder">
                    Hủy đơn
                </button>
            </div>
        </div>
    </div>
    <div v-if="isShowOrderConfirm" class="row m-2 border">
        <table class="responstable">

            <tr>
                <th>STT</th>
                <th>Người mua</th>
                <th>Ngày tạo</th>
                <th>Người nhận</th>
                <th> Địa chỉ nhận</th>
                <th> Số điện thoại</th>
                <th> Ghi chú</th>
                <th> Thanh toán</th>
                <th> ĐVVC</th>
                <th> Chọn</th>
                <th> Qr </th>
            </tr>

            <tr v-for="item, index in dataOrderConfim" class="tr-product-admin">
                <td @click="showDetailProduct(item.id)"> {{ index }} </td>
                <td @click="showDetailProduct(item.id)">{{ item.user_email }}</td>
                <td @click="showDetailProduct(item.id)">{{ item.datetime }}</td>
                <td @click="showDetailProduct(item.id)">{{ item.receiver }}</td>
                <td @click="showDetailProduct(item.id)">{{ item.address_receiver }}</td>
                <td @click="showDetailProduct(item.id)">{{ item.phone_receiver }}</td>
                <td @click="showDetailProduct(item.id)">{{ item.note }}</td>
                <td @click="showDetailProduct(item.id)">{{ item.total_price }}</td>
                <td @click="showDetailProduct(item.id)">{{ item.transport_name }}</td>

                <td class="">
                    <button class="button-28" :class="{ 'button-28-selected': checkOrderSelect(item.id) }" role="button"
                        @click="appendOrderSelected(item.id)">
                        <span class="" v-if="checkOrderSelect(item.id)"> Đã chọn </span>
                        <span class="" v-if="!checkOrderSelect(item.id)"> Chọn </span>
                    </button>
                </td>
                <td> 
                    <button v-if="item.qr_code_id" class="button-28" @click="setImgQrcode(item.qr_code_id.qr_code)">
                        QrCode
                    </button>
                    <p v-if="item.qr_code_id == null " class="m-0">
                        Không có
                    </p>
                </td>
            </tr>
        </table>
        <div class="btn btn-dark m-2" @click="cancelOrder">
            Hủy
        </div>
    </div>
    <div v-if="isShowOrderPayed" class="row m-2 border">
        <table class="responstable">

            <tr>
                <th>STT</th>
                <th>Người mua</th>
                <th>Ngày tạo</th>
                <th>Người nhận</th>
                <th> Địa chỉ nhận</th>
                <th> Số điện thoại</th>
                <th> Ghi chú</th>
                <th> Thanh toán</th>
                <th> ĐVVC</th>
                <th> Chọn</th>
            </tr>

            <tr v-for="item, index in dataOrderPaymented" class="tr-product-admin">
                <td @click="showDetailProduct(item.id)"> {{ index }} </td>
                <td @click="showDetailProduct(item.id)">{{ item.user_email }}</td>
                <td @click="showDetailProduct(item.id)">{{ item.datetime }}</td>
                <td @click="showDetailProduct(item.id)">{{ item.receiver }}</td>
                <td @click="showDetailProduct(item.id)">{{ item.address_receiver }}</td>
                <td @click="showDetailProduct(item.id)">{{ item.phone_receiver }}</td>
                <td @click="showDetailProduct(item.id)">{{ item.note }}</td>
                <td @click="showDetailProduct(item.id)">{{ item.total_price }}</td>
                <td @click="showDetailProduct(item.id)">{{ item.transport_name }}</td>

                <td class="">
                    <button class="button-28" :class="{ 'button-28-selected': checkOrderSelect(item.id) }" role="button"
                        @click="appendOrderSelected(item.id)">
                        <span class="" v-if="checkOrderSelect(item.id)"> Đã chọn </span>
                        <span class="" v-if="!checkOrderSelect(item.id)"> Chọn </span>
                    </button>
                </td>
            </tr>
        </table>
        <div class="btn btn-dark m-2" @click="cancelOrder">
            Hủy
        </div>
    </div>
</template>
    
<script>
import { mapGetters } from 'vuex'
import { useRoute } from 'vue-router'
import { actionAdmin } from './../../common/admin.service'
import { CategoryApiService } from './../../common/category.service'
import ListMediaComment from './../../layout/blog/ListMediaComment.vue'
import { Carousel, Navigation, Slide } from 'vue3-carousel'
import ImageSendComment from './../../components/blog/ImageSendComment.vue'
export default {
    name: "ContentOrder",
    setup() {
        const route = useRoute();
        return { route };
        watch(isShowOrderConfirm, (first, second) => {
            if(second == True){
                this.getOrderConfirm()
            }
        });
    },

    data: () => ({
        pageProduct: 1,
        numberQuantityPage: 20,
        dataOrderRequest: [],
        dataOrderConfirm : [],
        order_selected: [],
        dataOrderPaymented : [] ,
        keySearch: '',
        isShowOrderRequest: true,
        isShowOrderConfirm: false,
        isShowOrderPayed: false,
        isShowAllOrder: false,
        photo_qrcode : false,
        dataCategory: [],
        fileUpload: [],
        nameProductCreate: '',
        categoryProductCreate: '',
        sexProductCreate: '',
        priceProductCreate: '',
        saleProductCreate: '',
        quantityProductCreate: '',
        descriptionProductCreate: '',
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
        setImgQrcode(src){
            this.photo_qrcode = src
        },
        async getOrderRequest(){
            await actionAdmin.getAllOrderRequestPage({
                params: {
                    page: this.pageProduct,
                    number_quantity: this.numberQuantityPage
                }
            }).then(res => {
                console.log(res)
                this.dataOrderRequest = res.orders
            })
        },
        async getOrderPayment(){
            await actionAdmin.getAllOrderPaymentedPage({
                params: {
                    page: this.pageProduct,
                    number_quantity: this.numberQuantityPage
                }
            }).then(res => {
                this.dataOrderPaymented = res.orders
            })
        },
        async getOrderConfirm(){
            await actionAdmin.getAllOrderConfirmPage({
                params: {
                    page: this.pageProduct,
                    number_quantity: this.numberQuantityPage
                }
            }).then(res => {
                this.dataOrderConfim = res.orders
            })
        },
        selectedContent(type) {
            switch (type) {
                case 1:
                    this.isShowOrderRequest = true
                    this.isShowOrderConfirm = false
                    this.isShowOrderPayed = false
                    this.isShowAllOrder = false
                    break;
                case 2:
                    this.isShowOrderRequest = false
                    this.isShowOrderConfirm = true
                    this.order_selected = []
                    this.getOrderConfirm()
                    this.isShowOrderPayed = false
                    this.isShowAllOrder = false
                    break;
                case 3:
                    this.isShowOrderRequest = false
                    this.isShowOrderConfirm = false
                    this.isShowOrderPayed = true
                    this.isShowAllOrder = false
                    this.getOrderPayment()
                    break;
                case 4:
                    this.isShowOrderRequest = false
                    this.isShowOrderConfirm = false
                    this.isShowOrderPayed = false
                    this.isShowAllOrder = true
                    break;

                default:
                    this.isShowOrderRequest = true
                    this.isShowOrderConfirm = false
                    this.isShowOrderPayed = false
                    this.isShowAllOrder = false
                    break;
            }
        },
        appendOrderSelected(product_id) {
            if (this.checkOrderSelect(product_id) == true) {
                this.order_selected = this.order_selected.filter(val => {
                    return val != product_id
                })
            } else {
                this.order_selected = [product_id, ...this.order_selected]
            }
        },
        checkOrderSelect(product_id) {
            for (let item of this.order_selected) {
                if (item == product_id) return true;
            }
            return false;
        },
        checkProductDel(product_id, order_selected) {
            for (let item of order_selected) {
                if (item == product_id) return true;
            }
            return false;
        },
        /* ---------------------------------- order --------------------------------- */
        async confirmOrder() {
            await actionAdmin.confirmOrder({
                params: {
                    order_selected: this.order_selected,
                }
            }).then(res => {
                this.dataOrderRequest = this.dataOrderRequest.filter(product => {
                    if (this.checkProductDel(product.id, res.products_del) == false) {
                        return product
                    }
                })
            })
        },
        async cancelOrder() {
            await actionAdmin.cancelOrder({
                params: {
                    order_selected: this.order_selected,
                }
            }).then(res => {
                this.order_selected = []
                if(this.isShowOrderRequest == true){
                    this.getOrderRequest()
                }
                if(this.isShowOrderConfirm == true){
                    this.getOrderConfirm()
                }
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
                this.dataOrderRequest = res.products
            })
        },
        addCategoryLevel(length) {
            let text = "";
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
        async createProduct() {
            await actionAdmin.createProduct({
                params: {
                    media_file: this.fileUpload,
                    name: this.nameProductCreate,
                    category_id: this.categoryProductCreate,
                    sex: this.sexProductCreate,
                    price: this.priceProductCreate,
                    sale: this.saleProductCreate,
                    quantity: this.quantityProductCreate,
                    description: this.descriptionProductCreate,
                }
            }).then(res => {
                alert("thêm sản phẩm thành công")
                this.fileUpload = []
                this.nameProductCreate = ''
                this.categoryProductCreate = ''
                this.sexProductCreate = ''
                this.priceProductCreate = ''
                this.saleProductCreate = ''
                this.quantityProductCreate = ''
                this.descriptionProductCreate = ''
            })
        },
        showDetailProduct(product_id) {
            this.$store.dispatch('dashboard/actionSelectedDetailProduct', { product_id: product_id })
        }
    },
    async created() {
        await actionAdmin.getAllOrderRequestPage({
            params: {
                page: this.pageProduct,
                number_quantity: this.numberQuantityPage
            }
        }).then(res => {
            console.log(res)
            this.dataOrderRequest = res.orders
        })
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
    cursor: pointer;
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
    width: 100% !important;
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