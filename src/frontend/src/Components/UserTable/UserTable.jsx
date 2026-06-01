import React, { useEffect, useState } from "react";
import "./UserTable.css";

export default function UserTable() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);

  const fetchUsers = async () => {
    try {
      const res = await fetch("http://localhost:8000/all/users", {
        method: "GET",
        credentials: "include",
      });

      const data = await res.json();
      setUsers(data);
    } catch (err) {
      console.log(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  if (loading) {
    return <h3 className="loading">Loading users...</h3>;
  }

  return (
    <div className="table-wrapper">
      <h2 className="title">User Management</h2>

      <table className="user-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Username</th>
            <th>Superuser</th>
            <th>Actions</th>
          </tr>
        </thead>

        <tbody>
          {users.map((user) => (
            <tr key={user.id}>
              <td>#{user.id}</td>
              <td className="username">{user.username}</td>

              <td>
                <span
                  className={user.is_superuser ? "badge admin" : "badge user"}
                >
                  {user.is_superuser ? "Admin" : "User"}
                </span>
              </td>

              <td className="actions">
                <button className="btn details">Details</button>
                <button className="btn delete">Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}