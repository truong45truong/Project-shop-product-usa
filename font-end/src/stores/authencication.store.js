import { UserApiService } from "../common/user.service";
import {actionJWT} from "../common/jwt.service";

const user = localStorage.getItem('user');
const photo = localStorage.getItem('userProfile');
const initialState = { user :  user
  ? { status: { loggedIn: true , error : false}, user : user , userProfilePhoto : photo}
  : { status: { loggedIn: false , error : false}, user: null , userProfilePhoto : null },
  isLoading : false
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
      }})
      await UserApiService.get({params : {
        username : payload.username,
        password : payload.password
      }}).then(
         response => {
            if( response.data.user){
                localStorage.setItem('user',response.data.user.email);
                localStorage.setItem('userProfile',response.data.user.photo);
                commit('loginSuccess',response.data.user)
            }
            if (response.data.error.value){
              commit('loginFailure',response.data.error)
            }
         }, 
         error => {
            localStorage.removeItem('user')
            commit('loginFailure',error)
         }
      );
    },

     /* logout */

    logout({ commit }) {
      localStorage.removeItem('user')
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
            console.log(response.data.error.value)
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
      state.user.userProfilePhoto = user.photo
    },
    loginFailure(state,error) {
      state.user.status.loggedIn = false;
      state.user.status.error = error;
      state.user.user = null;
      state.user.userEmail = null;
      state.user.userProfilePhoto = null
    },
    logout(state) {
      state.user.status.loggedIn = false;
      state.user.status.error = false;
      state.user.user = null;
      state.user.userEmail = null;
      state.user.userProfilePhoto = null
    },
    registerSuccess(state) {
      state.status.loggedIn = false;
      state.status.error = false;
      state.user.user = null;
      state.userEmail = null;
      state.userProfilePhoto = null
    },
    registerActionsFailure(state,error) {
      state.user.status.loggedIn = false;
      state.user.status.error = error;
      state.user.user = null;
      state.user.userEmail = null;
      state.user.userProfilePhoto = null
    }
  }
};