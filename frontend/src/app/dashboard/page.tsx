// app/dashboard/page.tsx or pages/dashboard.tsx
'use client'

import React, { useState } from 'react'

export default function DashboardPage() {
    const [formData, setFormData] = useState({
        firstName: '',
        prepositionName: '',
        lastName: '',
        email: '',
        phone: '',
        studyPhase: '',
        study: '',
        studyYear: '',
        url: '',
        dietary: '',
    })

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value,
        })
    }

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault()

        try {
            const response = await fetch('http://localhost:8001/api/participants/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Bearer ${localStorage.getItem('token') || ''}`,
                },
                body: JSON.stringify({
                    first_name: formData.firstName,
                    preposition_name: formData.prepositionName,
                    last_name: formData.lastName,
                    email_address: formData.email,
                    phone_number: formData.phone,
                    study_phase: formData.studyPhase,
                    study: formData.study,
                    study_year: formData.studyYear,
                    url: formData.url,
                    dietary_requirements: formData.dietary,
                }),
            })

            if (!response.ok) throw new Error(`Server error: ${response.status}`)

            const result = await response.json()
            console.log('Participant created:', result)
            alert('Participant successfully registered.')
        } catch (error) {
            console.error('Submission failed:', error)
            alert('Submission failed. See console for details.')
        }
    }

    return (
        <div className="max-w-3xl mx-auto p-6">
            <div className="text-center mb-8">
                <h1 className="text-3xl font-bold mb-4">Dashboard</h1>
                <button
                    onClick={() => alert('Cover setup flow not implemented')}
                    className="bg-blue-600 hover:bg-blue-700 text-white font-semibold px-4 py-2 rounded-md"
                >
                    Set up with Cover
                </button>
            </div>

            <form onSubmit={handleSubmit} className="bg-white shadow-md rounded-lg p-6 space-y-6">
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                    {[
                        { name: 'firstName', label: 'First name', required: true },
                        { name: 'prepositionName', label: 'Preposition name', required: false },
                        { name: 'lastName', label: 'Last name', required: true },
                        { name: 'email', label: 'Email address', required: true },
                        { name: 'phone', label: 'Phone number', required: true },
                        { name: 'study', label: 'Study', required: true },
                        { name: 'studyPhase', label: 'Study Phase', required: true },
                        { name: 'studyYear', label: 'Study Year', required: true },
                        { name: 'url', label: 'URL', required: false },
                        { name: 'dietary', label: 'Dietary requirements', required: false },
                    ].map(({ name, label, required }) => (
                        <div key={name}>
                            <label htmlFor={name} className="block font-medium text-gray-700 mb-1">
                                {label} {required && <span className="text-red-500">*</span>}
                            </label>
                            <input
                                id={name}
                                name={name}
                                type="text"
                                required={required}
                                value={(formData as any)[name]}
                                onChange={handleChange}
                                className="w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 text-black"                            />
                        </div>
                    ))}
                </div>

                <div className="text-center">
                    <button
                        type="submit"
                        className="bg-green-600 hover:bg-green-700 text-white font-semibold px-6 py-2 rounded-md"
                    >
                        Submit
                    </button>
                </div>
            </form>
        </div>
    )
}
