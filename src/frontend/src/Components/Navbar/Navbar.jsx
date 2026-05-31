// Navbar.jsx
import React from 'react';
import './Navbar.css'
import {NavLink} from 'react-router-dom'
const Navbar = () => {
  return (
    <>
      <nav className="navbar">
        <div className="nav-container">
          <div className="logo">
            <a href="/">✨ Aurora</a>
          </div>

          {/* Hidden checkbox (no React state) */}
          <input type="checkbox" id="nav-checkbox" />
          <label htmlFor="nav-checkbox" className="menu-toggle">☰</label>

          <ul className="nav-links">
            <li><NavLink to="/">Home</NavLink></li>
            <li><NavLink to="/login">Login</NavLink></li>
            <li><NavLink to="/regsiter">Register</NavLink></li>
            <li><NavLink to="/about">Panel</NavLink></li>
            <li><NavLink to="/contact" className="btn-cta">Add a Todo</NavLink></li>
          </ul>
        </div>
      </nav>
    </>
  );
};

export default Navbar;