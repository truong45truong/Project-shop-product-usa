<template>
    <div :class="[ dataAddress.length > 3 ? 'hover-layout' : '' ]" class="border border-2">
        <div class="p-2">
            <p class=""><b>Chọn địa chỉ nhận hàng:</b> </p>
            <div v-for="item,index in dataAddress" class="text-dark d-flex my-2">
               <span class=""><b>{{index}}. </b></span> <p class="m-0">{{item.address_content}}</p>
               <button class="ms-3 btn-selected"
               @click="SelectedAddress(item.address_content)" >
                    Chọn
                </button>
            </div>
        </div>
    </div>
</template>

<script>
import {actionUser} from './../../common/user.service'
export default {
    name: "SelectAddress",
    props: {
        addressId : false,
    },
    data : () => ({
        dataAddress : [],
        addressSelected : false,
    }),
    components: {
        
    },
    async created (){
        // this.phoneSelected = this.phoneId;
        this.addressSelected = this.addressId;
        await actionUser.getAdressUser().then(res => {
            console.log("address user",res)
            this.dataAddress = res.data.success
        })
        // await actionUser.getPhoneUser().then(res => {
        //     console.log("phone user",res)
        // })
    },
    methods : {
        SelectedAddress(address){
            this.$emit('updateAddress', address)
        }

    }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
