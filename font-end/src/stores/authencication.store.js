import { actionUser } from "../common/user.service";
import { actionJWT } from "../common/jwt.service";
import { ApiService } from "./../common/api.service";
import { Buffer } from "buffer";
import { Crypto } from "./../security";
import { decryptRsaApiService } from "./../common/decrypt.rsa.service";

const user = localStorage.getItem("user");
const photo = localStorage.getItem("userProfile");
const initialState = {
  user: user
    ? {
        status: { loggedIn: true, error: false },
        user: user,
        userProfilePhoto: photo,
        inforUser: false,
      }
    : {
        status: { loggedIn: false, error: false },
        user: null,
        userProfilePhoto: null,
        inforUser: false,
      },
  isLoading: false,
  tokenGetInfor: false,
  isLogin : false
};
// Promise.resolve(user);
export const auth = {
  namespaced: true,
  state: initialState,
  getters: {
    isAuthenticated: (state) => state.user.status.loggedIn,
    currentUser: (state) => state.user,
    errorAuthenticated: (state) => state.user.status.error,
    getProfilePhoto: (state) => state.user.userProfilePhoto,
    isShowLogin: (state) => state.isLogin,
  },
  actions: {
    actionShowLogin({ commit }){
      commit('successShowLogin')
    },
    actionHideLogin({commit}){
      commit('successHideLogin')
    },
    /* login */
    async login({ commit }, payload) {
      var cipher = Crypto.encryptData(
        localStorage.getItem("public_key"),
        payload.password
      );

      await actionUser
        .loginUser({
          username: payload.username,
          password: cipher,
          device_id: localStorage.getItem("device_id")
        })
        .then(
          async (response) => {
            localStorage.setItem("jwt_token_access", response.data.access_token);
            ApiService.setHeader();
            await actionUser.getInforUser().then((response) => {
              console.log(response);
              if (response.status == 200) {
                console.log(response);
                localStorage.setItem("user", response.user.email);
                localStorage.setItem("userProfile", response.user.photo);
                localStorage.setItem(
                  "token_permission_infor_user",
                  response.user.token_permission_infor_user
                );
                commit("loginSuccess", response.user);

                console.log("loginSuccess");
              }
              return response;
            });
          },
          (error) => {
            localStorage.removeItem("user");
            commit("loginFailure", {
              value: error,
              type: 1,
            });
            return error;
          }
        );
    },

    /* logout */

    async logout({ commit }) {
      return await actionUser.logoutUser().then(response => {
          if(response.data.status == 200){
            localStorage.removeItem("user");
            localStorage.removeItem("userProfile");
            localStorage.removeItem("token_permission_infor_user");
            console.log("logout");
            commit("logout");
          }
        }).catch(error => {
          console.log(error)
          if(error.response.status == 401){
            commit("logout");
          }
        })
    },

    /* register */

    register({ commit }, payload) {
      var cipher = Crypto.encryptData(
        localStorage.getItem("public_key"),
        payload.password_register
      );
      console.log(cipher)
      console.log(payload)
      return actionUser.RegisterUser({
        params: {
          username: payload.username_register,
          password: cipher,
          email: payload.email_register,
          phone: payload.phone_register,
          name : payload.name_register,
          address : payload.address_register,
          device_id: localStorage.getItem("device_id")
        },
      }).then(
        (response) => {
          console.log(response)
          if (response.data.status = 200) {
            commit("registerSuccess");
          } else {
            console.log(response.data.error.value)
            commit("registerActionsFailure", response.data.error);
          }
        },
        (error) => {
          commit("registerActionsFailure", error);
        }
      );
    },
  },
  mutations: {
    successShowLogin(state){
      state.isLogin = true;
    },
    successHideLogin(state){
      state.isLogin = false;
    },
    loginSuccess(state, user) {
      state.user.status.loggedIn = true;
      state.user.status.error = false;
      state.user.user = user.email;
      state.user.inforUser = false;
      state.user.userProfilePhoto = user.photo;
    },
    loginFailure(state, error) {
      state.user.status.loggedIn = false;
      state.user.status.error = error;
      state.user.user = null;
      state.user.userEmail = null;
      state.user.inforUser = false;
      state.user.userProfilePhoto = null;
    },
    logout(state) {
      state.user.status.loggedIn = false;
      state.user.status.error = false;
      state.user.user = null;
      state.user.userEmail = null;
      state.user.inforUser = false;
      state.user.userProfilePhoto = null;
    },
    registerSuccess(state) {
      state.user.status.loggedIn = false;
      state.user.status.error = false;
      state.user.user = null;
      state.userEmail = null;
      state.user.inforUser = false;
      state.userProfilePhoto = null;
      state.isLoading = false;
    },
    registerActionsFailure(state, error) {
      state.user.status.loggedIn = false;
      state.user.status.error = error;
      state.user.user = null;
      state.user.userEmail = null;
      state.user.userProfilePhoto = null;
      state.user.inforUser = false;
      state.isLoading = false;
    },
  },
};
