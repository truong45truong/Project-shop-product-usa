import React, { useState, useEffect } from "react";
import {getAllProductApi} from './../../Apis/product.api'

const ListProductItem = (props) => {
    const [data,setData] = useState(false)
    useEffect(async ()=>{
        return await getAllProductApi().then(res => {
            console.log(res)
        })
    },[data])
    return (
        <>

        </>
    )
};
export default ListProductItem;