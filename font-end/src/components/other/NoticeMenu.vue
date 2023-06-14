<template >
    <div v-if="get_activate && get_type == 'addtocart'" class="pb-2 d-flex  text-bg-white text-dark rounded-fill end-0 shadow"
        :class="[ isShowNotify == false ? 'd-none' : 'notify-menu' ]"
    >    
        <div class="d-flex flex-column container-notice justify-content-center align-items-center">
            <img src="../../assets/icon/icon-correctcorrect.png" class="icon-corret-notice" alt="">
            <div class="p-2 text-center text-white">
                {{get_content}}
            </div>
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
                if (this.get_activate === false) {
                    this.isShowNotify = false
                }
                if (this.get_activate === true) {
                    this.isShowNotify = true
                    setTimeout(()=>{
                        this.$store.dispatch('notice/actionShowMenuCancel')
                    },2000)
                    
                }
                setTimeout(checkValue, 500);

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
        opacity : 0.5;
        display:none;
    }
}
.notify-menu{
    position :fixed;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
    width: 100%;
    top:0%;
    z-index: 9999;
    animation: notifyActivate 2s;
}
.container-notice{
    background-color: rgba(33, 33, 33, 0.9);
    width: 400px;
    height: 200px;
}
.notify-menu-hover {
    top:120%; 
    opacity: 1;
}
.icon-corret-notice{
    width:80px;
    height:80px;
}
</style>