<template>
  <div class="d-flex flex-column">
    <div class="d-flex icon-cancel justify-content-end ">
        <font-awesome-icon icon="fa-solid fa-rectangle-xmark" @click="removeImgUpload" />
    </div>
    <img class="img-image-send" :src="data" alt="Resized Image">
  </div>
</template>
<script>
export default {
    name: 'ImageSendComment',
    props: {
        data:'',
        index : ''
    },
    data() {
        return {
           
        } 
    }
    ,

    methods : {
        removeImgUpload(){
            this.$emit('removeFileUpload',this.index)
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.img-image-send {
    height : 100%;
    width:auto;
}
.icon-cancel {
    right:10%;
}
</style>