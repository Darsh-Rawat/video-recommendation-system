import React from 'react'
import '../App.css'
import SearchBar from '../components/SearchBar'
import HomeCard from '../components/HomeCard'
import Navbar from '../components/Navbar'



const Home = () => {
    return (
        <div className='App min-h-screen w-full bg-[#eee]'>
            <Navbar/>
            {/* <div className='search-bar-container pt-[1.5vh] w-[40%] m-auto flex flex-col items-center min-w-50'>
                <SearchBar />
                <div className='bg-[#BFC6C4] m-5 p-5 w-md rounded-2xl mx-auto'>
                    <h1 className='text-center font-bold text-xl'>Try searching to get started</h1>
                    <p className='text-center'>Start watching videos to help us build a feed of videos you'll love.</p>
                </div>
            </div> */}

            <div className='grid grid-cols-4 place-items-center'>
                <HomeCard />
                <HomeCard />
                <HomeCard />
                <HomeCard />
                <HomeCard />
                <HomeCard />
                <HomeCard />
                <HomeCard />
                <HomeCard />
                <HomeCard />
                <HomeCard />

            </div>
        </div>
    )
}

export default Home
