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
                <div
                    className="absolute top-1/2 left-1/2 z-20 -translate-x-1/2 -translate-y-1/2 w-4/5 max-w-4xl bg-white rounded-2xl shadow-lg h-[240px] flex flex-col items-center justify-center text-center px-6">
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
            <section className="bg-gray-100">
                <div className="grid grid-cols-1 md:grid-cols-2 p-10 gap-4 items-stretch">
                    {/* Text card */}
                    <div className="flex flex-col rounded-2xl bg-white text-black shadow-lg p-6 m-5">
                        <div className="font-bold text-3xl mb-4">About the Cover Career Day</div>
                        <div className="text-base leading-relaxed flex-grow">
                            <p>
                                The Cover Career Day is a day event packed with talks and workshops from
                                AI/CS/CCS-related companies in Groningen and in the Netherlands. Find companies that
                                match your interests and learn more about their work lifestyle, participate in workshops
                                to develop your professional skills, and in the end, join us for networking drinks and
                                talk with recruiters one-on-one.
                            </p>
                            <br/>
                            <p>
                                For those in pursuit of a career or just curious about their opportunities, Cover's
                                Career Day offers you the chance to put your foot in the door and start building your
                                professional network.
                            </p>
                        </div>
                    </div>

                    {/* Image card */}
                    <div className="flex rounded-2xl bg-white shadow-lg p-6 m-5">
                        <img
                            src="/images/careerdaypeoople.jpg"
                            alt="People paying attention to a speaker"
                            className="w-full h-full object-cover rounded-2xl"
                        />
                    </div>
                </div>
            </section>
        </main>
    );
}
