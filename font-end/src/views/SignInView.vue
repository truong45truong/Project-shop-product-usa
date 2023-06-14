<template>
        <div id="bg-login" class="position-fixed h-100 w-100">
            <SignIn @login="login" />
        </div>
</template>

<script>
    import SignIn  from './../components/login/SignIn.vue'
    import { mapGetters, mapActions } from 'vuex'

    export default {
        name : "SignInView",
        data : () => ({
            nextPage : ''
        }),
        components : {
            SignIn
        },
        computed: {
            ...mapGetters('auth', {
                get_user         : 'currentUser',
                get_authenticated: 'isAuthenticated',
                get_error        : 'errorAuthenticated',
                isShowLoginStore : 'isShowLogin'
            }),
        },
        watch: {
            get_authenticated(newValue, oldValue){
                if(newValue == true){
                    this.$router.push(this.nexPage)
                }
            } 
        },
        created(){
            if(this.get_authenticated == true){
                this.$router.push('/')
            }
            if(this.$router.currentRoute._value.query.nextPage)
            this.nexPage = '/' + this.$router.currentRoute._value.query.nextPage
            else {
                this.nexPage = '/'
            }
        },
        methods: {
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
        }
    }

</script>

<style>
#bg-login {
    display: flex;
    justify-content: center;
    /* Căn giữa chiều dọc */
    align-items: center;
    background-image: url('../assets/images/bg-login.jpg')
}
.login-bg {
    background-image: url('/assets/images/bg-login.jpg')
}
</style>