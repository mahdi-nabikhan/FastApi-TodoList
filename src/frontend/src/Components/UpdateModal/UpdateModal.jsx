import React, { useEffect, useState } from 'react'
import './UpdateModal.css'

export default function UpdateModal({
  isOpen,
  onClose,
  onSave,
  todo
}) {
  const [title, setTitle] = useState('')
  const [description, setDescription] = useState('')
  const [isCompleted, setIsCompleted] = useState(false)

  // وقتی todo عوض شد، فرم پر بشه
  useEffect(() => {
    if (todo) {
      setTitle(todo.title || '')
      setDescription(todo.description || '')
      setIsCompleted(todo.is_complated || false)
    }
  }, [todo])

  if (!isOpen) return null

  const handleSave = () => {
    onSave({
      id: todo.id,
      title,
      description,
      is_complated: isCompleted
    })
  }

  return (
    <div className="modal-overlay">
      <div className="modal">

        <h3>Update Todo</h3>

        <input
          type="text"
          placeholder="Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />

        <input
          type="text"
          placeholder="Description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />

        <label className="checkbox">
          <input
            type="checkbox"
            checked={isCompleted}
            onChange={(e) => setIsCompleted(e.target.checked)}
          />
          Completed
        </label>

        <div className="modal-actions">
          <button className="close-btn" onClick={onClose}>
            Close
          </button>

          <button className="save-btn" onClick={handleSave}>
            Save
          </button>
        </div>

      </div>
    </div>
  )
}