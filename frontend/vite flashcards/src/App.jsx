import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div class="bg-red-500 flex max-lg:300">
        <h2>
          Welcome to the store
        </h2>
      </div>
    </>
  )
}

export default App
