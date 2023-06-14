<template>
	<section class="ftco-section w-100">
		<div class="container position-relative" v-show="type">
			<font-awesome-icon icon="fa-solid fa-xmark" class="fs-4 position-absolute icon-cancel-login" @click="exit" />
			<div class="row justify-content-center layout-login bg-light shadow p-3 bg-body mx-1">
				<div class="col-lg-6 d-flex">
					<img class="img m-auto" src="./../../assets/images/milk-login.jpg">
				</div>
				<div class="col-lg-6">
					<div class="w-100 d-flex rounded fill-content">
						<div class="p-sm-5 p-3 w-100">
							<div class="d-flex flex-column w-100 align-items-center">
								<div>
									<h3 class="mb-4">Đăng nhập</h3>
								</div>
							</div>
							<form action="#" class="signin-form">
								<div class="mb-sm-3 w-100">
									<label class="label" for="name">Tài khoản </label>
									<input type="text" class="form-control w-100" placeholder="tài khoản" required
										v-model="username" :class="{ 'border border-danger' : message != ''}">
								</div>
								<div class="mb-sm-3 w-100">
									<label class="label" for="password">Mật khẩu</label>
									<input type="password" class="form-control w-100" placeholder="mật khẩu" required
										v-model="password" :class="{ 'border border-danger' : message != ''}">
								</div>
								<div class="mt-4 flex flex-column w-100 align-items-center">
									<div class="d-flex flex-column">
										<span v-if="get_error != false " class="text-danger text-center mb-2"> 
											<span v-if="get_error.type == 1 || get_error.type == 2">Tài khoản hoặc mật khẩu sai</span>
										</span>
										<span v-if="message != ''" class="text-danger text-center mb-2"> 
											<span>Tài khoản hoặc mật khẩu sai</span>
										</span>
									</div>
									<div class="d-flex flex-column">
										<button type="button"
											class="form-control btn btn-primary rounded submit px-3 m-auto"
											@click="login()"> Đăng nhập </button>
									</div>
								</div>
								<div class="d-flex w-100 justify-content-around mt-4">
									<a href="#"> Quên mật khẩu </a>
									<p class="text-center m-0">Chưa có tài khoản? <a data-toggle="tab" href="#signup"
											@click="signUp()">Đăng kí</a></p>
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
						<div class="login-wrap p-lg-4 p-md-5 p-2 w-100 mb-2">
							<div class="d-flex justify-content-center w-100">
								<h3 class="mb-sm-4 mb-2">Đăng kí</h3>
							</div>
							<form action="#" class="signin-form">
								<div class="mb-sm-3">
									<label class="label" for="name">Tài khoản </label>
									<input type="text" class="form-control w-100" placeholder="tài khoản" required
										v-model="username_register"
										:class="{ 'border border-danger': error_empty.username }">
									<p class="text-danger" v-if="showErrorUsernameRegister()">{{ get_error.value }}</p>
									<span v-if="error_empty.username" class="text-danger">Nhâp tên tài khoản</span>
								</div>
								<div class="mb-sm-3">
									<label class="label" for="password">Mật khẩu</label>
									<input type="password" class="form-control w-100" placeholder="mật khẩu" required
										v-model="password_register"
										:class="{ 'border border-danger': error_empty.password }">
									<span v-if="error_empty.password" class="text-danger">Nhập mật khẩu lần 1</span>
								</div>
								<div class="mb-sm-3">
									<label class="label" for="password">Nhập lại mật khẩu</label>
									<input type="password" class="form-control w-100" @blur="handleBlur"
										placeholder="mật khẩu" required v-model="password_register_confirm" ref="checkpw"
										:class="{ 'border border-danger': error_empty.password_confirm }">
									<p class="text-danger" v-if="password_register_confirm_error"> Password no same</p>
									<span v-if="error_empty.password_confirm" class="text-danger">Nhập mật khẩu lần 2</span>
								</div>
								<div class="mb-sm-3">
									<label class="label" for="name">Email </label>
									<input type="email" class="form-control w-100" placeholder="email" required v-on:blur="checkEmail"
										v-model="email_register" :class="{ 'border border-danger': error_empty.email }">
									<span v-if="error_empty.email" class="text-danger">Nhập email</span>
									<span v-if="check_mail_error.value" class="text-danger">{{check_mail_error.content}}</span>
								</div>
								<div class="mb-sm-3">
									<label class="label" for="name">Họ và tên </label>
									<input type="email" class="form-control w-100" placeholder="Họ và tên" required
										v-model="name_register" :class="{ 'border border-danger': error_empty.email }">
									<span v-if="error_empty.name" class="text-danger">Nhập họ và tên</span>
								</div>
								<div class="mb-sm-3">
									<label class="label" for="name">Số điện thoại </label>
									<input type="email" class="form-control w-100" placeholder="số điện thoại" required v-on:blur="checkPhone"
										v-model="phone_register" :class="{ 'border border-danger': error_empty.phone }" >
									<p class="text-danger" v-if="showErrorPhoneRegister()">{{ get_error.value }}</p>
									<span v-if="error_empty.phone" class="text-danger">Nhập số điện thoại</span>
									<span v-if="check_phone_error.value" class="text-danger">{{check_phone_error.content}}</span>
								</div>
								<div class="mb-sm-3">
									<label class="label" for="name">Địa chỉ </label>
									<input type="email" class="form-control w-100" placeholder="Địa chỉ" required
										v-model="address_register" :class="{ 'border border-danger': error_empty.email }">
									<span v-if="error_empty.address" class="text-danger">Nhập địa chỉ</span>
								</div>
								<div class=" d-flex justify-content-center">
									<button type="button" class="form-control btn btn-primary rounded submit px-3 my-2"
										@click="register">Sign Up</button>
								</div>
							</form>
							<p class="text-center">Đã có tài khoản? <a data-toggle="tab" href="#signin"
									@click="signIn()">Đăng nhập</a></p>
							<p class="text-danger" v-if="showMessage">{{ message }}</p>
						</div>
					</div>
				</div>
			</div>
		</div>
	</section>
</template>
<script>
import { mapGetters, mapActions } from 'vuex'
import {decryptRsaApiService} from './../../common/decrypt.rsa.service'
import forge from 'node-forge';
export default {
	name: 'SignIn',
	data() {
		return {
			/* ------------------------------- data login ------------------------------- */
			username: '',
			password: '',
			type: true,
			message: '',
			/* ------------------------------ data register ----------------------------- */
			username_register: '',
			password_register: '',
			password_register_confirm: '',
			email_register: '',
			phone_register: '',
			address_register : '' ,
			name_register : '',
			/* ---------------------------- data notify error --------------------------- */
			username_register_error: '',
			error_empty: {
				password: false,
				username: false,
				password_confirm: false,
				email: false,
				phone: false,
				name : false,
				address: false
			},
			password_register_confirm_error: false,
			email_register_error: '',
			phone_register_error: '',
			check_phone_error : {
				value : false,
				content : ''
			},
			check_mail_error : {
				value : false,
				content : ''
			}
		}
	},
	methods: {
		/* -------------------------------------------------------------------------- */
		/*                                   ACTIONS                                  */
		/* -------------------------------------------------------------------------- */
		/* -------------------------- method register user -------------------------- */
		login(){
			this.$emit('login', this.username, this.password)
			return new Promise((resolve) => {
            const checkValue = () => {
					if (this.get_authenticated === true) {
						this.$store.dispatch('cart/actionGetData')
						this.$store.dispatch('heart/actionGetData')
						this.$store.dispatch('auth/actionHideLogin')
						
						resolve();
					}
					else {
						setTimeout(checkValue, 500);
					}
				};

				checkValue();
			});
		},
		checkData() {
			console.log("check data running")
			if (this.username_register == '') this.error_empty.username = true; else this.error_empty.username = false;
			if (this.password_register == '') this.error_empty.password = true; else this.error_empty.password = false;
			if (this.password_register_confirm == '') this.error_empty.password_confirm = true; else this.error_empty.password_confirm = false;
			if (this.email_register == '') this.error_empty.email = true; else this.error_empty.email = false;
			if (this.phone_register == '') this.error_empty.phone = true; else this.error_empty.phone = false;
			if (this.name_register == '') this.error_empty.name = true; else this.error_empty.name = false;
			if (this.address_register == '') this.error_empty.address = true; else this.error_empty.address = false;

			if (
				this.error_empty.username == true ||
				this.error_empty.password == true ||
				this.error_empty.password_register == true ||
				this.error_empty.email == true ||
				this.error_empty.phone == true ||
				this.error_empty.name == true ||
				this.error_empty.address == true
			) {
				return false
			}
			return true
		},
		register (){
			if (this.checkData() == true){
				this.$store.dispatch('auth/register', { 
					username_register : this.username_register,
					password_register : this.password_register,
					email_register : this.email_register,
					phone_register : this.phone_register,
					name_register : this.name_register,
					address_register : this.address_register
				}).then(() => {
					if (this.get_error == false) {
						this.message = "Register Success";
					}
				}).catch( error => {
					console.error("error",error)
					this.message = "Register Failure";
				})
			}
		},
		checkPhone() {
            const pattern = /^(\+84|0)\d{9}$/;
            if (pattern.test(this.phone_register) == false) {
                this.check_phone_error.value = true
				this.check_phone_error.content = "Số điện thoại không đúng"
            } else {
                this.check_phone_error.error = false
				this.check_phone_error.content = ''
            }
        },
		checkEmail() {
			const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
			if(emailRegex.test(this.email_register) == false ){
				this.check_mail_error.value = true
				this.check_mail_error.content = "Email không đúng"
			}else {
				this.check_mail_error.error = false
				this.check_mail_error.content = ''
			}
		},
		/* ----------------------------- method sign up ----------------------------- */

		signUp() {
			this.type = false
			this.message = ''
		},

		/* ----------------------------- method sign in ----------------------------- */

		signIn() {
			this.type = true
			this.message = ''
			this.get_error = false
		},
		/* -------------------------------------------------------------------------- */
		/*                                   ERRORS                                   */
		/* -------------------------------------------------------------------------- */
		notifyAfferLogin(){
			return this.get_authenticated
		},

		/* -------------------------- method check message -------------------------- */

		showMessage() {
			return this.message != '' ? true : false
		},

		/* ------------------ method check error username register ------------------ */

		showErrorUsernameRegister() {
			return this.get_error.type == 3 ? true : false
		},

		/* -------------------- method check error email register ------------------- */

		showErrorEmailRegister() {
			return this.get_error.type == 4 ? true : false
		},

		/* -------------------- method check error phone register ------------------- */

		showErrorPhoneRegister() {
			return this.get_error.type == 5 ? true : false
		},

		/* --------------------- check password no same register -------------------- */

		checkPasswordSame() {
			return this.password_register == this.password_register_confirm ? true : false
		},

		/* -------------------------------------------------------------------------- */
		/*                              METHODS HANDLE UI                             */
		/* -------------------------------------------------------------------------- */
		handleBlur() {
			if (this.checkPasswordSame() == false) {
				this.password_register_confirm_error = true
			}
			else {
				this.password_register_confirm_error = false
			}
		},
		/* -------------------------------------------------------------------------- */
		/*                                 METHOD EXIT                                */
		/* -------------------------------------------------------------------------- */
		exit(){
			this.$store.dispatch('auth/actionHideLogin')
			this.$emit('hideLogin')
		}
	},
	computed: {
		...mapGetters('auth', {
			get_user: 'currentUser',
			get_authenticated: 'isAuthenticated',
			get_error: 'errorAuthenticated'
		}),
		...mapActions('auth', {
			login_user: 'login',
			register_user: 'register'
		}),
	},
	mounted() {
		if (this.authenticated == true) {
			this.$router.push("/");
		}
	},
	async created(){
		await decryptRsaApiService.decryptToken({ params : {
			device_id : localStorage.getItem('device_id') ? localStorage.getItem('device_id') : false,
		}}).then( response => {
			if(response.status == 200){
				localStorage.setItem('public_key',response.data.public_key);
				localStorage.setItem('device_id',response.data.device_id);
			}
			if(response.status == 201){
				localStorage.setItem('device_id',response.data.device_id);
				localStorage.setItem('public_key',response.data.public_key);
			}
		})
	}

}
</script>
<style lang="scss">
.ftco-section{
	z-index: 9999999;
}
.img {
	width: 100%;
	height: auto;

}

.form-group {
	max-width: 250px !important;
}

.form-control {
	width: fit-content !important;
}
.icon-cancel-login {
	right:3%;
	top:3%;
	cursor:pointer;
}
.icon-cancel-login:hover {
	color:rgb(104, 104, 104)
}
@media only screen and (max-width: 1024px) {
	.img {
		display :none;
	}
	.ftco-section {
		top:10%;
	}
	.icon-cancel-login {
		right:10%;
	}
}
@media only screen and (max-width: 424px){
	.label {
		font-size: 11px;;
	}
	input.form-control {
		font-size: 11px;
	}
	button.form-control {
		font-size: 11px;
	}
	p {
		font-size: 11px;
	}
	a {
		font-size: 11px;
	}
}
</style>