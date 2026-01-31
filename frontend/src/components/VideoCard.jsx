import React from 'react'
import thumbnail from "../assets/thumbnail.png";
import logo from "../assets/react.svg";


const VideoCard = ({ title }) => {
    return (
        <div className='video-card-wrapper flex gap-4 p-2 w-6xl hover:bg-[#BFC6C4] rounded-3xl'>
            <img src="https://i.ytimg.com/vi/v73-ps01c5w/hqdefault.jpg" alt="test" className="thumbnail w-sm rounded-2xl" />
            <div className='right'>
                <h2 className='title font-bold'>{title}</h2>
                <p>6.4M views . 2 days ago</p>
                <div className='channel-info w-fit flex gap-2 mt-2 hover:cursor-pointer' onClick={() => {alert("Channel Info")}}>
                    <div className='logo rounded-4xl bg-gray-700 w-7 h-7'><img src={logo} alt="logo" /></div>
                    <p className='channel-name'>Channel name</p>
                </div>
                <button className='border-2 p-1 w-20 mt-2 rounded-2xl hover:bg-gray-200 hover:cursor-pointer' onClick={() => {alert("Watching Video")}}>Watch</button>
            </div>

        </div>
    )
}

export default VideoCard
