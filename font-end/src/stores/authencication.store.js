import { UserApiService } from "../common/user.service";
import {actionJWT} from "../common/jwt.service";
import {ApiService} from './../common/api.service'
const user = localStorage.getItem('user');
const photo = localStorage.getItem('userProfile');
const initialState = { user :  user
  ? { status: { loggedIn: true , error : false}, user : user , userProfilePhoto : photo ,inforUser : false}
  : { status: { loggedIn: false , error : false}, user: null , userProfilePhoto : null , inforUser : false},
  isLoading : false,
  tokenGetInfor : false,
 }
// Promise.resolve(user);
export const auth = {
  namespaced: true,
  state: initialState,
  getters : {
    isAuthenticated : state  => state.user.status.loggedIn,
    currentUser : state => state.user,
    errorAuthenticated : state => state.user.status.error ,
    getProfilePhoto : state => state.user.userProfilePhoto 
  },  
  actions: {
    /* login */
    async login({ commit }, payload) {
      await actionJWT.setLocalTokenJWT({params : {
        username : payload.username,
        password : payload.password
      }}).catch(res => {
        return commit('loginFailure',"Wrong username or password")
      })
      await UserApiService.get({params : {
        username : payload.username,
        password : payload.password
      }}).then(
         response => {
          console.log("response.data",response.data)
            if( response.data.user){
                localStorage.setItem('user',response.data.user.email);
                localStorage.setItem('userProfile',response.data.user.photo);
                localStorage.setItem('token_permission_infor_user',response.data.user.token_permission_infor_user)
                localStorage.setItem('csrf_token',response.data.csrf_token)
                ApiService.setHeaderCookieCsrf()
                commit('loginSuccess',response.data.user)
                console.log('loginSuccess')
            }
            if (response.data.error.value){
              console.log("response.data",response.data)
              commit('loginFailure',response.data.error)
            }
            return response
         }, 
         error => {
            localStorage.removeItem('user')
            commit('loginFailure',error)
            return error
         }
      );
    },

     /* logout */

    logout({ commit }) {
      localStorage.removeItem('user')
      localStorage.removeItem('userProfile')
      localStorage.removeItem('token_permission_infor_user')
      console.log('logout')
      commit('logout');
    },

     /* register */

    register({commit},payload){
      return UserApiService.reggisterUser({
        params : {
          username : payload.username_register,
          password : payload.password_register,
          email : payload.email_register,
          phone : payload.phone_register
        }
      }).then(
        response => {
          if (response.data.error.value){
            commit('registerActionsFailure',response.data.error)
          }
          else {
            commit('registerSuccess')
          }
        },
         error => {
            commit('registerActionsFailure',error)
         }
      )
    }

  },
  mutations: {
    loginSuccess(state, user) {
      state.user.status.loggedIn = true;
      state.user.status.error = false;
      state.user.user = user.email;
      state.user.inforUser = false;
      state.user.userProfilePhoto = user.photo
    },
    loginFailure(state,error) {
      state.user.status.loggedIn = false;
      state.user.status.error = error;
      state.user.user = null;
      state.user.userEmail = null;
      state.user.inforUser = false
      state.user.userProfilePhoto = null
    },
    logout(state) {
      state.user.status.loggedIn = false;
      state.user.status.error = false;
      state.user.user = null;
      state.user.userEmail = null;
      state.user.inforUser = false
      state.user.userProfilePhoto = null
    },
    registerSuccess(state) {
      state.user.status.loggedIn = false;
      state.user.status.error = false;
      state.user.user = null;
      state.userEmail = null;
      state.user.inforUser = false
      state.userProfilePhoto = null
    },
    registerActionsFailure(state,error) {
      state.user.status.loggedIn = false;
      state.user.status.error = error;
      state.user.user = null;
      state.user.userEmail = null;
      state.user.userProfilePhoto = null;
      state.user.inforUser = false
    }
  }
};