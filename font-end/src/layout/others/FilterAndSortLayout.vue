<template>
    <div class="position-fixed layout-filter w-100 d-flex flex-row-reverse h-100">
        <div class="filter-sort bg-white w-100 shadow h-100">
            <div class="bg-dark w-100 btn-hide-filter-sort" @click="hide">
                <p class="text-white text-center">Ẩn</p>
            </div>
            <div class="title d-flex justify-content-between align-items-center w-100">
                <p class="fs-5 text-dark my-2 ms-2 py-1">
                    <b><i>Bộ lọc & Sắp xếp</i></b>
                </p>
                <button class="text-dark my-2 me-2 btn-clear-all" @click="resetStatus">
                    <i>Xóa tất cả thiết lập</i>
                </button>
            </div>
            <hr>
            <div class="applied-filter">
                <p class="fs-5 text-dark my-2 ms-2">
                    <b><i>Áp dụng</i>
                        <span v-if="category_applied == false"> ( {{ category_applied }} )</span>
                    </b>
                </p>
                <!-- <div class="d-flex align-items-center">
                    <p class="my-2 ms-2"> <i> sản phẩm : </i> </p>
                    <p v-if="products == false" class="my-2 ms-2 applied-content p-1">
                        Tất cả
                    </p>
                    <div class="row">
                        <ButtonRemoveApplied v-for="item in products" :type=1 :value="item"
                            @updateProduct="updateProducts" />
                    </div>
                </div> -->
                <div class="d-flex align-items-center">
                    <p class="my-2 ms-2"> <i> Sắp xếp : </i> </p>
                    <p v-if="sorts == false" class="my-2 ms-2 applied-content p-1">
                        A -> Z
                    </p>
                    <div class="row">
                        <ButtonRemoveApplied v-for="item in sorts" :type=2 :value="item" @updateSort="updateSorts" />
                    </div>
                </div>
                <div class="d-flex align-items-center">
                    <p class="my-2 ms-2"> <i> Giới hạn : </i> </p>
                    <p v-if="limits == false" class="my-2 ms-2 applied-content p-1">
                        Không có
                    </p>
                    <div class="row">
                        <ButtonRemoveApplied v-for="item in limits" :type=3 :value="item" @updateLimit="updateLimits" @removePriceUpDown="removePriceUpDown" />
                    </div>
                </div>
            </div>
            <!-- <hr v-if="hideProducts == false"> -->
            <!-- <div v-if="hideProducts == false" class="filter-select">
                <p class="fs-5 text-dark my-2 ms-2">
                    <b>
                        <i>Sản phẩm</i>
                    </b>
                </p>
                <div class="row">
                    <div v-for="item in listCategory" class="col-3 text-center">
                        <b class="applied-content p-2 text-dark" href="" @click="addFilterProduct(item.slug)">{{item.name}}</b>
                    </div>
                </div>
            </div> -->
            <hr>
            <div class="sort-select">
                <p class="fs-5 text-dark my-2 ms-2">
                    <b class="title-filter">
                        <i>Sắp xếp</i>
                    </b>
                <div class="row">
                    <div class="col-3">
                        <p class="my-2 ms-2 applied-content p-1" @click="addSort('Tên : A -> Z')">
                            Tên : A -> Z
                        </p>
                    </div>
                    <div class="col-3">
                        <p class="my-2 ms-2 applied-content p-1" @click="addSort('Tên : Z -> A')">
                            Tên : Z -> A
                        </p>
                    </div>
                    <div class="col-3">
                        <p class="my-2 ms-2 applied-content p-1" @click="addSort('Giá : Thấp -> Cao')">
                            Giá : Thấp -> Cao
                        </p>
                    </div>
                    <div class="col-3">
                        <p class="my-2 ms-2 applied-content p-1" @click="addSort('Giá : Cao -> Thấp')">
                            Giá : Cao -> Thấp
                        </p>
                    </div>
                    <div class="col-3">
                        <p class="my-2 ms-2 applied-content p-1" @click="addSort('Lượt mua : Thấp -> Cao')">
                            Lượt mua : Thấp -> Cao
                        </p>
                    </div>
                    <div class="col-3">
                        <p class="my-2 ms-2 applied-content p-1" @click="addSort('Lượt mua : Cao -> Thấp')">
                            Lượt mua : Cao -> Thấp
                        </p>
                    </div>
                    <div class="col-3">
                        <p class="my-2 ms-2 applied-content p-1" @click="addSort('Đánh giá : Thấp -> Cao')">
                            Đánh giá : Thấp -> Cao
                        </p>
                    </div>
                    <div class="col-3">
                        <p class="my-2 ms-2 applied-content p-1" @click="addSort('Đánh giá : Cao -> Thấp')">
                            Đánh giá : Cao -> Thấp
                        </p>
                    </div>
                </div>
                </p>
            </div>
            <hr>
            <div class="limit-select">
                <p class="fs-5 text-dark my-2 ms-2">
                    <b>
                        <i>Giới hạn</i>
                    </b>
                </p>
                <div class="row">
                    <div class="col-4">
                        <p class="my-2 ms-2 applied-content p-1" @click="addLimit('Đánh giá: hơn 3')">
                            Đánh giá: hơn 3 <font-awesome-icon icon="fa-solid fa-star" />
                        </p>
                    </div>
                    <div class="col-4">
                        <p class="my-2 ms-2 applied-content p-1" @click="addLimit('Đánh giá: hơn 4')">
                            Đánh giá: hơn 4 <font-awesome-icon icon="fa-solid fa-star" />
                        </p>
                    </div>
                    <div class="col-4">
                        <p class="my-2 ms-2 applied-content p-1" @click="addLimit('Đánh giá: hơn 5')">
                            Đánh giá: hơn 5 <font-awesome-icon icon="fa-solid fa-star" />
                        </p>
                    </div>
                </div>
                <div class="my-1 ms-2">
                    <p class="mb-1">Giá (Thấp)</p>
                    <input v-model="limitPrice.up" type="number">
                    <button class="btn btn-dark ms-1" @click="permisionPriceLimit(1)">
                        Xác nhận giá
                    </button>
                    <p class="mb-1">Tới giá (Cao) </p>
                    <input v-model="limitPrice.down" type="number">
                    <button class="btn btn-dark ms-1" @click="permisionPriceLimit(2)">
                        Xác nhận giá
                    </button>
                    <p class="text-danger mb-1"><b><i>Chú ý:</i></b></p>
                    <p class="">
                        <b>
                            <i>
                                Nhập Giá trị từ thấp không nhập cao bộ lọc sẽ lọc các giá trị bé hơn hoặc bằng
                            </i>
                            <i class="d-block">
                                Nhập Giá trị từ Cao không nhập thấp bộ lọc sẽ lọc các giá trị lớn hơn hoặc bằng
                            </i>
                        </b>
                    </p>
                </div>
            </div>
            <hr>
        </div>
    </div>
</template> 

<script>
import ButtonRemoveApplied from './../../components/other/ButtonRemoveApplied.vue'
export default {
    name: 'FilterAndSortLayout',
    components: {
        ButtonRemoveApplied
    },
    props: {
        category_applied: false,
        listCategory : [],
        hideProducts : false,
        type : false,
        key_search : false
    },
    data: () => ({
        products: [],
        sorts: [],
        limits: [],
        limitPrice: {
            up: null,
            down: null,
            message: false
        }
    }),
    methods: {
        resetStatus(){
            this.products = []
            this.sorts = [] 
            this.limits = []
            this.limitPrice = {
                up: null,
                down: null,
                message: false
            }
            let ValueFilterAndSort = {
                applied : {
                    products : false,
                    sorts : false,
                    limits : false,
                    category : this.category_applied,
                    up: false,
                    down : false
                }
            }
            sessionStorage.setItem('filter_sort', JSON.stringify(ValueFilterAndSort))
        },
        hide() {
            this.$emit('hideFilterAndSort')
        },
        addFilterProduct(value) {
            const jsonString = sessionStorage.getItem('filter_sort');
            let applied = JSON.parse(jsonString);
            if (applied.applied.products == false) {
                applied.applied.products = [value]
            } else {
                if (this.products.some(element => element == value) == false) {
                    applied.applied.products.push(value)
                }

            }
            this.products = applied.applied.products
            sessionStorage.setItem('filter_sort', JSON.stringify(applied));
        },
        updateProducts(data) {
            this.products = data
            this.filterAndSort()
        },
        addSort(value) {
            const jsonString = sessionStorage.getItem('filter_sort');
            let applied = JSON.parse(jsonString);
            if (applied.applied.sorts == false || applied.applied.sorts == 'false') {
                applied.applied.sorts = [value]
            }

            else {
                if (this.sorts.some(element => element == value) == false) {
                    for (let i of this.sorts) {
                        let typeAdd = value.split(":")[0]
                        let checkTypeAdd = i.indexOf(typeAdd);
                        console.log('checkTypeAdd', checkTypeAdd)
                        if (checkTypeAdd == 0) {
                            applied.applied.sorts = applied.applied.sorts.filter(item => item !== i);
                        }
                    }
                    applied.applied.sorts.push(value)

                }

            }
            this.sorts = applied.applied.sorts
            sessionStorage.setItem('filter_sort', JSON.stringify(applied));
            this.filterAndSort()
        },
        updateSorts(data) {
            console.log("update sort",data )
            this.sorts = data
            this.filterAndSort()
            console.log("end update sort")
        },
        addLimit(value) {
            const jsonString = sessionStorage.getItem('filter_sort');
            let applied = JSON.parse(jsonString);
            console.log(value,this.limits , "day la limit")
            if(this.limits == false){
                this.limits = []
            }
            if (applied.applied.limits == false || applied.applied.limits == 'false') {
                applied.applied.limits = [value]
                console.log(applied.applied.limits)
            } else {
                for (let i of this.limits) {
                    let typeAdd = value.split(":")[0]
                    let checkTypeAdd = i.indexOf(typeAdd);
                    console.log('checkTypeAdd', checkTypeAdd)
                    if (checkTypeAdd == 0) {
                        applied.applied.limits = applied.applied.limits.filter(item => item !== i);
                    }
                }
                applied.applied.limits.push(value)

            }
            this.limits = applied.applied.limits
            if (this.limitPrice.up != false && this.limitPrice.up != 'false') {
                applied.applied.up = this.limitPrice.up
            }
            if (this.limitPrice.down != false && this.limitPrice.down != 'false') {
                applied.applied.down = this.limitPrice.down
            }
            sessionStorage.setItem('filter_sort', JSON.stringify(applied));
            this.filterAndSort()
        },
        updateLimits(data) {
            console.log("update limit")
            this.limits = data
            this.filterAndSort()
            console.log("end update limit")
        },
        removePriceUpDown(){
            this.limitPrice.up = null
            this.limitPrice.down = null
        },
        permisionPriceLimit(type) {
            const jsonString = sessionStorage.getItem('filter_sort');
            let applied = JSON.parse(jsonString);
            function isNumeric(value) {
                return /^-?\d+$/.test(value);
            }
            console.log(isNumeric(this.limitPrice.up))
            if (type == 1) {
                if (isNumeric(this.limitPrice.up) == true) {
                    if (this.limitPrice.down != null && this.limitPrice.up < this.limitPrice.down) {
                        this.limitPrice.message = "Giá: từ " + this.limitPrice.up + " tới " + this.limitPrice.down
                    } else {
                        this.limitPrice.message = "Giá: lớn hơn " + this.limitPrice.up
                    }
                    this.addLimit(this.limitPrice.message)
                } else {
                    this.limitPrice.up = null
                }
                this.filterAndSort()
            }
            if (type == 2) {
                if (isNumeric(this.limitPrice.down) == true) {
                    if (this.limitPrice.up != null && this.limitPrice.up < this.limitPrice.down) {
                        this.limitPrice.message = "Giá: từ " + this.limitPrice.up + " tới " + this.limitPrice.down
                    } else {
                        this.limitPrice.message = "Giá: nhỏ hơn " + this.limitPrice.down
                    }
                    this.addLimit(this.limitPrice.message)
                } else {
                    this.limitPrice.down = null
                }
                this.filterAndSort()
            }
            // sessionStorage.setItem('filter_sort', JSON.stringify(applied));
        },
        filterAndSort() {
            console.log("start filter and sort")
            const jsonString = sessionStorage.getItem('filter_sort');
            let applied = JSON.parse(jsonString);
            if (this.type == 1){
                this.$router.push({
                    name: 'product',
                    params: { category: applied.applied.category },
                    query: applied.applied
                })
            }
            if( this.type == 2){
                this.$router.push({
                    name: 'products-search',
                    params: { 
                        key_search: this.key_search 
                    },
                    query: {
                        category : applied.applied.category,
                        sorts : applied.applied.sorts,
                        limits : applied.applied.limits
                    }
                })
            }
        }

    },

    created() {
        const jsonString = sessionStorage.getItem('filter_sort');
        const applied = JSON.parse(jsonString);
        if(applied.applied.products  == false || applied.applied.products  == "false"){
            this.products = false
        } else {
            this.products = applied.applied.products
        }
        if(applied.applied.limits  == false || applied.applied.limits  == "false"){
            this.limits = false
        } else {
            this.limits = applied.applied.limits
        }
        if(applied.applied.sorts  == false || applied.applied.sorts  == "false"){
            this.sorts = false
        } else {
            console.log("applied.applied.sorts",applied.applied.sorts,typeof applied.applied.sorts)
            if(typeof applied.applied.sorts == 'string' ){
                this.sorts.push(applied.applied.sorts)
            }else
            this.sorts = applied.applied.sorts
        }
        if( applied.applied.up != false &&  applied.applied.up == false){
            this.limitPrice.up = applied.applied.up
            this.limitPrice.down = null
            this.limitPrice.message = "Giá: lớn hơn " + this.limitPrice.up
        }
        if( applied.applied.up == false &&  applied.applied.up != false){
            this.limitPrice.down = applied.applied.down
            this.limitPrice.up = null
            this.limitPrice.message = "Giá: bé hơn " + this.limitPrice.up
        }
        if( applied.applied.up != false &&  applied.applied.up != false){
            this.limitPrice.up = applied.applied.up
            this.limitPrice.down = applied.applied.down
            this.limitPrice.message = "Giá: từ " + this.limitPrice.up + " tới " + this.limitPrice.down
        }
    }
}
</script>
<style scoped>
.layout-filter {
    top: 0%;
    left: 0%;
    z-index: 9999;
    background-color: rgba(167, 167, 167, 0.8);
}

.filter-sort {
    max-width: 800px;
    overflow: auto;
}

.filter-sort::-webkit-scrollbar {
    display: none;
}

.btn-clear-all {
    border: none;
    background: none;
    text-decoration: underline;
}

.btn-clear-all:active {
    color: brown;
}

.btn-hide-filter-sort {
    cursor: pointer
}

.applied-content {
    background-color: rgb(234, 235, 236);
    width: fit-content;
    text-decoration: none;
    cursor: pointer;
    font-size: 14px;
}

.title-filter {
    width: fit-content;
}

.button-filter-sort {
    width: fit-content;
    background-color: white;
    border: 1px solid black;
}</style>