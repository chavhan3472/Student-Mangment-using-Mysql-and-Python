# Student Management System (Python + MySQL)

## 📌 Project Description

This is a Student Management System built using Python and MySQL.  
The project helps in managing student records with full CRUD operations (Create, Read, Update, Delete).  
It also calculates percentage and automatically determines Pass/Fail result.

## ⚙️ Technologies Used

- Python
- MySQL
- mysql-connector-python

## ✨ Features

- Add new student records
- View all students
- Update student details
- Delete student records
- Auto calculation of:
  - Percentage
  - Pass / Fail result

## 🗄️ Database Structure

**Database Name:** student_db  
**Table Name:** students

| Column     | Type         |
| ---------- | ------------ |
| id         | INT (PK, AI) |
| name       | VARCHAR      |
| roll_no    | VARCHAR      |
| marks      | INT          |
| percentage | FLOAT        |
| result     | VARCHAR      |

## 🚀 How to Run the Project

### 1️⃣ Install MySQL Connector

```bash
pip install mysql-connector-python
```
