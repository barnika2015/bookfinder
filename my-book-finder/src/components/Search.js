import React, { useEffect, useState } from 'react';
import styles from './my-style.module.css'; // Import your CSS file for styling
import { data } from 'react-router-dom';

function Search() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState('');

  useEffect(() => {
    if (query) {
      fetch(`http://127.0.0.1:8000/api/search?search_term=${query}`, {
        mode: 'cors',
      })
      .then(response => response.json())  
      // .then(data => console.log(data.results))
      .then(data => {
        setResults(data.results);
        console.log(data.results);
      })

    //.then(data => setResults(data.items || []))
    //  .then(response => setResults(response.results))
        .catch(error => console.error('Error fetching data:', error));
    } else {
      setResults('');
    }
  }, [query]);

  return (
    <div className="search-container">
        <h1 className={styles.bigblue}><b>Book Finder</b></h1>
      <input
        type="text"
        placeholder="Search for books..."
        value={query}
        onChange={e => setQuery(e.target.value)}
      />
      <p>{results}</p>

    </div>
  );
};

export default Search;