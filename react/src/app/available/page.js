"use client";

import { useState, useEffect } from 'react';
import BookList from '../../components/booklist';
import { fetchAvailableBooks } from '../../api';

export default function Page() {
  const [books, setBooks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchBooks = async () => {
      try {
        setLoading(true);
        const data = await fetchAvailableBooks();
        setBooks(data);
      } catch (err) {
        setError(err.message);
        console.error('Error fetching books:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchBooks();
  }, []);

  if (loading) {
    return (
      <div className="flex justify-center items-center min-h-screen">
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500"></div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mx-auto max-w-md mt-10">
        <p>Error loading books: {error}</p>
        <p>Please try again later</p>
      </div>
    );
  }

  return <BookList books={books} />;
}