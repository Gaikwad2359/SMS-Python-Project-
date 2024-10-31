import React, { useState } from 'react';
import axios from 'axios';

const Login = () => {
    const [credentials, setCredentials] = useState({ username: '', password: '' });

    const handleLogin = async () => {
        try {
            const response = await axios.post('/api/login', credentials); // Adjust the endpoint accordingly
            console.log(response.data); // Handle successful login
        } catch (error) {
            console.error("Login failed", error); // Handle login failure
        }
    };

    return (
        <div>
            <h2>Login</h2>
            <input 
                type="text" 
                placeholder="Username" 
                value={credentials.username} 
                onChange={(e) => setCredentials({ ...credentials, username: e.target.value })} 
            />
            <input 
                type="password" 
                placeholder="Password" 
                value={credentials.password} 
                onChange={(e) => setCredentials({ ...credentials, password: e.target.value })} 
            />
            <button onClick={handleLogin}>Login</button>
        </div>
    );
};

export default Login;
