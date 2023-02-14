
const initialState = {
    isActivate: false,
    isAccept : null ,
    type : null,
    content : null ,
}
// Promise.resolve(user);
export const notice = {
    namespaced: true,
    state: initialState,
    getters: {
        isActivate: state => state.isActivate,
        isContent : state => state.content,
        isType : state => state.type,
        isAccept : state => state.isAccept,
    },
    actions: {
        activateShow({commit}){
            commit('activateSuccess')
        },
        activateHide({commit}){
            commit('hideSuccess')
        },
        actionTypeNotice({commit},payload){
            commit('typeNotice',payload)
        },
        actionAccept({commit}){
            commit('accept')
        },
        actionCancel({commit}){
            commit('cancel')
        },
        actionComplete({commit}){
            commit('complete')
        }
    },

    mutations: {
        activateSuccess(state) {
            state.isActivate = true
        },
        hideSuccess(state){
            state.isActivate = false
        },
        typeNotice(state,payload){
            state.type = payload.type;
            state.content = payload.content;
        },
        cancel(state){
            state.isAccept = false
        },
        accept(state){
            state.isAccept = true
        },
        complete(state){
            state.isActivate = false
            state.type = null;
            state.content = null;
            state.isAccept = null;
        }
    }
};