import React, { useState } from "react";

function Interuptor() {
    const [oscuro, setOscuro] = useState(false);

    const estilo = {
        backgroundColor: oscuro ? "#333" : "#fff",
        color: oscuro ? "#fff" : "#000",
        padding: 24,
        borderRadius: 8,
        border: "1px solid #ccc",
        textAlign: "center",
    };

    return (
    <div style={estilo}>
      <h2>{oscuro ? "Modo Oscuro" : "Modo Claro"}</h2>
      <button onClick={() => setOscuro(!oscuro)}>
        Cambiar modo
      </button>
    </div>
  );
}

export default Interuptor;