from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    Float,
    DateTime,
    ForeignKey,
    create_engine,
    update,
)
from sqlalchemy.orm import declarative_base, Session, relationship
import datetime
import bcrypt

Base = declarative_base()


class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    email_notifications = Column(Boolean, nullable=False)
    admin = Column(Boolean, default=False)
    active = Column(Boolean, default=True)


class Transaction(Base):
    __tablename__ = "Transactions"
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    amount = Column(Float, nullable=False)
    description = Column(String)
    market = Column(Integer, ForeignKey("Markets.id"))
    market_name = relationship("Market", back_populates="transactions_markets")
    transaction_type = Column(
        String, ForeignKey("Transaction_types.id"), nullable=False
    )
    type = relationship("TransactionType", back_populates="transactions_types")
    transaction_category = Column(String, ForeignKey("Categories.id"), nullable=False)
    category = relationship("Category", back_populates="transactions_categories")
    card = Column(Integer, ForeignKey("Bank_cards.id"), nullable=False)
    bank_card = relationship("BankCard", back_populates="transactions_cards")


class Market(Base):
    __tablename__ = "Markets"
    id = Column(Integer, primary_key=True)
    market_name = Column(String, nullable=False)
    transactions_markets = relationship("Transaction", back_populates="market_name")


class BankCard(Base):
    __tablename__ = "Bank_cards"
    id = Column(Integer, primary_key=True)
    bank = Column(String, ForeignKey("Banks.id"), nullable=False)
    banks = relationship("Bank", back_populates="card_bank")
    name = Column(String, nullable=False)
    transactions_cards = relationship("Transaction", back_populates="bank_card")


class Bank(Base):
    __tablename__ = "Banks"
    id = Column(Integer, primary_key=True)
    bank_name = Column(String, nullable=False, unique=True)
    card_bank = relationship("BankCard", back_populates="banks")


class Category(Base):
    __tablename__ = "Categories"
    id = Column(Integer, primary_key=True)
    category_hr = Column(String)
    category_en = Column(String)
    category_de = Column(String)
    transactions_categories = relationship("Transaction", back_populates="category")


class TransactionType(Base):
    __tablename__ = "Transaction_types"
    id = Column(Integer, primary_key=True)
    type_hr = Column(String, nullable=False)
    type_en = Column(String, nullable=False)
    type_de = Column(String, nullable=False)
    transactions_types = relationship("Transaction", back_populates="type")


db_engine = create_engine("sqlite:///Database/BudgetApp.db")
Base.metadata.create_all(db_engine)


# USERS FUNCTIONS
# Add user
def db_add_user(
    first_name, last_name, username, password, email, email_notifications, admin, active
):
    with Session(bind=db_engine) as session:
        user_exists = (
            session.query(User)
            .filter(User.username == username or User.email == email)
            .one_or_none()
        )

        if user_exists:
            return user_exists
        else:
            bytepassword = password.encode("utf-8")
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(bytepassword, salt)
            user = User(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=hashed,
                email=email,
                email_notifications=email_notifications,
                admin=admin,
                active=active,
            )
        session.add(user)
        session.commit()


# Delete user
def db_delete_user(username, password, email):
    with Session(bind=db_engine) as session:
        pass


# Update user
def db_update_user(
    first_name, last_name, username, password, email, email_notifications, admin, active
):
    with Session(bind=db_engine) as session:
        pass


# Get all users

# Check user for login
