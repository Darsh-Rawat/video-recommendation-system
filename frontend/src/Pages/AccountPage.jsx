import React from 'react'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'
import Navbar from '../components/Navbar.jsx'
import api from '../api.js'

const AccountPage = () => {
    const navigate = useNavigate();

    const redirectToAccount = async () => {
        try {
            const response = await api.get("/auth/me", { withCredentials: true });
            console.log(response.data);
        } catch (error) {
            console.error(error);
        }
    }
    return (
        <div>
            <Navbar></Navbar>
            <div className='text-center w-full'>
                <div>AccountPage</div>
            </div>
        </div>
    )
}

export default AccountPage