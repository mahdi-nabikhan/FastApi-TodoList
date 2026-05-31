import React, { useEffect, useState } from 'react'

export default function Index() {
  const [TodoList,setTodoList]=useState([])

  function TodoListRequest (){
    fetch('http://localhost:8000/tasks',{
      credentials:'include',
      method:'GET'
    }).then(res => res.json())
    .then((result)=>{
      setTodoList(result)
      console.log(result)
    })
  }

  useEffect(() => {
    fetch('http://localhost:8000/tasks/', {
      credentials: 'include'
    })
      .then(res => res.json())
      .then(result => {
        console.log(result)
  
        if (Array.isArray(result)) {
          setTodoList(result)
        } else {
          setTodoList([])
        }
      })
  }, [])
  return (
    <>
    {TodoList.map((todo)=>(
      <p key={todo.id}>{todo.title}</p>
    ))}
    
    </>
  )
}

