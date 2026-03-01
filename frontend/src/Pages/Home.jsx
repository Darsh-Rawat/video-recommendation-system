import React from 'react';
import '../App.css';
import SearchBar from '../components/SearchBar';
import HomeCard from '../components/HomeCard';
import Navbar from '../components/Navbar';
import api from '../api.js'
import { useState, useEffect } from 'react';


const Home = () => {
    const [result, setResult] = useState([]);
    const [isNew, setIsNew] = useState(true);
    const fetchFeed = async () => {
        try {
            const response = await api.get("/feed/search", { withCredentials: true });
            console.log(response.data);
            if (Array.isArray(response.data)) {
                setResult(response.data);
                setIsNew(false);
                console.log("isNew set to false");
            } else {
                // Not authenticated or unexpected response
                setIsNew(true);
            }
        } catch (error) {
            console.error(error);
        }
    }
    useEffect(() => {
        console.log("useEffect running");
        fetchFeed();
    }, []);
    return (
        <div className='App min-h-screen w-full bg-[#eee]'>
            <Navbar />
            {isNew ? (
                <div className='bg-[#BFC6C4] m-5 p-5 w-md rounded-2xl mx-auto'>
                    <h1 className='text-center font-bold text-xl'>Try searching to get started</h1>
                    <p className='text-center'>Start watching videos to help us build a feed of videos you'll love.</p>
                </div>) : (

                <div className='grid grid-cols-4 place-items-center'>
                    {(result).map((video) => (
                        <HomeCard key={video.video_id} video={video} />
                    ))}
                </div>

            )
            }
        </div>
    )
}

export default Home
