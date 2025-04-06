import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import React from 'react'; 
import Search from './components/Search'; // Import the Search component

function App() {

  return (
      <Router>
      <div className="container">
      <Routes>
      <Route path="/" element={<Search />} />
      </Routes>
      </div>
      </Router>
    );
}

export default App;
