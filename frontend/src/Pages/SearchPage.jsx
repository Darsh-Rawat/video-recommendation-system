import { useState, useEffect } from 'react'
import { HashRouter as Router, Route, Routes } from 'react-router-dom'
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
// import './App.css'
import { useLocation } from 'react-router-dom';
import axios from 'axios';
import SearchBar from '../components/SearchBar.jsx';
import SearchResult from '../components/SearchResult.jsx';
import Navbar from '../components/Navbar'



function SearchPage() {
    const location = useLocation();
    const [result, setResult] = useState([]);
    const queryParam = new URLSearchParams(location.search).get('query');
    useEffect(() => {
        if (!queryParam) return;

        const fetchData = async (queryParam) => {
            try {
                const response = await axios.get(`http://127.0.0.1:8000/search/?query=${queryParam}`);
                setResult(response.data);
            } catch (error) {
                if (error.response.status === 429) {
                    alert("Too Many Requests");
                }
                console.error(error);
            }
        };

        fetchData(queryParam);
    }, [queryParam]);

    return (
        <div className='App min-h-screen w-full bg-[#eee]'>
            <Navbar />
            <div className='pt-[1.5vh] w-[40%] m-auto flex flex-col items-center min-w-50'>
                <SearchResult data={result} />
                <h1 className='mx-auto'>Serach Page</h1>
            </div>

        </div>
    )
}

export default SearchPage 