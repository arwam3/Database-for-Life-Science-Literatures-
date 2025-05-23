# Life Science Literature Management System

This repository hosts the SQL scripts for setting up a MySQL database designed to manage life science literature data, including authors, research papers, journals, publishers, and their interconnections. Additionally, it provides guidance on how to integrate this database with a C# Windows Forms application for seamless data interaction.

## Project Structure

* `DVL.sql`: SQL script for creating database views.
* `load_data.sql`: SQL script for populating the database with sample data.
* `queries.sql`: SQL script containing example queries to retrieve data.
* `Tables.sql`: SQL script for defining the database schema and creating tables.
* `image_6fe553.jpg`: Screenshot of MySQL Workbench.
* `image_6fda6f.png`: Screenshot of the C# Windows Forms application.

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

## Application Connection (C# Windows Forms - Visual Studio)

### Prerequisites

* **Visual Studio**: The integrated development environment (IDE) necessary for C# application development.
* **MySQL Connector/NET**: This is the official ADO.NET driver that enables C# applications to establish connections and communicate with MySQL databases.

### Steps to Connect

1.  **Install MySQL Connector/NET:**
    * Within your Visual Studio project, navigate to `Tools` > `NuGet Package Manager` > `Manage NuGet Packages for Solution...`.
    * Search for `MySql.Data` and proceed to install this NuGet package into your project.

2.  **Establish Connection in C# Code:**
    * In the C# code files where you intend to perform database operations, add the following `using` directive:
        ```csharp
        using MySql.Data.MySqlClient;
        ```
    * Define your database connection string. This string contains essential connection parameters:
        ```csharp
        string connectionString = "server=localhost;port=3306;database=LifeScienceDB;uid=your_mysql_username;pwd=your_mysql_password;";
        ```
        * **Important**: Replace `your_mysql_username` and `your_mysql_password` with your actual MySQL server credentials. The `database` name should precisely match `LifeScienceDB`.
    * Utilize the `MySqlConnection` object to open and close connections to the database as needed.
    * Employ `MySqlCommand` objects to execute various SQL queries, including `INSERT`, `SELECT`, `UPDATE`, and `DELETE` statements.
    * For retrieving data, use `MySqlDataReader` for forward-only, read-only access, or `MySqlDataAdapter` for populating `DataSet` or `DataTable` objects, which can then be bound to UI controls like `DataGridView` or used to populate individual text boxes.

    }

    // Similar methods for 'Update' and 'Delete' operations would be implemented here, 
    // following the same pattern of opening a connection, executing a MySqlCommand, 
    // and handling potential exceptions.
}
