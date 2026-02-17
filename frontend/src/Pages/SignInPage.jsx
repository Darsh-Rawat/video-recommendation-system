import React from 'react'
import { useState } from 'react'
import axios from 'axios';

const SignInPage = () => {
    const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');

    const login = async (email, password) => {
        try {
            const response = await axios.post("http://localhost:8000/auth/login", { email, password }, { withCredentials: true });
            console.log(response.data);
        } catch (error) {
            console.error(error);
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
                        <h1 className='font-bold text-2xl text-center text-[#CECECE]'>Welcome Back !</h1>
                        <p className='inline text-[#7F7F7F]'>Don't have a account yet ? </p>
                        <p className='inline font-semibold text-[#CECECE] hover:cursor-pointer hover:underline'>Sign Up</p>
                    </div>
                    <div className="input-field flex flex-col gap-5 w-full shadow-md">
                        <input type="email" placeholder='Email address' className='border-[#1A1A1A] border-2 rounded-lg h-10 p-0 px-3.75 shadow-md bg-[#111111] placeholder-[#737373] text-[#737373] focus:border-[#191919] focus:outline-0' onChange={(e) => setEmail(e.target.value)} />
                        <input type="password" placeholder='Password' className='border-[#1A1A1A] border-2 rounded-lg h-10 p-0 px-3.75 shadow-md bg-[#111111] placeholder-[#737373] text-[#737373] focus:border-[#191919] focus:outline-0' onChange={(e) => setPassword(e.target.value)} />
                        <button className='border-[#093356] border-2 h-10 rounded-lg bg-[#0174DC] text-white font-semibold shadow-md hover:cursor-pointer' onClick={() => login(email, password)}>Login</button>
                    </div>
                    <p className='hover:cursor-pointer text-[#7F7F7F] hover:text-[#0174DC] underline' onClick={()=>{me()}}>Forgot Password ?</p>
                </div>
            </div>
        </div>
    )
}

export default SignInPage