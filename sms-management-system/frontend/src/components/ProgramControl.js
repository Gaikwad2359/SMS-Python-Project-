import React from 'react';
import axios from 'axios';

const ProgramControl = () => {
    const handleStart = async () => {
        await axios.post('/api/start'); // Adjust the endpoint accordingly
    };

    const handleStop = async () => {
        await axios.post('/api/stop'); // Adjust the endpoint accordingly
    };

    const handleRestart = async () => {
        await axios.post('/api/restart'); // Adjust the endpoint accordingly
    };

    return (
        <div>
            <h2>Program Control</h2>
            <button onClick={handleStart}>Start</button>
            <button onClick={handleStop}>Stop</button>
            <button onClick={handleRestart}>Restart</button>
        </div>
    );
};

export default ProgramControl;
