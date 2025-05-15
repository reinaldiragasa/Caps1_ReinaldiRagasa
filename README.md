# Caps1_ReinaldiRagasa

Drilling Equipment Management System
Overview
This Python program is a comprehensive Drilling Equipment Management System that allows users to:

Register and authenticate users with secure email/password validation

Manage a database of drilling equipment with full CRUD functionality

View equipment data with sorting and filtering options

Process equipment purchases with stock management

Key Features
User Authentication
Secure registration with email validation (@gmail.com required)

Password requirements:

Minimum 6 characters

Must contain letters and numbers

Must have uppercase and lowercase

No consecutive repeating characters

Equipment Management
View all equipment in a formatted table

Sort equipment by various attributes (weight, length, price, etc.)

Find minimum/maximum values for any attribute

Filter by equipment name or material grade

CRUD Operations
Create: Add new equipment with complete specifications

Read: View equipment details in organized tables

Update: Modify individual attributes or entire equipment records

Delete: Remove equipment with confirmation prompts

Purchase System
Check stock availability before purchase

Calculate total costs

Process payments and provide change

Update stock levels automatically

Data Structure
Equipment is stored with the following attributes:

Equipment Name

Weight (kg)

Length (m)

ID (mm)

OD (mm)

Price (USD)

Material Grade

Stock

Technical Implementation
Uses Python lists as the primary data structure

Implements bubble sort for sorting operations

Includes input validation for all user entries

Features a clean console-based interface

How to Use
Register with a valid gmail.com email

Log in with your credentials

Navigate the menu system to manage equipment

Use the various viewing options to analyze data

Process purchases through the dedicated menu

The program is designed for drilling equipment managers who need to track inventory, specifications, and sales in a user-friendly console application.
