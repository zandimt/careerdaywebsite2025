// components/Countdown.tsx
"use client";

import { useEffect, useState } from "react";

type CountdownProps = {
    target: string; // ISO string
};

export default function Countdown({ target }: CountdownProps) {
    const [timeLeft, setTimeLeft] = useState("");

    useEffect(() => {
        const targetDate = new Date(target);

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

            setTimeLeft(`${days}d ${hours}h ${minutes}m ${seconds}s`);
        };

        updateCountdown();
        const interval = setInterval(updateCountdown, 1000);
        return () => clearInterval(interval);
    }, [target]);

    return <div className="text-2xl font-mono text-red-700">{timeLeft}</div>;
}
