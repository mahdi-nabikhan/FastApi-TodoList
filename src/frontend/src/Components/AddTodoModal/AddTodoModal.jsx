import React, { useState } from 'react'
import { useNavigate } from 'react-router'
import './AddTodoModal.css'

export default function AddTodoModal({ isOpen, onClose }) {
  const [title, setTitle] = useState('')
  const [description, setDescription] = useState('')
  const [isCompleted, setIsCompleted] = useState(false)
  const navigate = useNavigate()

  if (!isOpen) return null

  const createTodoHandler = async (e) => {
    e.preventDefault()

    const todoData = {
      title,
      description,
      is_complated: isCompleted
    }

    try {
      const response = await fetch(
        'http://localhost:8000/task/create',
        {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          credentials: 'include',
          body: JSON.stringify(todoData)
        }
      )

      const result = await response.json()

      if (response.ok) {
        alert('Todo created successfully')

        setTitle('')
        setDescription('')
        setIsCompleted(false)

        onClose()
        window.location.reload()
      } else {
        console.log(result)
        alert('Failed to create todo')
      }
    } catch (err) {
      console.log(err)
      alert('Server Error')
    }
  }

  return (
    <div className="modal-overlay">
      <div className="modal">

        <h2>Create Todo</h2>

        <form onSubmit={createTodoHandler}>

          <input
            type="text"
            placeholder="Todo Title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
          />

          <textarea
            placeholder="Todo Description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            required
          />

          <label className="checkbox-label">
            <input
              type="checkbox"
              checked={isCompleted}
              onChange={(e) => setIsCompleted(e.target.checked)}
            />
            Mark as completed
          </label>

          <div className="modal-actions">

            <button
              type="button"
              onClick={onClose}
            >
              Close
            </button>

            <button type="submit">
              Create
            </button>

          </div>

        </form>

      </div>
    </div>
  )
}