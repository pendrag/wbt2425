import Link from 'next/link';

export default function Sections() {
    return (
      <div className="flex gap-6">
        <Link href="/" className="text-white hover:text-gray-300">
          BookCrossing
        </Link>
        <Link href="/available" className="text-white hover:text-gray-300">
          Available
        </Link>
        <Link href="/loans" className="text-white hover:text-gray-300">
          My loans
        </Link>
        <Link href="/owned" className="text-white hover:text-gray-300">
          My books
        </Link>
      </div>
    )

}