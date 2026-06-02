import React, { useEffect, useState } from 'react'
import './Index.css'
import DeleteModal from '../../../Components/DeleteModal/DeleteModal'
import UpdateModal from '../../../Components/UpdateModal/UpdateModal'
import TodoDetailModal from '../../../Components/TodoDeatilModal/TodoDeatilModal'
export default function Index() {
  const [todoList, setTodoList] = useState([])
  const [showModal, setShowModal] = useState(false)
  const [selectedTodo, setSelectedTodo] = useState(null)
  const [showEditModal, setShowEditModal] = useState(false)
  const [showDetailsModal, setShowDetailsModal] = useState(false)
  const [currentPage, setCurrentPage] = useState(1)
  const [limit] = useState(3)
  const offset = (currentPage - 1) * limit


  function fetchTodos() {
    fetch(`http://localhost:8000/tasks/?limit=${limit}&offset=${offset}`, {
      method: 'GET',
      credentials: 'include'
    })
      .then(res => res.json())
      .then(data => setTodoList(data))
  }

  useEffect(() => {
    fetchTodos()
  }, [currentPage])

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
  const updateTodo = (updatedTodo) => {
    fetch(`http://localhost:8000/task/${updatedTodo.id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json'
      },
      credentials: 'include',
      body: JSON.stringify(updatedTodo)
    })
      .then(res => res.json())
      .then(data => {
        setTodoList(prev =>
          prev.map(item =>
            item.id === updatedTodo.id ? data : item
          )
        )
      })
      .finally(() => {
        setShowEditModal(false)
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
                <button
                  className="btn details-btn"
                  onClick={() => {
                    setSelectedTodo(todo)
                    setShowDetailsModal(true)
                  }}
                >
                  Details
                </button>

                <button
                  className="btn edit-btn"
                  onClick={() => {
                    setSelectedTodo(todo)
                    setShowEditModal(true)
                  }}
                >
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
      <div className="pagination">
        <button
          disabled={currentPage === 1}
          onClick={() =>
            setCurrentPage(prev => prev - 1)
          }
        >
          Previous
        </button>

        <span>
          Page {currentPage}
        </span>

        <button
          onClick={() =>
            setCurrentPage(prev => prev + 1)
          }
        >
          Next
        </button>
      </div>

      <DeleteModal
        isOpen={showModal}
        todo={selectedTodo}
        onClose={() => {
          setShowModal(false)
          setSelectedTodo(null)
        }}
        onConfirm={deleteTodo}
      />
      <UpdateModal
        isOpen={showEditModal}
        todo={selectedTodo}
        onClose={() => {
          setShowEditModal(false)
          setSelectedTodo(null)
        }}
        onSave={updateTodo}
      />

      <TodoDetailModal
        isOpen={showDetailsModal}
        todo={selectedTodo}
        onClose={() => {
          setShowDetailsModal(false)
          setSelectedTodo(null)
        }}
      />
    </div>

  )
}

