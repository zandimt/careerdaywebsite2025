"use client";
import React, { useState, useEffect } from 'react';
import { CareerDayLogo } from './components/logos';
import Footer from './components/footer/footer';

interface TimeLeft {
  days: number;
  hours: number;
  minutes: number;
  seconds: number;
}

const calculateTimeLeft = (): TimeLeft => {
  const targetDate = new Date('2025-05-14T09:15:00');
  const now = new Date();
  const difference = targetDate.getTime() - now.getTime();

  if (difference > 0) {
    return {
      days: Math.floor(difference / (1000 * 60 * 60 * 24)),
      hours: Math.floor((difference / (1000 * 60 * 60)) % 24),
      minutes: Math.floor((difference / (1000 * 60)) % 60),
      seconds: Math.floor((difference / 1000) % 60),
    };
  } else {
    return { days: 0, hours: 0, minutes: 0, seconds: 0 };
  }
};

const App: React.FC = () => {
  const [timeLeft, setTimeLeft] = useState<TimeLeft>(calculateTimeLeft());

  useEffect(() => {
    const interval = setInterval(() => {
      setTimeLeft(calculateTimeLeft());
    }, 1000);

    return () => clearInterval(interval);
  }, []);

  return (
      <div className="app-container">
        <div className="flex flex-col items-center justify-center flex-grow bg-gray-100 pt-20">
          <CareerDayLogo />
          <h1 className="text-4xl font-bold mb-8 text-gray-600">14 May 2025, Energy Academy</h1>
          <div className="flex space-x-4">
            <div className="flex flex-col items-center bg-white p-6 rounded-lg shadow-lg">
              <span className="text-3xl font-bold text-gray-600">{timeLeft.days}</span>
              <span className="text-gray-600">Days</span>
            </div>
            <div className="flex flex-col items-center bg-white p-6 rounded-lg shadow-lg">
              <span className="text-3xl font-bold text-gray-600">{timeLeft.hours}</span>
              <span className="text-gray-600">Hours</span>
            </div>
            <div className="flex flex-col items-center bg-white p-6 rounded-lg shadow-lg">
              <span className="text-3xl font-bold text-gray-600">{timeLeft.minutes}</span>
              <span className="text-gray-600">Minutes</span>
            </div>
            <div className="flex flex-col items-center bg-white p-6 rounded-lg shadow-lg">
              <span className="text-3xl font-bold text-gray-600">{timeLeft.seconds}</span>
              <span className="text-gray-600">Seconds</span>
            </div>
          </div>
          <h2 className="text-3xl items-center font-bold mb-8 text-gray-600" style={{ padding: '40px' }}>
            <a href="https://www.svcover.nl/events/4695">Register your interest!</a>
          </h2>
        </div>
        <Footer />
      </div>
  );
};

export default App;