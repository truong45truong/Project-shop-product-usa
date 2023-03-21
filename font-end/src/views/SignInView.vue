<template>
    <div id="app">
        <div class="align-center">
            <div><SignIn /></div>
        </div>
    </div>
</template>

<script>
    import SignIn from './../components/login/SignIn.vue'
    export default {
        name : "SignInView",
        created (){
            
        },
        components : {
            SignIn
        }
    }

</script>

<style>
#bg-login {
    position:fixed;
    top:0;
}
.login-bg {
    background-color: aliceblue;
}
</style>