from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer, util

app = FastAPI(title="VibeSpace AI Matching API", version="1.0.0")

# Load a lightweight open-weight embedding model (Runs locally / CPU friendly)
# To this (adding '-v2'):
embedder = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Sample in-memory database of user vibe profiles
USERS_DB = [
    {"id": 1, "name": "Aarav", "bio": "Building low-level Python cybersecurity exploits and security auditing scripts. Passionate about tennis on weekends."},
    {"id": 2, "name": "Meera", "bio": "Creative writer drafting dark fantasy novels on Wattpad. Also loves vibe coding with React and Node.js."},
    {"id": 3, "name": "Kabir", "bio": "Deep learning enthusiast and AI researcher. Enjoys playing tennis and building smart automation agents."}
]

class MatchQuery(BaseModel, extra="allow"):
    query: str

@app.get("/")
def read_root():
    return {"message": "Welcome to VibeSpace AI API. Open-weight matching engine is active."}

@app.post("/api/match")
def find_matching_peers(payload: MatchQuery):
    user_query = payload.query
    
    # Encode user query into a vector
    query_embedding = embedder.encode(user_query, convert_to_tensor=True)
    
    results = []
    for user in USERS_DB:
        # Encode profile bio
        profile_embedding = embedder.encode(user["bio"], convert_to_tensor=True)
        # Compute cosine similarity score
        score = util.cos_sim(query_embedding, profile_embedding).item()
        
        results.append({
            "id": user["id"],
            "name": user["name"],
            "bio": user["bio"],
            "similarity_score": round(score * 100, 2)
        })
        
    # Sort by highest similarity score
    results = sorted(results, key=lambda x: x["similarity_score"], reverse=True)
    
    return {
        "query": user_query,
        "matches": results
    }
