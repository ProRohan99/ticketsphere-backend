# TicketSphere 🎟️

TicketSphere is a **Django REST API based event ticket booking system** that allows users to browse events, book tickets, and manage payments.
The project demonstrates backend architecture for a scalable ticketing platform.

---

## 🚀 Features

* Event management system
* Ticket booking functionality
* Seat availability tracking
* Overbooking prevention
* Payment record management
* Event filtering by location/category
* Django Admin management
* RESTful API architecture

---

## 🏗️ Backend Architecture

The backend is built using:

* Python
* Django
* Django REST Framework
* SQLite (development database)

Architecture flow:

User Request → API Endpoint → Serializer → Model → Database → Response

---

## 📂 Project Structure

```
ticketsphere/
│
├── core/                 # Django project settings
│
├── events/               # Event management
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── bookings/             # Ticket booking system
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── payments/             # Payment records
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── manage.py
└── requirements.txt
```

---

## 📡 API Endpoints

### Events

GET all events

```
GET /api/events/
```

Create event

```
POST /api/events/
```

Filter events

```
GET /api/events/?location=Bangalore
```

---

### Bookings

Create booking

```
POST /api/bookings/
```

Get bookings

```
GET /api/bookings/
```

---

### Payments

Create payment

```
POST /api/payments/
```

Get payments

```
GET /api/payments/
```

---

## 🎫 Booking Logic

When a user books tickets:

1. System checks seat availability
2. Prevents overbooking
3. Deducts booked seats from event
4. Creates booking record

Example:

```
Event seats: 500
User books: 2
Remaining seats: 498
```

---

## 🧪 Testing APIs

You can test APIs using:

* Postman
* Thunder Client
* Django REST Framework browser interface

Example API:

```
http://127.0.0.1:8000/api/events/
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/yourusername/ticketsphere-backend.git
```

Navigate to project:

```
cd ticketsphere-backend
```

Create virtual environment:

```
python -m venv venv
```

Activate environment:

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Run migrations:

```
python manage.py migrate
```

Create superuser:

```
python manage.py createsuperuser
```

Run server:

```
python manage.py runserver
```

---

## 🔑 Admin Panel

Access Django admin:

```
http://127.0.0.1:8000/admin
```

Admin can:

* create events
* manage bookings
* track payments

---

## 📈 Future Improvements

* JWT Authentication
* Payment gateway integration
* Email ticket confirmation
* Seat locking mechanism
* Analytics dashboard
* React frontend integration

---

## 👨‍💻 Author

Developed as a backend system for an event ticketing platform using Django REST Framework.
