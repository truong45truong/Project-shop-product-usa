<template>
    <div :class="[ dataVoucher.length > 3 ? 'hover-layout' : '' ]" class="border border-2">
        <div class="row mb-2">
            <div class="col-lg-3 col-md-4 col-sm-6 mt-2 d-flex justify-content-center" v-for="voucher in dataVoucher" :key="voucher.voucher">
                <div class="voucher-item border-none">
                    <p class="m-0 text-voucher-main text-white my-2 mx-2">
                        Giảm :{{voucher.voucher.sale}}%
                        <span>(tối đa {{voucher.voucher.limited_price}}k)</span>
                    </p>    
                    <div class="voucher-item-left"></div>
                    <div class="voucher-item-right"></div>
                </div>
                <button class="ms-3 btn-selected" @click="SelectedVoucher(voucher.voucher.id,voucher.voucher.sale,voucher.voucher.limited_price,voucher.product_in_vouchers)">
                    Chọn
                </button>
            </div>
        </div>
    </div>
</template>

<script>
import {VoucherAction} from './../../common/voucher.service'
export default {
    name: "SelectVoucher",
    props: {
        addressId : false,
    },
    data : () => ({
        dataVoucher : [],
    }),
    components: {
        
    },
    async created (){
        await VoucherAction.actionGetVoucher({
            params: {
                email_user: localStorage.getItem('user'),
                token_permission_infor_user: localStorage.getItem('token_permission_infor_user')
            }
        }).then(res => {
            console.log("voucehr",res)
            this.dataVoucher = res.data
        })
    },
    methods : {
        SelectedVoucher(id,sale,limited_price,product_in_vouchers){
            this.$emit('update', id,sale,limited_price,product_in_vouchers)
        }

    }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
