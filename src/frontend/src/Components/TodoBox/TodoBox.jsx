import React from 'react'
import './TodoBox.css'
export default function TodoBox() {
    const isDone = todo.is_complated;
  return (
        <div
      className={`todo-box ${isDone ? 'todo-box--done' : ''}`}
      onClick={() => onToggle && onToggle(todo.id)}
    >
      <div className="todo-content">
        <span className={`todo-title ${isDone ? 'todo-title--done' : ''}`}>
          {todo.title}
        </span>
        {todo.description && (
          <p className={`todo-desc ${isDone ? 'todo-desc--done' : ''}`}>
            {todo.description}
          </p>
        )}
      </div>
      {onToggle && (
        <input
          type="checkbox"
          className="todo-checkbox"
          checked={isDone}
          onChange={(e) => {
            e.stopPropagation();
            onToggle(todo.id);
          }}
        />
      )}
    </div>
    
  )
}
