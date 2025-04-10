import Navbar from '../components/navbar';
import './globals.css';

export const metadata = {
  title: 'My App',
  description: 'Application with user avatar and dropdown',
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <Navbar />
        <main className="container mx-auto px-4 py-8">
          {children}
        </main>
      </body>
    </html>
  );
}