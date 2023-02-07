<template>
    <div class="row d-flex d-flex-column align-items-center justify-content-center mt-2 mx-2">
        <font-awesome-icon icon="fa-regular fa-circle-xmark" class="icon-hide fs-2 text-dark" @click="$emit('hide')" />
        <div class="w-75 d-flex flex-column align-items-center mt-3">
            <img class="img-infor-user" :src="photo" :alt="photo">
            <p class="mt-2">{{ name }} {% csrf_token %} </p>
        </div>
        <div class="d-flex">
            <div class="selected-action w-100 row mt-3">
                <div class="d-flex col-lg-6">
                    <font-awesome-icon icon="fa-solid fa-location-dot" class="fs-2 text-dark ms-5 me-3" />
                    <p class="text-content-user m-0"> <b>Địa chỉ</b> :
                    </p>
                    <p v-if="address_selected != false">
                        <span>
                            {{ address_selected.address_content }}
                            <span v-if="address_selected.status" class="ms-1 text-primary"> (Mặc định)</span>
                        </span>

                    </p>
                    <font-awesome-icon icon="fa-solid fa-pencil" class="ms-2 fs-4 icon-select-address"
                        @click="isShowSelectAddress" />
                    <div v-if="isSelectAddress" class="select-address">
                        <div class="my-2 d-flex" v-for="item in address">
                            <p> {{ item.address_content }} </p>
                            <font-awesome-icon icon="fa-solid fa-circle-check" class="ms-2 fs-5 icon-select-address"
                                @click="selectedAdress(item.id)" />
                        </div>
                    </div>
                </div>

                <div class="d-flex col-lg-6">
                    <font-awesome-icon icon="fa-solid fa-phone" class="fs-3 text-dark ms-5 me-3" />
                    <p class="text-content-user m-0"> <b>Số điện thoại</b> : (+84)
                        <span v-if="isEditPhone.value == false & isEditPhone.contentEditPhone == ''">{{ phone }}</span>
                        <span v-if="isEditPhone.value == false & isEditPhone.contentEditPhone">
                            {{ isEditPhone.contentEditPhone }}</span>
                        <span class="ms-1 text-primary"
                            v-if="isEditPhone.value == false & isEditPhone.contentEditPhone == ''">(Mặc định)</span>
                    </p>
                    <img class="img-flag-phone-user mx-2" src="./../assets/images/flagflag.webp" alt="">
                    <input v-if="isEditPhone.value" v-model="isEditPhone.contentEditPhone" class="input-edit-phone"
                        type="text" :class="[isEditPhone.error == true ? 'edit-phone-error' : '']">
                    <font-awesome-icon v-if="!isEditPhone.value" icon="fa-solid fa-pencil"
                        class="ms-2 fs-4 icon-select-address" @click="isShowEditPhone" />
                    <font-awesome-icon v-if="isEditPhone.value" icon="fa-solid fa-circle-check"
                        class="ms-2 fs-4 icon-select-address" @click="editPhone()" />
                    <div v-if="isEditPhone.error == true" class="error-phone m-2">
                        <p class="content-error-phone">Số điện thoại vừa nhập ko đúng</p>
                    </div>
                </div>
            </div>
        </div>
        <div class="w-75 d-flex flex-column align-items-center my-2">
            <button class="btn btn-dark"> Lưu dữ liệu </button>
        </div>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { actionUser } from './../common/user.service'
export default ({
    name: 'InforUserLayout',
    components: {

    },
    data: () => ({
        photo: false,
        address: false,
        phone: false,
        name: false,
        address_selected: false,
        isSelectAddress: false,
        isEditPhone: {
            value: false,
            contentEditPhone: '',
            error: ''
        },
        isSave: false
    }),
    methods: {
        isShowSelectAddress() {
            this.isSelectAddress = !this.isSelectAddress
        },
        selectedAdress(id) {
            this.isShowSelectAddress()
            this.address_selected = this.address.filter((address) => {
                return address.id == id
            })[0]
            console.log("this.address_selected", this.address_selected, id)
        },
        isShowEditPhone() {
            this.isEditPhone.value = !this.isEditPhone.value
            this.isEditPhone.error = false
        },
        editPhone() {
            const pattern = /^(\+84|0)\d{9}$/;

            if (pattern.test(this.isEditPhone.contentEditPhone) == false) {
                this.isEditPhone.error = true
            } else {
                this.isShowEditPhone()
            }
        }
    },
    computed: {
        ...mapGetters('auth', {
            get_user: 'currentUser',
            get_authenticated: 'isAuthenticated',
            get_error: 'errorAuthenticated'
        }),
    },
    async created() {
        function getCookie(name) {
            const cookie = document.cookie.split("; ").find(c => c.startsWith(name + "="));
            if (!cookie) return null;
            return cookie.split("=")[1];
            }
        console.log("document.cookie;",getCookie('csrftoken'))
        return await actionUser.getInforUser({
            params: {
                email_user: localStorage.getItem('user'),
                token_permission_infor_user: localStorage.getItem('token_permission_infor_user')
            }
        }).then(async (response) => {
            console.log(response.user)
            this.photo = 'http://127.0.0.1:8000' + response.user.photo
            this.address = response.user.address
            for (let item of this.address) {
                console.log(item.status)
                    this.address_selected = item
                    await actionUser.deteleAddressUser('address-user/address_user_id=e5bab451-244b-49fc-91ef-3597deb0e2df/token_permission_infor_user=d311b4fd-e010-405d-ba3b-7fb1043cf80c').then(response => {
                        console.log(response)
                    }).catch(err => {
                        console.log("document.cookie;",getCookie('csrftoken'))
                    })
                
            }
            this.phone = response.user.phone
            this.name = response.user.name
        })
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
    position: absolute;
    margin: 0 10%;
    height: 50%;
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
</style>