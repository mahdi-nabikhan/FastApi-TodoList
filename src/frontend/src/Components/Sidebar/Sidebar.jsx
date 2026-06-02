import React from 'react'
import './Sidebar.css'
import { Link } from 'react-router'
export default function Sidebar() {
  return (
    <div className="sidebar">
        <div className="sidebarWrapper">
            <div className="sidebarMenu">
                <h3 className="sidebarTitle">Dashbord</h3>
                <ul className="sidebarList">
                    <Link className='text-link' to={'/'}><li className="sidebarListItem active">Home</li></Link>
                    <Link className='text-link' to={'todo'}><li className="sidebarListItem active">Todo</li></Link>
                    <Link className='text-link' to={'register/admin'}><li className="sidebarListItem active">Register a admin</li></Link>
                </ul>
            </div>
        </div>
    </div>
  )
}
