import React from 'react'
import '../App.css'
import SearchBar from '../components/SearchBar.jsx';


const Home = () => {
    return (
        <div className='App min-h-screen w-full bg-[#eee]'>
            <div className='search-bar-container pt-[1.5vh] w-[40%] m-auto flex flex-col items-center min-w-50'>
                <SearchBar />
                <div className='bg-[#BFC6C4] m-5 p-5 w-md rounded-2xl mx-auto'>
                    <h1 className='text-center font-bold text-xl'>Try searching to get started</h1>
                    <p className='text-center'>Start watching videos to help us build a feed of videos you'll love.</p>
                </div>
            </div>
        </div>
    )
}

export default Home
