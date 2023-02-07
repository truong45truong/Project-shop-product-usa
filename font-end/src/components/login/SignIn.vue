<template>
	<section class="ftco-section w-100">
		<div class="container" v-show="type">
			<div class="row justify-content-center layout-login bg-light shadow p-3 bg-body mx-1">
				<div class="col-lg-6 d-flex">
					<img class="img m-auto" src="./../../assets/images/milk-login.jpg">
				</div>
				<div class="col-lg-6">
					<div class="w-100 d-flex rounded fill-content">
						<div class="p-5 w-100">
							<div class="d-flex flex-column w-100 align-items-center">
								<div>
									<h3 class="mb-4">Đăng nhập</h3>
								</div>
							</div>
							<form action="#" class="signin-form">
								<div class="mb-3 w-100">
									<label class="label" for="name">Tài khoản </label>
									<input type="text" class="form-control w-100" placeholder="tài khoản" required
										v-model="username">
									<p v-if="showErrorUsername()" class="text-danger"> {{get_error.value}} </p>
							</div>
								<div class="mb-3 w-100">
									<label class="label" for="password">Mật khẩu</label>
									<input type="password" class="form-control w-100" placeholder="mật khẩu" required
										v-model="password">
										<p v-if="showErrorPassword()" class="text-danger"> {{get_error.value}} </p>
								</div>
								<div class="mt-4 flex flex-column w-100 align-items-center">
									<div class="d-flex">
										<button type="button" class="form-control btn btn-primary rounded submit px-3 m-auto"
										@click="$emit('login',username,password)"> Đăng nhập </button>
									</div>
								</div>
								<div class="d-flex w-100 justify-content-around mt-4">
										<a href="#"> Quên mật khẩu </a>
										<p class="text-center m-0">Chưa có tài khoản? <a data-toggle="tab" href="#signup" @click="signUp()" >Đăng kí</a></p>
								</div>
							</form>
						</div>
					</div>
				</div>
			</div>
		</div>

		<div class="container" v-show="!type">
			<div class="row d-flex justify-content-center w-100  bg-light shadow p-3 rounded m-0">
				<div class="col-lg-6 d-flex">
					<img class="img m-auto" src="./../../assets/images/sign-up-bg2.jpg">
				</div>
				<div class="col-lg-6">
					<div class="d-md-flex sigup-center fit-content">
						<div class="login-wrap p-4 p-md-5 w-100 mb-2">
							<div class="d-flex justify-content-center w-100">
								<h3 class="mb-4">Đăng kí</h3>
							</div>
							<form action="#" class="signin-form">
								<div class="mb-3">
									<label class="label" for="name">Tài khoản </label>
									<input type="text" class="form-control w-100" placeholder="tài khoản" required
										v-model="username_register">
										<p class="text-danger" v-if="showErrorUsernameRegister()">{{get_error.value}}</p>
								</div>
								<div class="mb-3">
									<label class="label" for="password">Mật khẩu</label>
									<input type="password" class="form-control w-100" placeholder="mật khẩu" required
										v-model="password_register">
								</div>
								<div class="mb-3">
									<label class="label" for="password" >Nhập lại mật khẩu</label>
									<input type="password" class="form-control w-100" @blur="handleBlur" placeholder="mật khẩu" required
										v-model="password_register_confirm" ref="checkpw" >
									<p class="text-danger" v-if="password_register_confirm_error"> Password no same</p>
								</div>
								<div class="mb-3">
									<label class="label" for="name">Email </label>
									<input type="email" class="form-control w-100" placeholder="email" required
										v-model="email_register">
								</div>
								<div class="mb-3">
									<label class="label" for="name">Số  điện thoại </label>
									<input type="email" class="form-control w-100" placeholder="số điện thoại" required
										v-model="phone_register">
										<p class="text-danger" v-if="showErrorPhoneRegister()">{{get_error.value}}</p>
								</div>
								<div class=" d-flex justify-content-center">
									<button type="button" class="form-control btn btn-primary rounded submit px-3 my-2"
										@click="register()">Sign Up</button>
								</div>
							</form>
							<p class="text-center">Đã có tài khoản? <a data-toggle="tab" href="#signin" @click="signIn()" >Đăng nhập</a></p>
							<p class="text-danger" v-if="showMessage">{{message}}</p>
						</div>
					</div>
				</div>
			</div>
		</div>
	</section>
</template>
<script>
import { mapGetters, mapActions } from 'vuex'
export default {
	name: 'SignIn',
	data() {
		return {
			/* ------------------------------- data login ------------------------------- */
			username: '',
			password: '',
			type    : true,
			message : '',
			/* ------------------------------ data register ----------------------------- */
			username_register        : '',
			password_register        : '',
			password_register_confirm: '',
			email_register           : '',
			phone_register           : '',
			/* ---------------------------- data notify error --------------------------- */
			username_register_error        : '',
			password_register_confirm_error: false,
			email_register_error           : '',
			phone_register_error           : '',
		}
	},
	methods: {
		/* -------------------------------------------------------------------------- */
		/*                                   ACTIONS                                  */
		/* -------------------------------------------------------------------------- */
		/* -------------------------- method register user -------------------------- */
		register (){
			this.register_user.then(() => {
				if (this.get_error == false) {
					this.message = "Register Success"
				}
			}).catch( error => {
				console.error("error",error)
				this.message = "Register Failure"
			})
		},
		/* ----------------------------- method sign up ----------------------------- */

		signUp() {
			this.type = false
		},

		/* ----------------------------- method sign in ----------------------------- */

		signIn(){
			this.type = true
		},
		/* -------------------------------------------------------------------------- */
		/*                                   ERRORS                                   */
		/* -------------------------------------------------------------------------- */
		/* ----------------------- method check error username ---------------------- */

		showErrorUsername (){
			return this.get_error.type == 1 ? true : false 
		},

		/* -------------------- method check error password wrong ------------------- */

		showErrorPassword (){
			return this.get_error.type == 2 ? true : false 
		},

		/* -------------------------- method check message -------------------------- */

		showMessage(){
			return this.message != '' ? true : false
		},

		/* ------------------ method check error username register ------------------ */

		showErrorUsernameRegister () {
			return this.get_error.type == 3 ? true : false 
		},

		/* -------------------- method check error email register ------------------- */

		showErrorEmailRegister () {
			return this.get_error.type == 4 ? true : false 
		},

		/* -------------------- method check error phone register ------------------- */

		showErrorPhoneRegister () {
			return this.get_error.type == 5 ? true : false 
		},

		/* --------------------- check password no same register -------------------- */

		checkPasswordSame () {
			return this.password_register == this.password_register_confirm ? true : false
		},

		/* -------------------------------------------------------------------------- */
		/*                              METHODS HANDLE UI                             */
		/* -------------------------------------------------------------------------- */
		handleBlur() {
			if (this.checkPasswordSame() == false ){
				this.password_register_confirm_error = true
			}
			else {
				this.password_register_confirm_error = false
			}
    	}
	},
	computed: {
		...mapGetters('auth', {
			get_user         : 'currentUser',
			get_authenticated: 'isAuthenticated',
			get_error        : 'errorAuthenticated'
		}),
		...mapActions('auth', {
			login_user   : 'login',
			register_user: 'register'
		}),
	},
	mounted() {
		if (this.authenticated == true) {
			this.$router.push("/");
		}
	}

}
</script>
<style lang="scss">
.img {
	width: 100%;
	height: auto;

}

.form-group {
	max-width: 250px !important;
}
.form-control {
	width:fit-content !important;
}
</style>