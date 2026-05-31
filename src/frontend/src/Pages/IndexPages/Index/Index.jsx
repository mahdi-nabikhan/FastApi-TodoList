import React, { useEffect, useState } from 'react'
import './Index.css'
import DeleteModal from '../../../Components/DeleteModal/DeleteModal'


export default function Index() {
  const [todoList, setTodoList] = useState([])
  const [showModal, setShowModal] = useState(false)
  const [selectedTodo, setSelectedTodo] = useState(null)

  function fetchTodos() {
    fetch('http://localhost:8000/tasks/?limit=10&offset=0', {
      method: 'GET',
      credentials: 'include'
    })
      .then(res => res.json())
      .then(data => setTodoList(data))
  }

  useEffect(() => {
    fetchTodos()
  }, [])

  const deleteTodo = () => {
    fetch(`http://localhost:8000/delete/task/${selectedTodo.id}`, {
      method: 'DELETE',
      credentials: 'include'
    })
      .then(res => {
        if (res.ok) {
          setTodoList(prev =>
            prev.filter(item => item.id !== selectedTodo.id)
          )
        }
      })
      .finally(() => {
        setShowModal(false)
        setSelectedTodo(null)
      })
  }

  return (
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
      {todoList.map(todo => (
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

            <button
              className="btn delete-btn"
              onClick={() => {
                setSelectedTodo(todo)
                setShowModal(true)
              }}
            >
              Delete
            </button>
          </td>
        </tr>
      ))}
    </tbody>
  </table>

  <DeleteModal
    isOpen={showModal}
    todo={selectedTodo}
    onClose={() => {
      setShowModal(false)
      setSelectedTodo(null)
    }}
    onConfirm={deleteTodo}
  />

</div>
  )
}

