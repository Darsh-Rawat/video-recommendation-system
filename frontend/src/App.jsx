import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import SearchBar from './components/SearchBar.jsx'
import SearchResult from './components/SearchResult.jsx'


function App() {
  const [count, setCount] = useState(0);
  const [result, setResult] = useState("");

  return (
    <div className='App min-h-screen w-full bg-[#eee]'>
    <div className='search-bar-container pt-[1.5vh] w-[40%] m-auto flex flex-col items-center min-w-50'>
        <SearchBar setResult={setResult}/>
        <SearchResult data={result}/>
    </div>
    </div>
  )
}

export default App
