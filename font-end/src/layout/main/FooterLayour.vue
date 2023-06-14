<template>
    <footer>
        <div class="footer-top">
            <div class="container mt-5 footer-layout">
                <div class="row">
                    <div class="col-lg-3 d-flex flex-column  mt-5">
                        <div class="d-flex justify-content-between">
                            <p class="text-title-footer">
                                DỊCH VỤ ĐỘC QUYỀN
                            </p>
                            <div class="d-flex align-items-center"  @click="showMoreExpand(1)"
                            v-if="isShowExpand && showMore.service == false "
                            >
                                <p class="text-title-footer m-0 me-2"> Xem thêm</p>
                                <font-awesome-icon class="text-title-footer"  icon="fa-solid fa-angle-down" />
                            </div>                        
                        </div>

                        <div :class="[isShowExpand == false ? '' : showMore.service == false ? 'show-hide' : '' ]">
                            <p class="text-content-footer"> Dịch vụ KatieShop</p>
                            <p class="text-content-footer"> Đặt lịch hẹn </p>
                            <p class="text-content-footer"> Thu thập trong của hàng </p>
                            <div class="text-center" 
                            v-if="isShowExpand && showMore.service"
                            >
                                <div class="d-flex">
                                    <p class="text-content-footer m-0 me-2">
                                        Rút gọn
                                    </p>
                                    <font-awesome-icon class="text-content-footer" icon="fa-solid fa-angle-up" />
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-3 d-flex flex-column  mt-5">
                        <div class="d-flex justify-content-between">
                            <p class="text-title-footer">
                                GIÚP ĐỠ
                            </p>
                            <div class="d-flex align-items-center" @click="showMoreExpand(2)"
                                v-if="isShowExpand && showMore.support == false "
                            >
                                <p class="text-title-footer m-0 me-2"> Xem thêm</p>
                                <font-awesome-icon class="text-title-footer" v-if="isShowExpand" icon="fa-solid fa-angle-down" />
                            </div>                        </div>

                        <div :class="[isShowExpand == false ? '' : showMore.support == false ? 'show-hide' : '' ]">
                            <p class="text-content-footer"> Liên hệ chúng tôi</p>
                            <p class="text-content-footer"> Đặt vận chuyển </p>
                            <p class="text-content-footer"> Các lựa chọn thanh toán </p>
                            <p class="text-content-footer"> Phản hổi về chất lượng sản phẩm </p>
                            <p class="text-content-footer"> Chăm sóc sản phẩm </p>
                            <p class="text-content-footer"> Câu hỏi thường gặp </p>
                            <div class="text-center" 
                            v-if="isShowExpand && showMore.support"
                            >
                                <div class="d-flex">
                                    <p class="text-content-footer m-0 me-2">
                                        Rút gọn
                                    </p>
                                    <font-awesome-icon class="text-content-footer" icon="fa-solid fa-angle-up" />
                                </div>
                            </div>
                        </div>
            
                    </div>
                    <div class="col-lg-3 d-flex flex-column mt-5">
                        <div class="d-flex justify-content-between">
                            <p class="text-title-footer">
                                CÔNG TY
                            </p>
                            <div class="d-flex align-items-center" @click="showMoreExpand(3)"
                            v-if="isShowExpand && showMore.information == false "
                            >
                                <p class="text-title-footer m-0 me-2"> Xem thêm</p>
                                <font-awesome-icon class="text-title-footer" v-if="isShowExpand" icon="fa-solid fa-angle-down" />
                            </div>                        </div>
                        <div :class="[isShowExpand == false ? '' : showMore.information  == false ? 'show-hide' : '' ]">
                            <p class="text-content-footer"> Về katieShop </p>
                            <p class="text-content-footer"> Quy tắc đạo đức </p>
                            <p class="text-content-footer"> Hợp pháp </p>
                            <p class="text-content-footer"> Quyền riêng tư </p>
                            <p class="text-content-footer"> Thông tin doanh nghiệp </p>
                            <div class="text-center" 
                            v-if="isShowExpand && showMore.information"
                            >
                                <div class="d-flex">
                                    <p class="text-content-footer m-0 me-2">
                                        Rút gọn
                                    </p>
                                    <font-awesome-icon class="text-content-footer" icon="fa-solid fa-angle-up" />
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-3 d-flex flex-column mt-5 ">
                        <div class="d-flex justify-content-between">
                            <p class="text-title-footer">
                                TÌM CHÚNG TÔI TRÊN
                            </p>
                            <div class="d-flex align-items-center" @click="showMoreExpand(4)"
                            v-if="isShowExpand && showMore.follow == false "
                            >
                                <p class="text-title-footer m-0 me-2"> Xem thêm</p>
                                <font-awesome-icon class="text-title-footer" v-if="isShowExpand" icon="fa-solid fa-angle-down" />
                            </div>
                        </div>
                        <div :class="[isShowExpand == false ? '' : showMore.follow  == false? 'show-hide' : '' ]">
                            <p class="text-content-footer"> <font-awesome-icon icon="fa-brands fa-facebook" class="me-1"/> Facebook</p>
                            <p class="text-content-footer"> <font-awesome-icon icon="fa-brands fa-instagram" class="me-1" /> Instagram</p>
                            <p class="text-content-footer"> <font-awesome-icon icon="fa-brands fa-youtube" class="me-1" /> Youtube</p>
                            <p class="text-content-footer"> <font-awesome-icon icon="fa-brands fa-tiktok" class="me-1" />Tiktok</p>
                            <div class="text-center" 
                            v-if="isShowExpand && showMore.follow"
                            >
                                <div class="d-flex">
                                    <p class="text-content-footer m-0 me-2">
                                        Rút gọn
                                    </p>
                                    <font-awesome-icon class="text-content-footer" icon="fa-solid fa-angle-up" />
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <div class="container">
                <div class="row d-flex justify-content-center">
                    <p class="text-title-footer-bottom m-0"> @ 2023 Bản quyền thuộc về  Công ty TNHH KatieShop </p>
                </div>
            </div>
        </div>
    </footer>
</template>
  
<script>
export default ({
    name: 'FooterLayout',
    components: {

    },
    data: () => ({
        isShowExpand : false,
        showMore : {
            service : false,
            support : false,
            information : false,
            follow : false
        }
    }),
    methods : {
        showMoreExpand(type){
            switch(type) {
                case 1:  
                this.showMore.service = !this.showMore.service
                    break

                case 2:  
                this.showMore.support = !this.showMore.support
                    break
                case 3:  
                this.showMore.information = !this.showMore.information

                    break

                case 4:  
                this.showMore.follow = !this.showMore.follow

                    break
                default:
                    
                    break
            }
        }
    },
    mounted(){
        if(window.innerWidth < 624){
            this.isShowExpand = true
        }else {
            this.isShowExpand = false
        }
    }
})
</script>
<style>
.footer-top {
    background-color: #212529;
}
.footer-bottom {
    background-color: rgba(12, 12, 12,0.98);
}
.footer-layout {
    font-family: 'Alumni Sans', sans-serif;
}
.text-title-footer {
    color:rgb(180, 172, 172);
    font-size: 13px;
    font-weight: 200 !important;
}
.text-title-footer:hover {
    color:white;
    cursor: pointer;
}
.text-content-footer {
    color:rgb(236, 234, 234);
    font-size: 13px;
    font-weight: 200 !important;
}
.text-content-footer:hover {
    color:white;
    cursor: pointer;
}
.text-title-footer-bottom {
    text-align: center;
    color:rgb(218, 218, 218);
    font-size: 13px;
    font-weight: 400;
}
.show-hide {
    height : 0;
    overflow-y: hidden;
}
@media only screen and (max-width: 624px) {

}
</style>