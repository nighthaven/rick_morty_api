from passlib.context import CryptContext
from dal.connexion_helper import get_connection
from models.users_models import User

pwd_context = CryptContext(schemes = ["bcrypt"], deprecated="auto")

def create_user(user:User):
    connection = get_connection()
    cursor = connection.cursor()
    creation_user = "INSERT INTO users(user_name, user_type, user_password) VALUES ('%s','%s','%s');" \
    % (user.user_name, user.user_type, user.user_password)
    cursor.execute(creation_user)
    connection.commit()

