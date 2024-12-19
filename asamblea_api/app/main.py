from fastapi import FastAPI

from app.api.routes import users, auth, sse, assembly, coproperties, notification, units, votations
from app.core.database import Base, engine

app = FastAPI()


app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(sse.router, prefix="/mistral", tags=["Mistral"])
app.include_router(assembly.router, prefix="/assembly", tags=["Assemblies"])
app.include_router(coproperties.router, prefix="/coproperties", tags=["Coproperties"])
app.include_router(notification.router, prefix="/notification", tags=["Notifications"])
app.include_router(units.router, prefix="/units", tags=["Units"])
app.include_router(votations.router, prefix="/votations", tags=["Votations"])


#Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
