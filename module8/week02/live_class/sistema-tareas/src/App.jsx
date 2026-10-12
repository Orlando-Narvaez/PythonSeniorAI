import { useState } from 'react';
import Navbar from './components/Navbar';
import TaskForm from './components/TaskForm';
import TaskList from './components/TaskList';

const INITIAL_TASKS = [
  { id: 1, title: 'Comprar pan' },
  { id: 2, title: 'Estudiar React' },
];

function App() {
  const [tasks] = useState(INITIAL_TASKS);

  return (
    <div className="min-h-screen bg-gradient-to-b from-slate-100 via-white to-indigo-50/30">
      <Navbar />

      <main className="mx-auto flex max-w-2xl flex-col gap-6 px-4 py-8 sm:px-6 sm:py-10">
        <TaskList tasks={tasks} />
        <TaskForm />
      </main>
    </div>
  );
}

export default App;
