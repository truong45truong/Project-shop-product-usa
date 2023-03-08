<template>
    <header>
        <div class="menu-bottom">
            <div class="container container-menu">
                <div class="row container-fluid d-flex align-items-center justify-content-between">
                    <div class="col-6 my-1 d-flex align-items-center">
                        <p class="m-0">Ngày</p>
                        <p class ="m-0 ms-2" id="current-time">{{ currentTime }}</p>
                    </div>
                    <div class="col-6 my-1 d-flex align-items-center justify-content-end">
                        <img class="img-flag mx-2" src="./../assets/images/flagflag.webp" alt="">
                        <p v-if="!isAuthenticated" class="m-0 btn-login" @click="showLogin" >Đăng nhập</p>
                        <p v-if="isAuthenticated" class="m-0"> {{get_user.user}}  </p>
                        <p v-if="isAuthenticated" class="m-0 ms-2 btn-login" @click="logoutUser()" > Đăng xuất  </p>
                    </div>
                </div>
            </div>
        </div>
        <div class="menu-top">
            <div class="container container-menu">
                <div class="row container-fluid d-flex align-items-center justify-content-between">
                    <div class="col-lg-4 my-3"><a class="navbar-brand" href="#">
                            <h2 class="m-0 font-logo"><b><i>ShopKatie</i></b></h2>
                        </a></div>
                    <div class="col-lg-4 d-flex align-items-center justify-content-around">
                        <p class="text-white m-0 ms-4  py-4 title-menu">TRANG CHỦ</p>
                        <p class="text-white m-0 ms-4  py-4 title-menu">GIỚI THIỆU</p>
                        <p class="text-white m-0  ms-4 py-4 title-menu" :class="{ 'border-4 border-bottom active-border' : isShowCategory == true}" @click="showCategory">SẢN PHẨM</p>
                        <p class="text-white m-0 ms-4 py-4  title-menu">LIÊN HỆ</p>
                        <p class="text-white m-0 ms-4 py-4  title-menu">THEO DÕI</p>
                    </div>
                    <div class="col-lg-4 my-3 d-flex justify-content-end align-items-center position-relative">
                        <div class="search-control">
                            <input type="text" class="input-search border" placeholder="Tìm kiếm sản phẩm">
                            <font-awesome-icon class="d-inline text-white icon-search" icon="fa-solid fa-magnifying-glass" />
                        </div>
                        <div class="position-relative" @click="$emit('hideListItemHeart',true)" >
                            <font-awesome-icon class="text-white fs-4 ms-3 icon-cursor" icon="fa-regular fa-heart"/>
                            <div class="number-product-cart text-white text-center m-0">{{get_is_number_product_heart}}</div> 
                        </div>
                        <div class="position-relative" @click="showUser">
                            <font-awesome-icon class="text-white fs-4 ms-3 icon-cursor" icon="fa-regular fa-user" />
                        </div>
                        <div class="position-relative" @click="$emit('hideCart',true)" >
                            <font-awesome-icon class="text-white fs-4 ms-3 icon-cursor" icon="fa-solid fa-basket-shopping" /> 
                            <div class="number-product-cart text-white text-center m-0">{{get_is_number_product}}</div> 
                        </div> 
                        <notice-menu />
                        <div v-if="isShowUser" class="position-absolute bg-white rounded shadow top-100 p-2 w-50 start-50 py-4 text-center">
                            <p class="text-dark action-menu-user" >Thông tin các nhân</p>
                            <p class="text-dark action-menu-user mb-0" @click="$emit('hideChangePassword',true)">Đổi mật khẩu</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <category-layout :class="[isShowCategory ? 'show-list-category' : 'list-category']" />
        <sign-in class="active-login" v-if="isShowLogin" @login = "login"/>
    </header>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import CategoryLayout from './CategoryLayout.vue'
import SignIn from './../components/login/SignIn.vue'
import NoticeMenu from './../components/other/NoticeMenu.vue'
export default {
    name: "MenuHeader",
    props: {
        msg: String,
    },
    data: () => ({
        isShowLogin : false,
        currentTime : new Date().toLocaleString(),
        isAuthenticated : false,
        isShowCategory : false,
        isShowNotify : false,
        isShowUser : false ,
    }),
    components : {
        CategoryLayout,
        SignIn,
        NoticeMenu
    },
    methods : {
        showUser(){
            this.isShowUser = ! this.isShowUser
        },
        showCategory (){
            this.isShowCategory = ! this.isShowCategory
        },
        showLogin(){
            this.isShowLogin = ! this.isShowLogin
        },
        /* -------------------------- method register user -------------------------- */
		register (){
			this.register_user.then(() => {
				if (this.get_error == false) {
					this.message = "Register Success";
				}
			}).catch( error => {
				console.error("error",error)
				this.message = "Register Failure";
			})
		},
		/* ------------------------------ method login ------------------------------ */

		async login(username,password) {
			return await this.$store.dispatch('auth/login', { username: username ,  password : password}).then((res) => {
				if (this.get_authenticated == true) {
					this.isAuthenticated = true;
					this.isShowLogin=false;
				}
			}).catch( error => {
				console.error("error",error);
			})
		},
        logoutUser () {
            this.$store.dispatch('auth/logout').then(() => {
                this.isAuthenticated = this.get_authenticated;
            })
        }
    },
    computed: {
		...mapGetters('auth', {
			get_user         : 'currentUser',
			get_authenticated: 'isAuthenticated',
			get_error        : 'errorAuthenticated'
		}),
        ...mapGetters('cart', {
        get_is_number_product: 'getNumberProduct',
        }),
        ...mapGetters('heart', {
        get_is_number_product_heart: 'getNumberProduct',
        }),
		...mapActions('auth', {
			login_user   : 'login',
			register_user: 'register',
            logout_user : 'logout'
		})
	},
    mounted() {
        this.isAuthenticated = this.get_authenticated
        setInterval(() => {
            this.currentTime = new Date().toLocaleString();
        }, 1000);
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
@keyframes bgNumberProductCart {
    0%{
        background-color:#30CFD0;
    }

    50% {
        background-color: #1071a8
    }
    100% {
        background-color: #30CFD0
    }
}

.number-product-cart {
    position:absolute;
    width:1.75rem;
    height:1.75rem;
    padding-top: 0.2rem;
    border-radius: 50%;
    top:-30%;
    right:-30%;
    font-weight: 600;
    animation: bgNumberProductCart 5s infinite;
    cursor:pointer;
}
header {
    background-color: #212529;
    font-family: 'Alumni Sans', sans-serif;
    position: relative;
}
.container-menu {
    max-width:1905px !important;
    z-index: 100;
}
.border-activate {
    border-bottom: red solid 4px;
}

.menu-bottom {
    background-color: rgba(255, 255, 255);
    position: relative;
    z-index: 100;
}

.menu-top {
    position: relative;
    background-color: #212529;
    z-index: 100;
}
.has-search .form-control {
    padding-left: 2.375rem;
}

.has-search .form-control-feedback {
    z-index: 2;
    display: block;
    width: 2.375rem;
    height: 2.375rem;
    line-height: 2.375rem;
    text-align: center;
    pointer-events: none;
    color: #aaa;
}
@keyframes showup {
    from {
        top:100%
    }
  to {top: -1000%;}
}
.list-category{
    top: -1000%;
    width: 100%;
    position:absolute;
    z-index: 99;
    background-color: rgba(179, 169, 169,0.2);
    transition: 3s;
    animation-name: showup;
    animation-duration: 0.5s;
    padding:5em 4em;
}
@keyframes showdown {
    from {
        top:-1000%
    }
  to {top: 100%;}
}
.show-list-category{
    width:100%;

    display: block;
    position:absolute;
    z-index: 99;
    background-color: rgba(179, 169, 169,0.8);
    animation-name: showdown;
    animation-duration: 0.5s;
    padding:5em 4em;
}
.btn-login {
    cursor :pointer;
}
.active-login {
    position:fixed;
    z-index: 999;
}
.btn-login:hover {
    cursor:pointer;
    color :rgb(56, 122, 245)
}
.font-logo {
    font-family: 'Sassy Frass', cursive;
    color: #F56A79
}
.input-search {
    border-radius: 15px;
    border-color: #aaa !important;
    padding : 10px 5px;
    background-color: #45474b;
}
.input-search::placeholder {
    color : white;
    padding-left: 2rem;
}
.img-flag {
    width:4%;
}
.search-control {
    position:relative;
}
.icon-search {
    position:absolute;
    top:30%;
    left:5%;
}
.title-menu {
    border-color: #212529 !important;
}
.title-menu:hover{
    color :rgb(0, 230, 230) !important;
    cursor:pointer;
}
.icon-cursor{
    cursor:pointer;
}
.icon-cursor:hover {
    color:#F56A79 !important;
}
.action-menu-user {
    cursor:pointer;
}
.action-menu-user:hover {
    color:rgb(3, 101, 182) !important;
}
</style>
