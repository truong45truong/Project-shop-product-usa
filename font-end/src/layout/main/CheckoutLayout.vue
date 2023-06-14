<template>
    <div class="container mt-5" id="checkout-content">
        <h1><b><i>Thanh toán</i></b></h1>
        <div class="row border py-3">
            <div class="d-flex">
                <font-awesome-icon class="icon-address" icon="fa-solid fa-location-dot" />
                <p class="text-dark m-0  ms-3 text-address">Địa chỉ nhận hàng</p>
            </div>
            <div class="d-flex mt-1 align-items-center">
                <p class="m-0"><b>Nguyễn Hoàng Trường (+84) 889287686</b></p>
                <p class="m-0 ms-3">Thôn Phước Lộc - Xã Lộc Tiến - Huyện Thừa Thiên Huế</p>
                <div class="ms-3 default-address px-1">
                    <p class="m-0 text-danger">Mặc định</p>
                </div>
                <button class="ms-3 button-change-address ps-0"> <p class="m-0 text-primary"> Thay đổi</p></button>
            </div>
        </div>
        <div class="mt-3 row py-3 border">
            <table class="table">
                <thead>
                    <tr>
                        <th scope="col">STT</th>
                        <th scope="col">Tên</th>
                        <th scope="col">Đơn giá</th>
                        <th scope="col">Số Lượng</th>
                        <th scope="col">Thành tiền</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                    <th scope="row">1</th>
                        <td>
                            <p class="m-0">ÁO THUN Local Brand OTIS CLUB- Unixex nam nữ from</p>
                            <img class="img-checkout-product" src="http://127.0.0.1:8000/media/photos/de00afb5b1ff35b91c8f3a1f77ca78d9.jpeg" alt="">
                        </td>
                        <td>94.520 vnđ </td>
                        <td>1</td>
                        <td>94.520 vnđ </td>
                    </tr>
                </tbody>
            </table>
            <div class="d-flex w-100">
                <div class="d-flex w-50">
                    <p class="m-0"> Lời nhắn: </p>
                    <textarea class="w-100"  placeholder="Nhập nội dung ..." ></textarea>
                </div>
                <div class="ms-2 d-flex">
                    <p class="m-0 text-transport">Chọn đơn vị vận chuyển:</p>
                    <div class="ms-2">
                        <p class="m-0">Vận chuyển Nhanh</p>
                        <p class="m-0 text-muted">Nhận hàng vào ngày 11 tháng 4</p>

                        <button class="button-change-address"> <p class="m-0 text-primary"> Thay đổi </p></button>
                    </div>
                    <div class="ms-3 text-end">
                        <p class="m-0">Phí:
                            <span class="text-decrease">
                                30.000 vnđ
                            </span>
                        </p>
                    </div>
                </div>
            </div>
        </div>
        <div class="row mt-3 border py-3">
            <div class="col-sm-6">
                <p class="m-0">
                    Voucher:
                </p>
                <div class="content-voucher">
                    <voucher-information />
                </div>
            </div>
            <div class="col-sm-6 text-end">
                <button class="ms-3 button-change-address"> <p class="m-0 text-primary"> Chọn voucher</p></button>
                <p class="m-0 text-decrease">
                    Đã giảm 30.000 vnđ
                </p>
            </div>
        </div>
        <div class="row mt-3 border py-3">
            <div class="d-flex justify-content-between">
                <p class="m-0"> Phương thức thanh toán:</p>
                <div class="d-flex">
                    <p class="m-0"> Thanh toán khi nhân hàng</p>
                    <button class="ms-3 button-change-address"> <p class="m-0 text-primary"> Thay đổi</p></button>
                </div>
            </div>
            <div class="mt-3">
                <div class="d-flex flex-row-reverse">
                    <p class="m-0 "> Tổng tiền :
                        <span> 1.000.000 vnđ </span>
                    </p>
                </div>
                <div class="d-flex flex-row-reverse">
                    <p class="m-0 "> Phí vận chuyển :
                        <span> 30.000 vnđ </span>
                    </p>
                </div>
                <div class="d-flex flex-row-reverse">
                    <p class="m-0 "> Tổng thanh toán:
                        <span> 1.030.000 vnđ </span>
                    </p>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="d-flex flex-row-reverse">
                <div class="btn btn-dark px-4 py-2 mt-4">
                    Đặt hàng
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import VoucherInformation from './../../components/other/VoucherInformation.vue'
export default {
    name: "CheckoutLayout",
    props: {
        msg : ''
    },
    data : () => ({
    }),
    components: {
        VoucherInformation
    },
    async created (){
    },
    methods : {

    }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
  .icon-address {
    font-size: 24px;
  }
  .text-address {
    font-size: 18px;
  }
  .default-address {
    border : 1px solid red;
  }
  .button-change-address {
    background-color :transparent;
    border:none;
  }
  .img-checkout-product {
    width : 100px;
  }
  .content-voucher {
    max-width: 300px;
  }
  #checkout-content .content-voucher {
    box-shadow: none;
  }
  .text-decrease {
    color :#ee4d2d
  }
  .text-transport {
    color:rgb(1, 86, 86)
  }
</style>
