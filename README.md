# Life Science Literature Management System

This repository hosts the SQL scripts for setting up a MySQL database designed to manage life science literature data, including authors, research papers, journals, publishers, and their interconnections. Additionally, it provides guidance on how to integrate this database with a C# Windows Forms application for seamless data interaction.

## Project Structure

* `DVL.sql`: SQL script for creating database views.
* `load_data.sql`: SQL script for populating the database with sample data.
* `queries.sql`: SQL script containing example queries to retrieve data.
* `Tables.sql`: SQL script for defining the database schema and creating tables.

## Database Setup (MySQL)

The database schema is structured to efficiently handle various entities within the domain of life science literature.

### 1. Database and Table Definitions

The `Tables.sql` file contains the SQL commands to create the `LifeScienceDB` database and define all its constituent tables.

* **Publisher**: Stores details about publishing houses.
* **PublicationType**: Enumerates different categories of publications such as Journal, Book, or Ebook.
* **PublisherPublicationType**: Establishes a many-to-many relationship linking publishers to the specific types of publications they handle.
* **PaymentMethod**: Lists various methods of payment accepted.
* **PublisherPaymentMethod**: Connects publishers with the payment methods they accept.
* **BiomedicalField**: Classifies research into distinct biomedical fields.
* **Journal**: Contains comprehensive information about journals, including their ISSN, impact factor, associated publisher, and more.
* **JournalField**: Defines a many-to-many relationship, associating journals with specific biomedical fields.
* **Author**: Stores authors' personal and professional details such as name, qualification, affiliation, and H-Index.
* **AuthorField**: Links authors to their primary fields of research interest.
* **Research**: Provides detailed information about research papers, including title, abstract, publication date, and the journal in which they were published.
* **Research_Authors**: Manages the many-to-many relationship between research papers and their contributing authors.
* **Citation**: A self-referencing table used to track citations between different research papers.

#### To set up the database:
1.  Open MySQL Workbench or any other preferred MySQL client.
2.  Execute the `Tables.sql` script to create the `LifeScienceDB` database and all its tables.

### 2. Data Population

The `load_data.sql` file provides `INSERT` statements to populate the newly created database tables with sample data.

* **BiomedicalField**: Inserts at least 10 distinct biomedical fields.
* **Publisher**: Adds 10 sample publisher entries.
* **PublicationType**: Includes 3 publication types: 'Journal', 'Book', and 'Ebook'.
* **PublisherPublicationType**: Establishes at least 10 links between publishers and publication types.
* **PaymentMethod**: Inserts at least 5 different payment methods.
* **PublisherPaymentMethod**: Creates at least 10 associations between publishers and payment methods.
* **Journal**: Populates the table with at least 10 journal entries, complete with various attributes.
* **JournalField**: Links at least 10 journals to their respective biomedical fields.
* **Author**: Adds at least 10 author records, including their qualifications and affiliations.
* **AuthorField**: Establishes at least 10 connections between authors and their fields of expertise.
* **Research**: Inserts at least 10 research paper entries with abstracts and publication dates.
* **Research_Authors**: Creates at least 10 links between research papers and their authors.
* **Citation**: Adds at least 10 citation entries, demonstrating inter-research paper references.

#### To load the data:
1.  Ensure you have successfully executed `Tables.sql` first.
2.  Execute the `load_data.sql` script in your MySQL client to populate the tables with the provided sample data.

### 3. Database Views

The `DVL.sql` file contains SQL commands for creating several database views, which are designed to simplify complex queries and offer summarized perspectives on the data.

* **View_Authors_Immunology**: Displays distinct authors whose research interests include 'Immunology'.
* **View_OpenAccess_Journals_Springer**: Lists open-access journals that are published by 'Springer'.
* **View_Author_Citation_Counts**: Calculates and presents the total citation count for each author, ordered in descending fashion.
* **View_Research_Authors**: Provides a consolidated list of research papers along with their associated authors.
* **View_Journal_BiomedicalFields**: Shows all journals and the biomedical fields they are related to.

#### To create the views:
1.  Verify that both `Tables.sql` and `load_data.sql` have been executed.
2.  Execute the `DVL.sql` script in your MySQL client.

### 4. Example Queries

The `queries.sql` file provides a set of example SQL queries that demonstrate how to retrieve specific information from the populated database.

* List the name of authors whose research of interest is Immunology.
* Who is the author with the most citations in 2023 (NOTE: This requires CitationDate in Citation table; adjust if not present).
* List open access journals published by Springer.
* List all publications (research titles) by author 'Dr. Alice Smith'.
* List journals and their impact factors that publish research in 'Genetics and Genomics'.
* Count how many research papers each author has published.
* List publishers who accept 'Ebook' publication type.
* List payment methods accepted by 'Nature Publishing Group'.

You can execute these queries in MySQL Workbench or your chosen MySQL client to test data retrieval and understand the database structure.

# Life Science Database Management System UI

This is a desktop application built using Python's Tkinter library and designed to manage and display information related to biomedical research, authors, and journals. It connects to a MySQL database (`LifeScienceDB`) to retrieve and present data.

## Features

* **User-Friendly Interface:** Intuitive graphical user interface (GUI) built with Tkinter.
* **Database Integration:** Connects to a MySQL database (`LifeScienceDB`) to fetch and display data.
* **Role-Based Access (Basic):** Differentiates between 'admin' and 'user' roles, with potential for extended functionalities for 'admin' users.
* **Data Visualization (Treeview):** Displays research papers, journals, and authors in an organized, scrollable table format using `ttk.Treeview`.
* **Login Screen:** Secure login interface for authentication.
* **Dynamic Content:** Tabs are generated and populated based on user roles after successful login.

## Setup Instructions

### 1. Database Setup

Before running the application, ensure your MySQL database is set up correctly.

* **Create the Database:** Execute the `Tables.sql` script to create the `LifeScienceDB` database and its tables.
* **Populate Data:** Execute the `load_data.sql` script to insert sample data into the tables.
* **Create Views (Optional but Recommended):** Execute the `DVL.sql` script to create the views that can simplify certain queries, although the current Python app does not directly use all of them.

### 2. Python Environment

1.  **Install Python:** Ensure you have Python 3.x installed (e.g., Python 3.8+).
2.  **Install Required Libraries:** Open your terminal or command prompt and install the necessary Python packages:
    ```bash
    pip install tk
    pip install Pillow
    pip install mysql-connector-python
    ```
    * `tk`: Tkinter is usually included with Python installations, but `python-tk` might be needed on some Linux distributions (e.g., `sudo apt-get install python3-tk`).
    * `Pillow`: For image handling (`PIL` fork).
    * `mysql-connector-python`: To connect to the MySQL database.

### 3. Application Files

1.  **Save the Python Code:** Save the provided Python code (from your prompt) as `app.py` (or any other `.py` file).
2.  **Background Image:** The application attempts to load a background image named `biomedical_bg.jpg`. Place an image with this name in the same directory as `app.py`, or modify the `load_images` method in `app.py` to point to your image file. If the image is not found, the background will simply be plain.

### 4. Database Credentials

Open `app.py` and locate the `db_connect` method. Update the `host`, `user`, and `password` parameters to match your MySQL database credentials:

```python
    def db_connect(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost", # Your MySQL host
                user="root",      # Your MySQL username
                password="Forrest_j7bye", # Your MySQL password
                database="LifeScienceDB"
            )
            self.cursor = self.conn.cursor(dictionary=True)
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to connect: {str(e)}")
            self.root.destroy().

    }

    // Similar methods for 'Update' and 'Delete' operations would be implemented here, 
    // following the same pattern of opening a connection, executing a MySqlCommand, 
    // and handling potential exceptions.
}
