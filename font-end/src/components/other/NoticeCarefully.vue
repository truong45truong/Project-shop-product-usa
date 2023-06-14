<template>
    <div class="p-3 notify-layout">
        <div class="w-100 d-flex flex-column align-items-center">
            <h5 class="m-0 content-notice">{{get_content}}</h5>
        </div>
        <div class="d-flex justify-content-bettween mt-4 w-100">
            <button class="btn btn-warning text-center layout-btn-notice" @click="backNoticeCarefully">
                <p class="m-0">Trở Lại</p>
            </button>
            <button class="btn btn-warning text-center layout-btn-notice" @click="acceptNoticeCarefully">
                <p class="m-0 text-center">{{get_type}}</p>
            </button>
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
            acceptNotice : 'actionAccept',
            cancelNotice : 'actionCancel'
		})
	},
    methods: {
        backNoticeCarefully() {
            this.cancelNotice
            this.hideNotice
        },
        acceptNoticeCarefully() {
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
    max-width:300px;
}
.layout-btn-notice {
    width:75px !important;
}
@media only screen and (max-width: 424px) {
    .content-notice {
        font-size: 14px;
    }
    .layout-btn-notice p {
        font-size:  13px;
    }
}
</style>