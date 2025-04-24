"use client";

import { useEffect, useState } from "react";
import PartnerInformation from "./PartnerInformation"; // import this



type Organisation = {
    id: string;
    name: string;
    logo: string;
    partner_type: string[]; // now an array of strings
    website?: string;
};

function formatType(type: string): string {
    return type
        .toLowerCase()
        .split("_")
        .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
        .join(" ");
}

export default function Partners() {
    const [grouped, setGrouped] = useState<Record<string, Organisation[]>>({});
    const [selectedPartner, setSelectedPartner] = useState<Organisation | null>(null);

    useEffect(() => {
        const fetchOrganisations = async () => {
            const res = await fetch("/api/organisations/", {
                method: "GET",
                credentials: "include",
            });
            const data = await res.json();
            const orgs: Organisation[] = data.organisations;

            const groupedByType: Record<string, Organisation[]> = {};

            for (const org of orgs) {
                for (const type of org.partner_type) {
                    if (!groupedByType[type]) groupedByType[type] = [];
                    groupedByType[type].push(org);
                }
            }

            setGrouped(groupedByType);
        };

        fetchOrganisations();
    }, []);

    return (
        <section className="p-6 bg-gray-200 text-black text-center">
            <h2 className="text-3xl font-bold mb-6">Partners</h2>

            {Object.entries(grouped).map(([type, orgs]) => (
                <div key={type} className="mb-12">
                    <h3 className="text-2xl font-semibold mb-4">{formatType(type)}</h3>
                    <div className="flex flex-wrap justify-center gap-6">
                        {orgs.map((org) => (
                            <button
                                key={org.id} // ✅ unique key here
                                onClick={() => setSelectedPartner(org)}
                                className="flex items-center justify-center w-48 h-28 bg-white rounded-xl shadow hover:shadow-lg transition p-4"
                            >
                                <img
                                    src={org.logo}
                                    alt={org.name}
                                    className="max-h-full max-w-full object-contain"
                                />
                            </button>
                        ))}
                    </div>
                </div>
            ))}
            {selectedPartner && (
                <PartnerInformation
                    partner={selectedPartner}
                    onClose={() => setSelectedPartner(null)}
                />
            )}
        </section>
    );
}
