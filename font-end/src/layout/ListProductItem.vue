<template>
    <div class="container">
        <div class="row">
            <div v-for="item in listProductItem" class="col-3">
                <div class="mx-3 shadow my-5 box-demo d-flex flex-column justify-content-center">
                    <product-item :slug="item.slug" :photo="item.photo_products[0]" :name="item.name"
                        :price="item.prices[0]"
                    />
                </div>
            </div>
        </div>
    </div>
</template>
  
<script>
import { ProductApiService } from './../common/product.service'
import ProductItem from './../components/product/ProductItem.vue'
export default ({
    name: 'ListProductItem',
    components: {
        ProductItem,
    },
    data: () => ({
        listProductItem : []
    }),
    async created(){
        await ProductApiService.get().then(res => {
            let array = []
            for(let item of res.data){
                console.log(item)
                array.push(item)
            }
            this.listProductItem = array
            console.log(this.listProductItem)
        })
    }
})
</script>
<style>
.box-demo {
    height:85%;
    position:relative;
    overflow:hidden
}
</style>