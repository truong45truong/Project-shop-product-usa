<template >
    <div v-if="get_activate && get_type == 'addtocart'" class="position-absolute pb-2 bg-white text-bg-white text-dark rounded-fill w-50 start-50 shadow"
        :class="[ isShowNotify == true ? 'notify-menu-hover' : 'notify-menu' ]" v-on:mouseout="showNotify" v-on:mouseover="showNotify"
    >    
        <div class="bg-light w-100 text-center position-relative d-flex flex-row-reverse">
            <font-awesome-icon icon="fa-solid fa-xmark"
            class="text-danger fs-4 me-1 cancel-notify " @click="cancel" />
        </div>
        <div class="p-2 text-center">
            {{get_content}}
        </div>
    </div>
</template>
  
<script>
import { mapActions,mapGetters } from 'vuex'
export default ({
    name: 'NoticeMenu',
    computed: {
        ...mapGetters('notice', {
			get_type         : 'isType',
			get_content: 'isContent',
            get_activate : 'isActivateMenu'
		}),
	},
    data: () => ({
        isShowNotify : false
    }),
    methods: {
        showNotify(){
            this.isShowNotify = ! this.isShowNotify
        },
        cancel(){
            this.$store.dispatch('notice/actionShowMenuCancel')
            
        }
    },
    mounted(){
        return new Promise((resolve) => {
            const checkValue = () => {
                if (this.showComponent === false) {
                    resolve();
                }
                else {
                    setTimeout(checkValue, 500);
                }
            };

            checkValue();
        });
    }
    
})
</script>
<style>
@keyframes notifyActivate {
    0%{
        opacity: 1;
        display:block;
    }
    100% {
        opacity : 0;
        display:none;
    }
}
.notify-menu{
    top:120%;   
    opacity : 0;
    animation: notifyActivate 5s;
}
.notify-menu-hover {
    top:120%; 
    opacity: 1;
}
.cancel-notify {
    cursor:pointer;
}
</style>