//============================================================================
// Name        : source.cpp
// Author      : Bryan Pirrone
// Version     : 1.0
// Copyright   : Copyright © 2017 SNHU
// Description : Project 2 Course
//               This program is designed to read an input file,
//               print a course list, and print a course list including
//               any prerequisites.
//============================================================================

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

//Menu display

void displayMenu() {
    cout << "1. Load Data Structure." << endl;
    cout << "2. Print Course List." << endl;
    cout << "3. Print Course." << endl;
    cout << "9. Exit." << endl;
    cout << endl;
    cout << "What would you like to do? " << endl;
}

//Course structure

struct Course {
    string courseName;
    string courseId;
    vector<string> prerequisites;
};

//Node structure

struct Node {
    Course course;
    Node* left;
    Node* right;

    Node() {
        left = nullptr;
        right = nullptr;
    }

    Node(Course aCourse) {
        this->course = aCourse;
    }
};

//Binary Search Tree

//Class definition

class BinarySearchTree{

    private:
        void Destruct(Node* node);
    
    public:
        Node* root;
        BinarySearchTree();
        virtual ~BinarySearchTree();
        void Insert(BinarySearchTree* tree, Node* node);
        void Search(string courseId);
        void PrintCourse(Node* node);

};

//Constructor

BinarySearchTree::BinarySearchTree() {
    root = nullptr;
};

//Destructor
BinarySearchTree::~BinarySearchTree() {
    Destruct(root);
}

void BinarySearchTree::Destruct(Node* node) {
    if (node != nullptr) {
        Destruct(node->left);
        node->left = nullptr;
        Destruct(node->right);
        node->right = nullptr;
        delete node;
    }
};

//Course search

void BinarySearchTree::Search(string courseId) {
    Node* currentNode = root;

    while (currentNode != nullptr) { 
        if (currentNode->course.courseId == courseId) {	 
            //prints course id and course name
            cout << currentNode->course.courseId << ", ";
            cout << currentNode->course.courseName;
            cout << endl;
            cout << "Prerequisites: ";
            //prints prerequisites
            for (string preRequisite : currentNode->course.prerequisites) { 
                if (preRequisite == currentNode->course.prerequisites.back()) {
                    
                    cout << preRequisite << endl; 
                }
                else {
                    cout << preRequisite << ", "; 
                }
            }

            return;
        }
        //searches left pointer if not found
        else if (courseId < currentNode->course.courseId) { 

            if (currentNode->left != nullptr) {
                currentNode = currentNode->left;
            }
        }
        //searches right pointer if not found
        else { 

            currentNode = currentNode->right;
        }
    }
    //course not found
    cout << "Course " << courseId << "not found. " << endl; 	
    return;
}

//inserts course into a course list
void BinarySearchTree::Insert(BinarySearchTree* tree, Node* node) {
    
    if (tree->root == nullptr) { 
        tree->root = node; 
    }
    else { 
        Node* curr = tree->root;
        while (curr != nullptr) { 

            if (node->course.courseId < curr->course.courseId) {
                if (curr->left == nullptr) {
                    curr->left = node;
                    curr = nullptr;
                }
                else {
                    curr = curr->left;
                }
            }
            else { 

                if (curr->right == nullptr) {
                    curr->right = node;
                    curr = nullptr;
                }
                else {
                    curr = curr->right;
                }
            }

        }
       
    }
}

//prints course list
void BinarySearchTree::PrintCourse(Node* node) {

    //if node is null, return
    if (node == nullptr) {
        return;
    }

    //in order traversal
    PrintCourse(node->left); 
    cout << node->course.courseId << ", ";
    cout << node->course.courseName << endl; 
    PrintCourse(node->right); 
};

//loads course from file
void loadCourse(string filename, BinarySearchTree* bst) {
    ifstream file(filename);
    if (file.is_open()) { 
        cout << "File loaded." << endl; 

        int num; 
        string line;
        string word;

        while (getline(file, line)) { 

            num = 0;
            Node* node = new Node();
            stringstream str(line);

            while (num < 2) {
                getline(str, word, ',');
                if (num == 0) {
                    node->course.courseId = word;
                }
                else {
                    node->course.courseName = word;
                }
                num++;
            }
            while (getline(str, word, ',')) {
                node->course.prerequisites.push_back(word);
            }

            //inserts course into course list
            bst->Insert(bst, node);
        }
    }
    //file error
    else {
        cout << "File error, please try again. " << endl;
        return;
    }

}

//main function
int main() {

    BinarySearchTree* bst = new BinarySearchTree();

    string fileChoice;
    string courseChoice;

    int userInput = 0;

    cout << "Welcome to the course planner." << endl << endl;
    //main while loop for menu
    while (userInput != 9) { 
        displayMenu();
        cin >> userInput;

        switch (userInput) {
        //loads file
        case 1: 
            cout << endl;
            cout << "What is the name of the file you would like to load? ";
            cin >> fileChoice;
            
            loadCourse(fileChoice, bst);
            cout << endl;
            break;

        //prints course list
        case 2:
            cout << endl;
            cout << "Here is a sample schedule:" << endl;
            cout << endl;   	
            bst->PrintCourse(bst->root); 
            cout << endl;
            break;
            
        //prints course and prerequisites
        case 3:
            cout << endl;
            cout << "What course do you want to know about? ";
            cin >> courseChoice;
            cout << endl;

            std::transform(courseChoice.begin(), courseChoice.end(), courseChoice.begin(), ::toupper);
            bst->Search(courseChoice);
            
            cout << endl;
            break;

        //exits program
        case 9:
            cout << "Thank you for using the course planner!" << endl;
            break;

        //invalid input
        default:
            cout << userInput << " is not a valid option." << endl << endl;
            break;
        }
    }
}


