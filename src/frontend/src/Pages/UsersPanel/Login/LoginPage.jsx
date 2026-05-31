import React, { useState } from 'react'
import {useNavigate} from 'react-router-dom'
import './LoginPage.css'
export default function LoginPage() {
  const [username,setUsername]=useState('')
  const[password,setPassword] = useState('')
  const navigate = useNavigate()
  const LoginHandler = (event) =>{
    event.preventDefault()
    let Data ={
      username,
      password
    }
    fetch('http://localhost:8000/login/jwt',{
      
      method:'POST',
      headers:{
        'Content-Type':'application/json'
      },
      credentials :'include',
      body:JSON.stringify(Data)
    }).then(res =>{
      if (res.ok) {
        
        navigate('/')
        return res.json()
      }
    }).then(response =>{console.log(response)})
  }

  return (
    <div className="login-container">
      <form className="login-form" onSubmit={LoginHandler}>
        <h2>Login</h2>

        <input
          type="username"
          placeholder="Username"
          className="login-input"
          onChange={(event)=>{setUsername(event.target.value)}}
        />

        <input
          type="password"
          placeholder="Password"
          className="login-input"
          onChange={(event) =>{setPassword(event.target.value)}}
        />

        <button type="submit" className="login-btn">
          Sign In
        </button>
      </form>
    </div>
  )
}
