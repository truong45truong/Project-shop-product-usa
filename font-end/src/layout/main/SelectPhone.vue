<template>
    <div :class="[ dataPhone.length > 3 ? 'hover-layout' : '' ]" class="border border-2">
        <div class="p-2">
            <p class=""><b>Chọn địa chỉ nhận hàng:</b> </p>
            <div v-for="item,index in dataPhone" class="text-dark d-flex my-2">
                <span class=""><b>{{index}}. </b></span>{{item.name}} (+84) <p class="m-0">{{item.phone.replace('0','')}}</p>
                <button class="ms-3 btn-selected" @click="updateSelected(item.name,item.phone)">
                    Chọn
                </button>
            </div>
        </div>
    </div>
</template>

<script>
import {actionUser} from './../../common/user.service'
export default {
    name: "SelectPhone",
    props: {
        phoneId : false,
    },
    data : () => ({
        dataPhone : [],
        phoneSelected : false,
    }),
    components: {
        
    },
    async created (){
        // this.phoneSelected = this.phoneId;
        this.addressSelected = this.addressId;
        
        await actionUser.getPhoneUser().then(res => {
            this.dataPhone = res.data.success
        })
    },
    methods : {
        updateSelected(name,phone){
            this.$emit('update', name,phone)
        }

    }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.hover-layout {
    overflow-y: scroll;
    max-height: 200px;
}
.btn-selected {
    background-color: transparent;
    border : none;
    cursor:pointer;
    color:rgb(9, 116, 193)
}
</style>
