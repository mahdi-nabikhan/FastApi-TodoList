import React, { useState } from 'react'
import './RegisterPage.css'

export default function RegisterPage() {

  const [username,setUsername]=useState('')
  const [password,setPassword]=useState('')
  const [passwordConfirm,setPasswordConfirm]=useState('')
  const registerHandler = event =>{
    event.preventDefault()
    let userInfo = {
      username:username,
      password:password,
      password_confirm:passwordConfirm
    }
  }
  fetch(`http://localhost:8000/register`,{
    method :'POST',
    body:JSON.stringify(userInfo)
  }).then(res =>console.log(res))

  return (
    <div className="register-container">
      <form className="register-form" onSubmit={registerHandler}>
        <h2>Register</h2>

        <input
          type="text"
          placeholder="Username"
          className="register-input"
          onChange={(event)=>{setUsername(event.target.value)}}
        />

        <input
          type="password"
          placeholder="Password"
          className="register-input"
          onChange={(event)=>{setPassword(event.target.value)}}
        />

        <input
          type="password"
          placeholder="Confirm Password"
          className="register-input"
          onChange={(event)=>{setPasswordConfirm(event.target.value)}}
        />

        <button type="submit" className="register-btn">
          Sign Up
        </button>
      </form>
    </div>
  )
}
