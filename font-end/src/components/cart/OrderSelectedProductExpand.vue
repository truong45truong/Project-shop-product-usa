<template>
    <div class="container position-relative">
        <div class="row my-3">
            <div class="col-sm-2 text-center">
                <p class="fw-semibold" :class="{ 'text-selected-infor-order': !isActiveInforOrder.product }"
                    @click="loadData(1)">Sản phẩm</p>
                <p class="fw-semibold" :class="{ 'text-selected-infor-order': !isActiveInforOrder.voucher }"
                    @click="loadData(2)">Voucher </p>
                <p class="fw-semibold" :class="{ 'text-selected-infor-order': !isActiveInforOrder.receiver }"
                    @click="loadData(3)">Thông tin người nhận </p>
                <p class="fw-semibold" :class="{ 'text-selected-infor-order': !isActiveInforOrder.transport }"
                    @click="loadData(4)">Nhà vận chuyển </p>
            </div>
            <div v-if="isActiveInforOrder.product" class="col layout-product-order border border-1">
                <hr classs="mt-2" v-if="get_is_order_selected_product.data.length != 0" >
                <div class="text-center mt-5" v-if="get_is_order_selected_product.data.length == 0" >
                    <h3>Không có sản phẩm được chọn</h3>
                </div>
                <div class="col mt-2" v-for="product,index in get_is_order_selected_product.data" :key="product">
                    <product-order :slug="product.product_slug" :name="product.product_name"
                        :category="product.category_name" :photo="product.photo_product" :price="product.product_price" :numberProduct="product.product_quantity"
                        :sale='product.product_sale' :total_price="product.product_price_total" :voucher_activate = "product.voucher_activate"
                        :price_status="product.product_price_status" :indexOrder="indexOrder" :index="index" :price_after_voucher ="product.price_after_voucher" />
                    <hr>
                </div>
            </div>
            <div v-if="isActiveInforOrder.receiver" class="col border border-1">
                <div class="selected-infor-receiver">
                    <div class="row">
                        <div class="col-sm-6">
                            <h5 class="text-dark">Địa chỉ</h5>
                            <div class="w-100" v-for="address in isDataInforOrder.receiver.address" :key="address">
                                <div class="custom-control custom-radio">
                                    <input type="radio" class="custom-control-input" :id="address.id"
                                        :checked="address.id == get_is_order_selected_product.address.address.id"
                                        name="defaultExampleRadios" @click="changeAddress(address)">
                                    <label class="custom-control-label" :for="address.id">
                                        <p class="m-0">
                                            {{ address.address_content }}
                                            <span v-if="address.status == true" class="text-primary">(Mặc định)</span>
                                        </p>
                                    </label>
                                </div>
                            </div>
                        </div>
                        <div class="col-sm-6">
                            <h5 class="text-dark">Di động</h5>
                            <div class="w-100" v-for="phone in isDataInforOrder.receiver.phones" :key="phone">
                                <div class="custom-control custom-radio cursor">
                                    <input type="radio" class="custom-control-input" :id="phone.id"
                                        :checked="phone.id == get_is_order_selected_product.address.phone.id"
                                        name="defaultPhoneRadios" @click="changePhone(phone)">
                                    <label class="custom-control-label" :for="phone.id">
                                        <p class="m-0">
                                            <span class="ms-2">{{ phone.phone }}</span>
                                            <span class="ms-2">{{ phone.name }}</span>
                                            <span v-if="phone.status == true" class="ms-1 text-primary">(Mặc định)</span>
                                        </p>
                                    </label>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div v-if="isActiveInforOrder.voucher" class="col border border-1">
                <div class="row mb-2">
                    <div class="col-lg-3 col-md-4 col-sm-6 mt-2 d-flex justify-content-center" v-for="voucher in isDataInforOrder.voucher" :key="voucher">
                        <input v-if="get_is_order_selected_product.voucher != false" type="radio" class="me-2 form-control-radio" 
                        name="selectVoucher" @click="selectVoucher(voucher)"
                        :checked="get_is_order_selected_product.voucher.voucher.id == voucher.voucher.id" >
                        <input  v-if="get_is_order_selected_product.voucher == false" type="radio" class="me-2 form-control-radio" 
                        name="selectVoucher" @click="selectVoucher(voucher)"
                        >
                        <div class="voucher-item border-none">
                            <p class="m-0 text-voucher-main text-white my-2 mx-2">
                                Giảm :{{voucher.voucher.sale}}%
                                <span>(tối đa {{voucher.voucher.limited_price}}k)</span>
                            </p>    
                            <div class="voucher-item-left"></div>
                            <div class="voucher-item-right"></div>
                        </div>
                    </div>
                </div>
            </div>
            <div v-if="isActiveInforOrder.transport"  class="col border border-1 d-flex flex-column">
                <div class="row mb-2">
                    <div class="col-lg-3 col-md-4 col-sm-6 mt-2 d-flex flex-column justify-content-center"
                    v-for="transport in isDataInforOrder.transport" :key="transport"
                    >
                        <div class="m-auto mt-2 content-name-transport text-center" >
                            <div class="text-white">{{transport.name}}</div>
                        </div>
                        <div class="m-auto content-price-transport text-center">
                            <span class="text-white">
                                {{transport.price}} vnđ
                            </span>
                        </div>
                        <input type="radio" class="mt-2 form-control-radio2" 
                        name="selectTransport" @click="selectTransport(transport)"
                        :checked="get_is_order_selected_product.transport.id == transport.id">
                    </div>
                </div>
            </div>
        </div>
    </div>  
    <div class="container position-relative mb-5">
        <div class="row w-100">
            <div class="col-sm-4">
                <voucher-information/>
            </div>
            <div class="col-sm-4">
                <div class="d-flex flex-column">
                    <div class="d-flex align-items-center">
                        <p class="my-2 ms-2 fs-5">Chọn sản phẩm</p>
                        <input type="checkbox" class="my-2 ms-2 fs-4">
                        <span> (Tất cá : {{ get_is_number_product }}) </span>
                    </div>
                    <div class="d-flex align-items-center">
                        <p class="my-2 ms-2 fs-5">
                            Thanh toán : {{ get_is_order_selected_product.numberProduct }}
                            <span class="text-span-modify"> (Sản phẩm) </span>
                        </p>
                    </div>
                    <div class="d-flex align-items-center">
                        <p v-if="inForReceiver.address != false " class="my-2 ms-2 fs-5">
                            Giao hàng tại :
                            <span class="text-span-modify"> {{ inForReceiver.address.address_content }} </span>
                        </p>
                    </div>
                    <div class="d-flex align-items-center">
                        <p v-if="inForReceiver.address != false " class="my-2 ms-2 fs-5">
                            Người nhận :
                            <span class="text-span-modify"> {{ inForReceiver.phone.name }}  ({{inForReceiver.phone.phone}}) </span>
                        </p>
                    </div>
                    <div class="d-flex align-items-center">
                        <p v-if="get_is_order_selected_product.transport != false " class="my-2 ms-2 fs-5">
                            ĐV Vận Chuyển :
                            <span class="text-span-modify"> {{ get_is_order_selected_product.transport.name }}({{get_is_order_selected_product.transport.price}}vnđ) </span>
                        </p>
                    </div>
                </div>
            </div>
            <div class="col-sm-4">
                <div class="d-flex flex-column justify-content-between align-items-end">
                    <div v-if="get_is_order_selected_product.numberProduct == 0 " class="total-price-layout text-center py-1 ms-2 mt-2">
                        {{ get_is_order_selected_product.totalPrice }} <span>vnđ</span>
                    </div>
                    <div v-if="get_is_order_selected_product.numberProduct > 0" class="total-price-layout text-center py-1 ms-2 mt-2">
                        {{ get_is_order_selected_product.totalPrice  +  get_is_order_selected_product.transport.price }} <span>vnđ</span>
                    </div>
                    <button v-if="get_is_order_selected_product.numberProduct > 0" class="button-57 ms-2 mt-3" role="button" @click="buyProduct">
                        <span class="text">Mua Ngay</span>
                        <span>Click để chuyển trang</span>
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script>
import VoucherInformation from './../other/VoucherInformation.vue'
import {VoucherAction}  from './../../common/voucher.service'
import  { ApiService } from './../../common/api.service'
import { mapGetters, mapActions } from 'vuex'
import { actionUser } from './../../common/user.service'
import ProductOrder from './../product/ProductOrder.vue'
import {OrderAction} from './../../common/order.service'
export default ({
    name: 'OrderSelectedProductExpand',
    props: {
        msg : '',
        indexOrder : ''
    },
    data: () => ({
        isActiveInforOrder: {
            product: true,
            voucher: false,
            receiver: false,
            transport: false,
        },
        isDataInforOrder: {
            voucher: false,
            receiver: false,
            transport: false,
        },
        inForReceiver: {
            address: false,
            phone: false,
            transport : false
        }
    }),
    components: {
        VoucherInformation,
        ProductOrder
    },
    computed: {
        ...mapGetters('cart', {
            get_is_number_product: 'getNumberProduct',
            get_is_order_selected_product: 'getorderSelectedProduct',
        }),
    },
    methods: {
        async buyProduct(){
            console.log(this.get_is_order_selected_product)
            let listProductSLugSelected = []
            for (let productSelected of this.get_is_order_selected_product.data){
                listProductSLugSelected.push({
                    slug : productSelected.product_slug ,
                    quantity : productSelected.product_quantity
                })
            }
            var voucher_id = false
            if (this.get_is_order_selected_product.voucher != false){
                voucher_id = get_is_order_selected_product.voucher.voucher.id
            }
            await OrderAction.createOrderWaitingBePaid({
                params : {
                    phone_id : this.get_is_order_selected_product.address.phone.id,
                    address_id : this.get_is_order_selected_product.address.address.id,
                    transport_id : this.get_is_order_selected_product.transport.id,
                    voucher_id : voucher_id,
                    products : listProductSLugSelected
                }
            }).then(res => {
                this.$router.push({
                    name : 'checkout' , query : {
                        name : res.name_order
                    }
                })
            })

        },
        async loadData(type) {
            switch (type) {
                case 1:
                    this.isActiveInforOrder.receiver = false;
                    this.isActiveInforOrder.product = true;
                    this.isActiveInforOrder.transport = false;
                    this.isActiveInforOrder.voucher = false;
                    break;
                case 2:
                    this.isActiveInforOrder.receiver = false;
                    this.isActiveInforOrder.product = false;
                    this.isActiveInforOrder.transport = false;
                    this.isActiveInforOrder.voucher = true;
                    break;
                case 3:
                    this.isActiveInforOrder.receiver = true;
                    this.isActiveInforOrder.product = false;
                    this.isActiveInforOrder.transport = false;
                    this.isActiveInforOrder.voucher = false;
                    break;
                case 4:
                    this.isActiveInforOrder.receiver = false;
                    this.isActiveInforOrder.product = false;
                    this.isActiveInforOrder.transport = true;
                    this.isActiveInforOrder.voucher = false;
                    break;
            }
        },
        changeAddress(address){
            this.inForReceiver.address = address
            this.$store.dispatch('cart/actionSelectedAddress', { address: {
                address : this.inForReceiver.address,
                phone : this.inForReceiver.phone
            }})
        },
        changePhone(phone){
            this.inForReceiver.phone = phone
            this.$store.dispatch('cart/actionSelectedAddress', { address: {
                address : this.inForReceiver.address,
                phone : this.inForReceiver.phone
            }})
        },
        selectVoucher(voucher){
            this.$store.dispatch('cart/actionSelectedVoucher', { voucher: voucher})
        },
        selectTransport(transport){
            this.inForReceiver.transport = transport
            this.$store.dispatch('cart/actionSelectedTransport', { transport: transport})
        }
    },
    async created() {
        await actionUser.getInforUser({
            params: {
                email_user: localStorage.getItem('user'),
                token_permission_infor_user: localStorage.getItem('token_permission_infor_user')
            }
        }).then(async (response) => {
            this.isDataInforOrder.receiver = {
                address: response.user.address,
                phones: response.user.phones,
            }
            this.isDataInforOrder.receiver.address.filter((address) => {
                if (address.status == true) {
                    this.inForReceiver.address = address
                }
            })
            this.isDataInforOrder.receiver.phones.filter((phone) => {
                if (phone.status == true) {
                    this.inForReceiver.phone = phone
                }
            })
            if(this.get_is_order_selected_product.address == false){
                this.$store.dispatch('cart/actionSelectedAddress', { address: {
                    address : this.inForReceiver.address,
                    phone : this.inForReceiver.phone
                }})
            }

        });
        await VoucherAction.actionGetVoucher({
            params: {
                email_user: localStorage.getItem('user'),
                token_permission_infor_user: localStorage.getItem('token_permission_infor_user')
            }
        }).then(res => {
            this.isDataInforOrder.voucher = res.data
            console.log(res.data)
        })
        await ApiService.query('transport/').then(res => {
            this.isDataInforOrder.transport = res.data.data
            this.$store.dispatch('cart/actionSelectedTransport', { transport: res.data.data[0]})
        })

    }

})
</script>
<style lang="scss">
.cursor {
    cursor: pointer !important;
}

.button-57 {
    max-width: 200px;
    min-width: 200px;
    position: relative;
    overflow: hidden;
    border: 1px solid #18181a;
    color: #18181a;
    display: inline-block;
    font-size: 15px;
    line-height: 15px;
    padding: 18px 18px 17px;
    text-decoration: none;
    cursor: pointer;
    background: #fff;
    user-select: none;
    -webkit-user-select: none;
    touch-action: manipulation;
}

.button-57 span:first-child {
    position: relative;
    transition: color 600ms cubic-bezier(0.48, 0, 0.12, 1);
    z-index: 10;
}

.button-57 span:last-child {
    color: white;
    display: block;
    position: absolute;
    bottom: 0;
    transition: all 500ms cubic-bezier(0.48, 0, 0.12, 1);
    z-index: 100;
    opacity: 0;
    top: 50%;
    left: 50%;
    transform: translateY(225%) translateX(-50%);
    height: 14px;
    line-height: 13px;
}

.button-57:after {
    content: "";
    position: absolute;
    bottom: -50%;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: linear-gradient(to right bottom, #3d3d3d, #181717, #444444, #0e0c0c) !important;
    transform-origin: bottom center;
    transition: transform 600ms cubic-bezier(0.48, 0, 0.12, 1);
    transform: skewY(9.3deg) scaleY(0);
    z-index: 50;
}

.button-57:hover:after {
    transform-origin: bottom center;
    transform: skewY(9.3deg) scaleY(2);
}

.button-57:hover span:last-child {
    transform: translateX(-50%) translateY(-100%);
    opacity: 1;
    transition: all 900ms cubic-bezier(0.48, 0, 0.12, 1);
}

.text-selected-infor-order {
    opacity: 0.5;
    cursor: pointer;
}

.text-selected-infor-order:hover {
    opacity: 1;
}
.voucher-item {
    background-image: linear-gradient(to right bottom, #d61717, #c41a1a, #e9700c, #fdbd5d) !important; 
    position:relative;
    overflow:hidden;
    padding: 0 15px;
    max-width:200px;
}
.voucher-item-left:before {
    content: "";
    position: absolute;
    left:93%;
    top:17%;
    width: 25px;
    height: 25px;
    border: 1px solid #e5e9ec;
    border-radius: 50%;
    background: #f8f9fa;
}
.voucher-item-right:before {
    content: "";    
    position: absolute;
    left:-7%;
    top:17%;
    width: 25px;
    height: 25px;
    border: 1px solid #e5e9ec;
    border-radius: 50%;
    background: #f8f9fa;
    /* Change THIS when changing container background color*/
}
.text-voucher-main{
    font-size: 14px;
}
.content-name-transport {
    background-image: linear-gradient(to right bottom, #d61717, #c41a1a, #e9700c, #fdbd5d) !important; 
    min-width:200px;
    padding: 0 15px;
    max-width:200px;
}
.content-price-transport{
    min-width:200px;
    background-image: linear-gradient(to right bottom, #4e4f50, #2c2f33, #282929, #5e5f5f) !important; 
}
.form-control-radio {
  font-family: system-ui, sans-serif;
  font-size: 2rem;
  font-weight: bold;
  line-height: 1.1;
  display: grid;
  grid-template-columns: 1.5rem;
  gap: 0.5em;
}
.form-control-radio2 {
  font-family: system-ui, sans-serif;
  font-size: 2rem;
  font-weight: bold;
  line-height: 1.1;
  display: grid;
  grid-template-columns: 1.5rem;
  gap: 0.5rem;
}
</style>