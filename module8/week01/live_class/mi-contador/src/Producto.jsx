function Producto({ nombre, precio, categoria }) {
  return (
    <div style={{ border: "1px solid #ccc", borderRadius: 8, padding: 16, margin: 8 }}>
      <h3>{nombre}</h3>
      <p>Precio: ${precio}</p>
      <span>Categoría: {categoria}</span>
    </div>
  );
}

export default Producto;