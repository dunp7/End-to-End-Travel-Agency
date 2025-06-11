# """
# to check whether the reques tis authorized or not [ verification of the proteced route]
# """
# from fastapi import Request, HTTPException
# from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

# from app.auth.jwt_handler import decodeJWT


# class JWTBearer(HTTPBearer):
#     def __init__(self, role_required: str = None, auto_error: bool = True):
#         super(JWTBearer, self).__init__(auto_error=auto_error)
#         self.role_required = role_required

#     async def __call__(self, request: Request):
#         credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
#         if credentials:
#             if not credentials.scheme == "Bearer":
#                 raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
#             payload = self.verify_jwt(credentials.credentials)
#             if not payload:
#                 raise HTTPException(status_code=403, detail="Invalid token or expired token.")
#             if self.role_required and payload.get("role") != self.role_required:
#                 raise HTTPException(status_code=403, detail="Not authorized.")
#             return payload
#         else:
#             raise HTTPException(status_code=403, detail="Invalid authorization code.")

#     def verify_jwt(self, jwtoken: str) -> dict:
#         try:
#             payload = decodeJWT(jwtoken)
#             return payload
#         except:
#             return None