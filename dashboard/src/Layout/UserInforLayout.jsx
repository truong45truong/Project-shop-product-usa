import React, { useState, useEffect } from "react";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

const UserInforLayout = (props) => {
    return(
        <>
        <div className="user-infor-top">
            <div className="p-3 d-flex justify-content-center">
                <i class="fa-regular fa-user text-white fs-1"></i>
            </div>
        </div>
        </>
    )
}
export default UserInforLayout;