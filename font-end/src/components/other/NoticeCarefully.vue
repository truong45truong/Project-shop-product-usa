<template>
    <div class="p-3 notify-layout w-25">
        <div class="w-100 d-flex flex-column align-items-center">
            <h5 class="m-0">{{get_content}}</h5>
        </div>
        <div class="d-flex justify-content-bettween mt-4 w-100">
            <div class="btn btn-warning w-100" @click="backNoticeCarefully">
                Trở Lại
            </div>
            <div class="btn btn-warning w-100" @click="acceptNoticeCarefully">
                {{get_type}}
            </div>
        </div>
    </div>
</template>
  
<script>
import { mapActions,mapGetters } from 'vuex'
export default ({
    name: 'NoticeCarefully',
    computed: {
        ...mapGetters('notice', {
			get_type         : 'isType',
			get_content: 'isContent',
		}),
		...mapActions('notice', {
			activateNotice   : 'activateShow',
            hideNotice : 'activateHide',
            acceptNotice : 'actionAccept'
		})
	},
    methods: {
        backNoticeCarefully() {
            this.hideNotice
        },
        acceptNoticeCarefully() {
            console.log("aceppt")
            this.acceptNotice
            this.hideNotice
    
        }
    }
    
})
</script>
<style>
.notify-layout {
    background-color:  white;
    width:inherit;
    max-width:inherit;
}
</style>