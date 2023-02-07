import { UserApiService } from "../common/user.service";
import { actionJWT } from "../common/jwt.service";

const user = localStorage.getItem('user');
const initialState = {
    isLoading: false,
    user: user ? user : false,
    productSupport: false,
    error: false,
}
// Promise.resolve(user);
export const virual_support = {
    namespaced: true,
    state: initialState,
    getters: {
        isLoading: state => state.isLoading,
        currentUser: state => state.user,
        errorAuthenticated: state => state.error,
        getProductSupport: state => state.productSupport
    },
    actions: {
        async answerTheQuestion(){

        }
    },

    mutations: {

    }
};