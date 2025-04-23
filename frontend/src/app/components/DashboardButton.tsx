"use client";

import { useEffect, useState } from "react";
import Link from "next/link";

const DashboardButton = () => {
    const [hasSession, setHasSession] = useState<boolean | null>(null);

    useEffect(() => {
        if (typeof window === "undefined") return; // ⛔ Don't run server-side

        const checkSession = async () => {
            try {
                const res = await fetch("/api/svcover", {
                    method: "GET",
                    credentials: "include",
                });
                setHasSession(res.status === 200);
            } catch {
                setHasSession(false);
            }
        };

        checkSession();
    }, []);

    if (hasSession === null) return null;

    return (
        <li>
            {hasSession ? (
                <Link href="/dashboard" className="text-white">
                    <img
                        width="32"
                        height="32"
                        src="https://img.icons8.com/windows/32/user.png"
                        alt="user"
                    />
                </Link>
            ) : (
                // TODO: Might be better to do a referer to the login page
                <a
                    href="https://svcover.nl/login"
                    className="text-white px-4 py-2 border rounded"
                >
                    Log In
                </a>
            )}
        </li>
    );
};

export default DashboardButton;
