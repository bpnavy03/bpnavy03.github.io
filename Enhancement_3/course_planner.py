#============================================================================
# Name        : course_planner.py
# Author      : Bryan Pirrone
# Version     : 7.0
# References  : SNHU CS-300 Project 2, source.cpp
# Description : This program allows the user to load a list of courses from a CSV file into a binary search tree (BST). 
#               The user can then print the entire course list, search for a specific course by its ID, 
#               view courses sorted by the number of prerequisites, or perform an interactive search. 
#               Additionally, MongoDB integration allows for course searching and retrieval.
#============================================================================

#============================================================================
# Revision History
# 1.0 - Initial version (conversion from C++ to Python)
# 2.0 - Added functionality to handle prerequisites for each course. Added title and spacing.
# 3.0 - Resolved CSV loading bugs (added prerequisites handling)
# 4.0 - Added feature to sort courses by the number of prerequisites
# 5.0 - Added interactive search feature
# 6.0 - Added MongoDB integration for course data storage (loading and searching only)
# 7.0 - Resolved interactive search bug
#============================================================================

import csv
from pymongo import MongoClient

# MongoDB Connection Setup
client = MongoClient("mongodb://localhost:27017/")
db = client["course_planner"]
courses_collection = db["courses"]

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

    def collect_courses(self, node, courses):
        if node:
            self.collect_courses(node.left, courses)
            courses.append(node.course)
            self.collect_courses(node.right, courses)
        return courses

    def sort_by_prerequisites(self):
        courses = self.collect_courses(self.root, [])
        courses.sort(key=lambda c: len(c.prerequisites), reverse=True)
        print("\n Courses Sorted by Number of Prerequisites:\n")
        for course in courses:
            print(f"{course.course_id}: {course.course_name} - Prerequisites: {', '.join(course.prerequisites) if course.prerequisites else 'None'}")
        print()

# Load courses from a CSV file into a BST
def load_courses(file_path, bst):
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                course_id = row[0]
                course_name = row[1]
                prerequisites = [prereq for prereq in row[2:] if prereq]
                course = Course(course_id, course_name, prerequisites)
                bst.insert(course)
        print("\n Courses loaded successfully into BST from CSV.\n")
    except FileNotFoundError:
        print("\n Error: File not found.\n")

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

# Load courses from MongoDB
def load_courses_from_mongodb():
    try:
        courses = list(courses_collection.find())
        if not courses:
            print("\n No courses found in MongoDB. Ensure the data is uploaded.\n")
            return
        print("\n Courses loaded from MongoDB:\n")
        for course in courses:
            prerequisites = [course.get(key, '') for key in ["prerequisite_1", "prerequisite_2", "prerequisite_3"] if course.get(key)]
            prerequisites = ", ".join(prerequisites) if prerequisites else "None"
            print(f"{course['course_id']}: {course['course_name']} - Prerequisites: {prerequisites}")
        print()
    except Exception as e:
        print(f" Error retrieving data from MongoDB: {e}")

# Search for a course in MongoDB
def search_course_in_mongodb(course_id):
    try:
        course = courses_collection.find_one({"course_id": course_id})
        if course:
            prerequisites = [course.get(key, '') for key in ["prerequisite_1", "prerequisite_2", "prerequisite_3"] if course.get(key)]
            prerequisites = ", ".join(prerequisites) if prerequisites else "None"
            print(f"\n Course Found: {course['course_id']} - {course['course_name']}")
            print(f" Prerequisites: {prerequisites}\n")
        else:
            print("\n Course not found in MongoDB.\n")
    except Exception as e:
        print(f" Error searching MongoDB: {e}")

# Display the menu
def display_menu():
    print("\n1. Load Data Structure from CSV.")
    print("2. Print Course List (BST).")
    print("3. Search Course (BST).")
    print("4. Sort Courses by Number of Prerequisites (BST).")
    print("5. Interactive Search (BST).")
    print("6. Load Courses from MongoDB.")  # New MongoDB Option
    print("7. Search Course in MongoDB.")   # New MongoDB Option
    print("9. Exit.\n")

# Main function
def main():
    # Title Banner
    print("=" * 60)
    print("               WELCOME TO THE COURSE PLANNER")
    print("=" * 60)
    print("\n This program allows you to:")
    print("- Load a list of courses from a CSV file")
    print("- View the entire course list")
    print("- Search for details about a specific course")
    print("- View courses sorted by number of prerequisites")
    print("- Perform an interactive search")
    print("- Load courses from MongoDB")
    print("- Search for a course in MongoDB\n")
    print("\n")
    bst = BinarySearchTree()
    while True:
        display_menu()
        choice = input("What would you like to do? ")
        print()
        if choice == '1':
            file_path = input("Enter the file name: ")
            print()
            load_courses(file_path, bst)
        elif choice == '2':
            print("\nCourse List (BST):\n")
            bst.print_courses(bst.root)
            print()
        elif choice == '3':
            course_id = input("Enter course ID to search (BST): ").upper()
            print()
            course = bst.search(course_id)
            if course:
                print(f"{course.course_id}, {course.course_name}")
                print("Prerequisites: " + ", ".join(course.prerequisites))
            else:
                print("\n Course not found in BST.\n")
        elif choice == '4':
            bst.sort_by_prerequisites()
        elif choice == '5':
            interactive_search(bst)
        elif choice == '6':
            load_courses_from_mongodb()
        elif choice == '7':
            course_id = input("Enter the Course ID to search in MongoDB: ").strip().upper()
            search_course_in_mongodb(course_id)
        elif choice == '9':
            print("\n Exiting program. Goodbye!")
            break
        else:
            print("\n Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()


