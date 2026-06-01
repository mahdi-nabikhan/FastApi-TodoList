import React from 'react'
import Features from '../../../Components/Features/Features'
import './Dashboard.css'
import Chart from '../../../Components/Chart/Chart'
export default function Dashboard() {
  return (
    <div className='home'><Features/>
    <Chart/>
    </div>
  )
}
