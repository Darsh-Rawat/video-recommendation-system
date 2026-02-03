import React, { use, useState } from 'react'
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { IoIosSearch } from "react-icons/io";


const SearchBar = () => {
    const [input, setInput] = useState('');
    const navigate = useNavigate();

    const handelSearch = async (query) => {
        if (!query) return;

        try {
            navigate(`/search?query=${encodeURIComponent(query)}`);
        } catch (error) {
            console.error("Error navigating :", error);
        }
    };


    const handleKeyDown = (e) => {
        if (e.key === 'Enter') {
            handelSearch(input);
        }
    };
  return (
    <div className='input-wrapper bg-white w-[60%] rounded-2xl h-10 p-0 px-3.75 shadow-md flex items-center sticky top-2'>
        <input type="text" placeholder='Search' value={input} onChange={(e) => setInput(e.target.value)} onKeyDown={handleKeyDown}  className='bg-transparent border-none outline-none h-full w-full mr-1.25 text-md hover:cursor-text'/>
        <IoIosSearch className='fill-blue-800 size-6 hover:cursor-pointer ' onClick={() => handelSearch(input)}/>
    </div>
  )
}

export default SearchBar
