import { useState } from 'react';

const TITLE_MAX_LENGTH = 120;

function TaskForm() {
  const [title, setTitle] = useState('');

  const handleTitleChange = (event) => {
    setTitle(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
  };

  return (
    <section
      className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm sm:p-6"
      aria-labelledby="task-form-heading"
    >
      <h2
        id="task-form-heading"
        className="text-base font-semibold text-slate-900 sm:text-lg"
      >
        Nueva tarea
      </h2>

      <form
        className="mt-4 flex flex-col gap-3 sm:flex-row sm:items-end"
        onSubmit={handleSubmit}
        noValidate
      >
        <div className="w-full">
          <label
            htmlFor="task-title"
            className="mb-1.5 block text-sm font-medium text-slate-700"
          >
            Descripción
          </label>
          <input
            id="task-title"
            name="title"
            type="text"
            value={title}
            onChange={handleTitleChange}
            maxLength={TITLE_MAX_LENGTH}
            autoComplete="off"
            placeholder="Escribe una tarea"
            className="block w-full rounded-xl border border-slate-200 bg-white px-3 py-2.5 text-sm text-slate-900 shadow-sm outline-none placeholder:text-slate-400 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-500/20"
          />
        </div>

        <button
          type="submit"
          className="inline-flex shrink-0 items-center justify-center rounded-xl bg-indigo-600 px-4 py-2.5 text-sm font-semibold text-white shadow-sm transition hover:bg-indigo-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
        >
          Agregar
        </button>
      </form>
    </section>
  );
}

export default TaskForm;
