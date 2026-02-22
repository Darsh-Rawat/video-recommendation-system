import React from 'react'
import axios from 'axios';
import SearchBar from '../components/SearchBar'
import { CiUser } from "react-icons/ci";
import { CiHome } from "react-icons/ci";
import { useNavigate } from 'react-router-dom';

const Navbar = () => {
    const navigate = useNavigate();
    const redirectToAccount = async () => {
        try {
            const response = await axios.get("http://localhost:8000/auth/account", { withCredentials: true });
            navigate('/account');
        } catch (error) {
            if(error.response.status === 401) navigate('/signin');
            console.error(error);
        }
    }
    return (
        <div className='navbar w-full h-15 flex items-center justify-between  sticky top-0 bg-[#eee]'>
            <button className='home-button m-5 p-3 rounded-2xl hover:bg-[#BFC6C4] hover:cursor-pointer' onClick={()=>{navigate(`/`);}}><CiHome size={25} color=''/></button>
            <SearchBar />
            <button className='login-button m-5 p-3 rounded-2xl hover:bg-[#BFC6C4] hover:cursor-pointer' onClick={()=>{redirectToAccount();}}><CiUser size={25} color=''/></button>
        </div>
    )
}

export default Navbar
