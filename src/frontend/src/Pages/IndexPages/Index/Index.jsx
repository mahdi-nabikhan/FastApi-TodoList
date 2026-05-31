import React, { useEffect, useState } from 'react'
import './Index.css'
export default function Index() {
  const [TodoList,setTodoList]=useState([])

  function TodoListRequest (){
    fetch('http://localhost:8000/tasks/?limit=10&offset=0',{
      credentials:'include',
      method:'GET'
    }).then(res => res.json())
    .then((result)=>{
      setTodoList(result)
      console.log(result)
    })
  }

  useEffect(() => {
    fetch('http://localhost:8000/tasks/?limit=10&offset=0', {
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
        <div className="table-container">
      <h2>Todo List</h2>

      <table className="todo-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Title</th>
            <th>Completed</th>
            <th>Actions</th>
          </tr>
        </thead>

        <tbody>
          {TodoList.map(todo => (
            <tr key={todo.id}>
              <td>{todo.id}</td>
              <td>{todo.title}</td>
              <td>{todo.is_complated ? '✅' : '❌'}</td>

              <td>
                <button className="btn details-btn">
                  Details
                </button>

                <button className="btn edit-btn">
                  Edit
                </button>

                <button className="btn delete-btn">
                  Delete
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
    
    </>
  )
}

