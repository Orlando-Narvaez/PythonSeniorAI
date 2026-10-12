import { useState } from 'react';

function TaskForm() {
  const [taskTitle, setTaskTitle] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    // La lógica de agregar tareas se implementará en una iteración posterior.
  };

  const handleChange = (event) => {
    setTaskTitle(event.target.value);
  };

  return (
    <section
      className="rounded-2xl border border-slate-200/80 bg-white p-6 shadow-sm"
      aria-labelledby="task-form-heading"
    >
      <h2
        id="task-form-heading"
        className="mb-4 text-sm font-medium uppercase tracking-wide text-slate-500"
      >
        Nueva tarea
      </h2>

      <form className="flex flex-col gap-3 sm:flex-row" onSubmit={handleSubmit}>
        <label htmlFor="task-title" className="sr-only">
          Título de la tarea
        </label>
        <input
          id="task-title"
          name="taskTitle"
          type="text"
          value={taskTitle}
          onChange={handleChange}
          placeholder="Escribe una tarea..."
          autoComplete="off"
          maxLength={200}
          className="min-w-0 flex-1 rounded-xl border border-slate-200 bg-slate-50 px-4 py-3 text-slate-900 outline-none transition focus:border-indigo-400 focus:bg-white focus:ring-2 focus:ring-indigo-500/20"
        />
        <button
          type="submit"
          className="rounded-xl bg-indigo-600 px-6 py-3 font-medium text-white shadow-sm transition hover:bg-indigo-700 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600 active:bg-indigo-800"
        >
          Agregar
        </button>
      </form>
    </section>
  );
}

export default TaskForm;
