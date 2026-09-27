
import './globals.css'
export const metadata = { title: 'Pharmora AI', description: 'Your Empathetic AI Health Companion' }
export default function RootLayout({children}:{children:React.ReactNode}) {
  return (<html lang="en"><body className="bg-[#F5F7FA] text-[#1B2430]">{children}</body></html>)
}
