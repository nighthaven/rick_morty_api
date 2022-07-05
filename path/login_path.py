from unittest import result
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from models.login_models import TokenData
from dal.connexion_helper import get_connection
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from jose import JWTError, jwt

from models.users_models import User



path=APIRouter()

SECRET_KEY = "1509a7470d85add7310f2596b0fb454fef7e35d1cd92a700daaee0805580bd5d"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1440

pwd_context = CryptContext(schemes = ["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def generate_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt =jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@path.post("/login",status_code = status.HTTP_201_CREATED)
def login(request: OAuth2PasswordRequestForm = Depends()):
    connection = get_connection()
    cursor = connection.cursor()
    find_user = "SELECT * FROM users WHERE user_name = '%s';" % (request.username)
    cursor.execute(find_user)
    data_userlogin = cursor.fetchall()
    data_userlogin[0][3]
    if not data_userlogin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="utilisateur incorrecte")
    if data_userlogin[0][3] != request.password :
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="mauvais mot de passe")
    access_token = generate_token(
        data={"sub":data_userlogin[0][1]}
    )
    return {"access_token":access_token, "token_type": "bearer"}

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    connection = get_connection()
    cursor = connection.cursor()
    user_query = "SELECT * from users WHERE user_name = '%s'" % (token_data.username)
    cursor.execute(user_query)
    results = cursor.fetchall()
    user = User(user_id= results[0][0],user_name= results[0][1],user_type=results[0][2], user_password=results[0][3])
    if user is None:
        raise credentials_exception
    return user

# 1er etape ( faite ) : creer la table d'utilisateur, et permettre d'ajouter des utilisateurs
# permettre de verifier dans la fonction login que l'utilisateur et le mot de passe corresponde
# ou rejeter si non 
# creer un token qui retiens le bordel
# creer token  

# trouve l'utilisateur qui correspond a username  
#    si le mot de passe entré dans login/mot de passe correspond a ce meme utilisateur
#    alors open sesame
# SINON
# va te faire voila 
