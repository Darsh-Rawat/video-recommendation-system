import React from 'react'
import Navbar from '../components/Navbar'
import { AiOutlineMail } from "react-icons/ai";

const SignInPage = () => {
    return (
        <div>
            <Navbar />
            <div className="flex flex-col items-center justify-center">
                <div className='sign-in-wrapper m-40 w-[20%] h-150 bg-[#BFC6C4] rounded-3xl flex flex-col items-center gap-30 p-10'>
                    <div className='welcome-message'>
                        <h1 className='font-bold text-2xl text-center'>Welcome Back !</h1>
                        <p className='inline'>Don't have a account yet ? </p>
                        <p className='inline font-semibold'>Sign Up</p>
                    </div>
                    <div className="input-field flex flex-col gap-5 w-full shadow-md">
                        <input type="email" placeholder='email address' className='border-zinc-950 border rounded-lg h-10 p-0 px-3.75 shadow-md' />
                        <input type="password" placeholder='password' className='border-zinc-950 border rounded-lg h-10 p-0 px-3.75 shadow-md' />
                        <button className='border-zinc- border h-10 rounded-lg bg-[#687FE5] shadow-md'>Login</button>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default SignInPage