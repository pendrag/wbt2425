// app/components/Navbar.jsx
"use client"; // This is needed because we use client-side state and event handlers
import Sections from "./sections"
import Avatar from "./avatar"

export default function Navbar() {

  return (
    <nav className="flex justify-between items-center px-4 py-3 bg-gray-800 text-white">
      <Sections/>
      <Avatar/>
    </nav>
  );
}