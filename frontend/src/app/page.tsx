"use client";

import Image from "next/image";
import { useEffect, useState } from "react";
import Countdown from "./components/Countdown";


export default function Home() {
    const [eventDateStr, setEventDateStr] = useState("");
    const [isoStartTime, setIsoStartTime] = useState("");

    useEffect(() => {
        const fetchEventInfo = async () => {
            const res = await fetch("/api/settings"); // adjust endpoint
            const data = await res.json();

            const localDate = new Date(`${data.EVENT_DATE}T${data.EVENT_START_TIME}`);
            const displayDate = localDate.toLocaleDateString("en-GB", {
                day: "numeric",
                month: "long",
                year: "numeric",
            });

            setEventDateStr(displayDate);
            setIsoStartTime(localDate.toISOString());
        };

        fetchEventInfo();
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
                    <p className="text-black font-semibold text-3xl">{eventDateStr} • Energy Academy Europe </p>
                    <Countdown target={isoStartTime} />
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
