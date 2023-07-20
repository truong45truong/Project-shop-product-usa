<template>
    <div class="h-100 d-flex">
        <div class="container">
            <h2 class="login-title">Đăng nhập</h2>
            <form class="login-form">
                <div>
                    <label for="email">Tên đăng nhập </label>
                    <input v-model="username" id="email" type="text" placeholder="tên đăng nhập" name="email" required />
                </div>
                <div>
                    <label for="password">Mật khẩu </label>
                    <input v-model="password" id="password" type="password" placeholder="mật khẩu" name="password" required />
                </div>
                <button class="btn btn--form" type="button" value="Log in" @click="login">
                    Đăng nhập
                </button>
            </form>
        </div>
    </div>
</template>

<script >
import { mapGetters } from 'vuex'
import { useRoute } from 'vue-router'
import {actionAdmin} from './../../common/admin.service'
export default {
    name: "LoginDashBoard",
    setup() {
        const route = useRoute();
        return { route };
    },
    async created() {
    },
    data: () => ({
        username : null,
        password : null

    }),
    components: {
    },
    computed: {
        ...mapGetters('notice', {
            get_is_activate: 'isActivate',
            get_activate_menu: 'isActivateMenu'
        }),
        ...mapGetters('dashboard', {
            get_is_show_layout: 'getIsShowLayout',
        }),
    },
    methods: {
        login(){
            this.$emit('login',this.username,this.password)
            actionAdmin.getInforAdmin().then(res => {
                if(res.status != 200){
                    // this.$store.dispatch('auth/logout')
                }
            }).catch(()=>{
                this.$store.dispatch('auth/logout')
            })

        }
    }
}
</script>
<style scoped>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html,
#app {
    height: 100%;
}

html {
    background: linear-gradient(to right bottom, #fbdb89, #f48982);
    background-repeat: no-repeat;
    background-size: cover;
    width: 100%;
    height: 100%;
    background-attachment: fixed;
}

#app {
    font-family: sans-serif;
    line-height: 1.4;
    display: flex;
}

.container {
    width: 400px;
    margin: auto;
    padding: 36px 48px 48px 48px;
    background-color: #f2efee;

    border-radius: 11px;
    box-shadow: 0 2.4rem 4.8rem rgba(0, 0, 0, 0.15);
}

.login-title {
    padding: 15px;
    font-size: 22px;
    font-weight: 600;
    text-align: center;
}

.login-form {
    display: grid;
    grid-template-columns: 1fr;
    row-gap: 16px;
}

.login-form label {
    display: block;
    margin-bottom: 8px;
}

.login-form input {
    width: 100%;
    padding: 1.2rem;
    border-radius: 9px;
    border: none;
}

.login-form input:focus {
    outline: none;
    box-shadow: 0 0 0 4px rgba(253, 242, 233, 0.5);
}

.btn--form {
    background-color: #f48982;
    color: #fdf2e9;
    align-self: end;
    padding: 8px;
}

.btn,
.btn:link,
.btn:visited {
    display: inline-block;
    text-decoration: none;
    font-size: 20px;
    font-weight: 600;
    border-radius: 9px;
    border: none;

    cursor: pointer;
    font-family: inherit;

    transition: all 0.3s;
}

button {
    outline: 1px solid #f48982;
}

.btn--form:hover {
    background-color: #fdf2e9;
    color: #f48982;
}
</style>