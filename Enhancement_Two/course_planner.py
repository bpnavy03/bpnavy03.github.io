#============================================================================
# Name        : course_planner.py
# Author      : Bryan Pirrone
# Version     : 5.0
# References  : SNHU CS-300 Project 2, source.cpp
# Description : This program allows the user to load a list of courses from a CSV file into a binary search tree (BST). 
#               The user can then print the entire course list, search for a specific course by its ID, 
#               view courses sorted by the number of prerequisites, or perform an interactive search. 
#               The program handles errors such as file not found and invalid input gracefully.
#               The program is designed to be user-friendly and robust, ensuring a smooth experience for managing course data.
#============================================================================

#============================================================================
# Revision History
# 1.0 - Initial version (conversion from C++ to Python)
# 2.0 - Added functionality to handle prerequisites for each course. Added title and spacing.
# 3.0 - Resolved CSV loading bugs (added prerequisites handling)
# 4.0 - Added feature to sort courses by the number of prerequisites
# 5.0 - Added interactive search feature
#============================================================================

import csv

# Class to represent a Course
class Course:
    def __init__(self, course_id, course_name, prerequisites):
        self.course_id = course_id
        self.course_name = course_name
        self.prerequisites = prerequisites

# Node structure for Binary Search Tree
class Node:
    def __init__(self, course):
        self.course = course
        self.left = None
        self.right = None

# Binary Search Tree Implementation
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, course):
        new_node = Node(course)
        if not self.root:
            self.root = new_node
        else:
            current = self.root
            while True:
                if course.course_id < current.course.course_id:
                    if current.left is None:
                        current.left = new_node
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    current = current.right

    def search(self, course_id):
        current = self.root
        while current:
            if current.course.course_id == course_id:
                return current.course
            elif course_id < current.course.course_id:
                current = current.left
            else:
                current = current.right
        return None

    def print_courses(self, node):
        if node:
            self.print_courses(node.left)
            print(f"{node.course.course_id}, {node.course.course_name}")
            self.print_courses(node.right)

    # Collect all courses in a list
    def collect_courses(self, node, courses):
        if node:
            self.collect_courses(node.left, courses)
            courses.append(node.course)
            self.collect_courses(node.right, courses)
        return courses

# Function to sort courses by the number of prerequisites
def print_sorted_courses_by_prerequisites(bst):
    courses = bst.collect_courses(bst.root, [])  # Collect all courses in a list
    # Sort courses based on the length of their prerequisites list
    sorted_courses = sorted(courses, key=lambda course: len(course.prerequisites), reverse=True)
    print("\nCourses sorted by number of prerequisites:")
    for course in sorted_courses:
        print(f"{course.course_id}, {course.course_name} - Prerequisites: {len(course.prerequisites)}")
    print()  # Add a blank line for readability

# Function to perform an interactive search
def interactive_search(bst):
    print("\nInteractive Search:\n")
    keyword = input("Enter part of a course ID or name to search: ").lower()
    print()
    courses = bst.collect_courses(bst.root, [])
    results = [course for course in courses if keyword in course.course_id.lower() or keyword in course.course_name.lower()]

    if results:
        print("Search Results:")
        for course in results:
            print(f"{course.course_id}, {course.course_name} - Prerequisites: {', '.join(course.prerequisites) if course.prerequisites else 'None'}")
    else:
        print("No matching courses found.")
    print()  # Add a blank line for readability

def load_courses(file_path, bst):
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                course_id = row[0]
                course_name = row[1]
                # Collect prerequisites from all remaining columns in the row
                prerequisites = [prereq for prereq in row[2:] if prereq]
                course = Course(course_id, course_name, prerequisites)
                bst.insert(course)
        print("\nCourses loaded successfully!\n")
    except FileNotFoundError:
        print("\nError: File not found.\n")

def display_menu():
    print("\n1. Load Data Structure.")
    print("2. Print Course List.")
    print("3. Print Course.")
    print("4. Print Courses Sorted by Prerequisites.") # New option for sorting by prerequisites
    print("5. Interactive Search.")  # New option for interactive search
    print("9. Exit.\n")

def main():
    # Title Banner
    print("=" * 60)
    print("               WELCOME TO THE COURSE PLANNER")
    print("=" * 60)
    print("\nThis program allows you to:")
    print("- Load a list of courses from a CSV file")
    print("- View the entire course list")
    print("- Search for details about a specific course")
    print("- View courses sorted by number of prerequisites")
    print("- Perform an interactive search")
    print("\n")

    bst = BinarySearchTree()
    while True:
        display_menu()
        choice = input("What would you like to do? ")
        print()  # Add a blank line for readability
        if choice == '1':
            file_path = input("Enter the file name: ")
            print()
            load_courses(file_path, bst)
        elif choice == '2':
            print("\nCourse List:")
            print()
            bst.print_courses(bst.root)
            print()  # Add a blank line for readability
        elif choice == '3':
            course_id = input("Enter course ID to search: ").upper()
            print()
            course = bst.search(course_id)
            if course:
                print(f"{course.course_id}, {course.course_name}")
                print("Prerequisites: " + ", ".join(course.prerequisites))
            else:
                print("\nCourse not found.\n")
            print()  # Add a blank line for readability
        elif choice == '4':
            print_sorted_courses_by_prerequisites(bst)
        elif choice == '5':
            interactive_search(bst)
        elif choice == '9':
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.\n")

if __name__ == "__main__":
    main()


