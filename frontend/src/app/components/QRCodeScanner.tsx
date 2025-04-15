'use client';

import { Html5Qrcode } from 'html5-qrcode';
import { useEffect, useRef, useState } from 'react';

export default function QrCheckIn() {
    const scannerRef = useRef<HTMLDivElement>(null);
    const [status, setStatus] = useState<string | null>(null);
    const html5QrCodeRef = useRef<Html5Qrcode | null>(null);

    useEffect(() => {
        const init = async () => {
            try {
                const cameraPermissions = await navigator.mediaDevices.getUserMedia({ video: true });
                const cameras = await Html5Qrcode.getCameras();

                if (!cameras.length) {
                    setStatus('No camera found');
                    return;
                }

                const scanner = new Html5Qrcode('qr-scanner');
                html5QrCodeRef.current = scanner;

                await scanner.start(
                    { deviceId: cameras[0].id },
                    {
                        fps: 10,
                        qrbox: { width: 250, height: 250 },
                    },
                    async (decodedText) => {
                        await scanner.stop();
                        setStatus(`✅ Checked in: ${decodedText}`);
                        await handleCheckIn(decodedText);
                    },
                    (error) => console.warn('Scan error', error)
                );
            } catch (err) {
                console.error(err);
                setStatus('❌ Please allow camera access.');
            }
        };

        init();

        return () => {
            html5QrCodeRef.current?.stop().catch(() => {});
        };
    }, []);

    const handleCheckIn = async (participantId: string) => {
        try {
            const BACKEND_URL = "http://localhost:8001"; // adjust if different

            const res = await fetch(`${BACKEND_URL}/api/participants/${participantId}/check_in/`, {
                method: "POST",
            });


            if (!res.ok) {
                const errorText = await res.text(); // Log backend response body
                console.error('❌ Check-in failed:', res.status, errorText);
            }

            const data = await res.json();
            setStatus(`✅ Checked in: ${data.participant}`);
        } catch (err) {
            console.error(err);
            setStatus('❌ Invalid or already checked in');
        }
    };

    return (
        <div className="flex flex-col items-center p-4">
            <h2 className="text-xl font-bold mb-2">Scan QR Code</h2>
            <div
                id="qr-scanner"
                ref={scannerRef}
                className="w-full max-w-md h-[300px] border border-gray-300 rounded"
            />
            {status && <p className="mt-4">{status}</p>}
        </div>
    );
}
