import React, { useState, useEffect } from "react";
import './../Layout/scss/MenuLayoutLeft.scss'
import UserInforLayout from './UserInforLayout'
const MenuLayoutLeft = (props) => {

    return(
        <>
            <div className="bg-dark menu-layout-left">
                <UserInforLayout />
                <div className="d-flex flex-column align-items-center justify-content-center">
                    <div>
                        <p class="my-2 mx-3 text-white text-center">Sản Phẩm</p>
                    </div>
                    <div>
                        <p class="my-2 mx-3 text-white text-center">Người dùng</p>
                    </div>
                </div>
            </div>
        </>
    )
}
export default MenuLayoutLeft