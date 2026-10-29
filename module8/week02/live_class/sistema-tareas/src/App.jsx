import { useState } from 'react';
import Navbar from './components/Navbar';
import TaskForm from './components/TaskForm';
import TaskList from './components/TaskList';

const INITIAL_TASKS = [
  { id: 'task-comprar-pan', title: 'Comprar pan' },
  { id: 'task-estudiar-react', title: 'Estudiar React' },
];

function App() {
  const [tasks] = useState(INITIAL_TASKS);

  return (
    <div className="min-h-screen bg-slate-100 text-slate-900">
      <Navbar />

      <main className="mx-auto flex w-full max-w-2xl flex-col gap-5 px-4 py-8 sm:px-6 sm:py-10">
        <TaskList tasks={tasks} />
        <TaskForm />
      </main>
    </div>
  );
}

export default App;
