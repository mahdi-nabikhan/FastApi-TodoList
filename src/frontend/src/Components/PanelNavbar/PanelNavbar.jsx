import React from 'react'
import {NavLink} from 'react-router-dom'
import './PanelNavbar.css'
export default function PanelNavbar() {
  return (
    <nav className="panel-navbar">

      <div className="panel-logo">
        Todo Panel
      </div>

      <ul className="panel-links">

        <li>
          <NavLink to="/panel">
            Dashboard
          </NavLink>
        </li>

        <li>
          <NavLink to="/panel/todos">
            Todos
          </NavLink>
        </li>

        <li>
          <NavLink to="/panel/profile">
            Profile
          </NavLink>
        </li>

        <li>
          <NavLink to="/panel/settings">
            Settings
          </NavLink>
        </li>

      </ul>

      <button className="logout-btn">
        Logout
      </button>

    </nav>
  )
}
