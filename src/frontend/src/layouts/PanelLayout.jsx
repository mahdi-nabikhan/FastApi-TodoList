// src/layouts/PanelLayout.jsx

import React from 'react'
import { Outlet } from 'react-router-dom'
import PanelNavbar from '../Components/PanelNavbar/PanelNavbar'

export default function PanelLayout() {
  return (
    <>
      <PanelNavbar />

      <main>
        <Outlet />
      </main>
    </>
  )
}