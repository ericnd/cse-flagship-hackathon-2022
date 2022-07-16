import React from "react";
import "./App.css";
import SearchBar from "./Components/SearchBar";
import BookData from "./Data.json";
import image from './beagle.png'

// used https://github.com/machadop1407/React-Search-Bar 


function App() {
  return (
    <div className="App">
        <img src={image} alt="beagle" />
      <SearchBar placeholder="Let's find real news..." data={BookData} />
    </div>
  );
}

export default App;
