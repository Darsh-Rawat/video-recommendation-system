import React, {use, useState} from 'react'
import axios from 'axios';
import { IoIosSearch } from "react-icons/io";

const SearchBar = ({ setResult }) => {
    const [input, setInput] = useState('');

    const fetchData = async (query) => {
        if (!query) return;

        try {
            const response = await axios.get(`http://127.0.0.1:8000/search/?query=${(query)}`);
            setResult(response.data);
        } catch (error) {
            console.error("Error fetching data:", error);
        }
    };


    const handleKeyDown = (e) => {
        if (e.key === 'Enter') {
            fetchData(input);
        }
    };
  return (
    <div className='input-wrapper bg-white w-[60%] rounded-2xl h-10 p-0 px-3.75 shadow-md flex items-center sticky top-2'>
        <input type="text" placeholder='Search' value={input} onChange={(e) => setInput(e.target.value)} onKeyDown={handleKeyDown}  className='bg-transparent border-none outline-none h-full w-full mr-1.25 text-md hover:cursor-text'/>
        <IoIosSearch className='fill-blue-800 size-6 hover:cursor-pointer ' onClick={() => fetchData(input)}/>
    </div>
  )
}

export default SearchBar
