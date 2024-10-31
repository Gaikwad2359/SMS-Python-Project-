import React, { useEffect, useState } from 'react';
import axios from 'axios';

const CountryOperator = () => {
    const [pairs, setPairs] = useState([]);
    const [newPair, setNewPair] = useState({ country: '', operator: '' });

    const fetchPairs = async () => {
        const response = await axios.get('/api/country-operators'); // Adjust the endpoint accordingly
        setPairs(response.data);
    };

    const handleAddPair = async () => {
        await axios.post('/api/country-operators', newPair); // Adjust the endpoint accordingly
        fetchPairs(); // Refresh the list
    };

    useEffect(() => {
        fetchPairs();
    }, []);

    return (
        <div>
            <h2>Country Operator Management</h2>
            <ul>
                {pairs.map((pair, index) => (
                    <li key={index}>{pair.country} - {pair.operator}</li>
                ))}
            </ul>
            <input 
                type="text" 
                placeholder="Country" 
                value={newPair.country} 
                onChange={(e) => setNewPair({ ...newPair, country: e.target.value })} 
            />
            <input 
                type="text" 
                placeholder="Operator" 
                value={newPair.operator} 
                onChange={(e) => setNewPair({ ...newPair, operator: e.target.value })} 
            />
            <button onClick={handleAddPair}>Add Pair</button>
        </div>
    );
};

export default CountryOperator;
