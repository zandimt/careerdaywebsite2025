// flake8: noqa
"use client";

import { useEffect, useState } from "react";

interface TimeSlot {
    id: string;
    start_time: string;
    end_time: string;
}

interface Organisation {
    name: string;
}

interface Session {
    id: string;
    title: string;
    location: string;
    time_slot: string;
    organisation?: Organisation;
    start_time: string;
    end_time: string;
}

interface PositionedSession extends Session {
    top: number;
    height: number;
    column: number;
    totalColumns: number;
}

export default function SchedulePage() {
    const [sessions, setSessions] = useState<Session[]>([]);

    const timeToMinutes = (time: string): number => {
        const [h, m] = time.split(":").map(Number);
        return h * 60 + m;
    };

    const overlap = (a: Session, b: Session) => {
        const aStart = timeToMinutes(a.start_time);
        const aEnd = timeToMinutes(a.end_time);
        const bStart = timeToMinutes(b.start_time);
        const bEnd = timeToMinutes(b.end_time);
        return aStart < bEnd && bStart < aEnd;
    };

    const gradientStops = [
        { stop: 0, color: "#FFADAD" },
        { stop: 0.14, color: "#FFD6A5" },
        { stop: 0.29, color: "#FDFFB6" },
        { stop: 0.43, color: "#CAFFBF" },
        { stop: 0.57, color: "#9BF6FF" },
        { stop: 0.71, color: "#A0C4FF" },
        { stop: 0.86, color: "#BDB2FF" },
        { stop: 1.0, color: "#FFC6FF" },
    ];

    const interpolateColor = (a: string, b: string, t: number) => {
        const hexToRgb = (hex: string) => hex.match(/\w\w/g)!.map(x => parseInt(x, 16));
        const rgbToHex = (r: number, g: number, b: number) =>
            "#" + [r, g, b].map(v => Math.round(v).toString(16).padStart(2, "0")).join("");

        const [ar, ag, ab] = hexToRgb(a);
        const [br, bg, bb] = hexToRgb(b);

        return rgbToHex(
            ar + (br - ar) * t,
            ag + (bg - ag) * t,
            ab + (bb - ab) * t
        );
    };

    const getGradientColor = (top: number, totalHeight: number) => {
        const ratio = top / totalHeight;

        for (let i = 0; i < gradientStops.length - 1; i++) {
            const current = gradientStops[i];
            const next = gradientStops[i + 1];

            if (ratio >= current.stop && ratio <= next.stop) {
                const rel = (ratio - current.stop) / (next.stop - current.stop);
                return interpolateColor(current.color, next.color, rel);
            }
        }
        return gradientStops[gradientStops.length - 1].color;
    };

    useEffect(() => {
        const fetchData = async () => {
            const slotRes = await fetch("/api/timeslots/");
            const sessionRes = await fetch("/api/sessions/");

            const slots = (await slotRes.json()).timeslots;
            const rawSessions = (await sessionRes.json()).sessions;

            const timeSlotMap = Object.fromEntries(slots.map((s: TimeSlot) => [s.id, s]));

            const enrichedSessions = rawSessions.map((s: any) => ({
                ...s,
                start_time: timeSlotMap[s.time_slot]?.start_time || "00:00:00",
                end_time: timeSlotMap[s.time_slot]?.end_time || "00:00:00",
            }));

            setSessions(enrichedSessions);
        };

        fetchData();
    }, []);

    const pixelsPerMinute = 2;

    const allTimes = sessions.flatMap((s) => [s.start_time, s.end_time]);
    const startMinutes = Math.min(...allTimes.map(timeToMinutes));
    const endMinutes = Math.max(...allTimes.map(timeToMinutes));
    const totalHeight = (endMinutes - startMinutes) * pixelsPerMinute;

    const getTop = (time: string) => (timeToMinutes(time) - startMinutes) * pixelsPerMinute;
    const getHeight = (start: string, end: string) =>
        (timeToMinutes(end) - timeToMinutes(start)) * pixelsPerMinute;

    const positionedSessions: PositionedSession[] = [];
    const sorted = [...sessions].sort((a, b) => timeToMinutes(a.start_time) - timeToMinutes(b.start_time));

    for (const session of sorted) {
        const top = getTop(session.start_time);
        const height = getHeight(session.start_time, session.end_time);

        const overlapping = positionedSessions.filter((s) =>
            overlap(s, session)
        );

        const usedColumns = new Set(overlapping.map((s) => s.column));
        let column = 0;
        while (usedColumns.has(column)) column++;

        const totalColumns = Math.max(column + 1, ...overlapping.map((s) => s.totalColumns || 1));

        for (const s of overlapping) {
            s.totalColumns = totalColumns;
        }

        positionedSessions.push({ ...session, top, height, column, totalColumns });
    }

    const timeLabels: string[] = [];
    for (let i = startMinutes; i <= endMinutes; i += 60) {
        const hours = Math.floor(i / 60).toString().padStart(2, "0");
        timeLabels.push(`${hours}:00`);
    }

    return (
        <main className="p-6 max-w-[1200px] mx-auto">
            <h1 className="text-3xl font-bold mb-6 text-center">Schedule</h1>

            <div className="grid grid-cols-[80px_1fr] gap-2">
                <div className="relative text-right text-xs pr-2">
                    {timeLabels.map((label) => (
                        <div
                            key={label}
                            className="h-[120px] border-b border-gray-200 pt-1 text-gray-500"
                        >
                            {label}
                        </div>
                    ))}
                </div>

                <div className="relative border-l border-gray-300" style={{ height: totalHeight }}>
                    {positionedSessions.map((s) => {
                        const widthPercent = 100 / s.totalColumns;

                        let colSpan = 1;
                        for (let i = s.column + 1; i < s.totalColumns; i++) {
                            const blocked = positionedSessions.some((other) =>
                                other.column === i &&
                                other !== s &&
                                overlap(s, other)
                            );
                            if (blocked) break;
                            colSpan++;
                        }

                        return (
                            <div
                                key={s.id}
                                className="absolute text-black text-xs px-4 py-2 rounded shadow flex flex-col items-center justify-center text-center"
                                style={{
                                    top: `${s.top}px`,
                                    height: `${s.height}px`,
                                    left: `${s.column * widthPercent}%`,
                                    width: `${widthPercent * colSpan}%`,
                                    backgroundColor: getGradientColor(s.top, totalHeight),
                                }}
                            >
                                <div className="font-semibold text-sm">{s.title}</div>
                                {s.organisation?.name && (
                                    <div className="text-[11px]">{s.organisation.name}</div>
                                )}
                                <div className="text-[10px]">{s.location}</div>
                            </div>
                        );
                    })}
                </div>
            </div>
        </main>
    );
}
