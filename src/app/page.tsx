"use client";

import Image from "next/image";
import { useEffect, useState } from "react";

export default function Home() {
    const [timeLeft, setTimeLeft] = useState("");

    useEffect(() => {
        // todo: variableize this date
        const targetDate = new Date("2025-05-14T09:15:00Z"); // Change this as needed

        const updateCountdown = () => {
            const now = new Date();
            const diff = targetDate.getTime() - now.getTime();

            if (diff <= 0) {
                setTimeLeft("Event has started!");
                return;
            }

            const days = Math.floor(diff / (1000 * 60 * 60 * 24));
            const hours = Math.floor((diff / (1000 * 60 * 60)) % 24);
            const minutes = Math.floor((diff / (1000 * 60)) % 60);
            const seconds = Math.floor((diff / 1000) % 60);

            setTimeLeft(
                `${days}d ${hours}h ${minutes}m ${seconds}s`
            );
        };

        updateCountdown(); // initial run
        const interval = setInterval(updateCountdown, 1000);
        return () => clearInterval(interval);
    }, []);

    return (
        <main>
            <section className="relative w-full h-[500px]">
                {/* Background Image */}
                <Image
                    src="/images/ea.png"
                    alt="Energy Academy Europe"
                    fill
                    className="object-cover z-0"
                />

                {/* White Card with content */}
                <div className="absolute top-1/2 left-1/2 z-20 -translate-x-1/2 -translate-y-1/2 w-4/5 max-w-4xl bg-white rounded-2xl shadow-lg h-[240px] flex flex-col items-center justify-center text-center px-6">
                    {/* Inner Logo */}
                    <Image
                        src="/logos/careerday_wide.svg"
                        alt="Career Day"
                        width={600}
                        height={200}
                        className="mb-4"
                    />
                    <p className="text-black font-semibold text-3xl">14 May 2025 • Energy Academy Europe </p>
                    <div className="text-2xl font-mono text-red-700">{timeLeft}</div>
                </div>
            </section>
        </main>
    );
}
