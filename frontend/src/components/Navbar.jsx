import React from 'react'
import axios from 'axios';
import SearchBar from '../components/SearchBar'
import { CiUser } from "react-icons/ci";
import { CiHome } from "react-icons/ci";
import { useNavigate } from 'react-router-dom';
import { useState, useRef, useEffect } from "react";
import { IoLogOutOutline } from "react-icons/io5";
import api from '../api.js'

const Navbar = () => {
    const navigate = useNavigate();
    const [open, setOpen] = useState(false);
    const menuRef = useRef(null);

    const handleLogout = async () => {
        try {
            const response = await api.post("/auth/logout", {},{ withCredentials: true });
            alert("Loged Out");
            window.location.reload();
        } catch (error) {
            console.error(error);
        }
    }

    // Close when clicking outside
    useEffect(() => {
        const handleClickOutside = (e) => {
            if (menuRef.current && !menuRef.current.contains(e.target)) {
                setOpen(false);
            }
        };

        document.addEventListener("mousedown", handleClickOutside);
        return () => document.removeEventListener("mousedown", handleClickOutside);
    }, []);

    const redirectToAccount = async () => {
        try {
            await api.get("/auth/account",{ withCredentials: true });
            navigate("/account");
        } catch (error) {
            if (error.response?.status === 401) navigate("/signin");
            console.error(error);
        }
    };

    return (
        <div className="navbar w-full h-15 flex items-center justify-between sticky top-0 bg-[#eee] px-5">

            {/* Home */}
            <button
                className="p-3 rounded-2xl hover:bg-[#BFC6C4]"
                onClick={() => navigate("/")}
            >
                <CiHome size={25} />
            </button>

            <SearchBar />

            {/* User Button + Dropdown */}
            <div className="relative" ref={menuRef}>
                <button
                    className="p-3 rounded-2xl hover:bg-[#BFC6C4]"
                    onClick={() => setOpen(!open)}
                >
                    <CiUser size={25} />
                </button>

                {open && (
                    <div className="absolute right-0 mt-2 w-40 bg-white rounded-xl shadow-lg border border-gray-200">
                        <button
                            className="block w-full text-left px-4 py-2 hover:bg-gray-100"
                            onClick={redirectToAccount}
                        >
                            Account
                        </button>
                        <button
                            className="block w-full text-left px-4 py-2 hover:bg-gray-100"
                            onClick={() => navigate("/signin")}
                        >
                            Sign In
                        </button>
                        <button
                            className="flex items-center gap-2 w-full text-left px-4 py-2 hover:bg-gray-100 text-red-500"
                            onClick={() => handleLogout()}
                        >
                            Logout <IoLogOutOutline />
                        </button>
                    </div>
                )}
            </div>
        </div>
    );
};

export default Navbar;
