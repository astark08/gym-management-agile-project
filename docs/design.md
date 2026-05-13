# System Design – Gym Management System

## 1. Design Goals
- Clean, maintainable code
- Clear naming conventions
- PEP 8 compliance
- Modular structure for future expansion

---

## 2. Class Design

### **Member Class**
Attributes:
- member_id
- first_name
- last_name
- membership_active

Methods:
- check_in()

### **Trainer Class**
Attributes:
- trainer_id
- name
- specialty

Methods:
- assign_class()

### **ClassSchedule Class**
Attributes:
- class_name
- trainer
- capacity
- enrolled_members

Methods:
- enroll_member()

---

## 3. Interaction Design
Example workflow:
1. Member object created  
2. Trainer assigned to class  
3. Member enrolls in class  
4. System validates capacity  
5. System returns confirmation  

---

## 4. Naming Conventions
- Classes: UpperCamelCase  
- Functions: snake_case  
- Booleans: is_active, has_permission  
- Variables: descriptive names (no single letters)

---

## 5. Documentation Standards
- Google-style docstrings  
- Inline comments explaining *why*, not what  
- Modules include top-level descriptions  

---

## 6. Future Design Enhancements
- Add error handling
- Add logging
- Add database persistence
- Add UI layer
