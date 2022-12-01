import React, { Component } from 'react';
import './App.css';
import logo from './assets/space_dog_big_jump.png'


export class Banner extends Component {
    render() {
      return(
        <div className="banner">
            <img alt="logo" className="bannerlogo" src={logo}></img>
            <h1 className="bannerlogo">ANIMAL RESCUE</h1>
            <h3> Please Support Your Local Shelter</h3>
        </div>
             
      )
    }
  
  }
  
  export default Banner