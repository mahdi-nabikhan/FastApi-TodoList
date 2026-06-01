import React from 'react'
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer
} from 'recharts'

import './Chart.css'

export default function Chart() {
  const data = [
    { name: 'Jan', todos: 12 },
    { name: 'Feb', todos: 19 },
    { name: 'Mar', todos: 8 },
    { name: 'Apr', todos: 27 },
    { name: 'May', todos: 35 },
    { name: 'Jun', todos: 22 },
    { name: 'Jul', todos: 41 }
  ]

  return (
    <div className="chart">
      <h3 className="chartTitle">
        Todo Activity
      </h3>

      <ResponsiveContainer width="100%" height={350}>
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />

          <XAxis dataKey="name" />

          <YAxis />

          <Tooltip />

          <Line
            type="monotone"
            dataKey="todos"
            stroke="#2563eb"
            strokeWidth={3}
          />
        </LineChart>
      </ResponsiveContainer>
    </div>
  )
}