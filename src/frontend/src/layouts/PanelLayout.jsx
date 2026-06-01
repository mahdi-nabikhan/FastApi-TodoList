// src/layouts/PanelLayout.jsx

import React from 'react'
import { Outlet } from 'react-router-dom'
import PanelNavbar from '../Components/PanelNavbar/PanelNavbar'
import Sidebar from '../Components/Sidebar/Sidebar'
import './PanelLayout.css'

export default function PanelLayout() {
  return (
    <>
      <PanelNavbar />
      <div className="container">
        <Sidebar/>
        <main>
          <Outlet />
        </main>

      </div>
      
    </>
  )
}