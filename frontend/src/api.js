import axios from "axios";

const api = axios.create({
    baseURL: "https://api.darshrawat.com",
});

export default api;