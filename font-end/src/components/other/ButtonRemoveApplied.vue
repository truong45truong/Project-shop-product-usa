<template>
   <p class="col-2 my-2 ms-2 applied-content p-1" @click="removeSelectedFilter" >
    <font-awesome-icon icon="fa-solid fa-xmark" />
        {{value}}
    </p>
</template>
  
<script>
export default ({
    name: 'ButtonRemoveApplied',
    props: {
        type : false,
        value : false
    },
    methods: {
        removeSelectedFilter(){
            const jsonString = sessionStorage.getItem('filter_sort');
            let applied = JSON.parse(jsonString);
            if(this.type == 1){
                applied.applied.products = applied.applied.products.filter(product => product !== this.value);
                if(applied.applied.products.length == 0 ) applied.applied.products =false
                this.$emit('updateProduct',applied.applied.products)
            }
            if(this.type == 2){
                applied.applied.sorts = applied.applied.sorts.filter(item => item !== this.value);
                if(applied.applied.sorts.length == 0 ) applied.applied.sorts =false
                this.$emit('updateSort',applied.applied.sorts)
            }
            if(this.type == 3){
                console.log(applied.applied.limits)
                let typeAdd = this.value.split(":")[0]
                applied.applied.limits = applied.applied.limits.filter(item => item !== this.value);
                if(applied.applied.limits.length == 0 ) applied.applied.limits =false
                this.$emit('updateLimit',applied.applied.limits)
                if(  typeAdd == 'Giá'){
                    this.$emit('removePriceUpDown')
                    applied.applied.up = false
                    applied.applied.down = false
                }
            }
            sessionStorage.setItem('filter_sort', JSON.stringify(applied));
        }
        
    }
    
})
</script>
<style>

</style>