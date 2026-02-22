import React from 'react'
import { useState } from 'react'
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { CiAlignCenterH } from 'react-icons/ci';

const SignInPage = () => {
    const navigate = useNavigate();
    const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');
    const [username, setUserName] = useState('');

    const login = async (email, password) => {
        try {
            const response = await axios.post("http://localhost:8000/auth/register", { email, username, password });
            navigate('/signin');
        } catch (error) {
            alert(error);
        }
    }

    const me = async () => {
        try {
            const response = await axios.get("http://localhost:8000/auth/me", { withCredentials: true });
            console.log(response.data);
        } catch (error) {
            console.error(error);
        }
    }

    return (
        <div>
            {/* <Navbar /> */}
            <div className="flex flex-col items-center justify-center">
                <div className='sign-in-wrapper m-40 w-[20%] h-150 bg-[#181818] rounded-3xl flex flex-col items-center gap-30 p-10'>
                    <div className='welcome-message'>
                        <h1 className='font-bold text-2xl text-center text-[#CECECE]'>Create a new account!</h1>
                        <p className='inline text-[#7F7F7F]'>Already have a account ? </p>
                        <p className='inline font-semibold text-[#CECECE] hover:cursor-pointer hover:underline' onClick={() => navigate('/signin')}>Sign In</p>
                    </div>
                    <div className="input-field flex flex-col gap-5 w-full shadow-md">
                        <input type="email" placeholder='Email address' className='border-[#1A1A1A] border-2 rounded-lg h-10 p-0 px-3.75 shadow-md bg-[#111111] placeholder-[#737373] text-[#737373] focus:border-[#191919] focus:outline-0' onChange={(e) => setEmail(e.target.value)} />
                        <input type="text" placeholder='User Name' className='border-[#1A1A1A] border-2 rounded-lg h-10 p-0 px-3.75 shadow-md bg-[#111111] placeholder-[#737373] text-[#737373] focus:border-[#191919] focus:outline-0' onChange={(e) => setUserName(e.target.value)} />
                        <input type="password" placeholder='Password' className='border-[#1A1A1A] border-2 rounded-lg h-10 p-0 px-3.75 shadow-md bg-[#111111] placeholder-[#737373] text-[#737373] focus:border-[#191919] focus:outline-0' onChange={(e) => setPassword(e.target.value)} />
                        <button className='border-[#093356] border-2 h-10 rounded-lg bg-[#0174DC] text-white font-semibold shadow-md hover:cursor-pointer' onClick={() => login(email, password)}>Register</button>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default SignInPage