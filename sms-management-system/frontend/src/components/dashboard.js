import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Dashboard = () => {
    const [metrics, setMetrics] = useState({});

    useEffect(() => {
        const fetchMetrics = async () => {
            const response = await axios.get('/api/metrics'); // Adjust the endpoint accordingly
            setMetrics(response.data);
        };
        
        fetchMetrics();
        const interval = setInterval(fetchMetrics, 5000); // Fetch every 5 seconds
        return () => clearInterval(interval);
    }, []);

    return (
        <div>
            <h1>Dashboard</h1>
            <pre>{JSON.stringify(metrics, null, 2)}</pre> {/* Display metrics */}
        </div>
    );
};

export default Dashboard;
