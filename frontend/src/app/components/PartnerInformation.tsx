"use client";

import { useEffect } from "react";

type Partner = {
    id: string;
    name: string;
    logo: string;
    description?: string;
    tagline?: string;
    website?: string;
};

type PartnerModalProps = {
    partner: Partner;
    onClose: () => void;
};

export default function PartnerInformation({ partner, onClose }: PartnerModalProps) {
    useEffect(() => {
        const handleEsc = (e: KeyboardEvent) => {
            if (e.key === "Escape") onClose();
        };
        document.addEventListener("keydown", handleEsc);
        return () => document.removeEventListener("keydown", handleEsc);
    }, [onClose]);

    return (
        <div className="fixed inset-0 z-50 bg-black bg-opacity-50 flex items-center justify-center px-4 sm:px-6">
            <div
                className="relative bg-white rounded-xl p-6 w-full max-w-md max-h-[90vh] overflow-y-auto shadow-xl text-center"
                role="dialog"
                aria-modal="true"
                aria-labelledby="partner-name"
                onClick={(e) => e.stopPropagation()}
            >
                {/* Close Button */}
                <button
                    onClick={onClose}
                    className="absolute top-3 right-4 text-2xl font-semibold text-gray-400 hover:text-black"
                >
                    ×
                </button>

                {/* Logo */}
                <div className="w-full flex justify-center mb-4">
                    <img
                        src={partner.logo}
                        alt={partner.name}
                        className="h-20 sm:h-24 object-contain"
                    />
                </div>

                {/* Name */}
                <h2 id="partner-name" className="text-xl sm:text-2xl font-bold mb-2">
                    {partner.name}
                </h2>

                {/* Tagline and Description */}
                {partner.tagline && (
                    <p className="text-sm text-gray-500 italic mb-1">{partner.tagline}</p>
                )}
                {partner.description && (
                    <p className="text-sm text-gray-700 mb-4">{partner.description}</p>
                )}

                {/* Website Button */}
                {partner.website && (
                    <div className="mt-4">
                        <a
                            href={partner.website}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="inline-flex items-center gap-2 px-4 py-2 text-sm sm:text-base bg-blue-600 text-white rounded-md hover:bg-blue-700 transition"
                        >
                            Visit Website
                            <svg
                                xmlns="http://www.w3.org/2000/svg"
                                className="w-4 h-4"
                                fill="none"
                                viewBox="0 0 24 24"
                                stroke="currentColor"
                            >
                                <path
                                    strokeLinecap="round"
                                    strokeLinejoin="round"
                                    strokeWidth="2"
                                    d="M14 3h7m0 0v7m0-7L10 14"
                                />
                            </svg>
                        </a>
                    </div>
                )}
            </div>
        </div>
    );
}
