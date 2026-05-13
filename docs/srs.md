# Software Requirements Specification (SRS)
## Gym Management System

## 1. Introduction
The Gym Management System is designed to streamline daily gym operations including member check-ins, class scheduling, trainer assignments, and administrative oversight. The system supports members, trainers, and gym administrators by providing an organized and efficient workflow.

### 1.1 Purpose
The purpose of this system is to centralize gym operations, reduce manual work, and improve member experience.

### 1.2 Scope
The system includes:
- Member registration and check-in
- Trainer profiles and class assignments
- Class scheduling and enrollment
- Basic reporting for administrators

---

## 2. System Overview
The system provides:
- A way for members to check in
- A way for trainers to manage classes
- A way for admins to oversee gym operations

Primary users:
- Members
- Trainers
- Administrators

---

## 3. Functional Requirements

### **R1 – Member Check-In**
The system must allow active members to check in.

### **R2 – Membership Validation**
The system must block inactive members from checking in.

### **R3 – Class Enrollment**
Members must be able to enroll in classes with available capacity.

### **R4 – Class Capacity Enforcement**
The system must prevent enrollment when a class is full.

### **R5 – Trainer Assignment**
Admins must be able to assign trainers to classes.

---

## 4. Non-Functional Requirements

### **Performance**
- Check-in should process in under 2 seconds.

### **Usability**
- System should be intuitive for non-technical staff.

### **Reliability**
- System should handle multiple check-ins without failure.

### **Maintainability**
- Code should follow PEP 8 and include documentation.

---

## 5. Constraints
- Python-based implementation
- Local or cloud-hosted environment
