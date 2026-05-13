# System Architecture – Gym Management System

## 1. Overview
The Gym Management System follows a modular architecture to ensure maintainability, scalability, and clear separation of responsibilities.

---

## 2. Architectural Style
The system uses a **modular layered architecture**:

### **Layer 1: Data Layer**
- Stores member, trainer, and class information
- Future expansion: database integration

### **Layer 2: Business Logic Layer**
- Member class
- Trainer class
- ClassSchedule class
- Handles check-ins, enrollment, and assignments

### **Layer 3: Application Layer**
- main.py orchestrates system behavior
- Provides a simple CLI demonstration

---

## 3. Module Breakdown

### **Member Module**
- Handles member data
- Validates membership status
- Provides check-in functionality

### **Trainer Module**
- Stores trainer information
- Assigns trainers to classes

### **ClassSchedule Module**
- Manages class capacity
- Enrolls members
- Tracks trainer assignments

---

## 4. Data Flow
1. User interacts with main.py  
2. main.py calls business logic modules  
3. Modules process data and return results  
4. Output displayed to user  

---

## 5. Future Architecture Enhancements
- REST API layer
- Database integration (PostgreSQL)
- Web UI or mobile app
