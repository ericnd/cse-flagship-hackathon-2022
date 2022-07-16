import { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [dataList, setData] = useState([{}])

  useEffect(() => {
    fetch("/data").then (
      res => res.json()
    ).then(
      dataList => {
        setData(dataList)
        console.log(dataList)
      }
    )
  }, [])

  const [query, setQuery] = useState("");

  // const {tracks} = Data;
  // const {items} = tracks;
  // items looks like this: [{name: 'name1'}, {name: 'name2'}]

  return (

    
    <div className="App">
      <h1 className='header1'>Beagle 🐶</h1>
      <h1 className='header1'>Sniffing Out 🐄💩</h1>
      <div className='wrapper'>
        <div className='search'>
        <input type='text' onChange={e => setQuery(e.target.value)} placeholder="Type Something Newsworthy..." />

        </div>
      </div>
    </div>
  );
}

export default App;
