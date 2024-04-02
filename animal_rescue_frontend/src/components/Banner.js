import React, { Component } from "react";
import "../App.css";
import logo from "../assets/space_dog_big_jump.png";

class Banner extends Component {
  render() {
    return (
      <header>
        <div className="container justify-content-center">
          <nav className="navbar navbar-expand-lg navbar-light">
            <a className="navbar-brand" href="#">
              <img
                alt="logo"
                className="navbar-brand-img"
                src={logo}
                width="80"
                height="80"
              />
              <span className="navbar-brand-text">ANIMAL RESCUE</span>
            </a>
            <button
              className="navbar-toggler"
              type="button"
              data-toggle="collapse"
              data-target="#navbarNav"
              aria-controls="navbarNav"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav ml-auto">
                <li className="nav-item">
                  <a className="nav-link" href="#">
                    About Us
                  </a>
                </li>
                <li className="nav-item">
                  <a className="nav-link" href="#">
                    Contact
                  </a>
                </li>
              </ul>
            </div>
          </nav>
          {/* <div className="banner">
            <div className="banner-content">
              <h1 className="banner-title">ANIMAL RESCUE</h1>
              <h3 className="banner-subtitle">Please Support Your Local Shelter</h3>
            </div>
          </div> */}
        </div>
      </header>
    );
  }
}

export default Banner;
