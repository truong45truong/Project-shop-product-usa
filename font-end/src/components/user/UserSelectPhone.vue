<template>
    <div class="position-absolute w-100" v-if="isShow">
        <div class="user-select-phone-layout border position-relative">
            <font-awesome-icon icon="fa-solid fa-xmark" class="position-absolute icon-cancel fs-4"  @click="show" />
            <h5 class="w-100 text-center mt-3" >Chọn địa chỉ</h5>
            <div class="my-2 d-flex justify-content-between mx-2" v-for="item,index of data">
                <p>
                    <span class="text-dark me-2">{{index + 1}}.</span>
                    {{ item.phone }}
                    <span class="text-primary me-1"> ({{ item.name }})</span>
                    <span v-if="item.status" class="ms-1 text-primary"> (Mặc định)</span>
                    </p>
                <div >
                    <font-awesome-icon icon="fa-solid fa-circle-check" class="ms-5 fs-5 icon-select-address"
                        @click="selectPhone(item)" />
                </div>
            </div>
        </div>
    </div>
</template>
  
<script>
import {actionUser} from './../../common/user.service'
export default ({
    name: 'UserSelectPhone',
    computed: {

	},
    data: () => ({
        data : false,
        isShow : false,
    }),
    methods: {
        selectPhone(item){
            this.$emit('selectPhone',item);
            this.show()
        },
        show(){
            this.isShow = ! this.isShow
        }
    },
    async created(){
        await actionUser.getPhoneUser().then(res => {
            console.log(res)
            this.data = res.data.success
        })
    }
    
})
</script>
<style>

.user-select-phone-layout{
    border-radius: 20px;
    position:absolute;
    left:0%;
    top:50%;
    min-height: 200px;
    max-height: 200px;
    width:100%;
    overflow-x:none;
    background-color: white;
    z-index: 999;
    overflow-y: scroll;
}

</style>