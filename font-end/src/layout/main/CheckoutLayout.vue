<template>
    <div class="container mt-5" id="checkout-content">
        <h1><b><i>Thanh toán</i></b></h1>
        <div class="row border py-3">
            <div class="d-flex">
                <font-awesome-icon class="icon-address" icon="fa-solid fa-location-dot" />
                <p class="text-dark m-0  ms-3 text-address">Địa chỉ nhận hàng</p>
            </div>
            <div v-if="order" class="d-flex mt-1 align-items-center">
                <p class="m-0"><b>{{ order.receiver }} (+84) {{ order.phone_receiver.replace('0', '') }}</b></p>
                <button class="ms-3 button-change-address ps-0" @click="showChangePhone">
                    <p class="m-0 text-primary"> Thay đổi</p>
                </button>
                <p class="m-0 ms-3">{{ order.address_receiver }}</p>
                <div class="ms-3 default-address px-1">
                    <p class="m-0 text-danger">Mặc định</p>
                </div>
                <button class="ms-3 button-change-address ps-0" @click="showChangeAddress">
                    <p class="m-0 text-primary"> Thay đổi</p>
                </button>
            </div>
            <select-phone @update="updateReceiveOrder" v-if="isShowChangePhone" />
            <select-address @updateAddress="updateAddressReceiveOrder" v-if="isShowChangeAddress" />
        </div>
        <div class="mt-3 row py-3 border">
            <table class="table">
                <thead>
                    <tr>
                        <th scope="col">STT</th>
                        <th scope="col">Tên</th>
                        <th scope="col">Đơn giá</th>
                        <th scope="col">Số Lượng</th>
                        <th scope="col">Thành tiền</th>
                        <th scope='col'> Voucher </th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="item, index in products">
                        <!-- {{item}} -->
                        <th scope="row">{{ index }}</th>
                        <td>
                            <p class="m-0">{{ item.product_name }}</p>
                            <img class="img-checkout-product" :src="URL_PATH_SERVER + '/' + item.photo_product">
                        </td>
                        <td>{{ new Intl.NumberFormat('vi-VN').format(item.product_price_total) }} vnđ</td>
                        <td>{{ item.product_quantity }}</td>
                        <td>{{ new Intl.NumberFormat('vi-VN').format(item.product_price_total * item.product_quantity) }} vnđ
                        </td>
                        <td v-if="checkProductInVouher(item.product_slug)"> <b class="text-danger">Đã áp dụng</b> </td>
                        <td v-if="!checkProductInVouher(item.product_slug)"> Chưa áp dụng </td>
                    </tr>
                </tbody>
            </table>
            <div class="d-flex w-100">
                <div class="d-flex w-50">
                    <p class="m-0"> Lời nhắn: </p>
                    <textarea class="w-100" placeholder="Nhập nội dung ..."></textarea>
                </div>
                <div class="ms-2 d-flex align-items-center">
                    <p class="m-0 text-transport">Chọn đơn vị vận chuyển:</p>
                    <div class="ms-2">
                        <p class="m-0">{{ transport.transport_name }}</p>
                    </div>
                    <div class="ms-3 text-end">
                        <p class="m-0">Phí:
                            <span class="text-decrease">
                                {{ new Intl.NumberFormat('vi-VN').format(transport.transport_price) }}vnđ
                            </span>
                        </p>
                    </div>
                    <button class="button-change-address" @click="showChangeTransport">
                        <p class="m-0 text-primary"> Thay đổi </p>
                    </button>
                </div>
            </div>
            <select-transport v-if="isShowChangeTransport" @update="updateTransportChangeOrder" />
        </div>
        <div class="row mt-3 border py-3">
            <div class="col-sm-6">
                <p v-if="selectVoucher" class="m-0">
                    <b>Voucher:</b> Giảm {{ contentSelectVoucher.sale }}%
                    <span>(tối đa {{ contentSelectVoucher.limited_price }}k)</span>
                </p>
                <p v-if="!selectVoucher" class="m-0">
                    <b>Voucher:</b> Chưa Chọn
                </p>
            </div>
            <div class="col-sm-6 text-end">
                <button class="ms-3 button-change-address" @click="showChangeVoucher">
                    <p class="m-0 text-primary"> Chọn voucher</p>
                </button>
                <p v-if="selectVoucher" class="m-0 text-decrease">
                    Đã giảm {{ new Intl.NumberFormat('vi-VN').format(contentSelectVoucher.total_price_sale) }} vnđ
                </p>
            </div>
        </div>
        <select-voucher v-if="isShowChangeVoucher" @update="updateVoucherOrder" />
        <div class="row mt-3 border py-3">
            <div class="d-flex justify-content-between">
                <p class="m-0"> Phương thức thanh toán:</p>
                <div v-if="!changePayment"  class="d-flex">
                    <p class="m-0"> {{contentPayment}}</p>
                    <button class="ms-3 button-change-address" @click="changeMethodPayment()">
                        <p class="m-0 text-primary"> Thay đổi</p>
                    </button>
                </div>
                <div v-if="changePayment" class="p-3 border border-2">
                    <p class="my-2 cursor-pointer"  @click="setCod()"> Thanh toán khi nhận hàng </p>
                    <p class="my-2 cursor-pointer" @click="setPaypal()"> Thanh toán bằng Paypal </p>
                </div>
            </div>
            <div class="mt-3">
                <div v-if="order" class="d-flex flex-row-reverse">
                    <p class="m-0 "> Tổng tiền :
                        <span> {{ new Intl.NumberFormat('vi-VN').format(order.total_price) }} vnđ </span>
                    </p>
                </div>
                <div class="d-flex flex-row-reverse">
                    <p class="m-0 "> Phí vận chuyển :
                        <span> {{ new Intl.NumberFormat('vi-VN').format(transport.transport_price) }} vnđ </span>
                    </p>
                </div>
                <div v-if="selectVoucher" class="d-flex flex-row-reverse">
                    <p class="m-0">Voucher đã giảm : {{ new
                        Intl.NumberFormat('vi-VN').format(contentSelectVoucher.total_price_sale) }} vnđ</p>
                </div>
                <div class="d-flex flex-row-reverse">
                    <p class="m-0 "> Tổng thanh toán:
                        <span> {{ new Intl.NumberFormat('vi-VN').format(order.total_price + transport.transport_price -
                            contentSelectVoucher.total_price_sale) }} vnđ </span>
                    </p>
                </div>
            </div>
        </div>
        <div class="row mt-3">
            <div class="col-sm-4"></div>
            <div class="col-sm-4"></div>
            <div  class="col-4">
                <div :class="{ 'd-none' : isPaypal}" class="btn btn-dark px-4 py-2 mt-4 w-100">
                    Đặt hàng
                </div>
                <div :class="{ 'd-none' : !isPaypal}" id="paypal-button-container"></div>
            </div>
        </div>
    </div>
</template>

<script>
import VoucherInformation from './../../components/other/VoucherInformation.vue'
import { OrderAction } from './../../common/order.service'
import { URL_PATH_SERVER } from '../../common/constants';
import SelectAddress from './SelectAddress.vue';
import SelectPhone from './SelectPhone.vue'
import SelectTransport from './SelectTransport.vue'
import SelectVoucher from './SelectVoucher.vue'
import { loadScript } from '@paypal/paypal-js';
export default {
    name: "CheckoutLayout",
    props: {
        msg: ''
    },
    async mounted() {
    },
    data: () => ({
        products: [],
        URL_PATH_SERVER: URL_PATH_SERVER,
        order: false,
        nameOrder: '',
        transport: false,
        isShowChangeAddress: false,
        isShowChangePhone: false,
        isShowChangeTransport: false,
        isShowChangeVoucher: false,
        selectVoucher: false,
        contentSelectVoucher: {
            sale: 0,
            limited_price: 0,
            total_price_sale: 0
        },
        productSlugVoucer: [],
        changePayment: false,
        isPaypal : false,
        contentPayment : "thanh toán khi nhận hàng"
    }),
    components: {
        VoucherInformation,
        SelectAddress,
        SelectPhone,
        SelectTransport,
        SelectVoucher
    },
    async created() {
        this.nameOrder = this.$router.currentRoute.value.query.name
    },
    watch: {
        nameOrder(newNameOrder) {
            if (this.$router.currentRoute.value.query.name != 'false') {
                OrderAction.getOrderCheckout({
                    params: {
                        nameOrder: this.nameOrder
                    }
                }).then(res => {
                    if (res == '') {
                        this.$router.push({ name: 'error' });
                    }
                    this.products = res.success[0].products
                    this.order = res.success[0].order
                    this.transport = res.success[0].transport
                }).catch(error => {
                    console.log("error orcer checkout", error)
                })
            } else {
                this.$router.push({ name: 'error' });
            }
        },
    },
    methods: {
        changeMethodPayment(){
            this.changePayment = !this.changePayment;
        },
        async setPaypal(){
            this.isPaypal = true ;
            this.changePayment = false;
            this.contentPayment = "thanh toán Paypal"
            const price = ((this.order.total_price + this.transport.transport_price -this.contentSelectVoucher.total_price_sale) / 23252).toFixed(1); 
            console.log(price)
            const orderName = this.$router.currentRoute.value.query.name
            const paypalSdk = await loadScript({
                'client-id': 'AW2NAbUhOu7zPCOIFW-4tZz7rUnKrSznrs13cp25WQyvP-fnXexYov3PXzF5SSX50V9BBFM206c3jBYl',
                currency: 'USD',
            });
            const history_page = localStorage.getItem("history_page")
            paypalSdk.Buttons({
                createOrder: function (data, actions) {
                    // Set the price and order ID dynamically
                    return actions.order.create({
                        purchase_units: [{
                            amount: {
                                value: price,
                                currency_code: 'USD',
                            },
                            reference_id: orderName,
                        }],
                    });
                },
                onApprove: async function (data, actions) {
                    // Redirect to a webpage after successful payment
                    await OrderAction.paymentSuccess({
                        params : {
                            type : true ,
                            total_price : price,
                            name_order : orderName
                        }
                    }).then(res => {
                        window.location.href = "http://localhost:5173/profile/?nameOrder=" + orderName;
                    })
                },
            }).render('#paypal-button-container');
        },
        setCod(){
            this.isPaypal = false ;
            this.changePayment = false;
            this.contentPayment = "thanh toán khi nhận hàng"
        },
        showChangeAddress() {
            this.isShowChangeAddress = !this.isShowChangeAddress;
        },
        showChangePhone() {
            this.isShowChangePhone = !this.isShowChangePhone;
        },
        showChangeTransport() {
            this.isShowChangeTransport = !this.isShowChangeTransport;
        },
        showChangeVoucher() {
            this.isShowChangeVoucher = !this.isShowChangeVoucher
        },
        async updateReceiveOrder(name, phone) {
            this.order.receiver = name
            this.order.phone_receiver = phone
            this.isShowChangePhone = false
            await OrderAction.updatePhoneOrderWaitingBePaid({
                params: {
                    receiver: name,
                    phone_receiver: phone,
                    name_order: this.nameOrder
                }
            })
        },
        async updateAddressReceiveOrder(address) {
            this.order.address_receiver = address
            this.isShowChangeAddress = false
            await OrderAction.updateAddressOrderWaitingBePaid({
                params: {
                    address_receiver: address,
                    name_order: this.nameOrder
                }
            })
        },
        async updateTransportChangeOrder(transport_id, name_transport, price) {
            this.transport.transport_name = name_transport
            this.isShowChangeTransport = false
            this.transport.transport_price = price
            await OrderAction.updateTransport({
                params: {
                    transport_id: transport_id,
                    name_order: this.nameOrder
                }
            })
        },
        checkProductInVouher(product_slug) {
            for (let product of this.productSlugVoucer) {
                if (product.product_slug_in_voucher == product_slug) return true

            }
            return false
        },
        async updateVoucherOrder(voucher_id, sale, limited_price, product_in_vouchers) {
            // this.transport.transport_name = name_transport
            this.isShowChangeVoucher = false
            this.productSlugVoucer = product_in_vouchers
            this.selectVoucher = true
            console.log(sale, limited_price)
            await OrderAction.updateVoucherOrderWaitungBePaid({
                params: {
                    voucher_id: voucher_id,
                    name_order: this.nameOrder
                }
            }).then(res => {
                console.log(res)
                this.contentSelectVoucher.sale = sale
                this.contentSelectVoucher.limited_price = limited_price
                this.contentSelectVoucher.total_price_sale = res.success

            })
        },

    }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.cursor-pointer {
    cursor:pointer;
}
.cursor-pointer:hover {
    color :rgb(22, 123, 206)
} 
.icon-address {
    font-size: 24px;
}

.text-address {
    font-size: 18px;
}

.default-address {
    border: 1px solid red;
}

.button-change-address {
    background-color: transparent;
    border: none;
}

.img-checkout-product {
    width: 100px;
}

.content-voucher {
    max-width: 300px;
}

#checkout-content .content-voucher {
    box-shadow: none;
}

.text-decrease {
    color: #ee4d2d
}

.text-transport {
    color: rgb(1, 86, 86)
}</style>
