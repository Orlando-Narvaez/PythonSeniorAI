import PropTypes from 'prop-types';

function TaskList({ tasks }) {
  const hasTasks = tasks.length > 0;

  return (
    <section
      className="rounded-2xl border border-slate-200/80 bg-white p-6 shadow-sm"
      aria-labelledby="task-list-heading"
    >
      <h2
        id="task-list-heading"
        className="mb-4 text-sm font-medium uppercase tracking-wide text-slate-500"
      >
        Tareas pendientes
      </h2>

      {!hasTasks && (
        <p className="text-center text-slate-500">No hay tareas por ahora.</p>
      )}

      {hasTasks && (
        <ul className="space-y-2" role="list">
          {tasks.map((task) => (
            <li
              key={task.id}
              className="flex items-center gap-3 rounded-xl border border-slate-100 bg-slate-50/80 px-4 py-3 text-slate-800 transition-colors hover:border-indigo-100 hover:bg-indigo-50/40"
            >
              <span
                className="size-2 shrink-0 rounded-full bg-indigo-500"
                aria-hidden="true"
              />
              <span>{task.title}</span>
            </li>
          ))}
        </ul>
      )}
    </section>
  );
}

TaskList.propTypes = {
  tasks: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.oneOfType([PropTypes.string, PropTypes.number]).isRequired,
      title: PropTypes.string.isRequired,
    }),
  ).isRequired,
};

export default TaskList;
