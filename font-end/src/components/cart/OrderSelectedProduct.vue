<template>
    <div class="shadow w-100"
        v-bind:class="[isShowDetailTotalSelectProduct == true ? 'detail-total-selected-items ' : 'detail-total-selected-items-down ']"
        :class="{ 'h-100 position-fixed' : isExpandDetailTotalSelectProduct}"
        >
        <font-awesome-icon v-if="isShowDetailTotalSelectProduct" class="pull-down-detail fs-3 text-white"
            icon="fa-solid fa-angle-down" @click="showDetailTotalSelectedProduct" />
        <div class="pull-up-detail-total text-center" @click="showExpandDetailTotalSelectedProduct">
            <span v-if="!isExpandDetailTotalSelectProduct" class="text-white text-center w-100">
                click để xem chi tiết sản phẩm đã chọn
            </span>
            <span v-if="isExpandDetailTotalSelectProduct" class="text-white text-center w-100">
                click để thu nhỏ
            </span>
        </div>
        <div v-if="!isExpandDetailTotalSelectProduct" class="container mb-2">
            <div class="row mt-1">
                <div class="col-sm-6">
                    <div class="d-flex mt-1">
                        <voucher-information />
                        <div class="d-flex flex-column">
                            <div class="d-flex align-items-center">
                                <p class="my-2 ms-2 fs-4">Chọn sản phẩm</p>
                                <input type="checkbox" class="my-2 ms-2 fs-4">
                                <span> (Tất cá : {{ get_is_number_product }}) </span>
                            </div>
                            <div class="d-flex align-items-center">
                                <p class="my-2 ms-2 fs-5">
                                    Thanh toán : {{ get_is_order_selected_product.numberProduct }}
                                    <span class="text-span-modify"> (Sản phẩm) </span>
                                </p>
                            </div>
                            <div class="total-price-layout text-center py-1 ms-2">
                                {{ get_is_order_selected_product.totalPrice }} <span>vnđ</span>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-sm-6 border border-dark border-1 text-center">
                    <p class="text-dark m-0 fw-semibold"> Sản phẩm đã chọn</p>
                    <p v-if="get_is_order_selected_product.data.length < 1" class="text-dark fs-4 m-0 fw-semibold mt-3">
                        Không có sản phẩm
                    </p>
                    <Carousel v-if="get_is_order_selected_product.data.length > 0" :settings="settings" :breakpoints="breakpoints">
                        <Slide v-for="slide in get_is_order_selected_product.data" :key="slide">
                            <div class="carousel__item">
                                <img class="slide-selected-product"
                                    :src="'http://127.0.0.1:8000/' + `${slide.photo_product}`" alt="">
                            </div>
                        </Slide>

                        <template #addons>
                            <Pagination />
                            <Navigation />
                        </template>
                    </Carousel>
                </div>
            </div>
        </div>
        <div class="layout-expand-selected-product">
            <order-selected-product-expand v-if="isExpandDetailTotalSelectProduct" />
        </div>
    </div>
    <font-awesome-icon v-if="!isShowDetailTotalSelectProduct" class="pull-up-detail fs-3 text-white"
        icon="fa-solid fa-angle-up" @click="showDetailTotalSelectedProduct" />
</template>
  
<script>
import VoucherInformation from './../other/VoucherInformation.vue'
import { Carousel, Navigation, Slide, Pagination } from 'vue3-carousel'
import { mapGetters, mapActions } from 'vuex'
import ProductOrder from './../product/ProductOrder.vue'
import OrderSelectedProductExpand from './OrderSelectedProductExpand.vue'
export default ({
    name: 'OrderSelectedProduct',
    props: {

    },
    data: () => ({
        isShowDetailTotalSelectProduct: true,
        isExpandDetailTotalSelectProduct: false,
        isActiveInforOrder : {
            product : true,
            voucher : false,
            address : false,
            transport : false,
        },
        settings: {
            itemsToShow: 4,
            snapAlign: 'center',
        },
        // breakpoints are mobile first
        // any settings not specified will fallback to the carousel settings
        breakpoints: {
            400: {
                itemsToShow: 2,
                snapAlign: 'center',
            },
            // 700px and up
            700: {
                itemsToShow: 3,
                snapAlign: 'center',
            },
            // 1024 and up
            1024: {
                itemsToShow: 4,
                snapAlign: 'center',
            },
        },
    }),
    components: {
        VoucherInformation,
        Pagination,
        Carousel,
        Slide,
        Navigation,
        ProductOrder,
        OrderSelectedProductExpand
    },
    computed: {
        ...mapGetters('cart', {
            get_is_number_product: 'getNumberProduct',
            get_is_order_selected_product: 'getorderSelectedProduct',
        }),
    },
    methods: {
        showDetailTotalSelectedProduct() {
            this.isShowDetailTotalSelectProduct = !this.isShowDetailTotalSelectProduct
        },
        showExpandDetailTotalSelectedProduct() {
            this.isExpandDetailTotalSelectProduct = !this.isExpandDetailTotalSelectProduct;
        }
    }

})
</script>
<style lang="scss">
@mixin keyframes($animation-name) {
    @-webkit-keyframes #{$animation-name} {
        @content;
    }

    @-moz-keyframes #{$animation-name} {
        @content;
    }

    @-ms-keyframes #{$animation-name} {
        @content;
    }

    @-o-keyframes #{$animation-name} {
        @content;
    }

    @keyframes #{$animation-name} {
        @content;
    }
}

@mixin animation($str) {
    -webkit-animation: #{$str};
    -moz-animation: #{$str};
    -ms-animation: #{$str};
    -o-animation: #{$str};
    animation: #{$str};
}

@include keyframes(detailTotalSeletedItemUp) {
    0% {
        bottom: -100%;
    }

    100% {
        bottom: 0%;
    }
}

@include keyframes(detailTotalSeletedItemDown) {
    0% {
        bottom: 0%;
    }

    100% {
        bottom: -100%;
    }
}

@include keyframes(down-arrow-before) {
    50% {
        transform: rotate(45deg) translate(70%, 70%);
    }

    100% {
        transform: rotate(45deg) translate(70%, 70%);
    }
}

@include keyframes(down-arrow-after) {
    50% {
        transform: rotate(45deg) translate(110%, 110%);
        opacity: 0;
    }

    51% {
        transform: rotate(45deg) translate(-130%, -130%);
    }

    100% {
        transform: rotate(45deg) translate(-70%, -70%);
        opacity: 1;
    }
}
.height-title {
    min-height: 80px;
}
.detail-total-selected-items {
    max-height: fit-content;
    background: white;
    position :fixed;
    bottom: 0%;
    @include animation('detailTotalSeletedItemUp 0.5s 1');
}

.detail-total-selected-items-down {
    cursor: pointer;
    position:fixed;
    bottom: -100%;
    background: white;
    z-index: 999;
    @include animation('detailTotalSeletedItemDown 1s 1');
}

.pull-up-detail {
    position: fixed;
    bottom: 0%;
    right: 4%;
    width: 5vw;
    background: linear-gradient(to bottom, #d1d2d3, #7a7a7a 100%);

}

.text-span-modify {
    font-size: 16px;
}

.pull-down-detail {
    position: absolute;
    top: 0%;
    width: 5vw;
    right: 4%;
    background: linear-gradient(to top, #afafaf, #777777 100%);
}

.total-price-layout {
    background-image: linear-gradient(to right bottom, #3d3d3d, #181717, #444444, #0e0c0c) !important;
    color: white;
    font-size: 18px;
    font-weight: 400;
    width:fit-content;
    min-width: 200px;
    span {
        font-weight: 800;
        font-size: 16px;
    }
}

.pull-up-detail-total {
    cursor: pointer;
    width: 100%;
    background-image: linear-gradient(to right bottom, #3d3d3d, #181717, #444444, #0e0c0c) !important;
    padding: 2px 0;
}

.slide-selected-product {
    max-width: 100px;
}

.pagination-container {
    background-color: rgb(36, 41, 47);
    padding: 10px;
    margin-top: 10px;
}

.carousel__icon {
    color: white;
}

.carousel__icon path {
    color: white;
    font-size: larger;
}

.pagination-button {
    background-color: rgb(36, 41, 47);
    color: white;
    font-size: 14px;
    padding: 8px 16px;
    border: 1px solid #ccc;
    border-radius: 5px;
    margin-right: 8px;
}
.layout-expand-selected-product {
    position:fixed;
    width:100%;
    height:100%;
    overflow-y:auto;
}
.layout-expand-selected-product::-webkit-scrollbar {
  display: none;
}
</style>