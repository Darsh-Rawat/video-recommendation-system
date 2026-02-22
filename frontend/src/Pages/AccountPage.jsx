import React from 'react'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'

const AccountPage = () => {
    const navigate = useNavigate();

    const redirectToAccount = async () => {
        try {
            const response = await axios.get("http://localhost:8000/auth/me", { withCredentials: true });
            console.log(response.data);
        } catch (error) {
            console.error(error);
        }
    }
  return (
    <div>AccountPage</div>
  )
}

export default AccountPage