import React, { useState } from "react";

function Contador() {
    const [contador, setContador] = useState(0);

    const incrementar = () => setContador(contador + 1);

    return (
        <div style={{ textAlign: "center", marginTop: "20px" }}>
            <h2>Contador: {contador}</h2>
            <button onClick={incrementar}>Aummetar</button>
        </div>
    );
}

export default Contador;