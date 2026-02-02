import { useState } from 'react'
import { HashRouter as Router, Route, Routes } from 'react-router-dom'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import SearchBar from './components/SearchBar.jsx'
import SearchResult from './components/SearchResult.jsx'
import Home from './Pages/Home.jsx'
import SearchPage from './pages/SearchPage';



function App() {
    
    return (
        <Router>
            <Routes>
                <Route path='/' element={<Home />} />
                <Route path='/search' element={<SearchPage />} />

            </Routes>
        </Router>
    )
}

export default App
