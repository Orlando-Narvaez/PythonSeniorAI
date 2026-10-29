import PropTypes from 'prop-types';

function TaskList({ tasks }) {
  const hasTasks = tasks.length > 0;

  return (
    <section
      className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm sm:p-6"
      aria-labelledby="task-list-heading"
    >
      <h2
        id="task-list-heading"
        className="text-base font-semibold text-slate-900 sm:text-lg"
      >
        Tareas pendientes
      </h2>

      {hasTasks ? (
        <ul className="mt-4 space-y-2">
          {tasks.map((task) => (
            <li
              key={task.id}
              className="rounded-xl border border-slate-100 bg-slate-50 px-4 py-3 text-sm text-slate-700 sm:text-base"
            >
              {task.title}
            </li>
          ))}
        </ul>
      ) : (
        <p className="mt-4 text-sm text-slate-500">
          No hay tareas registradas.
        </p>
      )}
    </section>
  );
}

TaskList.propTypes = {
  tasks: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.string.isRequired,
      title: PropTypes.string.isRequired,
    }),
  ).isRequired,
};

export default TaskList;
