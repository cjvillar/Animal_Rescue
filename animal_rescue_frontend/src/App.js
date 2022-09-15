import React, { Component } from "react";
import './App.css';
import AnimalProfile from './AnimalProfile.js';
import Banner from './Banner.js';


class App extends Component {
    render() {
      return (
        <div>
        <Banner />
        <AnimalProfile />
        </div>
      )
    }
  }
  
export default App;