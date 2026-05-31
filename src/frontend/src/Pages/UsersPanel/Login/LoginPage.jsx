import React from 'react'
import './LoginPage.css'
export default function LoginPage() {
  return (
    <div className="login-container">
      <form className="login-form">
        <h2>Login</h2>

        <input
          type="email"
          placeholder="Email"
          className="login-input"
        />

        <input
          type="password"
          placeholder="Password"
          className="login-input"
        />

        <button type="submit" className="login-btn">
          Sign In
        </button>
      </form>
    </div>
  )
}
