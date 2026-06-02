import React, { useState } from "react";
import useLogin from "../../../Hooks/useLogin";

export default function LoginPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const { login, loading, error } = useLogin();

  const LoginHandler = async (event) => {
    event.preventDefault();

    try {
      const result = await login(
        username,
        password
      );

      console.log(result);
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <form onSubmit={LoginHandler}>
      <input
        type="text"
        value={username}
        onChange={(e) =>
          setUsername(e.target.value)
        }
      />

      <input
        type="password"
        value={password}
        onChange={(e) =>
          setPassword(e.target.value)
        }
      />

      <button
        type="submit"
        disabled={loading}
      >
        {loading ? "Loading..." : "Login"}
      </button>

      {error && <p>{error}</p>}
    </form>
  );
}