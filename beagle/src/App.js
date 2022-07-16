import { useState, useEffect } from 'react';
import './App.css';

function App() {
  changeSearchTerms => (e) => {
    this.setState({
      searchTerms: e.target.value
    })
  }
  return (

    
    <div className="App">
      <h1> Beagle Search </h1>
      <form action = "">
        <input type="text" value=''onChange={this.changeSearchTerms} placeholder='search news' />
        <button type= 'submit' onClick = {this.changeSearchTerms}></button>
      </form>
      {/* {searchResults} */}
    </div>
  );
}

export default App;
