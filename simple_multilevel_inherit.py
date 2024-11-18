#include <iostream>
using namespace std;

// Base class
class Institution {
protected:
    string name;
public:
    Institution(string n) : name(n) {}
    void displayInstitution() {
        cout << "Institution Name: " << name << endl;
    }
};

// Derived class 1
class Department : public Institution {
protected:
    string departmentName;
public:
    Department(string instName, string deptName) 
        : Institution(instName), departmentName(deptName) {}
    void displayDepartment() {
        displayInstitution();
        cout << "Department: " << departmentName << endl;
    }
};

// Derived class 2
class Student : public Department {
private:
    string studentName;
public:
    Student(string instName, string deptName, string studName)
        : Department(instName, deptName), studentName(studName) {}
    void displayStudent() {
        displayDepartment();
        cout << "Student Name: " << studentName << endl;
    }
};

// Main function
int main() {
    // Creating an object of Student
    Student s("MIT", "Computer Science", "John Doe");
    s.displayStudent();

    cout << endl;

    // Creating another object of Student
    Student s2("Harvard", "Economics", "Jane Smith");
    s2.displayStudent();

    return 0;
}