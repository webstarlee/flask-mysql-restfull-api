from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, and_, desc, asc, or_, Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

db = SQLAlchemy()