import { useState } from 'react';
import './App.css';

function App() {
  const [query, setQuery] = useState("");

  // const {tracks} = Data;
  // const {items} = tracks;
  // items looks like this: [{name: 'name1'}, {name: 'name2'}]

  return (
    <div className="App">
      <header className="App-header">
        <label></label>
        <input type="text" onChange={e => setQuery(e.target.value)} placeholder="Search" />

      </header>
    </div>
  );
}

export default App;
