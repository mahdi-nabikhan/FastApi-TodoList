import React, { useEffect, useState } from "react";

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
      console.log("Error fetching users:", err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  if (loading) {
    return <h3>Loading users...</h3>;
  }

  return (
    <div style={{ padding: "20px" }}>
      <h2>User List</h2>

      <table border="1" cellPadding="10" width="100%">
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
              <td>{user.id}</td>
              <td>{user.username}</td>
              <td>{user.is_superuser ? "✅" : "❌"}</td>

              <td>
                <button
                  onClick={() => alert(`User ID: ${user.id}`)}
                >
                  Details
                </button>

                <button
                  style={{ marginLeft: "10px", color: "red" }}
                  onClick={() => alert(`Delete user ${user.id}`)}
                >
                  Delete
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}