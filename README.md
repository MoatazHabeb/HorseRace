# 🏇 HorseRace API

A production-style Horse Racing & Betting REST API built with **FastAPI**, **SQLAlchemy ORM**, and **JWT Authentication**. The project demonstrates role-based authorization, betting business logic, race management, and wallet transactions.

---

## 🚀 Features

### Authentication
- JWT Authentication
- Secure password hashing with bcrypt
- Login endpoint
- Role-Based Access Control (RBAC)

### Player Management
- Register player
- Update player
- Delete player
- View player profile
- Wallet balance

### Owner Management
- Create owner
- Update owner
- Delete owner
- Get owner details

### Horse Management
- Create horse
- Update horse
- Delete horse
- Horse statistics
- Horse ownership

### Race Track Management
- Create race track
- Update race track
- Delete race track
- View race tracks

### Race Management
- Create race
- Update race
- Delete race
- View races
- Race status management

### Betting System
- Place a bet
- Validate player balance
- Prevent betting on finished races
- Calculate betting profit
- Update player balance

### Race Results
- Finish race
- Save race results
- Select winner
- Update horse wins
- Settle bets
- Calculate winnings automatically

### Wallet Transactions
- BET
- WIN
- DEPOSIT *(Future)*
- WITHDRAW *(Future)*
- REFUND *(Future)*

---

# 🛠 Technologies

- Python 3
- FastAPI
- SQLAlchemy ORM
- SQLite
- JWT (python-jose)
- Passlib (bcrypt)
- Pydantic
- Uvicorn

---

# 📂 Project Structure

```
HorseRace/
│
├── horse/
│   ├── repository/
│   ├── routers/
│   ├── models.py
│   ├── schemas.py
│   ├── oauth.py
│   ├── jwt_handler.py
│   ├── hashing.py
│   └── database.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

# 🔐 Authentication

The API uses **JWT Bearer Token Authentication**.

### Roles

- ADMIN
- PLAYER

Protected endpoints require:

```
Authorization: Bearer <token>
```

---

# 📚 Main APIs

## Authentication

| Method | Endpoint |
|----------|-------------------------|
| POST | /login |

---

## Players

| Method | Endpoint |
|----------|----------------|
| POST | /players |
| GET | /players |
| GET | /players/{id} |
| PUT | /players/{id} |
| DELETE | /players/{id} |

---

## Owners

| Method | Endpoint |
|----------|----------------|
| POST | /owners |
| GET | /owners |
| GET | /owners/{id} |
| PUT | /owners/{id} |
| DELETE | /owners/{id} |

---

## Horses

| Method | Endpoint |
|----------|---------------|
| POST | /horses |
| GET | /horses |
| GET | /horses/{id} |
| PUT | /horses/{id} |
| DELETE | /horses/{id} |

---

## Race Tracks

| Method | Endpoint |
|----------|-------------------|
| POST | /race-tracks |
| GET | /race-tracks |
| GET | /race-tracks/{id} |
| PUT | /race-tracks/{id} |
| DELETE | /race-tracks/{id} |

---

## Races

| Method | Endpoint |
|----------|----------------|
| POST | /races |
| GET | /races |
| GET | /races/{id} |
| PUT | /races/{id} |
| DELETE | /races/{id} |

---

## Bets

| Method | Endpoint |
|----------|----------------|
| POST | /bets |
| GET | /bets |
| GET | /bets/{id} |

---

## Race Results

| Method | Endpoint |
|----------|--------------------------------|
| POST | /race-results/finish/{race_id} |
| GET | /race-results/race/{race_id} |
| GET | /race-results/{id} |

---

## Wallet

| Method | Endpoint |
|----------|----------------|
| GET | /wallet |
| GET | /wallet/all |
| GET | /wallet/{id} |

---

# 💰 Betting Workflow

1. Player logs in.
2. Player places a bet.
3. Player balance is reduced.
4. BET transaction is created.
5. Admin finishes the race.
6. Race results are saved.
7. Winning horse is determined.
8. Winning bets are calculated.
9. Winners receive their profit.
10. WIN transactions are recorded.

---

# ▶️ Run the Project

Clone the repository

```bash
git clone https://github.com/MoatazHabeb/HorseRace.git
```

Navigate to the project

```bash
cd HorseRace
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the server

```bash
uvicorn main:app --reload
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# 🔮 Future Improvements

- Dynamic betting odds
- Deposit & Withdraw APIs
- Email verification
- Refresh Tokens
- Docker support
- PostgreSQL support
- Unit & Integration Tests
- CI/CD Pipeline
- Redis caching
- Admin Dashboard

---

# 👨‍💻 Author

**Moataz Mohamed**

Backend Developer

GitHub: https://github.com/MoatazHabeb
