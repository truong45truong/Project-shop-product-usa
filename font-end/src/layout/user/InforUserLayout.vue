<template>
    <div class="row d-flex d-flex-column align-items-center justify-content-center mt-2 mx-2">
        <font-awesome-icon icon="fa-regular fa-circle-xmark" class="icon-hide fs-2 text-dark" @click="$emit('hide')" />
        <div class="w-75 d-flex flex-column align-items-center mt-3">
            <!-- <img class="img-infor-user" :src="photo" :alt="photo"> -->
            <p class="mt-2">{{ name }}</p>
        </div>
        <div class="d-flex">
            <div class="selected-action w-100 row mt-3">
                <div class="d-flex col-lg-6 content-address">
                    <font-awesome-icon icon="fa-solid fa-location-dot" class="fs-2 text-dark ms-5 me-3" />
                    <p class="text-content-user m-0"> <b>Địa chỉ</b> :
                    </p>
                    <p v-if="address_selected != false">
                        <span>
                            {{ address_selected.address_content }}
                            <span v-if="address_selected.status" class="ms-1 text-primary"> (Mặc định)</span>
                        </span>

                    </p>
                    <font-awesome-icon v-if="!isSelectAddress & isSelectPhone != true" icon="fa-solid fa-pencil"
                        class="ms-2 fs-4 icon-select-address" @click="isShowSelectAddress" />
                    <div v-if="isSelectAddress" class="w-100 select-address"
                        :class="[dataAddress.length > 5 & !isAddAddress ? 'select-over-item' : '']">
                        <font-awesome-icon icon="fa-solid fa-xmark" class="ms-2 fs-5 icon-select-address"
                            @click="isShowSelectAddress" />
                        <div v-if="!isAddAddress" class="my-2 d-flex justify-content-between"
                            v-for="item, index of dataAddress">
                            <p>
                                <span class="text-success me-2">{{ index + 1 }}.</span>
                                {{ item.address_content }}
                                <span v-if="item.status" class="ms-1 text-primary"> (Mặc định)</span>
                            </p>
                            <div>
                                <font-awesome-icon icon="fa-solid fa-circle-check" class="ms-5 fs-5 icon-select-address"
                                    @click="selectedAdress(item.id)" />
                                <font-awesome-icon v-if="item.status != true" icon="fa-solid fa-xmark"
                                    class="ms-2 fs-5 icon-select-address" @click="deleteAddressUser(item.id)" />
                            </div>
                        </div>
                        <div class="btn-add-address">
                            <div v-if="!isAddAddress"
                                class="btn btn-warning d-flex align-items-center justify-content-center"
                                @click="isShowAddAddress">
                                <font-awesome-icon icon="fa-solid fa-plus" class="fs-5 icon-select-address" />
                                <p class="m-0 ms-3">Thêm địa chỉ mới</p>
                            </div>
                        </div>
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
                                    <font-awesome-icon icon="fa-solid fa-circle-check" class="fs-4 icon-select-address" />
                                </div>
                                <div class="btn btn-warning mt-2 mx-3 w-100" @click="isShowAddAddress">
                                    <p class="m-0">Hủy</p>
                                    <font-awesome-icon icon="fa-solid fa-xmark"
                                        class="text-warning icon-select-address-cancel" />
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="d-flex col-lg-6 content-phone">
                    <font-awesome-icon icon="fa-solid fa-phone" class="fs-3 text-dark ms-5 me-3" />
                    <p class="text-content-user m-0"> <b>Số điện thoại</b> : (+84)
                        <span>{{ phone_selected.phone }}</span>
                        <span class="ms-1 text-primary" v-if="phone_selected.status == true">(Mặc định)</span>
                    </p>
                    <img class="img-flag-phone-user mx-2" src="./../assets/images/flagflag.webp" alt="">
                    <font-awesome-icon v-if="!isSelectPhone & isSelectAddress != true" icon="fa-solid fa-pencil"
                        class="ms-2 fs-4 icon-select-address" @click="isShowSelectPhone" />
                    <div v-if="isSelectPhone == true" class="select-phone w-100"
                        :class="[dataPhone.length > 5 & !isAddPhone ? 'select-over-item' : '']">
                        <font-awesome-icon icon="fa-solid fa-xmark" class="ms-2 fs-5 icon-select-address"
                            @click="isShowSelectPhone" />
                        <div v-if="!isAddPhone" class="my-2 d-flex justify-content-between" v-for="item, index of dataPhone">
                            <div class="d-flex">
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
                                <font-awesome-icon icon="fa-solid fa-circle-check" class="ms-5 fs-5 icon-select-address"
                                    @click="selectedPhone(item.id)" />
                                <font-awesome-icon v-if="item.status != true" icon="fa-solid fa-xmark"
                                    class="ms-2 fs-5 icon-select-address" @click="deletePhoneUser(item.id)" />
                            </div>
                        </div>
                        <div v-if="!isAddPhone" class="btn-add-address">
                            <div v-if="isSelectPhone"
                                class="btn btn-warning d-flex align-items-center justify-content-center"
                                @click="isShowAddphone">
                                <font-awesome-icon icon="fa-solid fa-plus" class="fs-5 icon-select-address" />
                                <p class="m-0 ms-3">Thêm di động</p>
                            </div>
                        </div>
                        <div v-if="isAddPhone" class=" w-100 align-items-center mt-2">
                            <div class="d-flex flex-column w-100 align-items-center">
                                <h5 class="m-0">Thêm di động mới</h5>
                            </div>
                            <div class="d-flex flex-column mt-2">
                                <div class="d-flex align-items-center">
                                    <p class="m-0 me-1">(+84)</p>
                                    <img src="./../assets/images/flagflag.webp" class="img-flag-phone-user me-2" alt="">
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
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="w-75 d-flex flex-column align-items-center my-2">
            <button class="btn btn-dark" @click="saveResult"> Lưu dữ liệu </button>
        </div>
    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import { actionUser } from '../../common/user.service'
import { OrderAction } from '../../common/order.service'
export default ({
    name: 'InforUserLayout',
    props: {
        photo: false,
        address: false,
        phone: false,
        name: false,
    },
    components: {
    },
    data: () => ({
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
    }),
    methods: {
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
                if (this.statusAddress == true) {
                    this.dataAddress = this.dataAddress.filter((address) => {
                        address.status = false
                        return address
                    })
                }
                this.dataAddress.push(res.address)
                this.isAddAddress = !this.isAddAddress;
            })
        },
        deleteAddressUser(address_user_id) {
            this.isShowNoticeCarefully('Bạn có chắc chắn muốn xóa địa chỉ này','Xóa')
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
                if (this.contentPhone.status == true) {
                    this.dataPhone = this.dataPhone.filter((phone) => {
                        phone.status = false
                        return phone
                    })
                }
                this.dataPhone.push(res.phone)
                this.isAddPhone = false
            })
        },
        deletePhoneUser(phone_user_id) {
            this.isShowNoticeCarefully('Bạn có muốn Xóa đố điện thoại này','Xóa')
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
        isShowNoticeCarefully(content , type) {
            this.$store.dispatch('notice/actionTypeNotice', { content: content, type : type })
            this.$store.dispatch('notice/activateShow')
        },
        /* -------------------------------------------------------------------------- */
        /*                                 METHOD SAVE                                */
        /* -------------------------------------------------------------------------- */
        async saveResult() {
            this.isShowNoticeCarefully('Bạn có muốn lưu thay đổi này','Lưu')
            return new Promise((resolve) => {
                const checkValue = () => {
                    if (this.get_accept === true) {
                        OrderAction.actionChangeOrderToday({
                            params: {
                                address_change: this.address_selected,
                                phone_change: this.phone_selected,
                                type: 1
                            }
                        }).then(response => {
                            this.$store.dispatch('notice/actionComplete')
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

        }
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
    created() {
        this.dataAddress = Array.from(this.address)
        this.dataPhone = Array.from(this.phone)
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
.img-infor-user {
    width: 100px;
    height: 100px;
    border-radius: 50%;
}

.icon-hide {
    position: absolute;
    left: 45%;
    top: 5%;
}

.icon-hide:hover {
    cursor: pointer;
    color: brown !important;
}

.selected-action {
    margin: 5% 5%;
}

.text-content-user {
    font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
    font-size: 16px;
}

.icon-edit:hover {
    cursor: pointer;
}

.select-address {
    max-width: 100%;
    position: absolute;
    height: fit-content;
    background-color: rgb(243, 237, 227);
    top: 55%;
    padding: 15px;
    overflow-y: scroll;
    border: 1px solid black;
}

.select-over-item {
    height: 400px;
}

.select-phone {
    max-width: 100%;
    position: absolute;
    height: fit-content;
    background-color: rgb(243, 237, 227);
    top: 55%;
    padding: 15px;
    overflow-y: scroll;
    border: 1px solid black;
}

.icon-select-address:hover {
    cursor: pointer;
    color: brown;
}

.input-edit-phone {
    padding: 0 0;
    height: fit-content;
}

.img-flag-phone-user {
    width: 35px;
    height: 20px;
}

.edit-phone-error {
    border-color: red;
}

.content-error-phone {
    color: red;
    font-size: 13px;
}

.content-address,
.content-phone {
    position: relative;
}

.icon-cancel {
    align-items: end;
}

.btn-warning {
    margin: 0 15%;
}

.icon-select-address-cancel {
    border-radius: 50%;
    padding: 4px 7px;
    background-color: rgb(0, 0, 0);
}

.icon-select-address-cancel:hover {
    background-color: brown
}

.checkbox-status {
    width: 20px;
    height: 20px;
}</style>