
<template>
  <div class="p-3">
        <div class="input-group">
          <div class="form-outline">
            <input v-model="keySearch" type="search" id="form1" class="form-control" @blur="searchUser"
            v-on:keyup.enter="searchUser" />
            <label class="form-label search-dashboard" for="form1">Tìm kiếm</label>
          </div>
          <button type="button" class="btn btn-primary">
            <i class="fas fa-search"></i>
          </button>
        </div>
      </div>
<table class="responstable">
  
  <tr>
    <th>STT</th>
    <th>Tên đăng nhập</th>
    <th>Email</th>
    <th>Họ và tên</th>
    <th>Ngày tạo</th>
    <th> hoạt động</th>
    <th> Chọn</th>
  </tr>
  
  <tr v-for="item,index in dataUsers">
    <td> {{index}} </td>
    <td>{{item.username}}</td>
    <td>{{item.email}}</td>
    <td>{{item.name}}</td>
    <td>{{formatDateTime(item.date_joined)}}</td>
    <td>{{item.is_active}}</td>
    <td class="">
      <button class="button-28" :class="{ 'button-28-selected' : checkUserSelect(item.username) }"  role="button" @click="appendUserSelected(item.username)">
        <span class="" v-if="checkUserSelect(item.username)" > Đã chọn </span>
        <span class="" v-if="!checkUserSelect(item.username)" > Chọn </span>
      </button>
    </td>
  </tr>
  
  
</table>
<div class="d-flex justify-content-end">
  <button class="custom-btn btn-12" @click="delUser"><span>{{users_del.length}} User </span><span>Xóa</span></button>
</div>
</template>
  
<script>
import { mapGetters } from 'vuex'
import { useRoute } from 'vue-router'
import { actionAdmin } from './../../common/admin.service'

export default {
    name: "ContentUser",
    setup() {
        const route = useRoute();
        return { route };
    },

    data: () => ({
      page : 1 ,
      numberQuantity : 20,
      dataUsers : [],
      users_del : [],
      keySearch : '',
    }),
    components: {
    },
    computed: {
        ...mapGetters('dashboard', {
            get_is_show_layout: 'getIsShowLayout',
        }),
    },
    methods: {
      formatDateTime(dateString){
        const date = new Date(dateString);

        const year = date.getFullYear();
        const month = date.getMonth() + 1; // Note: Months are zero-based, so we add 1
        const day = date.getDate();

        return `${month}/${day}/${year}`
      },
      appendUserSelected(user_name){
        if( this.checkUserSelect(user_name) == true){
          this.users_del =  this.users_del.filter(val => {
            return val != user_name
          })
        } else {
          this.users_del = [user_name,...this.users_del]
        }
      },
      checkUserSelect(username){
        for(let item of this.users_del){
          if (item == username) return true;
        }
        return false;
      },
      checkUserDel(username , user_deleted){
        for(let item of user_deleted){
          if (item == username) return true;
        }
        return false;
      },
      async delUser(){
        await actionAdmin.delUser({
          params : {
            users_del : this.users_del ,
          }
        }).then(res => {
          this.dataUsers = this.dataUsers.filter( user => {
            if( this.checkUserDel(user.username , res.users_deleted) == false ) {
              return user
            }
          })
        })
      },
      async searchUser(){
        await actionAdmin.searchUser({
          params : {
            key_search : this.keySearch ,
          }
        }).then(res => {
          this.dataUsers = res.users
        })
      }
    },
    async created() {
      await actionAdmin.getAllUserPage({
        params : {
          page : this.page ,
          number_quantity : this.numberQuantity
        }
      }).then(res => {
        this.dataUsers = res.users
      })
    }
}
</script>
<style lang="scss" scoped>
$table-breakpoint: 480px;
$table-background-color: #FFF;
$table-text-color: #024457;
$table-outer-border: 1px solid #167F92;
$table-cell-border: 1px solid #D9E4E6;

// Extra options for table style (parse these arguments when including your mixin)
$table-border-radius: 10px;
$table-highlight-color: #EAF3F3;
$table-header-background-color: #167F92;
$table-header-text-color: #FFF;
$table-header-border: 1px solid #FFF;

// The Responstable mixin

@mixin responstable(
  $breakpoint: $table-breakpoint,
  $background-color: $table-background-color,
  $text-color: $table-text-color,
  $outer-border: $table-outer-border,
  $cell-border: $table-cell-border,
  $border-radius: none,
  $highlight-color: none,
  $header-background-color: $table-background-color,
  $header-text-color: $table-text-color,
  $header-border: $table-cell-border) {
  
  .responstable {
    margin: 1em 0;
    width: 100%;
    overflow: hidden;  
    background: $background-color;
    color: $text-color;
    border-radius: $border-radius;
    border: $outer-border;
  
    tr {
      border: $cell-border; 
      &:nth-child(odd) { // highlight the odd rows with a color
        background-color: $highlight-color;
      }  
    }
  
    th {
      display: none; // hide all the table header for mobile
      border: $header-border;
      background-color: $header-background-color;
      color: $header-text-color;
      padding: 1em;  
      &:first-child { // show the first table header for mobile
        display: table-cell;
        text-align: center;
      }
      &:nth-child(2) { // show the second table header but replace the content with the data-th from the markup for mobile
        display: table-cell;
        span {display:none;}
        &:after {content:attr(data-th);}
      }
      @media (min-width: $breakpoint) {
        &:nth-child(2) { // hide the data-th and show the normal header for tablet and desktop
          span {display: block;}
          &:after {display: none;}
        }
      }
    }
  
    td {
      display: block; // display the table data as one block for mobile
      word-wrap: break-word;
      max-width: 7em;
      &:first-child { 
        display: table-cell; // display the first one as a table cell (radio button) for mobile
        text-align: center;
        border-right: $cell-border;
      }
      @media (min-width: $breakpoint) {
        border: $cell-border;
      }
    }
  
    th, td {
      text-align: left;
      margin: .5em 1em;  
      @media (min-width: $breakpoint) {
        display: table-cell; // show the table as a normal table for tablet and desktop
        padding: 1em;
      }
    }  
  }    
}

// Include the mixin (with extra options as overrides)

@include responstable(
  $border-radius: $table-border-radius,
  $highlight-color: $table-highlight-color,
  $header-background-color: $table-header-background-color,
  $header-text-color: $table-header-text-color,
  $header-border: $table-header-border);

// General styles

body {
  padding: 0 2em;
  font-family: Arial, sans-serif;
  color: #024457;
  background: #f2f2f2;
}

h1 {
  font-family: Verdana;
  font-weight: normal;
  color: #024457;
  span {color: #167F92;}
}

/* CSS */
.button-28 {
  appearance: none;
  background-color: transparent;
  border: 2px solid #1A1A1A;
  border-radius: 15px;
  box-sizing: border-box;
  color: #3B3B3B;
  cursor: pointer;
  display: inline-block;
  font-family: Roobert,-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol";
  font-size: 16px;
  font-weight: 600;
  line-height: normal;
  margin: 0;
  min-height: 60px;
  min-width: 0;
  outline: none;
  padding: 16px 24px;
  text-align: center;
  text-decoration: none;
  transition: all 300ms cubic-bezier(.23, 1, 0.32, 1);
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  width: 100%;
  will-change: transform;
}
.button-28-selected {
  border: 2px solid white;
  background-color: #1A1A1A;
  color : white;
}
.button-28:disabled {
  pointer-events: none;
}

.button-28:hover {
  color: #fff;
  background-color: #1A1A1A;
  box-shadow: rgba(0, 0, 0, 0.25) 0 8px 15px;
  transform: translateY(-2px);
}

.button-28:active {
  box-shadow: none;
  transform: translateY(0);
}
/* 12 */
.custom-btn {
  width: 230px;
  height: 50px;
  color: #fff;
  border-radius: 5px;
  padding: 10px 25px;
  font-family: 'Lato', sans-serif;
  font-weight: 500;
  background: transparent;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  display: inline-block;
   box-shadow:inset 2px 2px 2px 0px rgba(255,255,255,.5),
   7px 7px 20px 0px rgba(0,0,0,.1),
   4px 4px 5px 0px rgba(0,0,0,.1);
  outline: none;
}
.btn-12{
  position: relative;
  right: 20px;
  bottom: 20px;
  border:none;
  box-shadow: none;
  width: 230px;
  height: 50px;
  line-height: 42px;
  -webkit-perspective: 230px;
  perspective: 230px;
}
.btn-12 span {
  background: rgb(0,172,238);
background: linear-gradient(0deg, rgba(0,172,238,1) 0%, rgba(2,126,251,1) 100%);
  display: block;
  position: absolute;
  width: 230px;
  height: 50px;
  box-shadow:inset 2px 2px 2px 0px rgba(255,255,255,.5),
   7px 7px 20px 0px rgba(0,0,0,.1),
   4px 4px 5px 0px rgba(0,0,0,.1);
  border-radius: 5px;
  margin:0;
  text-align: center;
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
  -webkit-transition: all .3s;
  transition: all .3s;
}
.btn-12 span:nth-child(1) {
  box-shadow:
   -7px -7px 20px 0px #fff9,
   -4px -4px 5px 0px #fff9,
   7px 7px 20px 0px #0002,
   4px 4px 5px 0px #0001;
  -webkit-transform: rotateX(90deg);
  -moz-transform: rotateX(90deg);
  transform: rotateX(90deg);
  -webkit-transform-origin: 50% 50% -20px;
  -moz-transform-origin: 50% 50% -20px;
  transform-origin: 50% 50% -20px;
}
.btn-12 span:nth-child(2) {
  -webkit-transform: rotateX(0deg);
  -moz-transform: rotateX(0deg);
  transform: rotateX(0deg);
  -webkit-transform-origin: 50% 50% -20px;
  -moz-transform-origin: 50% 50% -20px;
  transform-origin: 50% 50% -20px;
}
.btn-12:hover span:nth-child(1) {
  box-shadow:inset 2px 2px 2px 0px rgba(255,255,255,.5),
   7px 7px 20px 0px rgba(0,0,0,.1),
   4px 4px 5px 0px rgba(0,0,0,.1);
  -webkit-transform: rotateX(0deg);
  -moz-transform: rotateX(0deg);
  transform: rotateX(0deg);
}
.btn-12:hover span:nth-child(2) {
  box-shadow:inset 2px 2px 2px 0px rgba(255,255,255,.5),
   7px 7px 20px 0px rgba(0,0,0,.1),
   4px 4px 5px 0px rgba(0,0,0,.1);
 color: transparent;
  -webkit-transform: rotateX(-90deg);
  -moz-transform: rotateX(-90deg);
  transform: rotateX(-90deg);
}
</style>