import { ApiService } from "./api.service";
import { actionJWT } from "./jwt.service";
/* -------------------------------------------------------------------------- */
/*                                 API SERVICE                                */
/* -------------------------------------------------------------------------- */
export const AdminApiService = {
  /* ---------------------------------- users --------------------------------- */
  async get() {
    return await ApiService.query("admin/get-info");
  },
  async searchUser(params) {
    return await ApiService.query("admin/search-user",params);
  },
  async getAllUserPage(params) {
    return await ApiService.query("admin/get-all-user",params);
  },
  async delUser(params) {
    return await ApiService.post("admin/del-user", params);
  },
  /* -------------------------------- products -------------------------------- */
  async getAllProductPage(params) {
    return await ApiService.query("admin/get-all-product",params);
  },
  async searchProduct(params) {
    return await ApiService.query("admin/search-all-product",params);
  },
  async delProduct(params) {
    return await ApiService.post("admin/del-product", params);
  },
  async createProduct(params) {
    return await ApiService.post("admin/create-product", params);
  },
  async getDetailProduct(params) {
    return await ApiService.query("admin/detail-product",params);
  },
  async updateProduct(params) {
    return await ApiService.post("admin/update-product", params);
  },
  /* --------------------------------- voucher -------------------------------- */
  async getAllVoucherPage(params) {
    return await ApiService.query("admin/get-all-voucher",params);
  },
  async searchAllVoucherPage(params) {
    return await ApiService.query("admin/search-all-voucher",params);
  },
  async delVoucher(params) {
    return await ApiService.post("admin/del-voucher", params);
  },
  async createVoucher(params) {
    return await ApiService.post("admin/create-voucher", params);
  },
  async getAllVoucherNoProductPage(params) {
    return await ApiService.query("admin/get-voucher-no-product",params);
  },
  async addProductVoucher(params) {
    return await ApiService.post("admin/add-product-voucher", params);
  },
  async detailVoucher(params) {
    return await ApiService.query("admin/detail-voucher",params);
  },
  async delProductVoucher(params) {
    return await ApiService.post("admin/del-product-voucher", params);
  },
  /* ------------------------------- flash sale ------------------------------- */
  async getAllFlashSalePage(params) {
    return await ApiService.query("admin/get-all-flash-sale",params);
  },
  async searchAllFlashSalePage(params) {
    return await ApiService.query("admin/search-all-flash-sale",params);
  },
  async delFlashSale(params) {
    return await ApiService.post("admin/del-flash-sale", params);
  },
  async createFlashSale(params) {
    return await ApiService.post("admin/create-flash-sale", params);
  },
  async getAllFlashSaleNoProductPage(params) {
    return await ApiService.query("admin/get-flash-sale-no-product",params);
  },
  async addProductFlashSale(params) {
    return await ApiService.post("admin/add-product-flash-sale", params);
  },
  async detailFlashSale(params) {
    return await ApiService.query("admin/detail-flash-sale",params);
  },
  async delProductFlashSale(params) {
    return await ApiService.post("admin/del-product-flash-sale", params);
  },
  /* ---------------------------------- order --------------------------------- */
  async getAllOrderPage(params) {
    return await ApiService.query("admin/get-all-order",params);
  },
  async getAllOrderRequestPage(params) {
    return await ApiService.query("admin/get-all-order-request",params);
  },
  async getAllOrderConfirmPage(params) {
    return await ApiService.query("admin/get-all-order-confirm",params);
  },
  async getAllOrderPaymentedPage(params) {
    return await ApiService.query("admin/get-all-order-paymented",params);
  },
  async confirmOrder(params) {
    return await ApiService.post("admin/confirm-order", params);
  },
  async cancelOrder(params) {
    return await ApiService.post("admin/cancel-order", params);
  },
};
/* -------------------------------------------------------------------------- */
/*                                   ACTION                                   */
/* -------------------------------------------------------------------------- */
export const actionAdmin = {
  /* --------------------------------- user -------------------------------- */
  async getInforAdmin() {
    let infor = false;
      let jwt_token_access = localStorage.getItem("jwt_token_access");
      ApiService.setHeader(jwt_token_access);
      await AdminApiService.get().then((response) => {
        infor = response.data;
      });
    return infor;
  },
  async getAllUserPage(params) {
    let infor = false;
      let jwt_token_access = localStorage.getItem("jwt_token_access");
      ApiService.setHeader(jwt_token_access);
      await AdminApiService.getAllUserPage(params).then((response) => {
        infor = response.data;
      });
    return infor;
  },
  async searchUser(params) {
    let infor = false;
      let jwt_token_access = localStorage.getItem("jwt_token_access");
      ApiService.setHeader(jwt_token_access);
      await AdminApiService.searchUser(params).then((response) => {
        infor = response.data;
      });
    return infor;
  },
  async delUser(params) {
    let infor = false;
      let jwt_token_access = localStorage.getItem("jwt_token_access");
      ApiService.setHeader(jwt_token_access);
      await AdminApiService.delUser(params).then((response) => {
        infor = response.data;
      });
    return infor;
  },
  /* --------------------------------- product -------------------------------- */
  async getAllProductPage(params) {
    let infor = false;
      let jwt_token_access = localStorage.getItem("jwt_token_access");
      ApiService.setHeader(jwt_token_access);
      await AdminApiService.getAllProductPage(params).then((response) => {
        infor = response.data;
      });
    return infor;
  },
  async searchProduct(params) {
    let infor = false;
      let jwt_token_access = localStorage.getItem("jwt_token_access");
      ApiService.setHeader(jwt_token_access);
      await AdminApiService.searchProduct(params).then((response) => {
        infor = response.data;
      });
    return infor;
  },
  async delProduct(params) {
    let infor = false;
      let jwt_token_access = localStorage.getItem("jwt_token_access");
      ApiService.setHeader(jwt_token_access);
      await AdminApiService.delProduct(params).then((response) => {
        infor = response.data;
      });
    return infor;
  },
  async createProduct(params) {
    let infor = false;
      let jwt_token_access = localStorage.getItem("jwt_token_access");
      ApiService.setHeader(jwt_token_access);
      await AdminApiService.createProduct(params).then((response) => {
        infor = response.data;
      });
    return infor;
  },
  async getDetailProduct(params) {
    let infor = false;
      let jwt_token_access = localStorage.getItem("jwt_token_access");
      ApiService.setHeader(jwt_token_access);
      await AdminApiService.getDetailProduct(params).then((response) => {
        infor = response.data;
      });
    return infor;
  },
  async updateProduct(params) {
    let infor = false;
      let jwt_token_access = localStorage.getItem("jwt_token_access");
      ApiService.setHeader(jwt_token_access);
      await AdminApiService.updateProduct(params).then((response) => {
        infor = response.data;
      });
    return infor;
  },
  /* --------------------------------- voucher -------------------------------- */
  async getAllVoucherPage(params){
    let infor = false;
      let jwt_token_access = localStorage.getItem("jwt_token_access");
      ApiService.setHeader(jwt_token_access);
      await AdminApiService.getAllVoucherPage(params).then((response) => {
        infor = response.data;
      });
    return infor;
  },
  async searchAllVoucherPage(params){
    let infor = false;
      let jwt_token_access = localStorage.getItem("jwt_token_access");
      ApiService.setHeader(jwt_token_access);
      await AdminApiService.searchAllVoucherPage(params).then((response) => {
        infor = response.data;
      });
    return infor;
  },
  async delVoucher (params) {
    let infor = false;
      let jwt_token_access = localStorage.getItem("jwt_token_access");
      ApiService.setHeader(jwt_token_access);
      await AdminApiService.delVoucher(params).then((response) => {
        infor = response.data;
      });
    return infor;
  },
  async createVoucher(params) {
    let infor = false;
      let jwt_token_access = localStorage.getItem("jwt_token_access");
      ApiService.setHeader(jwt_token_access);
      await AdminApiService.createVoucher(params).then((response) => {
        infor = response.data;
      });
    return infor;
  },
  async getAllVoucherNoProductPage(params) {
    let infor = false;
      let jwt_token_access = localStorage.getItem("jwt_token_access");
      ApiService.setHeader(jwt_token_access);
      await AdminApiService.getAllVoucherNoProductPage(params).then((response) => {
        infor = response.data;
      });
    return infor;
  },
  async addProductVoucher(params){
    let infor = false;
      let jwt_token_access = localStorage.getItem("jwt_token_access");
      ApiService.setHeader(jwt_token_access);
      await AdminApiService.addProductVoucher(params).then((response) => {
        infor = response.data;
      });
    return infor;
  },
  async detailVoucher(params){
    let infor = false;
      let jwt_token_access = localStorage.getItem("jwt_token_access");
      ApiService.setHeader(jwt_token_access);
      await AdminApiService.detailVoucher(params).then((response) => {
        infor = response.data;
      });
    return infor;
  },
  async delProductVoucher(params){
    let infor = false;
      let jwt_token_access = localStorage.getItem("jwt_token_access");
      ApiService.setHeader(jwt_token_access);
      await AdminApiService.delProductVoucher(params).then((response) => {
        infor = response.data;
      });
    return infor;
  },
  /* ------------------------------- flash sale ------------------------------- */
  async getAllFlashSalePage(params){
    let infor = false;
      let jwt_token_access = localStorage.getItem("jwt_token_access");
      ApiService.setHeader(jwt_token_access);
      await AdminApiService.getAllFlashSalePage(params).then((response) => {
        infor = response.data;
      });
    return infor;
  },
  async searchAllFlashSalePage(params){
    let infor = false;
      let jwt_token_access = localStorage.getItem("jwt_token_access");
      ApiService.setHeader(jwt_token_access);
      await AdminApiService.searchAllFlashSalePage(params).then((response) => {
        infor = response.data;
      });
    return infor;
  },
  async delFlashSale(params) {
    let infor = false;
      let jwt_token_access = localStorage.getItem("jwt_token_access");
      ApiService.setHeader(jwt_token_access);
      await AdminApiService.delFlashSale(params).then((response) => {
        infor = response.data;
      });
    return infor;
  },
  async createFlashSale(params) {
    let infor = false;
      let jwt_token_access = localStorage.getItem("jwt_token_access");
      ApiService.setHeader(jwt_token_access);
      await AdminApiService.createFlashSale(params).then((response) => {
        infor = response.data;
      });
    return infor;
  },
  async getAllFlashSaleNoProductPage(params) {
    let infor = false;
      let jwt_token_access = localStorage.getItem("jwt_token_access");
      ApiService.setHeader(jwt_token_access);
      await AdminApiService.getAllFlashSaleNoProductPage(params).then((response) => {
        infor = response.data;
      });
    return infor;
  },
  async addProductFlashSale(params){
    let infor = false;
      let jwt_token_access = localStorage.getItem("jwt_token_access");
      ApiService.setHeader(jwt_token_access);
      await AdminApiService.addProductFlashSale(params).then((response) => {
        infor = response.data;
      });
    return infor;
  },
  async detailFlashSale(params){
    let infor = false;
      let jwt_token_access = localStorage.getItem("jwt_token_access");
      ApiService.setHeader(jwt_token_access);
      await AdminApiService.detailFlashSale(params).then((response) => {
        infor = response.data;
      });
    return infor;
  },
  async delProductFlashSale(params){
    let infor = false;
      let jwt_token_access = localStorage.getItem("jwt_token_access");
      ApiService.setHeader(jwt_token_access);
      await AdminApiService.delProductFlashSale(params).then((response) => {
        infor = response.data;
      });
    return infor;
  },
  /* ---------------------------------- order --------------------------------- */
  async getAllOrderPage(params){
    let infor = false;
      let jwt_token_access = localStorage.getItem("jwt_token_access");
      ApiService.setHeader(jwt_token_access);
      await AdminApiService.getAllOrderPage(params).then((response) => {
        infor = response.data;
      });
    return infor;
  },
  async getAllOrderRequestPage(params){
    let infor = false;
      let jwt_token_access = localStorage.getItem("jwt_token_access");
      ApiService.setHeader(jwt_token_access);
      await AdminApiService.getAllOrderRequestPage(params).then((response) => {
        infor = response.data;
      });
    return infor;
  },
  async getAllOrderConfirmPage(params){
    let infor = false;
      let jwt_token_access = localStorage.getItem("jwt_token_access");
      ApiService.setHeader(jwt_token_access);
      await AdminApiService.getAllOrderConfirmPage(params).then((response) => {
        infor = response.data;
      });
    return infor;
  },
  async getAllOrderPaymentedPage(params){
    let infor = false;
      let jwt_token_access = localStorage.getItem("jwt_token_access");
      ApiService.setHeader(jwt_token_access);
      await AdminApiService.getAllOrderPaymentedPage(params).then((response) => {
        infor = response.data;
      });
    return infor;
  },
  async confirmOrder(params){
    let infor = false;
      let jwt_token_access = localStorage.getItem("jwt_token_access");
      ApiService.setHeader(jwt_token_access);
      await AdminApiService.confirmOrder(params).then((response) => {
        infor = response.data;
      });
    return infor;
  },
  async cancelOrder(params){
    let infor = false;
      let jwt_token_access = localStorage.getItem("jwt_token_access");
      ApiService.setHeader(jwt_token_access);
      await AdminApiService.cancelOrder(params).then((response) => {
        infor = response.data;
      });
    return infor;
  },
};
