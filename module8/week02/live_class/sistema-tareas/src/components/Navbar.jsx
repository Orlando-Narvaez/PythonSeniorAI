const SYSTEM_TITLE = 'Sistema de Tareas';

function Navbar() {
  return (
    <header className="border-b border-slate-200/80 bg-white/80 shadow-sm backdrop-blur-md">
      <nav
        className="mx-auto flex max-w-2xl items-center justify-center px-4 py-5 sm:px-6"
        aria-label="Principal"
      >
        <h1 className="text-xl font-semibold tracking-tight text-slate-900 sm:text-2xl">
          {SYSTEM_TITLE}
        </h1>
      </nav>
    </header>
  );
}

export default Navbar;
