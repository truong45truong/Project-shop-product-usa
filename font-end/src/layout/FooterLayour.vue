<template>
    <footer>
        <div class="footer-top">
            <div class="container mt-5 footer-layout">
                <div class="row">
                    <div class="col-lg-3 d-flex flex-column  mt-5">
                        <p class="text-title-footer"> DỊCH VỤ ĐỘC QUYỀN </p>
                        <p class="text-content-footer"> Dịch vụ KatieShop</p>
                        <p class="text-content-footer"> Đặt lịch hẹn </p>
                        <p class="text-content-footer"> Thu thập trong của hàng </p>
                    </div>
                    <div class="col-lg-3 d-flex flex-column  mt-5">
                        <p class="text-title-footer"> GIÚP ĐỠ </p>
                        <p class="text-content-footer"> Liên hệ chúng tôi</p>
                        <p class="text-content-footer"> Đặt vận chuyển </p>
                        <p class="text-content-footer"> Các lựa chọn thanh toán </p>
                        <p class="text-content-footer"> Phản hổi về chất lượng sản phẩm </p>
                        <p class="text-content-footer"> Chăm sóc sản phẩm </p>
                        <p class="text-content-footer"> Câu hỏi thường gặp </p>
            
                    </div>
                    <div class="col-lg-3 d-flex flex-column mt-5">
                        <p class="text-title-footer"> CÔNG TY </p>
                        <p class="text-content-footer"> Về katieShop </p>
                        <p class="text-content-footer"> Quy tắc đạo đức </p>
                        <p class="text-content-footer"> Hợp pháp </p>
                        <p class="text-content-footer"> Quyền riêng tư </p>
                        <p class="text-content-footer"> Thông tin doanh nghiệp </p>
                    </div>
                    <div class="col-lg-3 d-flex flex-column mt-5 ">
                        <p class="text-title-footer"> TÌM CHÚNG TÔI TRÊN </p>
                        <p class="text-content-footer"> <font-awesome-icon icon="fa-brands fa-facebook" class="me-1"/> Facebook</p>
                        <p class="text-content-footer"> <font-awesome-icon icon="fa-brands fa-instagram" class="me-1" /> Instagram</p>
                        <p class="text-content-footer"> <font-awesome-icon icon="fa-brands fa-youtube" class="me-1" /> Youtube</p>
                        <p class="text-content-footer"> <font-awesome-icon icon="fa-brands fa-tiktok" class="me-1" />Tiktok</p>
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
    })
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
</style>