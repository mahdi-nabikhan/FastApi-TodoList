import React from 'react'
import './DeleteModal.css'

export default function DeleteModal({id}) {
    

    return (
    <div className="modal-overlay">
      <div className="modal">
        <h3>Delete Todo</h3>

        <p>
          Are you sure you want to delete this item?
        </p>

        <div className="modal-actions">
          <button
            className="close-btn"
            onClick={onClose}
          >
            Close
          </button>

          <button
            className="ok-btn"
            onClick={onConfirm}
          >
            OK
          </button>
        </div>
      </div>
    </div>
  )
}