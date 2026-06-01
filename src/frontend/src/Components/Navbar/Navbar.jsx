// Navbar.jsx
import React from 'react';
import './Navbar.css'
import {NavLink} from 'react-router-dom'
import AddTodoModal from '../AddTodoModal/AddTodoModal';
import { useState } from 'react';
const Navbar = () => {
  const [showAddModal, setShowAddModal] = useState(false)
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
            <button
                className="btn-cta"
                onClick={() => setShowAddModal(true)}
              >
                Add a Todo
              </button>
          </ul>
          
        </div>
      </nav>
      <AddTodoModal
        isOpen={showAddModal}
        onClose={() => setShowAddModal(false)}
      />
    </>
  );
};

export default Navbar;