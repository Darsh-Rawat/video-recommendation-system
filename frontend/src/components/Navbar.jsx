import React from 'react'
import SearchBar from '../components/SearchBar'
import { CiUser } from "react-icons/ci";
import { CiHome } from "react-icons/ci";
import { useNavigate } from 'react-router-dom';

const Navbar = () => {
    const navigate = useNavigate();
    return (
        <div className='navbar w-full h-15 flex items-center justify-between  sticky top-0 bg-[#eee]'>
            <button className='login-button m-5 p-3 rounded-2xl hover:bg-[#BFC6C4] hover:cursor-pointer' onClick={()=>{navigate(`/`);}}><CiHome size={25} color=''/></button>
            <SearchBar />
            <button className='login-button m-5 p-3 rounded-2xl hover:bg-[#BFC6C4] hover:cursor-pointer' onClick={()=>{navigate(`/signin`);}}><CiUser size={25} color=''/></button>
        </div>
    )
}

export default Navbar
