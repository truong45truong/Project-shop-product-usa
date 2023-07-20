<template>
    <div :class="[ dataTransport.length > 3 ? 'hover-layout' : '' ]" class="border border-2">
        <div class="p-2">
            <p class=""><b>Chọn đơn vị vận chuyển:</b> </p>
            <div v-for="item,index in dataTransport" class="text-dark d-flex my-2">
               <span class=""><b>{{index}}. </b></span> <p class="m-0">{{item.name}}</p>
               <button class="ms-3 btn-selected"
               @click="SelectedTransport(item.id,item.name,item.price)" >
                    Chọn
                </button>
            </div>
        </div>
    </div>
</template>

<script>
import {OrderApiService} from './../../common/order.service'
export default {
    name: "SelectTransport",
    props: {
        addressId : false,
    },
    data : () => ({
        dataTransport : [],
    }),
    components: {
        
    },
    async created (){
        await OrderApiService.getTransport().then(res => {
            console.log("address user",res)
            this.dataTransport = res.data.data
        })
    },
    methods : {
        SelectedTransport(id,name,price){
            this.$emit('update', id,name,price)
        }

    }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
