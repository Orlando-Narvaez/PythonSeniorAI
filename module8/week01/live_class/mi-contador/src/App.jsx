
import './App.css';
import Contador from './Contador';
import Saludo from './Saludo';
import Producto from './Producto';
import Interruptor from './Interruptor';  

function App() {

  return (
    <div style={{ textAlign: "center", marginTop: "20px" }}>
      <h1>Mi App React</h1>
      <Saludo nombre="Orlando"></Saludo>
      <Saludo nombre="Kevin"></Saludo>
      <Saludo nombre="Juana"></Saludo>
    

      <h1>Mis productos</h1>
      <Producto nombre="Computador portátil" precio={2500000} categoria="Tecnología" />
      <Producto nombre="Audífonos inalámbricos" precio={180000} categoria="Audio" />
      <Producto nombre="Teclado mecánico" precio={220000} categoria="Periféricos" />


      <h1>Selector de modo</h1>
      <Interruptor />

      <h1>Contador</h1>
      <Contador />
    </div>
  );
}

export default App
