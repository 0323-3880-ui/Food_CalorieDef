const API_URL = 
    process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export async function getHealth() {
    const response = await fetch(`${API_URL}/health`);
    
    if (!response.ok) {
        throw new Error("Failed to connect to Backend");
    }

    return response.json();
}