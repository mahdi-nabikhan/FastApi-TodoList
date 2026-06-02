import React, { useEffect, useState } from "react";
import "./UserTable.css";
import DeleteModal from '../DeleteModal/DeleteModal'
import DetailModal from '../DeatilModal/DeatilModal'

export default function UserTable() {
    const [users, setUsers] = useState([]);
    const [loading, setLoading] = useState(true);
    const [showModal, setShowModal] = useState(false);
    const [selectedItem, setSelectedItem] = useState(null);
    const [showDetailModal, setShowDetailModal] = useState(false);


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
    const handleDelete = async () => {
        try {
            const res = await fetch(
                `http://localhost:8000/admin/users/${selectedItem.id}`,
                {
                    method: "DELETE",
                    credentials: "include",
                }
            );

            if (res.ok) {
                setUsers((prev) =>
                    prev.filter((u) => u.id !== selectedItem.id)
                );
            }
        } catch (err) {
            console.log(err);
        } finally {
            setShowModal(false);
            setSelectedItem(null);
        }
    };
    const getUserDetail = async (id) => {
        try {
          const res = await fetch(
            `http://localhost:8000/admin/users/${id}`,
            {
              method: "GET",
              credentials: "include",
            }
          );
      
          const data = await res.json();
      
          setSelectedItem(data);
          setShowDetailModal(true);
        } catch (err) {
          console.log(err);
        }
      };

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
                                <button className="btn details" onClick={() => getUserDetail(user.id)}>Details</button>
                                <button className="btn delete" onClick={() => {
                                    setSelectedItem(user);
                                    setShowModal(true);
                                }}>Delete</button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
            <DeleteModal
                isOpen={showModal}
                onClose={() => {
                    setShowModal(false);
                    setSelectedItem(null);
                }}
                onConfirm={handleDelete}
            />
            <DetailModal
                isOpen={showDetailModal}
                data={selectedItem}
                onClose={() => {
                    setShowDetailModal(false);
                    setSelectedItem(null);
                }}
            />
        </div>
    );
}