# Caps1_ReinaldiRagasa

# Drilling Equipment Management System
## A. Overview
This Python program is a comprehensive Drilling Equipment Management System that allows users to:
- Register and authenticate users with secure email/password validation
- Manage a database of drilling equipment with full CRUD functionality
- View equipment data with sorting and filtering options
- Process equipment purchases with stock management

## B. Key Features
### B1. User Authentication
- Secure registration with email validation (@gmail.com required)
- Password requirements:
- - Minimum 6 characters
- - Must contain letters and numbers
- - Must have uppercase and lowercase
- - No consecutive repeating characters

### B2. Equipment Management
- View all equipment in a formatted table
- Sort equipment by various attributes (weight, length, price, etc.)
- Find minimum/maximum values for any attribute
- Filter by equipment name or material grade

### B3. CRUD Operations
- **Create**: Add new equipment with complete specifications
- **Read**: View equipment details in organized tables
- **Update**: Modify individual attributes or entire equipment records
- **Delete**: Remove equipment with confirmation prompts

### B4. Purchase System
- Check stock availability before purchase
- Calculate total costs
- Process payments and provide change
- Update stock levels automatically

### C. Data Structure
Equipment is stored with the following attributes:
1. Equipment Name
2. Weight (kg)
3. Length (m)
4. ID (mm)
5. OD (mm)
6. Price (USD)
7. Material Grade
8. Stock

### D. Technical Implementation
- Uses Python lists as the primary data structure
- Implements bubble sort for sorting operations
- Includes input validation for all user entries
- Features a clean console-based interface

### E. How to Use
1. Register with a valid gmail.com email
2. Log in with your credentials
3. Navigate the menu system to manage equipment
4. Use the various viewing options to analyze data
5. Process purchases through the dedicated menu
6. The program is designed for drilling equipment managers who need to track inventory, specifications, and sales in a user-friendly console application.
