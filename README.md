# 🎟️ TicketSphere Backend API

A scalable Event Ticket Booking Backend built using Django and Django REST Framework.

This project provides REST APIs for managing events, bookings, and payments with authentication and seat management logic.

---

## 🚀 Features

### 🔐 Authentication

* JWT-based authentication
* Secure API access using access tokens

### 🎫 Event Management

* Create, update, delete events
* Filter events by category and location
* Track total and available seats

### 📌 Booking System

* Book tickets for events
* Prevent duplicate bookings per user
* Prevent overbooking
* Automatic seat deduction on booking

### 💳 Payment System

* Record payment details
* Link payments with bookings
* Track payment status

---

## 🛠️ Tech Stack

* Python
* Django
* Django REST Framework
* JWT Authentication
* SQLite

---

## 📂 Project Structure

ticketsphere/
│
├── core/              # Project settings
├── events/            # Event APIs
├── bookings/          # Booking logic
├── payments/          # Payment APIs
├── manage.py
├── requirements.txt
└── README.md

---

## ⚙️ Setup Instructions

### 1. Clone Repository

git clone https://github.com/ProRohan99/ticketsphere-backend.git

cd ticketsphere

---

### 2. Create Virtual Environment

python -m venv venv

Activate:

Windows:
venv\Scripts\activate

---

### 3. Install Dependencies

pip install -r requirements.txt

---

### 4. Apply Migrations

python manage.py migrate

---

### 5. Create Superuser

python manage.py createsuperuser

---

### 6. Run Server

python manage.py runserver

---

## 🔑 Authentication (JWT)

### Get Token

POST /api/token/

Body:

{
"username": "your_username",
"password": "your_password"
}

---

### Use Token in APIs

Add header:

Authorization: Bearer <access_token>

---

## 📡 API Endpoints

### Events

* GET /api/events/
* POST /api/events/

### Bookings

* GET /api/bookings/
* POST /api/bookings/

### Payments

* GET /api/payments/
* POST /api/payments/

---

## 🧪 Sample Booking JSON

{
"user": 1,
"event": 1,
"quantity": 2,
"total_price": 2000,
"status": "confirmed"
}

---

## 🧠 Key Backend Logic

* Seat availability validation before booking
* Duplicate booking prevention
* Automatic seat deduction
* Token-based authentication

---

## 🔮 Future Enhancements

* Payment gateway integration (Stripe/Razorpay)
* Email notifications
* Admin dashboard
* Event analytics
* Frontend integration (React)

---

## 👨‍💻 Author

Rohan Mukherjee

---

## ⭐ Notes

This project is built for learning, backend development practice, and demonstrating API design using Django REST Framework.
