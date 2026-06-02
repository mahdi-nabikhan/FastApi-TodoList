import React, { useEffect, useState } from "react";
import "./TaskTable.css";
import DeleteModal from "../DeleteModal/DeleteModal";
export default function TaskTable() {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showDeleteModal, setShowDeleteModal] = useState(false);
  const [selectedTask, setSelectedTask] = useState(null);

  const fetchTasks = async () => {
    try {
      const response = await fetch(
        "http://localhost:8000/panel/tasks",
        {
          method: "GET",
          credentials: "include",
        }
      );

      const data = await response.json();

      if (response.ok) {
        setTasks(data);
      } else {
        console.log(data);
      }
    } catch (error) {
      console.log("Error fetching tasks:", error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  if (loading) {
    return (
      <div className="tasks-loading">
        Loading Tasks...
      </div>
    );
  }
  const handleDeleteTask = async () => {
    try {
      const response = await fetch(
        `http://localhost:8000/panel/delete/task/${selectedTask.id}`,
        {
          method: "DELETE",
          credentials: "include",
        }
      );

      if (response.ok) {
        setTasks((prev) =>
          prev.filter(
            (task) => task.id !== selectedTask.id
          )
        );
      }
    } catch (error) {
      console.log(error);
    } finally {
      setShowDeleteModal(false);
      setSelectedTask(null);
    }
  };

  return (
    <div className="tasks-table-container">
      <div className="table-header">
        <h2>Tasks Management</h2>
        <span>{tasks.length} Tasks</span>
      </div>

      <table className="tasks-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Title</th>
            <th>Description</th>
            <th>Status</th>
            <th>User ID</th>
            <th>Created At</th>
            <th>Actions</th>
          </tr>
        </thead>

        <tbody>
          {tasks.map((task) => (
            <tr key={task.id}>
              <td>{task.id}</td>

              <td>{task.title}</td>

              <td>
                {task.description?.length > 50
                  ? task.description.slice(0, 50) + "..."
                  : task.description}
              </td>

              <td>
                {task.is_complated ? (
                  <span className="status-completed">
                    Completed
                  </span>
                ) : (
                  <span className="status-pending">
                    Pending
                  </span>
                )}
              </td>

              <td>{task.user_id}</td>

              <td>
                {task.created_date
                  ? new Date(task.created_date).toLocaleDateString()
                  : "-"}
              </td>

              <td>
                <div className="action-buttons">
                  <button
                    className="details-btn"
                    onClick={() =>
                      console.log("Details", task.id)
                    }
                  >
                    Details
                  </button>

                  <button
                    className="edit-btn"
                    onClick={() =>
                      console.log("Edit", task.id)
                    }
                  >
                    Edit
                  </button>

                  <button
                    className="delete-btn"
                    onClick={() => {
                      setSelectedTask(task);
                      setShowDeleteModal(true);
                    }}
                  >
                    Delete
                  </button>
                </div>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      <DeleteModal
        isOpen={showDeleteModal}
        todo={selectedTask}
        onClose={() => {
          setShowDeleteModal(false);
          setSelectedTask(null);
        }}
        onConfirm={handleDeleteTask}
      />
    </div>
  );
}