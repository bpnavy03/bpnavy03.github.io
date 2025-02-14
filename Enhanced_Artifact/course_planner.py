#============================================================================
# Name        : course_planner.py
# Author      : Bryan Pirrone
# Version     : 8.0
# References  : 1) SNHU CS-300 Project 2, source.cpp
#               2) Python Tkinter Documents, https://docs.python.org/3/library/tkinter.html
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
# 8.0 - GUI implementation
#============================================================================

import tkinter as tk
from tkinter import filedialog, messagebox
import csv
from pymongo import MongoClient

# Binary Search Tree (BST) Implementation
class TreeNode:
    def __init__(self, course_id, course_name, prerequisites):
        self.course_id = course_id
        self.course_name = course_name
        self.prerequisites = prerequisites
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, course_id, course_name, prerequisites):
        new_node = TreeNode(course_id, course_name, prerequisites)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_recursive(self.root, new_node)

    def _insert_recursive(self, current, new_node):
        if new_node.course_id < current.course_id:
            if current.left is None:
                current.left = new_node
            else:
                self._insert_recursive(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self._insert_recursive(current.right, new_node)

    def search(self, course_id):
        return self._search_recursive(self.root, course_id)

    def _search_recursive(self, current, course_id):
        if current is None:
            return None
        if current.course_id == course_id:
            return current
        elif course_id < current.course_id:
            return self._search_recursive(current.left, course_id)
        else:
            return self._search_recursive(current.right, course_id)

    def print_courses(self, node, output_list):
        if node:
            self.print_courses(node.left, output_list)
            output_list.append(f"{node.course_id}: {node.course_name} - Prerequisites: {', '.join(node.prerequisites) if node.prerequisites else 'None'}")
            self.print_courses(node.right, output_list)

# MongoDB connection setup
client = MongoClient("mongodb://localhost:27017/")
db = client["course_planner"]
courses_collection = db["courses"]

# GUI Application
class CoursePlannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Course Planner GUI")

        self.bst = BinarySearchTree()

        # Buttons
        tk.Button(root, text="Load Courses from CSV", command=self.load_courses_from_csv).grid(row=0, column=0, padx=10, pady=5)
        tk.Button(root, text="Print Course List (BST)", command=self.print_courses).grid(row=0, column=1, padx=10, pady=5)
        tk.Button(root, text="Search Course (BST)", command=self.search_course_bst).grid(row=1, column=0, padx=10, pady=5)
        tk.Button(root, text="Sort Courses by Prerequisites (BST)", command=self.sort_courses_bst).grid(row=1, column=1, padx=10, pady=5)
        tk.Button(root, text="Interactive Search (BST)", command=self.interactive_search_bst).grid(row=2, column=0, padx=10, pady=5)
        tk.Button(root, text="Load Courses from MongoDB", command=self.load_courses_from_mongodb).grid(row=2, column=1, padx=10, pady=5)
        tk.Button(root, text="Search Course in MongoDB", command=self.search_course_mongodb).grid(row=3, column=0, padx=10, pady=5)

        # Output Display
        self.text_output = tk.Text(root, height=20, width=80)
        self.text_output.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def display_output(self, text):
        self.text_output.delete(1.0, tk.END)
        self.text_output.insert(tk.END, text)

    def load_courses_from_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if not file_path:
            return

        try:
            with open(file_path, newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip header row
                for row in reader:
                    course_id, course_name, *prerequisites = row
                    prerequisites = [p.strip() for p in prerequisites if p.strip()]
                    self.bst.insert(course_id, course_name, prerequisites)
            self.display_output("✅ Courses successfully loaded into BST from CSV.\n")
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found. Please check the filename and try again.")

    def print_courses(self):
        output_list = []
        self.bst.print_courses(self.bst.root, output_list)
        self.display_output("\n".join(output_list) if output_list else "No courses available in BST.")

    def search_course_bst(self):
        course_id = self.get_input("Enter Course ID to search (BST):").upper()
        course = self.bst.search(course_id)
        if course:
            self.display_output(f"{course.course_id}: {course.course_name}\nPrerequisites: {', '.join(course.prerequisites) if course.prerequisites else 'None'}")
        else:
            self.display_output("❌ Course not found in BST.")

    def sort_courses_bst(self):
        output_list = []
        self.bst.print_courses(self.bst.root, output_list)
        sorted_list = sorted(output_list, key=lambda x: x.count(","))
        self.display_output("\n".join(sorted_list) if sorted_list else "No courses available in BST.")

    def interactive_search_bst(self):
        keyword = self.get_input("Enter keyword to search (BST):").lower()
        output_list = []
        self.bst.print_courses(self.bst.root, output_list)
        filtered_courses = [course for course in output_list if keyword in course.lower()]
        self.display_output("\n".join(filtered_courses) if filtered_courses else "No matching courses found.")

    def load_courses_from_mongodb(self):
        courses = list(courses_collection.find())
        if not courses:
            self.display_output("⚠️ No courses found in MongoDB. Ensure the data is uploaded.")
            return

        output_list = []
        for course in courses:
            prerequisites = [course.get(key, '') for key in ["prerequisite_1", "prerequisite_2", "prerequisite_3"] if course.get(key)]
            prerequisites = ", ".join(prerequisites) if prerequisites else "None"
            output_list.append(f"{course['course_id']}: {course['course_name']} - Prerequisites: {prerequisites}")

        self.display_output("\n".join(output_list))

    def search_course_mongodb(self):
        course_id = self.get_input("Enter Course ID to search in MongoDB:").strip().upper()
        course = courses_collection.find_one({"course_id": course_id})
        if course:
            prerequisites = [course.get(key, '') for key in ["prerequisite_1", "prerequisite_2", "prerequisite_3"] if course.get(key)]
            prerequisites = ", ".join(prerequisites) if prerequisites else "None"
            self.display_output(f"🔍 Course Found: {course['course_id']} - {course['course_name']}\n📌 Prerequisites: {prerequisites}")
        else:
            self.display_output("❌ Course not found in MongoDB.")

    def get_input(self, prompt):
        return tk.simpledialog.askstring("Input", prompt)

# Run the Tkinter GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = CoursePlannerApp(root)
    root.mainloop()



