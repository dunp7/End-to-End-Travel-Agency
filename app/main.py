from fastapi import FastAPI
from app.routers import destinations, itineraries, transports, accomodations


app = FastAPI(title= "Travel Bot API", version="1.0.0")


# Routers
app.include_router(destinations.router, prefix="/destinations", tags=["Destinations"])
app.include_router(itineraries.router, prefix="/itineraries", tags=["Itineraries"])
app.include_router(transports.router, prefix="/transports", tags=["Transport"])
app.include_router(accomodations.router, prefix="/accommodations", tags=["Accommodations"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=9999, reload=True) 

# http://127.0.0.1:9999 to access API