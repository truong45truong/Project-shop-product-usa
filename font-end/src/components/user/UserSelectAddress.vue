<template>
    <div class="position-absolute w-100" v-if="isShow">
        <div class="user-select-address-layout border position-relative">
            <font-awesome-icon icon="fa-solid fa-xmark" class="position-absolute icon-cancel fs-4"  @click="show" />
            <h5 class="w-100 text-center mt-3" >Chọn địa chỉ</h5>
            <div class="my-2 d-flex justify-content-between mx-2" v-for="item,index of data">
                <p>
                    <span class="text-dark me-2">{{index + 1}}.</span>
                    {{ item.address_content }}
                    <span v-if="item.status" class="ms-1 text-primary"> (Mặc định)</span>
                    </p>
                <div >
                    <font-awesome-icon icon="fa-solid fa-circle-check" class="ms-5 fs-5 icon-select-address"
                        @click="selectAddress(item)" />
                </div>
            </div>
        </div>
    </div>
</template>
  
<script>
import {actionUser} from './../../common/user.service'
export default ({
    name: 'UserSelectAddress',
    computed: {

	},
    data: () => ({
        data : false,
        addressSelect : false,
        isShow : false,
    }),
    methods: {
        selectAddress(item){
            this.$emit('selectAddress',item);
            this.show()
        },
        show(){
            this.isShow = ! this.isShow
        }
    },
    async created(){
        await actionUser.getAdressUser().then(res => {
            console.log(res)
            this.data = res.data.success
        })
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
.user-select-address-layout{
    border-radius: 20px;
    position:absolute;
    top:0%;
    width:fit-content;
    min-height: 200px;
    width:100%;
    overflow-x:none;
    background-color: white;
    z-index: 999;
    overflow-y: scroll;
}
.icon-cancel {
    cursor:pointer;
    top:0%;
    right:10%
}
.icon-cancel:hover {
    color:rgb(116, 115, 115) !important;
}
</style>