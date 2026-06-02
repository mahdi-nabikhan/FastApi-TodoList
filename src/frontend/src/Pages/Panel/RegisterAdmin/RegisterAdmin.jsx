import React, { useState } from "react";
import "./RegisterAdmin.css";

export default function RegisterAdmin() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [passwordConfirm,setPasswordConfirm]=useState('')

  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");

  const registerAdminHandler = async (e) => {
    e.preventDefault();

    try {
      setLoading(true);
      setMessage("");

      const response = await fetch(
        "http://localhost:8000/admin/register",
        {
          method: "POST",
          credentials: "include",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            username,
            password,
            passwordConfirm
          }),
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail);
      }

      setMessage("Admin created successfully ✅");

      setUsername("");
      setPassword("");
    } catch (error) {
      setMessage(error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="adminRegisterCard">
      <h2>Create New Admin</h2>

      <form onSubmit={registerAdminHandler}>
        <div className="formGroup">
          <label>Username</label>

          <input
            type="text"
            placeholder="Enter username"
            value={username}
            onChange={(e) =>
              setUsername(e.target.value)
            }
          />
        </div>

        <div className="formGroup">
          <label>Password</label>

          <input
            type="password"
            placeholder="Enter password"
            value={password}
            onChange={(e) =>
              setPassword(e.target.value)
            }
          />
        </div>
        <div className="formGroup">
          <label>Confirm Password</label>

          <input
            type="password"
            placeholder="confirm password"
            value={passwordConfirm}
            onChange={(e) =>
              setPasswordConfirm(e.target.value)
            }
          />
        </div>


        <button
          type="submit"
          disabled={loading}
        >
          {loading
            ? "Creating..."
            : "Create Admin"}
        </button>
      </form>

      {message && (
        <p className="message">{message}</p>
      )}
    </div>
  );
}