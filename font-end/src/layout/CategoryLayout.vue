<template>
    <div class="row d-flex">
        <div class="col-3">
            <div v-for=" item in listCateogry " class="d-flex align-items-center justify-content-between px-5">
                <p :id="`${item.id}`" v-if='item.level==0' class="text-white title-name m-0 me-2" >
                    {{ item.name }}
                </p>
                <div v-if='item.level==0'>
                    <font-awesome-icon v-if="isShowChild[item.id].expand == false " class="text-white icon-expand" :id='"icon-"+`${item.id}`' icon="fa-solid fa-plus" @click="checkChildCategogy(item.id,item.level)" />
                </div>
                <div v-if='item.level==0' class="hr-category ms-2" :class="[ isShowChild[item.id].expand == true ? 'activate-expand' : 'non-activate-expand']" ></div>
            </div>
        </div>
        <div class="col-3">
            <div v-for=" item in listCateogry " class="d-flex align-items-center justify-content-between px-5">
                <p :id="`${item.id}`" v-if='item.level==1 & isShowChild[item.id].value == true' class="text-white title-name m-0 me-2 p-0" >
                    {{ item.name }}
                </p>
                <div v-if='item.level==1 & isShowChild[item.id].value == true'>
                    <font-awesome-icon v-if="isShowChild[item.id].expand == false " class="text-white icon-expand" :id='"icon-"+`${item.id}`' icon="fa-solid fa-plus" @click="checkChildCategogy(item.id,item.level)" />
                </div>
                <div v-if='item.level==1 & isShowChild[item.id].value == true' class="hr-category ms-2" :class="[ isShowChild[item.id].expand == true ? 'activate-expand' : 'non-activate-expand']" ></div>
            </div>
        </div>
        <div class="col-3">
            <div v-for=" item in listCateogry " class="d-flex align-items-center justify-content-between px-5">
                <p :id="`${item.id}`" v-if='item.level==2 & isShowChild[item.id].value == true' class="text-white title-name m-0 me-2" >
                    {{ item.name }}
                </p>
                <div v-if='item.level==2 & isShowChild[item.id].value == true'>
                    <font-awesome-icon v-if="isShowChild[item.id].expand == false " class="text-white icon-expand" :id='"icon-"+`${item.id}`' icon="fa-solid fa-plus" @click="checkChildCategogy(item.id,item.level)" />
                </div>
                <div v-if='item.level==2 & isShowChild[item.id].value == true' class="hr-category ms-2" :class="[ isShowChild[item.id].expand == true ? 'activate-expand' : 'non-activate-expand']" ></div>
            </div>
        </div>
        <div class="col-3">
            <div v-for=" item in listCateogry " class="d-flex align-items-center justify-content-between px-5">
                <p :id="`${item.id}`" v-if='item.level==3 & isShowChild[item.id].value == true' class="text-white title-name   m-0 me-2" >
                    {{ item.name }}
                </p>
                <div v-if='item.level==3 & isShowChild[item.id].value == true'>
                    <font-awesome-icon v-if="isShowChild[item.id].expand == false " class="text-white icon-expand" :id='"icon-"+`${item.id}`' icon="fa-solid fa-plus" @click="checkChildCategogy(item.id,item.level)" />
                </div>
                <div v-if='item.level==3 & isShowChild[item.id].value == true' class="hr-category ms-2" :class="[ isShowChild[item.id].expand == true ? 'activate-expand' : 'non-activate-expand']" ></div>
            </div>
        </div>
    </div>
</template>

<script>
import {CategoryApiService} from './../common/category.service'
export default {
    name: "CategoryLayout",
    props: {
        msg: String,
    },
    data : () => ({
        listCateogry : false,
        isShowChild : []
    }),
    async created (){
        await CategoryApiService.get().then(res => {
            this.listCateogry = res.data.category
        })
        for (let item of this.listCateogry){
                this.isShowChild[item.id] = {value : false , level : item.level , expand : false}
        }
    },
    methods : {
        checkChildCategogy(category_id,level) {
            //this.resetExpandLevel(category_id,level)
            this.isShowChild[category_id].expand = true
            for( let item of this.listCateogry){
                /* -------------------------- reset child category -------------------------- */
                if(item.level > level){
                    this.isShowChild[item.id] = {value : false , level : item.level , expand : false}
                }
                /* -------------------------- reset expand category ------------------------- */
                if(item.level >= level & item.id != category_id){
                    this.isShowChild[item.id].expand = false
                }
                if(item.parent == category_id){
                    this.isShowChild[item.id] = {value : true , level : item.level , expand : false}
                }
            }
        }
    }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>S
.title-name{
    word-wrap: none !important;
}
.title-name:hover {
    color: rgb(14, 14, 85) !important;
    cursor:pointer;
}
@keyframes showdowncategory {
    from {
        top:0%
    }
  to {top: 32%;}
}
@keyframes showActionExpandLine {
    from {
        width: 0%;
    }
    to {
        width: 100%;
    }
}
.activate-animation {
    position:absolute;
    top:32%;
    animation-name: showdowncategory;
    animation-duration: 0.5s;
}
@keyframes xoayvong {
  from {
    -webkit-transform:rotate(0deg);
    -moz-transform:rotate(0deg);
    -o-transform:rotate(0deg);
  }
  to {
    -webkit-transform:rotate(360deg);
    -moz-transform:rotate(360deg);
    -o-transform:rotate(360deg);
  }
}
.icon-expand{
    font-size: 14px !important;
    cursor: pointer;
}
.icon-expand:hover {
    animation-name: xoayvong;
    animation-duration: 0.5s;
}
.hr-category{
    width:100%;
    height:2px;
    background-color: white;
}
.activate-expand {
    display :block;
    animation-name: showActionExpandLine;
    animation-duration: 0.5s;
}
.non-activate-expand{
    display:none;
}
</style>
