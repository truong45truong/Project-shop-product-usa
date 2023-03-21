<template>

</template>

<script>
({
    name: 'ListProductCategory',
    components: {
        
    },
    data: () => ({
      
      
    }),
    methods :{
       
    },
    async created(){
        await ProductApiService.get().then(res => {
            this.listProductItem = Array.from(res.data.products)
            console.log(this.listProductItem )
        })
    }
})
</script>
<style>
</style>