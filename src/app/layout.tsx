import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
    title: "Cover Career Day",
    description: "Further your career at the annual Cover Career Day!",
    icons: {
        icon: "/favicon.ico", // Path to your .ico file
    },
};

export default function RootLayout({children,}: Readonly<{
    children: React.ReactNode;
}>) {
    return (
        <html lang="en">
        <body className="antialiased">{children}</body>
        </html>
    );
}
