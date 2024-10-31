import axios from 'axios';

const api = axios.create({
    baseURL: 'http://127.0.0.1:8000/api', // Adjust to your backend API base URL
    timeout: 1000,
});

// Add any additional custom configurations or interceptors if needed

export default api;
