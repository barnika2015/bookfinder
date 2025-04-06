import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import React from 'react'; 
import Search from './components/Search'; // Import the Search component
import styles from './components/my-style.module.css'; // Import your CSS file for styling

function App() {

  return (
      <Router>
      <div className="container" style={{ textAlign: 'center' }}>
      <Routes>
      <Route path="/" element={<Search />} />
      </Routes>
      </div>
      </Router>
    );
}

export default App;
