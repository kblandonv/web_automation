import React, { useState } from "react";

function App() {
  const [query, setQuery] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const API_URL = process.env.REACT_APP_API_URL;

  const handleSearch = async () => {
    if (!query) return;
    setLoading(true);
    try {
      const res = await fetch(
        `${API_URL}/search?query=${encodeURIComponent(query)}`
      );
      const json = await res.json();
      setResult(json);
    } catch (err) {
      setResult({ status: "error", message: err.message });
    } finally {
      setLoading(false);
    }
  };

  const container = {
    maxWidth: 600,
    margin: "40px auto",
    padding: 20,
    background: "#fff",
    borderRadius: 8,
    boxShadow: "0 2px 8px rgba(0,0,0,0.1)",
    fontFamily: "Segoe UI, sans-serif",
  };
  const input = { padding: 8, fontSize: 16, width: "70%" };
  const button = {
    padding: "8px 16px",
    marginLeft: 8,
    fontSize: 16,
    background: "#007bff",
    color: "#fff",
    border: "none",
    borderRadius: 4,
    cursor: "pointer",
  };
  const card = {
    marginTop: 20,
    padding: 16,
    border: "1px solid #ddd",
    borderRadius: 4,
    background: "#f9f9f9",
  };
  const link = { color: "#007bff", textDecoration: "none" };

  return (
    <div style={container}>
      <h1 style={{ textAlign: "center" }}>Web Automation UI</h1>

      <div style={{ textAlign: "center" }}>
        <input
          style={input}
          type="text"
          placeholder="Término de búsqueda"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button style={button} onClick={handleSearch}>
          Buscar
        </button>
      </div>

      {loading && <p style={{ textAlign: "center" }}>Cargando…</p>}

      {result && (
        <div style={card}>
          <h2>{result.result_title}</h2>
          <p>
            <a
              href={result.result_url}
              target="_blank"
              rel="noreferrer"
              style={link}
            >
              Ver en Wikipedia
            </a>
          </p>
          <p>
            <strong>Descargas:</strong>
            <br />
            <a
              href={`${API_URL}/${result.pdf_path}`}
              target="_blank"
              rel="noreferrer"
              style={link}
            >
              📄 PDF
            </a>
            {" | "}
            <a
              href={`${API_URL}/${result.zip_path}`}
              target="_blank"
              rel="noreferrer"
              style={link}
            >
              📦 ZIP
            </a>
          </p>
        </div>
      )}
    </div>
  );
}

export default App;
