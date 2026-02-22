import { useState } from 'react'
import { HashRouter as Router, Route, Routes } from 'react-router-dom'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Home from './Pages/Home.jsx'
import SearchPage from './Pages/SearchPage';
import SignInPage from './Pages/SignInPage';
import RegisterPage from './Pages/RegisterPage';
import AccountPage from './Pages/AccountPage';



function App() {
    
    return (
        <Router>
            <Routes>
                <Route path='/' element={<Home />} />
                <Route path='/search' element={<SearchPage />} />
                <Route path='/signin' element={<SignInPage />} />
                <Route path='/register' element={<RegisterPage />} />
                <Route path='/account' element={<AccountPage />} />
            </Routes>
        </Router>
    )
}

export default App
