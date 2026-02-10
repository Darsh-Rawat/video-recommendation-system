import React from 'react'
import logo from "../assets/react.svg";

const HomeCard = () => {
    const thumbnailUrl = `https://img.youtube.com/vi/UWe4aMPAyvc/0.jpg`;
    return (
        <div className='video-card-wrapper p-2 w-100 h-94 hover:bg-[#BFC6C4] rounded-3xl '>
            <img src={thumbnailUrl} alt="test" className="thumbnail w-100 rounded-2xl mx-auto" />
            <div className='flex mt-2 gap-2'>
                <div className='logo rounded-4xl bg-gray-700 w-7 h-7 mt-1'><img src={logo} alt="logo" className='size-7' /></div>
                <div>
                    <div className='text-lg font-bold'>Google Job Offer</div>
                    <div>Channel Name</div>
                    <div>200K views . 2 days ago</div>
                </div>


            </div>

        </div>
    )
}

export default HomeCard
