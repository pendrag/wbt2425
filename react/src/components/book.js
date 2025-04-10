// Individual book card component
export default function Book ({ title, author }) {
  return (
    <div className="max-w-sm p-6 bg-white border border-gray-200 rounded-lg shadow-sm dark:bg-gray-800 dark:border-gray-700 flex flex-col">
      {/* Author in the top bar */}
      <div className="w-full text-gray-700 dark:text-gray-400">
        <p className="font-medium truncate text-left">{author}</p>
      </div>
      
      {/* Title in the card body */}
      <div className="w-full mt-2">
        <h3 className="text-2xl font-bold tracking-tight text-gray-900 dark:text-white text-left">{title}</h3>
      </div>

      {/* Buttons - aligned to the right */}
      <div className="w-full flex justify-end mt-5">
        <a href="#" className="inline-flex items-center px-3 py-2 text-sm font-medium text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
          Read more
          <svg className="rtl:rotate-180 w-3.5 h-3.5 ms-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 10">
              <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M1 5h12m0 0L9 1m4 4L9 9"/>
          </svg>
        </a>
      </div>
    </div>

  );
};