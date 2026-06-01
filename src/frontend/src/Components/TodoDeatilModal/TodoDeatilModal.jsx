import React from 'react'
import './TodoDeatilModal.css'

export default function TodoDetailModal({
  isOpen,
  onClose,
  todo
}) {
  if (!isOpen || !todo) return null

  return (
    <div className="modal-overlay">
      <div className="modal">

        <h2>Todo Details</h2>

        <div className="detail-item">
          <strong>ID:</strong>
          <span>{todo.id}</span>
        </div>

        <div className="detail-item">
          <strong>Title:</strong>
          <span>{todo.title}</span>
        </div>

        <div className="detail-item">
          <strong>Description:</strong>
          <span>{todo.description}</span>
        </div>

        <div className="detail-item">
          <strong>Status:</strong>
          <span>
            {todo.is_complated ? '✅ Completed' : '❌ Not Completed'}
          </span>
        </div>

        <div className="detail-item">
          <strong>Created:</strong>
          <span>{todo.created_date}</span>
        </div>

        <div className="detail-item">
          <strong>Updated:</strong>
          <span>{todo.updated_date}</span>
        </div>

        <div className="modal-actions">
          <button
            className="close-btn"
            onClick={onClose}
          >
            Close
          </button>
        </div>

      </div>
    </div>
  )
}