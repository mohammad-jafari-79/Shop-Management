# Shop-Management
 Windows software for product and sales management

# Application Description

This application is a desktop-based tool designed for managing customer, product, and invoice data. Below are the detailed functionalities of the application:

## **Features**

### **1. Customers Menu:**
- **Actions:** Add, update, delete, and select (search) customers.
- **Search Options:**
  - By ID (highest priority).
  - By name.
  - By family name.
  - By phone number.
- **Data Display:** Shows a list of all customers.

### **2. Storage Menu:**
- **Actions:** Add, update, delete, and select (search) products.
- **Inputs:**
  - Product name.
  - Product count.
  - Product ID.

### **3. Invoice Menu:**
- **Actions:** Add, update, delete, and select (search) invoices.
- **Inputs:**
  - Invoice ID.
  - Customer ID.
  - Name.
  - Price.

### **4. Main Menu:**
- **Join Button:** Matches `customer_id` from the Invoice table with `id` from the Customers table and displays matching results.
- **Save to CSV:** Exports all tables (Customers, Storage, Invoice) to a CSV file.

### **5. Console Integration:**
- Displays timestamps for the following operations:
  - **Add**
  - **Update**
  - **Save**
- The timestamps are shown in a textbox console within the application.

---

### **How to Use**
- Navigate through the menus to perform specific actions (e.g., manage customers, storage, or invoices).
- Use the "Join" button on the main menu to link customers and invoices based on their IDs.
- Export all data to a CSV file by clicking the "Save CSV" button.

This application provides a simple yet powerful interface for managing essential business operations.

