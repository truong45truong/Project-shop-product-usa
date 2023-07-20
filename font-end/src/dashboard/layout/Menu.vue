
<template>
    <div id="viewport">
        <!-- Sidebar -->
        <div id="sidebar" class="d-flex flex-column align-items-center">
            <header class="w-100">
                <a class="navbar-brand mt-3" href="/">
                    <h2 class="m-0 font-logo"><b><i>ShopKatie</i></b></h2>
                </a>
                <button class="btn-logout mx-5 my-3" @click="logout()">
                    <font-awesome-icon icon="fa-solid fa-arrow-right-from-bracket" /> <span>Đăng xuất</span>
                 </button>
            </header>
            <div class="rounded mt-5">
                 <button class="btn-menu-1 mx-5 my-3 px-2" @click="clickLayout(1)" :class="{ 'text-info' : get_is_show_layout.isShowDashboard}">
                    <font-awesome-icon icon="fa-solid fa-house" /> <span>DashBoard</span>
                 </button>
                 <hr class="hr-menu">
                 <button class="btn-menu-1 mx-5 my-3 px-2" :class="{ 'text-info' : get_is_show_layout.isShowUser}" @click="clickLayout(2)">
                    <font-awesome-icon icon="fa-solid fa-user" /> <span>User</span>
                 </button>
                 <hr class="hr-menu">
                 <button class="btn-menu-1 mx-5 my-3 px-2" :class="{ 'text-info' : get_is_show_layout.isShowOrder}" @click="clickLayout(3)">
                    <font-awesome-icon icon="fa-solid fa-money-check" /> <span>Order</span>
                 </button>
                 <hr class="hr-menu">
                 <button class="btn-menu-1 mx-5 my-3 px-2" :class="{ 'text-info' : get_is_show_layout.isShowProduct}" @click="clickLayout(4)">
                    <font-awesome-icon icon="fa-brands fa-product-hunt" /> <span>Product</span>
                 </button>
            </div>
        </div>
    </div>
</template>
  
<script>
import { mapGetters } from 'vuex'
import { useRoute } from 'vue-router'


export default {
    name: "MenuDashBoard",
    setup() {
        const route = useRoute();
        return { route };
    },
    async created() {
    },
    data: () => ({
        isShowListHeart: null,
        isShowCart: null,
        isShowChangePassword: null,
        isShowDashboard : true,
        isShowUser : false,
        isShowOrder : false,
        isShowProduct : false ,
    }),
    components: {
    },
    computed: {
        ...mapGetters('dashboard', {
            get_is_show_layout: 'getIsShowLayout',
        }),
    },
    methods: {
        clickLayout( type){
            switch (type) {
                case 1:
                    this.$store.dispatch('dashboard/actionSelectedLayout' , { type : 1})
                    break;
                case 2:
                    this.$store.dispatch('dashboard/actionSelectedLayout' , { type : 2})
                    break;
                case 3:
                    this.$store.dispatch('dashboard/actionSelectedLayout' , { type : 3})
                    break;
                case 4:
                    this.$store.dispatch('dashboard/actionSelectedLayout' , { type : 4})
                    break;

                default:
                    this.$store.dispatch('dashboard/actionSelectedLayout' , { type : 1})
                    break;
            }
        },
        logout(){
            this.$store.dispatch('auth/logout')
        }
    },
    created(){
        this.$store.dispatch('dashboard/actionSelectedLayout' , { type : 1})
    }
}
</script>
<style scoped>
.btn-logout {
    font-size: 14px;
    border :none ;
    background-color:  transparent;
    color : white;
}
#accordion .panel {
    margin-bottom: 20px;
}

#accordion .panel-heading {
    background-color: #3bb7c1 ;
    color: #fff;
    text-transform: uppercase;
}

.accordion-toggle {
    padding: 0px;
}

.accordion-toggle:hover {
    cursor: pointer;
}

.accordion-toggle h4 {
    line-height: 50px;
    padding-left: 15px;
}

.accordion-toggle span {
    background-color: #0d4b50;
    padding: 0px 15px 0px 15px;
    line-height: inherit;
    top: 0;
}
.bg-menu {
    background-color: #020c1a;
}
.hr-menu {
    background-color: white;
    color: white;
    margin : 0;
    padding:0.5px 0;
}
.btn-menu-1 {
    background-color: transparent;
    border:none;
    color:#fff;
}
</style>