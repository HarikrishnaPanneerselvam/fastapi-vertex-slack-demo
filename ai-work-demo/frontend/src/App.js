import React, { useState } from "react";

function App() {
  const [loading, setLoading] = useState(false);
  const [status, setStatus] = useState("");

  const callEndpoint = async (path) => {
    setLoading(true);
    setStatus("");
    try {
      const res = await fetch(`http://127.0.0.1:8000${path}`);
      const ct = res.headers.get("content-type") || "";
      let body;
      if (ct.includes("application/json")) {
        body = await res.json();
        body = JSON.stringify(body, null, 2);
      } else {
        body = await res.text();
      }

      if (!res.ok) {
        throw new Error(`${res.status} ${res.statusText} — ${body}`);
      }
      setStatus(`Success:\n${body}`);
    } catch (err) {
      setStatus(`Request failed:\n${err.message}`);
      console.error("Error calling endpoint:", err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: 20, fontFamily: "Arial, sans-serif" }}>
      <h1>React + FastAPI Demo</h1>

      <div style={{ display: "flex", gap: 10, marginBottom: 12 }}>
        <button onClick={() => callEndpoint("/error1")} disabled={loading}>
          Trigger Error 1
        </button>
        <button onClick={() => callEndpoint("/error2")} disabled={loading}>
          Trigger Error 2
        </button>
        <button onClick={() => callEndpoint("/slow")} disabled={loading}>
          Trigger Slow Endpoint
        </button>
      </div>

      {loading && <div>Calling backend…</div>}

      {status && (
        <pre
          style={{
            background: "#f6f8fa",
            padding: 12,
            borderRadius: 6,
            whiteSpace: "pre-wrap",
            maxWidth: "90%",
          }}
        >
          {status}
        </pre>
      )}
    </div>
  );
}

export default App;
