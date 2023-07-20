<template>
    <div class="container">
        <div class="text-center my-3">
            <h1 class="">THÔNG TIN</h1>
        </div>
        <div class="row mt-2 mx-2 border p-2">
            <div class="d-flex flex-column align-items-center mt-3 col-2">
                <img class="img-infor-profile" :src="inforUser.photo" :alt="inforUser.photo" />
                <div class="">
                    <input class="choose-file" type="file" ref="imagePhoto" id="choose-file" @change="uploadPhoto" multiple>
                    <label for="choose-file" class="upload-file"> {{ messageChooseFile }} </label>
                </div>
                <hr>
                <div class="">
                    <p class="is-action-profile" :class="[isActivateProfile ? 'is-activa-profile ' : '']"
                        @click="showActivateProfile">
                        <b> Thông tin Cá nhân </b>
                    </p>
                    <p class="is-action-profile" :class="[isActivateOrderBePaid ? 'is-activa-profile ' : '']"
                        @click="showActivateOrderBePaid">
                        <b>Đơn chờ thanh toán</b>
                    </p>
                    <p class="is-action-profile" :class="[isActivateOrderPaied ? 'is-activa-profile ' : '']"
                        @click="showActivateOrderPaided">
                        <b>Đơn đã thanh toán</b>
                    </p>
                    <p class="is-action-profile" :class="[isActivateOrderBought ? 'is-activa-profile ' : '']"
                        @click="showActivateOrderBought">
                        <b>Đơn đã mua</b>
                    </p>
                </div>
            </div>
            <div v-if="isActivateProfile && inforOrder == false" class="col">
                <div class="w-100 row border p-2 m-2">
                    <div class="col-6 d-flex align-items-center justify-content-center">
                        <p class="m-0 me-3"> <b class="">Tên : </b> </p>
                        <input type="text" class="p-1 border form-input-profile" v-model="inforUser.name">
                    </div>
                    <div class="col-6 d-flex align-items-center justify-content-center mt-2">
                        <p class="m-0 me-3"> <b class="">Email : </b> </p>
                        <input type="text" class="p-1 border form-input-profile" v-model="inforUser.email">
                    </div>
                    <div class="col d-flex mt-2 justify-content-center">
                        <button class="btn btn-dark" @click="uploadInformation">Lưu thông tin</button>
                    </div>
                </div>
                <div class="selected-action w-100 mt-3 border p-2 m-2">
                    <div class="content-address m-3">
                        <div class="w-100 d-flex align-items-center justify-content-between">
                            <div class="w-25 d-flex">
                                <font-awesome-icon icon="fa-solid fa-location-dot" class="fs-2 text-dark ms-5 me-3" />
                                <p class="mt-1"><b> ĐỊA CHỈ </b></p>
                            </div>

                            <div class="w-75 btn-add-address justify-content-end">
                                <div v-if="!isAddAddress"
                                    class="btn btn-warning d-flex align-items-center justify-content-center"
                                    @click="isShowAddAddress">
                                    <font-awesome-icon icon="fa-solid fa-plus" class="fs-5 icon-select-address" />
                                    <p class="m-0 ms-3">Thêm địa chỉ mới</p>
                                </div>
                            </div>
                        </div>
                        <hr class="style2">
                        <div class="w-100">
                            <div class=" w-100 d-flex flex-column justify-content-between" v-if="isAddAddress">
                                <div class="d-flex w-100 flex-column align-items-center">
                                    <h5 class="mt-2 mb-4">Thêm địa chỉ mới</h5>
                                </div>
                                <input v-model="contentAddAdress" class="input-edit-phone w-100 py-1 ps-2"
                                    placeholder="Nhập địa chỉ mới">
                                <div class="d-flex">
                                    <input v-model="statusAddress" type="checkbox" class="checkbox-status m-1">
                                    <div class="m-0 my-1"> Đặt làm địa chỉ mặt định</div>
                                </div>
                                <div class="d-flex">
                                    <div class="btn btn-warning mt-2 mx-3 w-100" @click="addAddressUser">
                                        <p class="m-0">Xác nhận</p>
                                        <font-awesome-icon icon="fa-solid fa-circle-check"
                                            class="fs-4 icon-select-address" />
                                    </div>
                                    <div class="btn btn-warning mt-2 mx-3 w-100" @click="isShowAddAddress">
                                        <p class="m-0">Hủy</p>
                                        <font-awesome-icon icon="fa-solid fa-xmark"
                                            class="text-warning icon-select-address-cancel" />
                                    </div>
                                </div>
                                <hr class="style2">
                            </div>
                            <div class="my-2 justify-content-between" v-for="item, index of dataAddress">
                                <p>
                                    <span class="text-success me-2">{{ index + 1 }}.</span>
                                    {{ item.address_content }}
                                    <span v-if="item.status" class="ms-1 text-primary"> (Mặc định)</span>
                                </p>
                                <div class="d-flex">
                                    <button v-if="item.status != true" class="btn btn-dark d-flex"
                                        @click="setAddressDefault(item.id)">
                                        <p class="m-0"> Đặt mặc định</p>
                                        <font-awesome-icon icon="fa-solid fa-circle-check"
                                            class="ms-5 fs-5 icon-select-address" />
                                    </button>
                                    <button class="btn btn-dark d-flex ms-3" v-if="item.status != true">
                                        <p class="m-0"> Xóa </p>
                                        <font-awesome-icon icon="fa-solid fa-xmark" class="ms-2 fs-5 icon-select-address"
                                            @click="deleteAddressUser(item.id)" />
                                    </button>

                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="selected-action w-100 mt-3 border p-2 m-2">
                    <div class="content-address m-3">
                        <div class="w-100 d-flex align-items-center justify-content-between">
                            <div class="w-25 d-flex align-items-center">
                                <font-awesome-icon icon="fa-solid fa-phone" class="fs-3 text-dark ms-5 me-3" />
                                <img class="img-flag-phone-user mx-2" src="./../../assets/images/flagflag.webp" alt="">
                                <p class="m-0 mt-1"><b> SỐ ĐIỆN THOẠI </b></p>
                            </div>

                            <div class="w-75 btn-add-address justify-content-end">
                                <div v-if="!isAddPhone"
                                    class="btn btn-warning d-flex align-items-center justify-content-center"
                                    @click="isShowAddphone">
                                    <font-awesome-icon icon="fa-solid fa-plus" class="fs-5 icon-select-address" />
                                    <p class="m-0 ms-3">Thêm Số điện thoại mới</p>
                                </div>
                            </div>
                        </div>
                        <hr class="style2">
                    </div>
                    <div v-if="isAddPhone" class=" w-100 align-items-center mt-2 p-3">
                        <div class="d-flex flex-column w-100 align-items-center">
                            <h5 class="m-0">Thêm di động mới</h5>
                        </div>
                        <div class="d-flex flex-column mt-2">
                            <div class="d-flex align-items-center">
                                <p class="m-0 me-1">(+84)</p>
                                <img src="./../../assets/images/flagflag.webp" class="img-flag-phone-user me-2" alt="">
                                <input v-model="contentPhone.phone" type="text" class="m-0 my-1 mt-2 py-1 ps-2 w-100"
                                    placeholder="Nhập số đi động" @change="checkPhone()">
                            </div>
                            <input type="text" v-model="contentPhone.name" class="m-0 my-1 mt-2 py-1 ps-2"
                                placeholder="Nhập tên người dùng di động">
                            <div v-if="contentPhone.error" class="error-phone w-100">
                                <span class="text-danger">Nhập sai số điện thoại</span>
                            </div>
                        </div>
                        <div class="d-flex">
                            <input v-model="this.contentPhone.status" type="checkbox" class="checkbox-status m-1">
                            <div class="m-0 my-1"> Đặt làm di động mặt định</div>
                        </div>
                        <div class="d-flex w-100">
                            <div class="btn btn-warning mt-2 mx-3 w-100" @click="addPhoneUser">
                                <p class="m-0">Xác nhận</p>
                                <font-awesome-icon icon="fa-solid fa-circle-check" class="fs-4 icon-select-address" />
                            </div>
                            <div class="btn btn-warning mt-2 mx-3 w-100" @click="isShowAddphone">
                                <p class="m-0">Hủy</p>
                                <font-awesome-icon icon="fa-solid fa-xmark"
                                    class="text-warning icon-select-address-cancel" />
                            </div>

                        </div>
                        <hr class="style2">
                    </div>

                    <div class="content-phone">
                        <div class="w-100 m-3">
                            <div class="my-2 justify-content-between" v-for="item, index of dataPhone">
                                <div class="w-100 d-flex">
                                    <p>
                                        <span class="text-success me-2">{{ index + 1 }}.</span>
                                        {{ item.phone }}
                                        <span class="ms-2 text-info">({{ item.name }})</span>
                                    </p>
                                    <p v-if="item.status == true" class="ms-2 text-primary">
                                        (Mặc định)
                                    </p>
                                </div>
                                <div class="d-flex">
                                    <button v-if="item.status != true" class="btn btn-dark d-flex"
                                        @click="setPhoneDefault(item.id)">
                                        <p class="m-0"> Đặt mặc định</p>
                                        <font-awesome-icon icon="fa-solid fa-circle-check"
                                            class="ms-5 fs-5 icon-select-address" />
                                    </button>
                                    <button class="btn btn-dark d-flex ms-3" v-if="item.status != true">
                                        <p class="m-0"> Xóa </p>
                                        <font-awesome-icon icon="fa-solid fa-xmark" class="ms-2 fs-5 icon-select-address"
                                            @click="deletePhoneUser(item.id)" />
                                    </button>
                                </div>
                            </div>

                        </div>
                    </div>
                </div>
            </div>
            <div v-if="isActivateOrderBePaid && inforOrder == false" class="col">
                <h3 class=""> Đơn chờ thanh toán </h3>
                <div v-if="dataOrderBeWaitingPaid.length == 0" class="p-5 text-center">
                    <p><b>Không có dữ liệu</b></p>
                </div>
                <div v-for="item in dataOrderBeWaitingPaid" class="m-2 border">
                    <div class="order-be-waiting-order text-center p-2">
                        <p class="m-0"> {{ formatDateTime(item.datetime) }} </p>
                    </div>
                    <div class="d-flex border p-2 align-items-center justify-content-between">
                        <p class="">
                            Giá : {{ new Intl.NumberFormat('vi-VN').format(item.total_price) }} vnđ
                        </p>
                        <div class="border p-2">
                            <p class="m-0 text-danger">Chờ thanh toán</p>
                        </div>
                        <button class="btn btn-dark" @click="nextDetailOrder(item.name)">
                            Xem chi tiết
                        </button>
                    </div>
                </div>
            </div>
            <div v-if="isActivateOrderPaied && inforOrder == false" class="col">
                <h3 class=""> Đơn đã thanh toán </h3>
                <div v-if="dataOrderPaid.length == 0" class="p-5 text-center">
                    <p><b>Không có dữ liệu</b></p>
                </div>
                <div v-for="item in dataOrderPaid" class="m-2 border">
                    <div class="order-be-waiting-order text-center p-2">
                        <p class="m-0"> {{ formatDateTime(item.datetime) }} </p>
                    </div>
                    <div class="d-flex border p-2 align-items-center justify-content-between">
                        <p class="">
                            Giá : {{ new Intl.NumberFormat('vi-VN').format(item.total_price) }} vnđ
                        </p>
                        <div class="border p-2">
                            <p class="m-0 text-danger">Đã thanh toán</p>
                        </div>
                        <button class="btn btn-dark" @click="nextDetailOrder(item.name)">
                            Xem chi tiết
                        </button>
                    </div>
                </div>
            </div>
            <div v-if="isActivateOrderBought && inforOrder == false" class="col">
                <h3 class=""> Đơn đã nhận </h3>
                <div v-if="dataOrderBougnt.length == 0" class="p-5 text-center">
                    <p><b>Không có dữ liệu</b></p>
                </div>
                <div v-for="item in dataOrderBougnt" class="m-2 border">
                    <div class="order-be-waiting-order text-center p-2">
                        <p class="m-0"> {{ formatDateTime(item.datetime) }} </p>
                    </div>
                    <div class="d-flex border p-2 align-items-center justify-content-between">
                        <p class="">
                            Giá : {{ new Intl.NumberFormat('vi-VN').format(item.total_price) }} vnđ
                        </p>
                        <div class="border p-2">
                            <p class="m-0 text-danger">Đã Nhân hàng</p>
                        </div>
                        <button class="btn btn-dark" @click="nextDetailOrder(item.name)">
                            Xem chi tiết
                        </button>
                    </div>
                </div>
            </div>
            <div v-if="inforOrder" class="col">
                <h3 class=""> Chi tiết đơn : {{ inforOrder.order[0].name }} </h3>
                <div class="p-3 border">
                    <p class=""><b>Đơn thanh toán : </b>
                        <span v-if="inforOrder.payment == false" class="ms-2">
                            Chưa thanh toán
                        </span>
                        <span v-if="inforOrder.payment != false " class="ms-2">
                            Vào lúc {{ formatDateTime(inforOrder.payment.created_at) }}
                        </span>
                    </p>
                    <p class=""><b>Địa chỉ người nhận :</b>
                        <span class="ms-2"> {{ inforOrder.order[0].address_receiver }} </span>
                    </p>
                    <p class=""><b>Số điện thoại người nhận :</b>
                        <span class="ms-2"> {{ inforOrder.order[0].phone_receiver }} </span>
                    </p>
                    <p class=""><b>Số tiền thanh toán : </b>
                        <span class="ms-2"> {{ new Intl.NumberFormat('vi-VN').format(inforOrder.order[0].total_price) }} vnđ
                        </span>
                    </p>
                    <div class="">
                        <hr class="">
                        <p class=""> <b class=""> <i class=""> Sản phẩm </i></b> </p>
                    </div>
                    <table  class="table">
                        <thead>
                            <tr>
                                <th scope="col">STT</th>
                                <th scope="col">Tên</th>
                                <th scope="col">Đơn giá</th>
                                <th scope="col">Số Lượng</th>
                                <th scope="col">Thành tiền</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="item, index in productInforOrder">
                                <!-- {{item}} -->
                                <th scope="row">{{ index }}</th>
                                <td>
                                    <p class="m-0">{{ item.product_name }}</p>
                                    <img class="img-checkout-product" :src="URL_PATH_SERVER + '/' + item.photo_product">
                                </td>
                                <td>{{ new Intl.NumberFormat('vi-VN').format(item.product_price_total) }} vnđ</td>
                                <td>{{ item.product_quantity }}</td>
                                <td>{{ new Intl.NumberFormat('vi-VN').format(item.product_price_total *
                                    item.product_quantity) }} vnđ
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>

            </div>
        </div>
    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import { actionUser } from '../../common/user.service'
import { OrderAction } from '../../common/order.service'
import { URL_PATH_SERVER } from '../../common/constants'
export default ({
    name: 'ProfileLayout',
    props: {
        photo: false,
        address: false,
        phone: false,
        name: false,
    },
    components: {
    },
    watch: {
        nameOrder(newNameOrder) {
            this.nextDetailOrder(this.nameOrder)

        },
    },
    data: () => ({
        URL_PATH_SERVER : URL_PATH_SERVER ,
        address_selected: false,
        isSelectAddress: false,
        isSelectPhone: false,
        statusAddress: false,
        isSave: false,
        isAddAddress: false,
        isAddPhone: false,
        isEditPhone: false,
        phone_selected: "Chưa có số  điện thoại",
        contentAddAdress: '',
        contentPhone: {
            name: '',
            phone: '',
            error: false,
            status: false
        },
        dataAddress: new Array(),
        dataPhone: new Array(),
        isValueNotify: false,
        isShowNotice: false,
        inforUser: false,
        fileUpload: '',
        messageChooseFile: 'Thay ảnh đại diện',
        isActivateProfile: true,
        isActivateOrderBePaid: false,
        isActivateOrderPaied: false,
        isActivateOrderBought: false,
        dataOrderBeWaitingPaid: [],
        dataOrderPaid: [],
        dataOrderBougnt: [],
        inforOrder: false,
        productInforOrder: [],
        nameOrder: false,
    }),
    methods: {
        async nextDetailOrder(nameOrder) {
            return await OrderAction.getInfor({
                params: {
                    name_order: nameOrder,
                }
            }).then(res => {
                console.log('indf', res)
                this.inforOrder = {
                    order: res.order,
                    payment: res.payment
                }
                OrderAction.getInforProduct({
                    params: {
                        nameOrder: nameOrder
                    }
                }).then(res => {
                    console.log(res)
                    this.productInforOrder = res.success[0].products
                }).catch(error => {
                    console.log("error orcer checkout", error)
                })

            })
        },
        showActivateProfile() {
            this.isActivateProfile = true
            this.isActivateOrderBePaid = false
            this.isActivateOrderPaied = false
            this.isActivateOrderBought = false
            this.inforOrder = false
        },
        showActivateOrderBePaid() {
            this.isActivateProfile = false
            this.isActivateOrderBePaid = true
            this.isActivateOrderPaied = false
            this.isActivateOrderBought = false
            this.getAllOrderBeWaitingPaid()
            this.inforOrder = false
        },
        showActivateOrderPaided() {
            this.isActivateProfile = false
            this.isActivateOrderBePaid = false
            this.isActivateOrderPaied = true
            this.isActivateOrderBought = false
            this.getAllOrderPaymented()
            this.inforOrder = false
        },
        showActivateOrderBought() {
            this.isActivateProfile = false
            this.isActivateOrderBePaid = false
            this.isActivateOrderPaied = false
            this.isActivateOrderBought = true
            this.inforOrder = false
        },
        /* -------------------------------------------------------------------------- */
        /*                               ADDRESS METHODS                              */
        /* -------------------------------------------------------------------------- */
        isShowSelectAddress() {
            this.isSelectAddress = !this.isSelectAddress
        },
        selectedAdress(id) {
            this.isShowSelectAddress()
            this.address_selected = this.dataAddress.filter((phone) => {
                return phone.id == id
            })[0]
        },
        isShowAddAddress() {
            this.isAddAddress = !this.isAddAddress;
        },
        async addAddressUser() {
            return await actionUser.createAdressUser({
                params: {
                    address_content: this.contentAddAdress,
                    status: this.statusAddress
                }
            }).then(res => {
                if (res.status == 200) {
                    if (this.statusAddress == true) {
                        this.dataAddress = this.dataAddress.filter((address) => {
                            address.status = false
                            return address
                        })
                    }
                    this.dataAddress.push(res.address)
                    this.isAddAddress = !this.isAddAddress;
                    this.$store.dispatch('notice/actionTypeNotice', { content: 'Đã thêm thành công ', type: 'addtocart' })
                    this.$store.dispatch('notice/activateShowMenu')
                }
            })
        },
        deleteAddressUser(address_user_id) {
            this.isShowNoticeCarefully('Bạn có chắc chắn muốn xóa địa chỉ này', 'Xóa')
            return new Promise((resolve) => {
                const checkValue = () => {
                    if (this.get_accept === true) {
                        actionUser.deteleAddressUser({
                            params: {
                                address_user_id: address_user_id
                            }
                        }).then(res => {
                            this.$store.dispatch('notice/actionComplete')
                            this.dataAddress = this.dataAddress.filter((address) => {
                                return address.id != address_user_id
                            })
                            this.$store.dispatch('notice/actionTypeNotice', { content: 'Đã Xóa địa chỉ thành công ', type: 'addtocart' })
                            this.$store.dispatch('notice/activateShowMenu')
                        })
                        resolve();
                    }
                    if (this.get_accept === false || this.get_accept === true) {
                        this.$store.dispatch('notice/actionComplete')
                    }
                    else {
                        setTimeout(checkValue, 500);
                    }
                };

                checkValue();
            });
        },
        /* -------------------------------------------------------------------------- */
        /*                                PHONE METHODS                               */
        /* -------------------------------------------------------------------------- */
        isShowSelectPhone() {
            this.isSelectPhone = !this.isSelectPhone
        },
        isShowAddphone() {
            this.isAddPhone = !this.isAddPhone
        },
        selectedPhone(id) {
            this.isShowSelectPhone()
            this.phone_selected = this.dataPhone.filter((address) => {
                return address.id == id
            })[0]
        },
        checkPhone() {
            const pattern = /^(\+84|0)\d{9}$/;
            if (pattern.test(this.contentPhone.phone) == false) {
                this.contentPhone.error = true
            } else {
                this.contentPhone.error = false
            }
        },
        async addPhoneUser() {
            return await actionUser.createPhoneUser({
                params: {
                    phone_user: this.contentPhone.phone,
                    name_user: this.contentPhone.name,
                    status: this.contentPhone.status
                }
            }).then(res => {
                if (res.status = 200) {
                    if (this.contentPhone.status == true) {
                        this.dataPhone = this.dataPhone.filter((phone) => {
                            phone.status = false
                            return phone
                        })
                    }
                    this.dataPhone.push(res.phone)
                    this.isAddPhone = false
                    this.$store.dispatch('notice/actionTypeNotice', { content: 'Đã thêm thành công ', type: 'addtocart' })
                    this.$store.dispatch('notice/activateShowMenu')
                }
            })
        },
        deletePhoneUser(phone_user_id) {
            this.isShowNoticeCarefully('Bạn có muốn Xóa đố điện thoại này', 'Xóa')
            return new Promise((resolve) => {
                const checkValue = () => {
                    if (this.get_accept === true) {
                        actionUser.detelePhoneUser({
                            params: {
                                phone_user_id: phone_user_id
                            }
                        }).then(res => {
                            this.$store.dispatch('notice/actionComplete')
                            this.dataPhone = this.dataPhone.filter((phone) => {
                                return phone.id != phone_user_id
                            })
                            this.$store.dispatch('notice/actionTypeNotice', { content: 'Đã Xóa Số điện thoại thành công ', type: 'addtocart' })
                            this.$store.dispatch('notice/activateShowMenu')
                        })
                        resolve();
                    }
                    if (this.get_accept === false || this.get_accept === true) {
                        this.$store.dispatch('notice/actionComplete')
                    }
                    else {
                        setTimeout(checkValue, 500);
                    }
                };

                checkValue();
            });
        },
        /* -------------------------------------------------------------------------- */
        /*                               NOTICE METHODS                               */
        /* -------------------------------------------------------------------------- */
        isShowNoticeCarefully(content, type) {
            this.$store.dispatch('notice/actionTypeNotice', { content: content, type: type })
            this.$store.dispatch('notice/activateShow')
        },
        /* -------------------------------------------------------------------------- */
        /*                                 METHOD SAVE                                */
        /* -------------------------------------------------------------------------- */
        async uploadInformation() {
            await actionUser.uploadInformation({
                params: {
                    name: this.inforUser.name,
                    email: this.inforUser.email
                }
            }).then((response) => {
                if (response.data.status == 200) {

                    this.$store.dispatch('notice/actionTypeNotice', { content: 'Thay đổi thông tin thành công ', type: 'addtocart' })
                    this.$store.dispatch('notice/activateShowMenu')
                }
            })

        },
        /* -------------------------------------------------------------------------- */
        /*                                GET INFORUSER                               */
        /* -------------------------------------------------------------------------- */
        async isShowInforUser() {
            this.isInforUser = !this.isInforUser
            if (this.inforUser == false) {
                await actionUser.getInforUser().then(async (response) => {
                    console.log('response', response)
                    this.inforUser = {
                        photo: URL_PATH_SERVER + response.user.photo,
                        address: response.user.address,
                        phones: response.user.phones,
                        name: response.user.name,
                        email: response.user.email
                    }
                })
            }
        },
        async uploadPhoto() {
            const file = this.$refs.imagePhoto.files[0]
            console.log('file', file)
            const dataUrl = await new Promise((resolve) => {
                const reader = new FileReader()
                reader.onload = () => resolve(reader.result)
                reader.readAsDataURL(file)
            })
            if (file.type.startsWith('image/')) {
                this.fileUpload = {
                    data: dataUrl,
                }
            }

            await actionUser.uploadPhoto({
                params: {
                    file: this.fileUpload
                }
            }).then((response) => {
                if (response.data.status == 200) {
                    this.inforUser.photo = this.fileUpload.data
                    this.messageChooseFile = "Đã cập nhật ảnh"
                    this.$store.dispatch('notice/actionTypeNotice', { content: 'Đã cập nhật ảnh thành công ', type: 'addtocart' })
                    this.$store.dispatch('notice/activateShowMenu')
                }
            })
        },
        async setPhoneDefault(id) {
            await actionUser.setPhoneDefault({
                params: {
                    phone_id: id
                }
            }).then(res => {
                if (res.status == 200) {
                    this.dataPhone = this.dataPhone.filter(phone => {
                        if (String(phone.id) == String(id)) {
                            phone.status = true
                        } else {
                            phone.status = false
                        }
                        return phone
                    })
                    this.$store.dispatch('notice/actionTypeNotice', { content: 'Đã cập nhật thành công ', type: 'addtocart' })
                    this.$store.dispatch('notice/activateShowMenu')
                }
            })
        },
        async setAddressDefault(id) {
            await actionUser.setAddressDefault({
                params: {
                    address_id: id
                }
            }).then(res => {
                if (res.status == 200) {
                    this.dataAddress = this.dataAddress.filter(address => {
                        if (String(address.id) == String(id)) {
                            address.status = true
                        } else {
                            address.status = false
                        }
                        return address
                    })
                    this.$store.dispatch('notice/actionTypeNotice', { content: 'Đã cập nhật thành công ', type: 'addtocart' })
                    this.$store.dispatch('notice/activateShowMenu')
                }
            })
        },
        /* -------------------------------------------------------------------------- */
        /*                                ORDER METHOD                                */
        /* -------------------------------------------------------------------------- */
        async getAllOrderBeWaitingPaid() {
            await OrderAction.getAllOrderBeWaitingPaid().then(res => {
                this.dataOrderBeWaitingPaid = res.success
            })
        },
        async getAllOrderPaymented() {
            await OrderAction.getAllOrderPaymented().then(res => {
                console.log(res.success)
                this.dataOrderPaid = res.success
            })
        },
        formatDateTime(datetime) {
            const dateString = "2023-06-17T15:49:47Z";
            const date = new Date(dateString);

            const hours = date.getUTCHours();
            const minutes = date.getUTCMinutes();
            const seconds = date.getUTCSeconds();
            const day = date.getUTCDate();
            const month = date.getUTCMonth() + 1; // Lưu ý: tháng bắt đầu từ 0, nên cần cộng thêm 1
            const year = date.getUTCFullYear();

            const formattedTime = `${hours}:${minutes}:${seconds}`;
            const formattedDate = `${day}/${month}/${year}`;

            return formattedTime + " ngày " + formattedDate;
        },
    },
    computed: {
        ...mapGetters('auth', {
            get_user: 'currentUser',
            get_authenticated: 'isAuthenticated',
            get_error: 'errorAuthenticated'
        }),
        ...mapGetters('notice', {
            get_accept: 'isAccept'
        }),
        ...mapActions('notice', {
            activateNotice: 'activateShow',
            actionTypeNotice: 'actionTypeNotice'
        })
    },
    async created() {
        
        const nameOrder = this.$router.currentRoute.value.query.nameOrder
        if(nameOrder != null){
            this.nameOrder = nameOrder
            console.log('nameOrder', nameOrder)
            this.nextDetailOrder(this.nameOrder)
        }
        await this.isShowInforUser()
        this.dataAddress = Array.from(this.inforUser.address)
        this.dataPhone = Array.from(this.inforUser.phones)
        for (let item of this.address) {
            if (item.status == true) {
                this.address_selected = item
            }
        }
        for (let item of this.phone) {
            if (item.status == true) {
                this.phone_selected = item
            }
        }
    },
    async mounted() {
    }
})
</script>
<style>
.img-infor-profile {
    max-width: 200px;
}

hr.style2 {
    border-top: 3px double #8c8b8b;
}

.btn-add-address {
    width: 100%;
}

.choose-file {
    height: 0.1px;
    opacity: 0;
    overflow: hidden;
    position: absolute;
    width: 0.1px;
    z-index: -1;
}

/* Style both input field and label */
.choose-file+.upload-file {
    margin-top: 15px;
    background-color: #3b1b28;
    border-radius: 15px;
    box-sizing: border-box;
    color: #fff;
    display: block;
    font-family: Sans-serif;
    font-size: 1rem;
    font-weight: 300;
    padding: .5rem 0.5rem;
    text-align: center;
}

.choose-file:focus+.upload-file,
.choose-file+.upload-file:hover {
    background-color: #E5246E;
    content: "Đã cập nhật";
}

.is-activa-profile {
    color: #E5246E
}

.is-action-profile {
    cursor: pointer
}
.img-checkout-product {
    width: 100px;
}
.order-be-waiting-order {
    background-color: rgb(37, 175, 175);
}</style>