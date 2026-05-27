// Navbar.jsx
import React from 'react';
import './Navbar.css'
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
            <li><a href="/">Home</a></li>
            <li><a href="/features">Features</a></li>
            <li><a href="/pricing">Pricing</a></li>
            <li><a href="/about">About</a></li>
            <li><a href="/contact" className="btn-cta">Get Started</a></li>
          </ul>
        </div>
      </nav>
    </>
  );
};

export default Navbar;