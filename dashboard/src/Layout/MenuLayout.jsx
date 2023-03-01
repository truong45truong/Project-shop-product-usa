import React, { useState, useEffect } from "react";
import './scss/MenuLayout.scss'
const MenuLayout = (props) => {
    const [timeMenutop, setTimeMenutop] = useState(new Date());
    const formattedTime = timeMenutop.toLocaleTimeString();
    useEffect(() => {
        const intervalId = setInterval(() => {
            setTimeMenutop(new Date());
        }, 1000);
        return () => clearInterval(intervalId);
    }, []);

    return (
        <>
            <div className="menu-top bg-dark d-flex justify-content-center  ">
                <p class="m-0 text-white py-1">{formattedTime}</p>
            </div>
        </>
    )
};
export default MenuLayout;