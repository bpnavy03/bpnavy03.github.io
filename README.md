# Course Planner - Enhancements Overview
 This repository contains the Course Planner project, which uses a Binary Search Tree (BST) to manage and search for college courses. The project has undergone three major enhancements, improving functionality, efficiency, and user interaction. A GUI has been implemented for a greater user experience.

# Features
🔹 Load course data from a CSV file into a BST

🔹 Search for courses by ID in BST

🔹 Sort courses by the number of prerequisites in BST

🔹 Interactive keyword-based search in BST (now case-insensitive!)

🔹 Load courses from MongoDB

🔹 Search for a course in MongoDB

🔹 Graphic User Interface (GUI) using Tkinter for improved usability

# 📽️ Code Review Video
 Watch a video code review of the original artifact:

 https://youtu.be/bYgaW_qT7aQ

# 🚀 Enhancements Summary

# Enhancement 1: C++ to Python Conversion
✅ Converted the entire project from C++ to Python while maintaining original functionality.

✅ Implemented Python’s csv module for file handling.

✅ Replaced manual memory management from C++ with Python’s garbage collection.

# Enhancement 1 Narrative

The Course Planner was initially developed in C++ and later converted to Python to enhance readability, maintainability, and ease of use. The artifact was chosen for my ePortfolio because it demonstrates my ability to transition between programming languages while preserving functionality. This enhancement improved the program by leveraging Python’s built-in libraries for file handling and data structures, eliminating the need for manual memory management. Through this conversion, I demonstrated proficiency in software design principles, memory management, and data structure implementation.

Reflecting on this enhancement, I learned how to translate C++ logic into Python while maintaining efficiency. One of the challenges was ensuring that Python’s garbage collection system handled memory effectively, as opposed to C++’s manual allocation and deallocation. Another challenge was restructuring the file handling system to utilize Python’s CSV module instead of C++’s standard I/O operations. These challenges reinforced my understanding of software engineering principles, particularly how different languages handle memory and data structures. This enhancement met the course outcomes related to designing and evaluating computing solutions while improving program efficiency.

# Enhancement 2: Sorting & Interactive Search

✅ Sorting courses by prerequisite count, improving data organization.

✅ Interactive keyword-based search, allowing users to find courses dynamically.

✅ Enhanced error handling and formatted output for a better user experience.

# Enhancement 2 Narrative

The second enhancement introduced sorting and an interactive search function to the Course Planner. This allowed users to organize courses based on the number of prerequisites and dynamically search for courses using keywords. The artifact was included in my ePortfolio because it showcases my ability to implement algorithmic solutions that enhance data accessibility and user experience. The introduction of sorting algorithms made prerequisite-based organization possible, while the interactive search feature improved usability by allowing users to find courses more efficiently.

This enhancement taught me that algorithm optimization directly impacts the user experience. One of the main challenges was modifying the Binary Search Tree (BST) to sort courses dynamically based on prerequisites instead of alphabetical order. Another challenge was implementing a keyword-based search feature while ensuring the BST maintained its efficiency. Overcoming these obstacles required refining my approach to data structures and algorithm implementation. This enhancement successfully met the course outcomes by improving data organization, optimizing searching and sorting techniques, and enhancing the program’s usability.

# Enhancement 3: Database Integration Using MongoDB

✅ Implemented MongoDB for course storage, replacing in-memory BST for scalability.

✅ Enabled persistent data storage, eliminating the need to reload courses on every run.

✅ Developed MongoDB queries to efficiently retrieve and sort courses.

✅ Enhanced search functionality, leveraging MongoDB's indexing for faster lookups.

✅ Modified the program structure to interact with both CSV files and MongoDB.

# Enhancement 3 Narrative

The final enhancement integrated MongoDB into the Course Planner, allowing courses to be stored and retrieved from a NoSQL database in addition to CSV files. This update provided scalability, improved data persistence, and allowed users to switch between file-based storage and database queries. The artifact was selected for my ePortfolio because it highlights my ability to work with databases, optimize storage solutions, and apply real-world software engineering techniques. The transition from a BST-only structure to a hybrid CSV and MongoDB system demonstrated my ability to balance memory efficiency with persistent data storage.

Throughout this enhancement, I learned how to integrate a NoSQL database into an existing application while ensuring compatibility with previous functionality. Challenges included setting up a local MongoDB instance, designing the database schema to match the existing CSV structure, and ensuring seamless interaction between Python and MongoDB using pymongo. Additionally, implementing robust error handling and validation was crucial to maintaining data integrity. This enhancement met the course outcomes by demonstrating the ability to design scalable computing solutions, integrate databases, and ensure usability improvements.

# Finalized Enhanced Artifact with GUI

✅ Introduced a Tkinter-based GUI for an improved user experience.

✅ Designed a main window with buttons to load, search, and view courses.

✅ Added input fields for user-friendly course searching.

✅ Implemented list displays for course data from CSV and MongoDB.

✅ Enhanced application accessibility by removing the need for command-line interaction.

# 💡 Professional Self-Assessment

Throughout my academic journey in the Computer Science program, I have gained extensive knowledge and hands-on experience that have significantly shaped my professional aspirations and strengthened my technical expertise. Completing my coursework and developing my ePortfolio have allowed me to refine my problem-solving skills, enhance my ability to collaborate in a team environment, and improve my ability to communicate complex technical concepts to diverse stakeholders. These experiences have prepared me to enter the software development field as a more competent and well-rounded professional.

One of the most impactful aspects of my learning experience has been working with data structures and algorithms. The coursework reinforced my ability to develop efficient, scalable software solutions by applying fundamental concepts such as algorithms, recursion, and tree-based structures. My work on the Course Planner project demonstrates my ability to design and implement a Binary Search Tree (BST) to efficiently store and retrieve course information. Additionally, incorporating MongoDB as an alternative data storage option enhanced my understanding of database management, query optimization, and real-world data handling. These experiences have strengthened my ability to analyze trade-offs in software design and select the best approach based on performance requirements.

Collaboration has also played a vital role in my development. Whether working on team-based projects or engaging in peer reviews, I have improved my ability to work effectively with others in a professional setting. I have learned to communicate my ideas clearly and provide constructive feedback, which is essential in a collaborative software development environment. Communicating with stakeholders, whether through technical documentation or project presentations, has been another key skill I developed. Being able to explain software solutions to both technical and non-technical audiences is crucial in the industry, and my coursework has helped me refine this skill.

The artifacts I have developed throughout my academic journey collectively demonstrate my ability to integrate multiple disciplines in computer science, including software engineering, algorithms and data structures, database management, and security principles. My work on the Course Planner project exemplifies my ability to build robust software solutions while considering efficiency, scalability, and security. This project also highlights my ability to transition between different programming paradigms, as it was originally implemented in C++ before being optimized and extended in Python.

Overall, my ePortfolio is a comprehensive representation of my capabilities as a software developer. It showcases my ability to design and implement efficient algorithms, develop secure database-driven applications, and effectively communicate my work to a broader audience. The skills I have acquired throughout this program have prepared me to enter the industry with confidence, and I am eager to apply my knowledge in a professional setting. This professional self-assessment serves as a reflection of my growth and as an introduction to my technical artifacts, which illustrate the depth of my expertise and my commitment to excellence in software development.

# 📥 Installation & Usage
🔹Installation & Setup:

Clone the Repository:

git clone https://github.com/bpnavy03/bpnavy03.github.io.git

cd bpnavy03.github.io

1️⃣  Install Python

	a) Ensure Python 3.10+ is installed. You can check this by running the following line in command prompt/windows powershell: python --version
	
	b) If Python is not installed, download and install it from python.org

2️⃣  Install Required Packages

	a) Run the following command to install dependencies:
	
		pip install pymongo
		
		pip install tk

3️⃣  Prepare the Course Data (CSV File)

	a) The program can read course data from a CSV file. This file has been provided.
	
	b) File Name: courses.csv
	
	c) Location: courses.csv must be in the same directory as course_planner.py

4️⃣  Setup MongoDB (Optional)-- If you want to use MongoDB integration, follow these steps:

	a) Install MongoDB
	
		1)Download from mongodb.com. Install it and ensure the server is running.
		
	b) Import course data into MongoDB
	
		1) Start MongoDB: mongod --dbpath "C:\Program Files\MongoDB\Server\8.0\data"
		
		2) Open the Mongo Shell: mongosh
		
		3) Switch to the course database: use course_planner
		
		4) Import the CSV file into MongoDB: mongoimport --db course_planner --collection courses --type csv --file courses.csv --headerline
		
		5) Verify CSV file was imported into MongoDB correctly: db.courses.find().pretty()

🔹Usage Instructions:

1️⃣  Running the GUI Mode

	a) Open a command prompt/windows PowerShell/terminal, navigate to the program directory, and run:
	
		python course_planner.py
		
	b) The Tkinter GUI will launch, providing buttons for loading course data, searching, and sorting courses.
	
	c) Start with option 1 and enter courses.csv. The CSV file should be loaded successfully. Then use option 6 to load course data from MongoDB.
	
	d) The GUI includes interactive elements such as dropdowns, text input, and buttons for a seamless experience.

2️⃣  Running the Command-Line Interface (CLI) Mode

	a) Open a command prompt/windows PowerShell/terminal and navigate to the program directory.
	
	b) Run: python course_planner.py
	
	c) Navigate the menu using the provided options.
	
	d) Start with option 1 and enter courses.csv. The CSV file should be loaded successfully. The use option 6 to load course data from MongoDB.
	
	e) Use options 2, 3, 4, or 5 to perform course searches. Use option 9 to exit the program.

# 🌐 GitHub Pages Site
The latest version of the Course Planner is deployed here:

🔗 https://bpnavy03.github.io/

# 🛠 Future Improvements

🔹 Implement MongoDB Atlas for cloud-based storage.

🔹 Add function for creating a tentative course schedule.

🔹 Expand search features using AI-based recommendations.

# 📧 Contact & Contributions

💡 Have suggestions or want to contribute? Feel free to open a pull request or submit an issue!
