import React from 'react'
import logo from "../assets/react.svg";
import axios from 'axios';


const VideoCard = ({ video }) => {
    const thumbnailUrl = `https://img.youtube.com/vi/${video.video_id}/0.jpg`;

    const handelWatch = async() => {
    await axios.post("http://127.0.0.1:8000/watch/", {
        video_id: video.id,
        title: video.title,
    });
    alert("Video Watched");
};

return (
    <div className='video-card-wrapper flex gap-4 p-2 w-6xl hover:bg-[#BFC6C4] rounded-3xl'>
        <img src={thumbnailUrl} alt="test" className="thumbnail w-sm rounded-2xl" />
        <div className='right'>
            <h2 className='title font-bold'>{video.title}</h2>
            <p>{video.views} views . {video.published_at} . {video.likes} likes</p>
            <div className='channel-info w-fit flex gap-2 mt-2 hover:cursor-pointer' onClick={() => { alert("Channel Info") }}>
                <div className='logo rounded-4xl bg-gray-700 w-7 h-7'><img src={logo} alt="logo" className='size-7' /></div>
                <p className=' font-semibold'>{video.channel_name}</p>
            </div>
            <button className='border-2 p-1 w-20 mt-2 rounded-2xl hover:bg-gray-200 hover:cursor-pointer' onClick={() => { handelWatch() }}>Watch</button>
        </div>

    </div>
)
}

export default VideoCard
