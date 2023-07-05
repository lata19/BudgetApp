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
    ForeignKeyConstraint,
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
    user_card = relationship("BankCard", back_populates="user_owner")


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
    card = Column(Integer, nullable=False)
    receiving_card = Column(Integer)

    __table_args__ = (
        ForeignKeyConstraint(
            ["card", "receiving_card"], ["Bank_cards.id", "Bank_cards.id"]
        ),
    )
    bank_card = relationship(
        "BankCard",
        foreign_keys="[Transaction.card, Transaction.receiving_card]",
        back_populates="cards",
    )

    # receiving_bank_card = relationship("BankCard", back_populates="transfer_card")
    # bank_card = relationship("BankCard", back_populates="transactions_cards")


class Market(Base):
    __tablename__ = "Markets"
    id = Column(Integer, primary_key=True)
    market_name = Column(String, nullable=False)
    transactions_markets = relationship("Transaction", back_populates="market_name")
    logo = Column(String)


class BankCard(Base):
    __tablename__ = "Bank_cards"
    card_name = Column(String, nullable=False)
    id = Column(Integer, primary_key=True)
    bank = Column(String, ForeignKey("Banks.id"), nullable=False)
    banks = relationship("Bank", back_populates="card_bank")
    cards = relationship("Transaction", back_populates="bank_card")
    owner = Column(Integer, ForeignKey("Users.id"))
    user_owner = relationship("User", back_populates="user_card")
    balance = Column(Float, nullable=False)


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
    """
    Adds a new user to the database
    param first_name: string variable for users first name
    param last_name: string variable for users last name
    param username: string variable for users username
    param password: string variable for users password
    param email: string variable for users email
    param email_notifications: boolean variable in which user decides if he wants to recieve notificatiosn by e-mail
    param admin: boolean variable that sets user as admin or non-admin user
    param active: boolean variable for user account activity
    """
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
            return None


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
def db_get_all_users():
    with Session(bind=db_engine) as session:
        return session.query(User).all()


# Check user for login
def db_check_user_for_login(username, inserted_password):
    with Session(bind=db_engine) as session:
        user = (session.query(User).filter(User.username == username)).one_or_none()
    if user:
        inserted_password = inserted_password.encode("utf-8")
        password = bcrypt.checkpw(inserted_password, user.password)
        if password:
            return user


# Check for username
def db_username_check(username):
    with Session(bind=db_engine) as session:
        username_exists = (
            session.query(User).filter(User.username == username).one_or_none()
        )
        if username_exists:
            return username_exists


# Check email
def db_email_check(email):
    with Session(bind=db_engine) as session:
        email_exists = session.query(User).filter(User.email == email).one_or_none()
        if email_exists:
            return email_exists


# TRANSACTION FUNCTIONS
# Add transaction
def db_add_new_transaction(
    date,
    amount,
    description,
    market,
    transaction_type,
    transaction_category,
    card,
    receiving_card,
):
    with Session(bind=db_engine) as session:
        new_transaction = Transaction(
            date=date,
            amount=amount,
            description=description,
            market=market,
            transaction_type=transaction_type,
            transaction_category=transaction_category,
            card=card,
            receiving_card=receiving_card,
        )
        session.add(new_transaction)
        session.commit()


# Edit transaction
def db_edit_transaction(
    transaction,
    new_date,
    new_amount,
    new_description,
    new_market,
    new_transaction_type,
    new_transaction_category,
    new_card,
    new_receiving_card,
):
    with Session(bind=db_engine) as session:
        transaction = session.query(Transaction).filter(
            Transaction.id == transaction.id
        )
        transaction.update(
            date=new_date,
            amount=new_amount,
            description=new_description,
            market=new_market,
            transaction_type=new_transaction_type,
            transaction_category=new_transaction_category,
            card=new_card,
            receiving_card=new_receiving_card,
        )
        session.commit()


# Delete transaction(s)
def db_delete_transaction(
    transaction,
):
    with Session(bind=db_engine) as session:
        transaction = session.query(Transaction).filter(
            Transaction.id == transaction.id
        )
        transaction.delete()
        session.commit()


# Get transaction(s) by date
def db_get_transactions_by_date(date):
    with Session(bind=db_engine) as session:
        return session.query(Transaction).filter(Transaction.date == date).all()


# Get transaction(s) by amount>
def db_get_transactions_by_amount_greater(amount):
    with Session(bind=db_engine) as session:
        return session.query(Transaction).filter(Transaction.amount > amount).all()


# Get transaction(s) by amount<
def db_get_transactions_by_amount_smaller(amount):
    with Session(bind=db_engine) as session:
        return session.query(Transaction).filter(Transaction.amount < amount).all()


# Get transaction(s) by amount=
def db_get_transactions_by_amount_equal(amount):
    with Session(bind=db_engine) as session:
        return session.query(Transaction).filter(Transaction.amount == amount).all()


# Get transaction(s) by market
def db_get_transactions_by_market(market):
    with Session(bind=db_engine) as session:
        return session.query(Transaction).filter(Transaction.market == market.id).all()


# Get transaction(s) by type
def db_get_transactions_by_type(type):
    with Session(bind=db_engine) as session:
        return session.query(Transaction).filter(Transaction.type == type.id).all()


# Get transaction(s) by category
def db_get_transactions_by_category(category):
    with Session(bind=db_engine) as session:
        return (
            session.query(Transaction).filter(Transaction.category == category.id).all()
        )


# Get transaction(s) by bank card
def db_get_transactions_by_bank_card(bank_card):
    with Session(bind=db_engine) as session:
        return (
            session.query(Transaction)
            .filter(Transaction.bank_card == bank_card.id)
            .all()
        )


# Get all transactions
def db_get_all_transactions():
    with Session(bind=db_engine) as session:
        return session.query(Transaction).order_by(Transaction.id).all()


# MARKETS FUNCTIONS
# Add new market
def db_add_new_market(
    market_name,
):
    with Session(bind=db_engine) as session:
        new_market = Market(
            market_name=market_name,
        )
        session.add(new_market)
        session.commit()


# Edit market
def db_edit_market(
    market,
    new_market_name,
):
    with Session(bind=db_engine) as session:
        market = session.query(Market).filter(Market.market_name == market.market_name)
        market.update(
            market_name=new_market_name,
        )
        session.commit()


# Get all markets
def db_get_all_markets():
    with Session(bind=db_engine) as session:
        return session.query(Market).order_by(Market.id).all()


# Delete market
def db_delete_market(
    market,
):
    with Session(bind=db_engine) as session:
        market = session.query(Market).filter(Market.id == market.id)
        market.delete()
        session.commit()


# BANKS & BANK CARDS FUNCTIONS
# Add new bank card
def db_add_new_bank_card(card_name, bank, owner, balance):
    with Session(bind=db_engine) as session:
        new_bank_card = BankCard(
            card_name=card_name, bank=bank, owner=owner, balance=balance
        )
        session.add(new_bank_card)
        session.commit()


# Edit bank card
def db_edit_bank_card(card, card_name, bank, owner, balance):
    with Session(bind=db_engine) as session:
        bank_card = session.query(BankCard).filter(BankCard.card_name == card.card_name)
        bank_card.update(card_name=card_name, bank=bank, owner=owner, balance=balance)
        session.commit()


# Delete bank card
def db_delete_bank_card(card):
    with Session(bind=db_engine) as session:
        bank_card = session.query(BankCard).filter(BankCard.card_name == card.card_name)
        bank_card.delete()
        session.commit()


# Get all bank cards
def db_get_all_bank_cards():
    with Session(bind=db_engine) as session:
        return session.query(BankCard).order_by(BankCard.id).all()


# Get bank cards by owner
def db_get_bank_cards_by_owner(owner):
    with Session(bind=db_engine) as session:
        return session.query(BankCard).filter(BankCard.owner == owner.id).all()


# Get bank card by bank
def db_get_bank_cards_by_bank(bank):
    with Session(bind=db_engine) as session:
        return session.query(BankCard).filter(BankCard.bank == bank.id).all()


# Add new bank
def db_add_new_bank(bank_name):
    with Session(bind=db_engine) as session:
        new_bank = Bank(bank_name=bank_name)
        session.add(new_bank)
        session.commit()


# Delete bank
def db_delete_bank(bank):
    with Session(bind=db_engine) as session:
        bank = session.query(Bank).filter(Bank.bank_name == bank.bank_name)
        bank.delete()
        session.commit()


# Edit bank
def db_edit_bank(bank, new_bank_name):
    with Session(bind=db_engine) as session:
        bank = session.query(Bank).filter(Bank.bank_name == bank.bank_name)
        bank.update(bank_name=new_bank_name)
        session.commit()


# Get all banks
def db_get_all_banks():
    with Session(bind=db_engine) as session:
        return session.query(Bank).order_by(Bank.id).all()


# CATEGORY FUNCTIONS
# Add category
def db_add_new_category(category_hr, category_en, category_de):
    with Session(bind=db_engine) as session:
        new_category = Category(
            category_hr=category_hr, category_en=category_en, category_de=category_de
        )
        session.add(new_category)
        session.commit()


# Edit categrory
def db_edit_category(category, category_hr, category_en, category_de):
    with Session(bind=db_engine) as session:
        category = session.query(Category).filter(Category.id == category.id)
        category.update(
            category_hr=category_hr, category_en=category_en, category_de=category_de
        )
        session.commit()


# Delete category
def db_delete_category(category):
    with Session(bind=db_engine) as session:
        category = session.query(Category).filter(Category.id == category.id)
        category.delete()
        session.commit()


# Get all categories
def db_get_all_categories():
    with Session(bind=db_engine) as session:
        return session.query(Category).order_by(Category.id).all()


# TRANSACTION TYPES FUNCTIONS
# Add transaction type
def db_add_new_transaction_type(type_hr, type_en, type_de):
    with Session(bind=db_engine) as session:
        new_transaction_type = TransactionType(
            type_hr=type_hr, type_en=type_en, type_de=type_de
        )
        session.add(new_transaction_type)
        session.commit()


# Delete transaction type
def db_delete_transaction_type(type):
    with Session(bind=db_engine) as session:
        transaction_type = session.query(TransactionType).filter(
            TransactionType.id == type.id
        )
        type.delete()
        session.commit()


# Edit transaction type
def db_edit_transaction_type(type, type_hr, type_en, type_de):
    with Session(bind=db_engine) as session:
        transaction_type = session.query(TransactionType).filter(
            TransactionType.id == type.id
        )
        transaction_type.update(type_hr=type_hr, type_en=type_en, type_de=type_de)
        session.commit()


# Get all transaction types
def db_get_all_transaction_types():
    with Session(bind=db_engine) as session:
        return session.query(TransactionType).order_by(TransactionType.id).all()
