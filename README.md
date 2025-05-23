
        <h1>Life Science Literature Management System</h1>

        <p>This repository hosts the SQL scripts for setting up a MySQL database designed to manage life science literature data, including authors, research papers, journals, publishers, and their interconnections. Additionally, it provides guidance on how to integrate this database with a C# Windows Forms application for seamless data interaction.</p>

        <img src="image_6fe553.jpg" alt="MySQL Workbench Screenshot">
        <p style="text-align: center; font-style: italic; color: #555;">Figure 1: Example of MySQL Workbench with SQL schema.</p>

        <img src="image_6fda6f.png" alt="Visual Studio C# Application Screenshot">
        <p style="text-align: center; font-style: italic; color: #555;">Figure 2: Example of a C# Windows Forms Application in Visual Studio.</p>


        <h2>Database Setup (MySQL)</h2>
        <p>The database schema is structured to efficiently handle various entities within the domain of life science literature.</p>

        <h3>1. Database and Table Definitions</h3>
        <p>The <code>Tables.sql</code> file contains the SQL commands to create the <code>LifeScienceDB</code> database and define all its constituent tables <span class="file-citation"></span>.</p>
        <ul>
            <li><strong>Publisher</strong>: Stores details about publishing houses <span class="file-citation"></span>.</li>
            <li><strong>PublicationType</strong>: Enumerates different categories of publications such as Journal, Book, or Ebook <span class="file-citation"></span>.</li>
            <li><strong>PublisherPublicationType</strong>: Establishes a many-to-many relationship linking publishers to the specific types of publications they handle <span class="file-citation"></span>.</li>
            <li><strong>PaymentMethod</strong>: Lists various methods of payment accepted <span class="file-citation"></span>.</li>
            <li><strong>PublisherPaymentMethod</strong>: Connects publishers with the payment methods they accept <span class="file-citation"></span>.</li>
            <li><strong>BiomedicalField</strong>: Classifies research into distinct biomedical fields <span class="file-citation"></span>.</li>
            <li><strong>Journal</strong>: Contains comprehensive information about journals, including their ISSN, impact factor, associated publisher, and more <span class="file-citation"></span>.</li>
            <li><strong>JournalField</strong>: Defines a many-to-many relationship, associating journals with specific biomedical fields <span class="file-citation"></span>.</li>
            <li><strong>Author</strong>: Stores authors' personal and professional details such as name, qualification, affiliation, and H-Index <span class="file-citation"></span>.</li>
            <li><strong>AuthorField</strong>: Links authors to their primary fields of research interest <span class="file-citation"></span>.</li>
            <li><strong>Research</strong>: Provides detailed information about research papers, including title, abstract, publication date, and the journal in which they were published <span class="file-citation"></span>.</li>
            <li><strong>Research_Authors</strong>: Manages the many-to-many relationship between research papers and their contributing authors <span class="file-citation"></span>.</li>
            <li><strong>Citation</strong>: A self-referencing table used to track citations between different research papers <span class="file-citation"></span>.</li>
        </ul>

        <h4>To set up the database:</h4>
        <ol>
            <li>Open MySQL Workbench or any other preferred MySQL client.</li>
            <li>Execute the <code>Tables.sql</code> script to create the <code>LifeScienceDB</code> database and all its tables <span class="file-citation"></span>.</li>
        </ol>

        <h3>2. Data Population</h3>
        <p>The <code>load_data.sql</code> file provides <code>INSERT</code> statements to populate the newly created database tables with sample data <span class="file-citation"></span>.</p>
        <ul>
            <li><strong>BiomedicalField</strong>: Inserts at least 10 distinct biomedical fields <span class="file-citation"></span>.</li>
            <li><strong>Publisher</strong>: Adds 10 sample publisher entries <span class="file-citation"></span>.</li>
            <li><strong>PublicationType</strong>: Includes 3 publication types: 'Journal', 'Book', and 'Ebook' <span class="file-citation"></span>.</li>
            <li><strong>PublisherPublicationType</strong>: Establishes at least 10 links between publishers and publication types <span class="file-citation"></span>.</li>
            <li><strong>PaymentMethod</strong>: Inserts at least 5 different payment methods <span class="file-citation"></span>.</li>
            <li><strong>PublisherPaymentMethod</strong>: Creates at least 10 associations between publishers and payment methods <span class="file-citation"></span>.</li>
            <li><strong>Journal</strong>: Populates the table with at least 10 journal entries, complete with various attributes <span class="file-citation"></span>.</li>
            <li><strong>JournalField</strong>: Links at least 10 journals to their respective biomedical fields <span class="file-citation"></span>.</li>
            <li><strong>Author</strong>: Adds at least 10 author records, including their qualifications and affiliations <span class="file-citation"></span>.</li>
            <li><strong>AuthorField</strong>: Establishes at least 10 connections between authors and their fields of expertise <span class="file-citation"></span>.</li>
            <li><strong>Research</strong>: Inserts at least 10 research paper entries with abstracts and publication dates <span class="file-citation"></span>.</li>
            <li><strong>Research_Authors</strong>: Creates at least 10 links between research papers and their authors <span class="file-citation"></span>.</li>
            <li><strong>Citation</strong>: Adds at least 10 citation entries, demonstrating inter-research paper references <span class="file-citation"></span>.</li>
        </ul>

        <h4>To load the data:</h4>
        <ol>
            <li>Ensure you have successfully executed <code>Tables.sql</code> first.</li>
            <li>Execute the <code>load_data.sql</code> script in your MySQL client to populate the tables with the provided sample data <span class="file-citation"></span>.</li>
        </ol>

        <h3>3. Database Views</h3>
        <p>The <code>DVL.sql</code> file contains SQL commands for creating several database views, which are designed to simplify complex queries and offer summarized perspectives on the data <span class="file-citation"></span>.</p>
        <ul>
            <li><strong>View_Authors_Immunology</strong>: Displays distinct authors whose research interests include 'Immunology' <span class="file-citation"></span>.</li>
            <li><strong>View_OpenAccess_Journals_Springer</strong>: Lists open-access journals that are published by 'Springer' <span class="file-citation"></span>.</li>
            <li><strong>View_Author_Citation_Counts</strong>: Calculates and presents the total citation count for each author, ordered in descending fashion <span class="file-citation"></span>.</li>
            <li><strong>View_Research_Authors</strong>: Provides a consolidated list of research papers along with their associated authors <span class="file-citation"></span>.</li>
            <li><strong>View_Journal_BiomedicalFields</strong>: Shows all journals and the biomedical fields they are related to <span class="file-citation"></span>.</li>
        </ul>

        <h4>To create the views:</h4>
        <ol>
            <li>Verify that both <code>Tables.sql</code> and <code>load_data.sql</code> have been executed.</li>
            <li>Execute the <code>DVL.sql</code> script in your MySQL client <span class="file-citation"></span>.</li>
        </ol>

        <h3>4. Example Queries</h3>
        <p>The <code>queries.sql</code> file provides a set of example SQL queries that demonstrate how to retrieve specific information from the populated database <span class="file-citation"></span>.</p>
        <ul>
            <li>Retrieve the names of authors whose research interest is Immunology <span class="file-citation"></span>.</li>
            <li>Identify the author with the highest number of citations in 2023 (requires a <code>CitationDate</code> column in the <code>Citation</code> table) <span class="file-citation"></span>.</li>
            <li>List all open access journals published by Springer <span class="file-citation"></span>.</li>
            <li>Find all publications (research titles) authored by 'Dr. Alice Smith' <span class="file-citation"></span>.</li>
            <li>List journals and their impact factors that publish research in 'Genetics and Genomics' <span class="file-citation"></span>.</li>
            <li>Count the total number of research papers published by each author <span class="file-citation"></span>.</li>
            <li>Identify publishers that support 'Ebook' as a publication type <span class="file-citation"></span>.</li>
            <li>List all payment methods accepted by 'Nature Publishing Group' <span class="file-citation"></span>.</li>
        </ul>
        <p>You can execute these queries in MySQL Workbench or your chosen MySQL client to test data retrieval and understand the database structure.</p>

        <h2>Application Connection (C# Windows Forms - Visual Studio)</h2>
        <p>The C# Windows Forms application, as depicted in <a href="image_6fda6f.png"><code>image_6fda6f.png</code></a>, is designed to interact with this MySQL database.</p>

        <h3>Prerequisites</h3>
        <ul>
            <li><strong>Visual Studio</strong>: The integrated development environment (IDE) necessary for C# application development.</li>
            <li><strong>MySQL Connector/NET</strong>: This is the official ADO.NET driver that enables C# applications to establish connections and communicate with MySQL databases.</li>
        </ul>

        <h3>Steps to Connect</h3>
        <ol>
            <li><strong>Install MySQL Connector/NET:</strong>
                <p>Within your Visual Studio project, navigate to <code>Tools</code> > <code>NuGet Package Manager</code> > <code>Manage NuGet Packages for Solution...</code>.</p>
                <p>Search for <code>MySql.Data</code> and proceed to install this NuGet package into your project.</p>
            </li>
            <li><strong>Establish Connection in C# Code:</strong>
                <p>In the C# code files where you intend to perform database operations, add the following <code>using</code> directive:</p>
<pre><code>using MySql.Data.MySqlClient;
</code></pre>
                <p>Define your database connection string. This string contains essential connection parameters:</p>
<pre><code>string connectionString = "server=localhost;port=3306;database=LifeScienceDB;uid=your_mysql_username;pwd=your_mysql_password;";
</code></pre>
                <p><strong>Important</strong>: Replace <code>your_mysql_username</code> and <code>your_mysql_password</code> with your actual MySQL server credentials. The <code>database</code> name should precisely match <code>LifeScienceDB</code>.</p>
                <p>Utilize the <code>MySqlConnection</code> object to open and close connections to the database as needed.</p>
                <p>Employ <code>MySqlCommand</code> objects to execute various SQL queries, including <code>INSERT</code>, <code>SELECT</code>, <code>UPDATE</code>, and <code>DELETE</code> statements.</p>
                <p>For retrieving data, use <code>MySqlDataReader</code> for forward-only, read-only access, or <code>MySqlDataAdapter</code> for populating <code>DataSet</code> or <code>DataTable</code> objects, which can then be bound to UI controls like <code>DataGridView</code> or used to populate individual text boxes.</p>
            </li>
        </ol>

        <h3>Example C# Code Snippet (Conceptual)</h3>
<pre><code>using MySql.Data.MySqlClient;
using System;
using System.Windows.Forms;

public partial class PublisherForm : Form
{
    // Ensure you replace 'root' and 'your_password' with your actual MySQL credentials
    private string connectionString = "server=localhost;port=3306;database=LifeScienceDB;uid=root;pwd=your_password;"; 

    public PublisherForm()
    {
        InitializeComponent();
        LoadPublishers(); // Example of loading data when the form initializes
    }

    private void LoadPublishers()
    {
        // This method demonstrates how to retrieve and display publishers
        try
        {
            using (MySqlConnection connection = new MySqlConnection(connectionString))
