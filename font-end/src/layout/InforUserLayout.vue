<template>
    <div class="row d-flex d-flex-column align-items-center justify-content-center mt-2 mx-2">
        <font-awesome-icon icon="fa-regular fa-circle-xmark" class="icon-hide fs-2 text-dark" @click="$emit('hide')"/>
        <div class="w-75 d-flex flex-column align-items-center mt-3">
            <img class="img-infor-user" src="./../assets/images/useruser.jpg" alt="">
            <p  class="mt-2">Truong</p>
        </div>
        <div class="d-flex">
            <div class="selected-action">
                <div class="d-flex">
                    <font-awesome-icon icon="fa-solid fa-location-dot align-items-center" class="fs-2 text-dark ms-5 me-1"/>
                    <p class="text-content-user m-0"> <b>Địa chỉ</b></p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapGetters} from 'vuex'
export default ({
    name: 'InforUserLayout',
    components: {

    },
    data: () => ({
    }),
    computed : {
        ...mapGetters('auth', {
			get_user         : 'currentUser',
			get_authenticated: 'isAuthenticated',
			get_error        : 'errorAuthenticated'
		}),
    },
    created(){
        console.log(this.get_user)
    }
})
</script>
<style>
.img-infor-user {
    width : 10%;
    border-radius: 50%;
}
.icon-hide {
    position:absolute;
    left:45%;
    top:5%;
}
.selected-action {
    margin : 5% 5%;
}
.text-content-user {
    font-family:'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
    font-size: 16px;
}
</style>