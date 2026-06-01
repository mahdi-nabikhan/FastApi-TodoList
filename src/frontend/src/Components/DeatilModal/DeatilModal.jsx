import './DetailModal.css'

export default function DetailModal({ isOpen, onClose, data }) {
    if (!isOpen || !data) return null;
  
    return (
      <div className="modal-overlay">
        <div className="modal">
  
          <h2>Details</h2>
  
          <p><b>ID:</b> {data.id}</p>
  
          {data.username && (
            <p><b>Username:</b> {data.username}</p>
          )}
  
          {data.title && (
            <>
              <p><b>Title:</b> {data.title}</p>
              <p><b>Description:</b> {data.description}</p>
              <p>
                <b>Completed:</b>{" "}
                {data.is_complated ? "Yes" : "No"}
              </p>
            </>
          )}
  
          <button onClick={onClose}>
            Close
          </button>
  
        </div>
      </div>
    );
  }