from fastapi import FastAPI
from app.routers import destinations, itineraries, transport, accommodations


app = FastAPI(title= "Travel Bot API", version="1.0.0")


# Routers
app.include_router(destinations.router, prefix="/destinations", tags=["Destinations"])
app.include_router(itineraries.router, prefix="/itineraries", tags=["Itineraries"])
app.include_router(transport.router, prefix="/transport", tags=["Transport"])
app.include_router(accommodations.router, prefix="/accommodations", tags=["Accommodations"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True) 

# http://127.0.0.1:5000 to access API