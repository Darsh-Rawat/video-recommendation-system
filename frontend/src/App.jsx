import { useState } from 'react'
import { HashRouter as Router, Route, Routes } from 'react-router-dom'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Home from './Pages/Home.jsx'
import SearchPage from './Pages/SearchPage';
import SignInPage from './Pages/SignInPage';



function App() {
    
    return (
        <Router>
            <Routes>
                <Route path='/' element={<Home />} />
                <Route path='/search' element={<SearchPage />} />
                <Route path='/signin' element={<SignInPage />} />
            </Routes>
        </Router>
    )
}

export default App
