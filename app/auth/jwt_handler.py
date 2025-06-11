# """
# This file is responsible for signing, encoding, decoding and returning JWTs

# """
# import logging
# import jwt
# from app.config import SECRET_KEY, ALGORITHM
# from app.models.schemas import CreateUserRequest
# from app.core.database import get_db
# from sqlalchemy.orm import Session
# from app.models.schemas import UserDB, CreateUserRequest

# logger = logging.getLogger(__name__)
# def signJWT(user: CreateUserRequest):
#     payload = {
#         "userID": user.user_id,
#         "role": user.role
#     }
#     token= jwt.encode(payload, SECRET_KEY, algorithm= ALGORITHM)
#     return {"access_token": token, "token_type": "bearer"}

# def decodeJWT(token: str):
#     try:
#         decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         return decoded_token if decoded_token["userID"] else None
#     except jwt.JWTError:
#         return None

# def verify_user(user: CreateUserRequest, db: Session):
#     try: 
#         user = db.query(UserDB).filter(UserDB.user_id == user.user_id).first()
#         if user:
#             logger.info(f"User '{user.user_id}' retrieved from the database")
#             return True
#         else:
#             return False
#     except Exception as e:
#         logger.error(f"Error retrieving user '{user.user_id}': {e}")
#         return False
