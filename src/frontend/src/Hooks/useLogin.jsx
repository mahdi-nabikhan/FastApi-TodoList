import React,{useState} from 'react'
import { useNavigate } from 'react-router';
export default function useLogin() {
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const navigate= useNavigate()
    const login = async (username,password) =>{
        try{
            setLoading(true)
            setError(null)
            const response = await fetch('http://localhost:8000/login/jwt',{
                credentials:'include',
                method:'POST',
                headers: {
                    "Content-Type": "application/json",
                  },
                  body:JSON.stringify({username,password})
            })
            const data = response.json()
            if (!response.ok){
                throw new Error(
                    data.detail || "Login failed"
                  );
            }
            console.log('this is data',data.is_superuser)
            if(data.is_superuser){
                navigate('/panel')
                return data
            }
            
            navigate('/')
            return data
        }catch(err){
            setError(err.message)
            throw err
        }finally{
            setLoading(false)
        }

    }
  return {login,loading,error}
}
