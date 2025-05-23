import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import mysql.connector
from datetime import datetime

class BiomedicalResearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LifeScienceDB")
        self.root.geometry("1200x800")
        self.root.state('zoomed')  # Start maximized
        
        # Database connection
        self.db_connect()
        
        # Load images
        self.load_images()
        
        # Create UI
        self.create_main_frame()
        self.create_login_frame()
        
        # Start with login screen
        self.show_login()
    
    def db_connect(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Karem606",
                database="LifeScienceDB"
            )
            self.cursor = self.conn.cursor(dictionary=True)
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to connect to database: {str(e)}")
            self.root.destroy()
    
    def load_images(self):
        try:
            # Use a placeholder image path - replace with your actual image
            self.bg_image = Image.open("biomedical_bg.jpg")  # Replace with your image path
            self.bg_image = self.bg_image.resize((1200, 800), Image.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        except Exception as e:
            print(f"Error loading image: {e}")
            self.bg_photo = None
    
    def create_main_frame(self):
        self.main_frame = tk.Frame(self.root)
        
        # Header
        header_frame = tk.Frame(self.main_frame, bg="#2c3e50", height=80)
        header_frame.pack(fill=tk.X)
        
        self.header_label = tk.Label(
            header_frame, 
            text="Life Science Research Database", 
            font=("Segoe UI", 20, "bold"), 
            fg="white", 
            bg="#2c3e50"
        )
        self.header_label.pack(side=tk.LEFT, padx=20)
        
        self.user_label = tk.Label(
            header_frame, 
            text="", 
            font=("Segoe UI", 12), 
            fg="white", 
            bg="#2c3e50"
        )
        self.user_label.pack(side=tk.RIGHT, padx=20)
        
        logout_btn = tk.Button(
            header_frame, 
            text="Logout", 
            command=self.show_login,
            font=("Segoe UI", 10),
            bg="#e74c3c",
            fg="white",
            relief=tk.FLAT
        )
        logout_btn.pack(side=tk.RIGHT, padx=10)
        
        # Content area
        self.content_frame = tk.Frame(self.main_frame)
        self.content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Background image label
        if self.bg_photo:
            self.bg_label = tk.Label(self.content_frame, image=self.bg_photo)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Notebook for tabs
        self.notebook = ttk.Notebook(self.content_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    def create_login_frame(self):
        self.login_frame = tk.Frame(self.root, bg="#f0f4f7")
        
        if self.bg_photo:
            bg_label = tk.Label(self.login_frame, image=self.bg_photo)
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        login_container = tk.Frame(self.login_frame, bg="white", padx=30, pady=30)
        login_container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        tk.Label(
            login_container, 
            text="Life Science Research Database", 
            font=("Segoe UI", 18, "bold"),
            bg="white"
        ).pack(pady=(0, 20))
        
        tk.Label(
            login_container, 
            text="Login", 
            font=("Segoe UI", 14),
            bg="white"
        ).pack()
        
        # Username
        tk.Label(
            login_container, 
            text="Username:", 
            font=("Segoe UI", 10),
            bg="white"
        ).pack(anchor=tk.W, pady=(10, 0))
        self.username_entry = ttk.Entry(login_container, width=30)
        self.username_entry.pack()
        
        # Password
        tk.Label(
            login_container, 
            text="Password:", 
            font=("Segoe UI", 10),
            bg="white"
        ).pack(anchor=tk.W, pady=(10, 0))
        self.password_entry = ttk.Entry(login_container, width=30, show="*")
        self.password_entry.pack()
        
        # Login button
        login_btn = tk.Button(
            login_container, 
            text="Login", 
            command=self.authenticate,
            font=("Segoe UI", 10),
            bg="#3498db",
            fg="white",
            relief=tk.FLAT,
            padx=20,
            pady=5
        )
        login_btn.pack(pady=20)
        
        # Demo credentials
        tk.Label(
            login_container, 
            text="(Use 'admin' or 'user' for demo)", 
            font=("Segoe UI", 8),
            bg="white",
            fg="gray"
        ).pack()
    
    def authenticate(self):
        username = self.username_entry.get()
        password = self.password_entry.get()  # In real app, hash and verify properly
        
        # Demo authentication - replace with real authentication
        if username in ['admin', 'user']:
            self.current_user = username
            self.user_label.config(text=f"Welcome, {username.capitalize()}")
            self.show_main()
            self.setup_ui_based_on_role()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")
    
    def show_login(self):
        self.main_frame.pack_forget()
        self.login_frame.pack(fill=tk.BOTH, expand=True)
        self.username_entry.focus_set()
    
    def show_main(self):
        self.login_frame.pack_forget()
        self.main_frame.pack(fill=tk.BOTH, expand=True)
    
    def setup_ui_based_on_role(self):
        # Clear existing tabs
        for tab in self.notebook.tabs():
            self.notebook.forget(tab)
        
        # Common tabs for all users
        self.create_research_view_tab()
        self.create_journals_view_tab()
        self.create_authors_view_tab()
        
        # Admin-only tabs
        if self.current_user == 'admin':
            self.create_admin_tabs()
    
    def create_research_view_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Research Papers")
        
        # Search frame
        search_frame = ttk.Frame(tab)
        search_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(search_frame, text="Search:").pack(side=tk.LEFT)
        self.research_search_entry = ttk.Entry(search_frame, width=40)
        self.research_search_entry.pack(side=tk.LEFT, padx=5)
        self.research_search_entry.bind("<KeyRelease>", self.search_research)
        
        ttk.Button(
            search_frame, 
            text="Search", 
            command=self.search_research
        ).pack(side=tk.LEFT)
        
        # Treeview for research papers
        columns = ("ID", "Title", "Journal", "Date", "Citations", "Authors")
        self.research_tree = ttk.Treeview(
            tab, 
            columns=columns, 
            show="headings",
            selectmode="browse"
        )
        
        for col in columns:
            self.research_tree.heading(col, text=col)
            self.research_tree.column(col, width=120, anchor=tk.W)
        
        self.research_tree.column("Title", width=250)
        self.research_tree.column("Authors", width=200)
        
        scrollbar = ttk.Scrollbar(tab, orient=tk.VERTICAL, command=self.research_tree.yview)
        self.research_tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.research_tree.pack(fill=tk.BOTH, expand=True)
        
        # Details frame
        details_frame = ttk.Frame(tab)
        details_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.research_details = tk.Text(
            details_frame, 
            wrap=tk.WORD, 
            height=8,
            font=("Segoe UI", 10)
        )
        scrollbar = ttk.Scrollbar(details_frame, orient=tk.VERTICAL, command=self.research_details.yview)
        self.research_details.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.research_details.pack(fill=tk.BOTH, expand=True)
        
        # Load data
        self.load_research_data()
        self.research_tree.bind("<<TreeviewSelect>>", self.show_research_details)
    
    def load_research_data(self):
        query = """
        SELECT r.ResearchID, r.Title, j.Name AS JournalName, r.PublicationDate, 
               r.Citations, r.Abstract,
               GROUP_CONCAT(DISTINCT a.Name SEPARATOR ', ') AS Authors
        FROM Research r
        LEFT JOIN Journal j ON r.JournalISSN = j.ISSN
        LEFT JOIN ResearchAuthor ra ON r.ResearchID = ra.ResearchID
        LEFT JOIN Author a ON ra.AuthorID = a.AuthorID
        GROUP BY r.ResearchID
        ORDER BY r.PublicationDate DESC
        """
        
        self.cursor.execute(query)
        research_papers = self.cursor.fetchall()
        
        self.research_tree.delete(*self.research_tree.get_children())
        
        for paper in research_papers:
            self.research_tree.insert("", tk.END, values=(
                paper['ResearchID'],
                paper['Title'],
                paper['JournalName'],
                paper['PublicationDate'].strftime('%Y-%m-%d') if paper['PublicationDate'] else '',
                paper['Citations'],
                paper['Authors']
            ))
    
    def search_research(self, event=None):
        search_term = self.research_search_entry.get()
        
        query = """
        SELECT r.ResearchID, r.Title, j.Name AS JournalName, r.PublicationDate, 
               r.Citations, r.Abstract,
               GROUP_CONCAT(DISTINCT a.Name SEPARATOR ', ') AS Authors
        FROM Research r
        LEFT JOIN Journal j ON r.JournalISSN = j.ISSN
        LEFT JOIN ResearchAuthor ra ON r.ResearchID = ra.ResearchID
        LEFT JOIN Author a ON ra.AuthorID = a.AuthorID
        WHERE r.Title LIKE %s OR r.Abstract LIKE %s OR a.Name LIKE %s OR j.Name LIKE %s
        GROUP BY r.ResearchID
        ORDER BY r.PublicationDate DESC
        """
        
        self.cursor.execute(query, (f"%{search_term}%", f"%{search_term}%", f"%{search_term}%", f"%{search_term}%"))
        research_papers = self.cursor.fetchall()
        
        self.research_tree.delete(*self.research_tree.get_children())
        
        for paper in research_papers:
            self.research_tree.insert("", tk.END, values=(
                paper['ResearchID'],
                paper['Title'],
                paper['JournalName'],
                paper['PublicationDate'].strftime('%Y-%m-%d') if paper['PublicationDate'] else '',
                paper['Citations'],
                paper['Authors']
            ))
    
    def show_research_details(self, event):
        selected_item = self.research_tree.focus()
        if not selected_item:
            return
            
        item_data = self.research_tree.item(selected_item)
        research_id = item_data['values'][0]
        
        query = """
        SELECT r.*, j.Name AS JournalName,
               GROUP_CONCAT(DISTINCT a.Name SEPARATOR ', ') AS Authors,
               GROUP_CONCAT(DISTINCT f.FieldName SEPARATOR ', ') AS Fields
        FROM Research r
        LEFT JOIN Journal j ON r.JournalISSN = j.ISSN
        LEFT JOIN ResearchAuthor ra ON r.ResearchID = ra.ResearchID
        LEFT JOIN Author a ON ra.AuthorID = a.AuthorID
        LEFT JOIN ResearchField rf ON r.ResearchID = rf.ResearchID
        LEFT JOIN Field f ON rf.FieldID = f.FieldID
        WHERE r.ResearchID = %s
        GROUP BY r.ResearchID
        """
        
        self.cursor.execute(query, (research_id,))
        paper = self.cursor.fetchone()
        
        self.research_details.config(state=tk.NORMAL)
        self.research_details.delete(1.0, tk.END)
        
        if paper:
            details = f"Title: {paper['Title']}\n\n"
            details += f"Journal: {paper['JournalName']}\n"
            details += f"Publication Date: {paper['PublicationDate'].strftime('%B %d, %Y')}\n"
            details += f"Citations: {paper['Citations']}\n\n"
            details += f"Authors: {paper['Authors']}\n"
            details += f"Fields: {paper['Fields']}\n\n"
            details += "Abstract:\n"
            details += paper['Abstract']
            
            self.research_details.insert(tk.END, details)
        
        self.research_details.config(state=tk.DISABLED)
    
    def create_journals_view_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Journals")
        
        # Search frame
        search_frame = ttk.Frame(tab)
        search_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(search_frame, text="Search:").pack(side=tk.LEFT)
        self.journal_search_entry = ttk.Entry(search_frame, width=40)
        self.journal_search_entry.pack(side=tk.LEFT, padx=5)
        self.journal_search_entry.bind("<KeyRelease>", self.search_journals)
        
        ttk.Button(
            search_frame, 
            text="Search", 
            command=self.search_journals
        ).pack(side=tk.LEFT)
        
        # Treeview for journals
        columns = ("ISSN", "Name", "Impact Factor", "Publisher", "Open Access")
        self.journal_tree = ttk.Treeview(
            tab, 
            columns=columns, 
            show="headings",
            selectmode="browse"
        )
        
        for col in columns:
            self.journal_tree.heading(col, text=col)
            self.journal_tree.column(col, width=120, anchor=tk.W)
        
        self.journal_tree.column("Name", width=250)
        self.journal_tree.column("ISSN", width=100)
        
        scrollbar = ttk.Scrollbar(tab, orient=tk.VERTICAL, command=self.journal_tree.yview)
        self.journal_tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.journal_tree.pack(fill=tk.BOTH, expand=True)
        
        # Details frame
        details_frame = ttk.Frame(tab)
        details_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.journal_details = tk.Text(
            details_frame, 
            wrap=tk.WORD, 
            height=6,
            font=("Segoe UI", 10)
        )
        scrollbar = ttk.Scrollbar(details_frame, orient=tk.VERTICAL, command=self.journal_details.yview)
        self.journal_details.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.journal_details.pack(fill=tk.BOTH, expand=True)
        
        # Load data
        self.load_journal_data()
        self.journal_tree.bind("<<TreeviewSelect>>", self.show_journal_details)
    
    def load_journal_data(self):
        query = """
        SELECT j.ISSN, j.Name, j.ImpactFactor, p.Name AS PublisherName, 
               j.OpenAccess, j.Country, j.StartDate, j.VolumeRate,
               GROUP_CONCAT(DISTINCT f.FieldName SEPARATOR ', ') AS Fields
        FROM Journal j
        JOIN Publisher p ON j.PublisherID = p.PublisherID
        LEFT JOIN JournalField jf ON j.ISSN = jf.ISSN
        LEFT JOIN Field f ON jf.FieldID = f.FieldID
        GROUP BY j.ISSN
        ORDER BY j.ImpactFactor DESC
        """
        
        self.cursor.execute(query)
        journals = self.cursor.fetchall()
        
        self.journal_tree.delete(*self.journal_tree.get_children())
        
        for journal in journals:
            self.journal_tree.insert("", tk.END, values=(
                journal['ISSN'],
                journal['Name'],
                journal['ImpactFactor'],
                journal['PublisherName'],
                "Yes" if journal['OpenAccess'] else "No"
            ))
    
    def search_journals(self, event=None):
        search_term = self.journal_search_entry.get()
        
        query = """
        SELECT j.ISSN, j.Name, j.ImpactFactor, p.Name AS PublisherName, 
               j.OpenAccess, j.Country, j.StartDate, j.VolumeRate,
               GROUP_CONCAT(DISTINCT f.FieldName SEPARATOR ', ') AS Fields
        FROM Journal j
        JOIN Publisher p ON j.PublisherID = p.PublisherID
        LEFT JOIN JournalField jf ON j.ISSN = jf.ISSN
        LEFT JOIN Field f ON jf.FieldID = f.FieldID
        WHERE j.Name LIKE %s OR p.Name LIKE %s OR f.FieldName LIKE %s
        GROUP BY j.ISSN
        ORDER BY j.ImpactFactor DESC
        """
        
        self.cursor.execute(query, (f"%{search_term}%", f"%{search_term}%", f"%{search_term}%"))
        journals = self.cursor.fetchall()
        
        self.journal_tree.delete(*self.journal_tree.get_children())
        
        for journal in journals:
            self.journal_tree.insert("", tk.END, values=(
                journal['ISSN'],
                journal['Name'],
                journal['ImpactFactor'],
                journal['PublisherName'],
                "Yes" if journal['OpenAccess'] else "No"
            ))
    
    def show_journal_details(self, event):
        selected_item = self.journal_tree.focus()
        if not selected_item:
            return
            
        item_data = self.journal_tree.item(selected_item)
        issn = item_data['values'][0]
        
        query = """
        SELECT j.*, p.Name AS PublisherName,
               GROUP_CONCAT(DISTINCT f.FieldName SEPARATOR ', ') AS Fields
        FROM Journal j
        JOIN Publisher p ON j.PublisherID = p.PublisherID
        LEFT JOIN JournalField jf ON j.ISSN = jf.ISSN
        LEFT JOIN Field f ON jf.FieldID = f.FieldID
        WHERE j.ISSN = %s
        GROUP BY j.ISSN
        """
        
        self.cursor.execute(query, (issn,))
        journal = self.cursor.fetchone()
        
        self.journal_details.config(state=tk.NORMAL)
        self.journal_details.delete(1.0, tk.END)
        
        if journal:
            details = f"Journal: {journal['Name']}\n"
            details += f"ISSN: {journal['ISSN']}\n"
            details += f"Publisher: {journal['PublisherName']}\n"
            details += f"Impact Factor: {journal['ImpactFactor']}\n"
            details += f"Fields: {journal['Fields']}\n"
            details += f"Country: {journal['Country']}\n"
            details += f"Start Date: {journal['StartDate'].strftime('%Y')}\n"
            details += f"Volume Rate: {journal['VolumeRate']}\n"
            details += f"Open Access: {'Yes' if journal['OpenAccess'] else 'No'}"
            
            self.journal_details.insert(tk.END, details)
        
        self.journal_details.config(state=tk.DISABLED)
    
    def create_authors_view_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Authors")
        
        # Search frame
        search_frame = ttk.Frame(tab)
        search_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(search_frame, text="Search:").pack(side=tk.LEFT)
        self.author_search_entry = ttk.Entry(search_frame, width=40)
        self.author_search_entry.pack(side=tk.LEFT, padx=5)
        self.author_search_entry.bind("<KeyRelease>", self.search_authors)
        
        ttk.Button(
            search_frame, 
            text="Search", 
            command=self.search_authors
        ).pack(side=tk.LEFT)
        
        # Treeview for authors
        columns = ("ID", "Name", "Affiliation", "H-Index", "Fields")
        self.author_tree = ttk.Treeview(
            tab, 
            columns=columns, 
            show="headings",
            selectmode="browse"
        )
        
        for col in columns:
            self.author_tree.heading(col, text=col)
            self.author_tree.column(col, width=120, anchor=tk.W)
        
        self.author_tree.column("Name", width=200)
        self.author_tree.column("Affiliation", width=250)
        self.author_tree.column("Fields", width=200)
        
        scrollbar = ttk.Scrollbar(tab, orient=tk.VERTICAL, command=self.author_tree.yview)
        self.author_tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.author_tree.pack(fill=tk.BOTH, expand=True)
        
        # Details frame
        details_frame = ttk.Frame(tab)
        details_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.author_details = tk.Text(
            details_frame, 
            wrap=tk.WORD, 
            height=6,
            font=("Segoe UI", 10)
        )
        scrollbar = ttk.Scrollbar(details_frame, orient=tk.VERTICAL, command=self.author_details.yview)
        self.author_details.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.author_details.pack(fill=tk.BOTH, expand=True)
        
        # Load data
        self.load_author_data()
        self.author_tree.bind("<<TreeviewSelect>>", self.show_author_details)
    
    def load_author_data(self):
        query = """
        SELECT a.AuthorID, a.Name, a.Affiliation, a.HIndex, a.Qualification, a.JobTitle, a.Email,
               GROUP_CONCAT(DISTINCT f.FieldName SEPARATOR ', ') AS Fields
        FROM Author a
        LEFT JOIN AuthorField af ON a.AuthorID = af.AuthorID
        LEFT JOIN Field f ON af.FieldID = f.FieldID
        GROUP BY a.AuthorID
        ORDER BY a.HIndex DESC
        """
        
        self.cursor.execute(query)
        authors = self.cursor.fetchall()
        
        self.author_tree.delete(*self.author_tree.get_children())
        
        for author in authors:
            self.author_tree.insert("", tk.END, values=(
                author['AuthorID'],
                author['Name'],
                author['Affiliation'],
                author['HIndex'],
                author['Fields']
            ))
    
    def search_authors(self, event=None):
        search_term = self.author_search_entry.get()
        
        query = """
        SELECT a.AuthorID, a.Name, a.Affiliation, a.HIndex, a.Qualification, a.JobTitle, a.Email,
               GROUP_CONCAT(DISTINCT f.FieldName SEPARATOR ', ') AS Fields
        FROM Author a
        LEFT JOIN AuthorField af ON a.AuthorID = af.AuthorID
        LEFT JOIN Field f ON af.FieldID = f.FieldID
        WHERE a.Name LIKE %s OR a.Affiliation LIKE %s OR f.FieldName LIKE %s
        GROUP BY a.AuthorID
        ORDER BY a.HIndex DESC
        """
        
        self.cursor.execute(query, (f"%{search_term}%", f"%{search_term}%", f"%{search_term}%"))
        authors = self.cursor.fetchall()
        
        self.author_tree.delete(*self.author_tree.get_children())
        
        for author in authors:
            self.author_tree.insert("", tk.END, values=(
                author['AuthorID'],
                author['Name'],
                author['Affiliation'],
                author['HIndex'],
                author['Fields']
            ))
    
    def show_author_details(self, event):
        selected_item = self.author_tree.focus()
        if not selected_item:
            return
            
        item_data = self.author_tree.item(selected_item)
        author_id = item_data['values'][0]
        
        query = """
        SELECT a.*, 
               GROUP_CONCAT(DISTINCT f.FieldName SEPARATOR ', ') AS Fields,
               COUNT(DISTINCT r.ResearchID) AS PaperCount
        FROM Author a
        LEFT JOIN AuthorField af ON a.AuthorID = af.AuthorID
        LEFT JOIN Field f ON af.FieldID = f.FieldID
        LEFT JOIN ResearchAuthor ra ON a.AuthorID = ra.AuthorID
        LEFT JOIN Research r ON ra.ResearchID = r.ResearchID
        WHERE a.AuthorID = %s
        GROUP BY a.AuthorID
        """
        
        self.cursor.execute(query, (author_id,))
        author = self.cursor.fetchone()
        
        self.author_details.config(state=tk.NORMAL)
        self.author_details.delete(1.0, tk.END)
        
        if author:
            details = f"Name: {author['Name']}\n"
            details += f"Qualification: {author['Qualification']}\n"
            details += f"Affiliation: {author['Affiliation']}\n"
            details += f"Job Title: {author['JobTitle']}\n"
            details += f"Email: {author['Email']}\n"
            details += f"H-Index: {author['HIndex']}\n"
            details += f"Fields: {author['Fields']}\n"
            details += f"Published Papers: {author['PaperCount']}"
            
            self.author_details.insert(tk.END, details)
        
        self.author_details.config(state=tk.DISABLED)
    
    def create_admin_tabs(self):
        # Publisher management tab
        self.create_publisher_admin_tab()
        
        # Journal management tab
        self.create_journal_admin_tab()
        
        # Author management tab
        self.create_author_admin_tab()
        
        # Research management tab
        self.create_research_admin_tab()
    
    def create_publisher_admin_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Manage Publishers")
        
        # Form frame
        form_frame = ttk.Frame(tab)
        form_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(form_frame, text="Publisher Name:").grid(row=0, column=0, sticky=tk.W)
        self.publisher_name_entry = ttk.Entry(form_frame, width=40)
        self.publisher_name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(form_frame, text="Publisher ID:").grid(row=1, column=0, sticky=tk.W)
        self.publisher_id_entry = ttk.Entry(form_frame, width=40)
        self.publisher_id_entry.grid(row=1, column=1, padx=5, pady=5)
        
        button_frame = ttk.Frame(form_frame)
        button_frame.grid(row=2, column=0, columnspan=2, pady=10)
        
        ttk.Button(button_frame, text="Add", command=self.add_publisher).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Update", command=self.update_publisher).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Delete", command=self.delete_publisher).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_publisher_form).pack(side=tk.LEFT, padx=5)
        
        # List frame
        list_frame = ttk.Frame(tab)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        columns = ("ID", "Name")
        self.publisher_tree = ttk.Treeview(
            list_frame, 
            columns=columns, 
            show="headings",
            selectmode="browse"
        )
        
        for col in columns:
            self.publisher_tree.heading(col, text=col)
            self.publisher_tree.column(col, width=120, anchor=tk.W)
        
        self.publisher_tree.column("Name", width=300)
        
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.publisher_tree.yview)
        self.publisher_tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.publisher_tree.pack(fill=tk.BOTH, expand=True)
        
        self.publisher_tree.bind("<<TreeviewSelect>>", self.load_publisher_data)
        
        # Load data
        self.load_publishers()
    
    def load_publishers(self):
        query = "SELECT * FROM Publisher ORDER BY Name"
        self.cursor.execute(query)
        publishers = self.cursor.fetchall()
        
        self.publisher_tree.delete(*self.publisher_tree.get_children())
        
        for publisher in publishers:
            self.publisher_tree.insert("", tk.END, values=(
                publisher['PublisherID'],
                publisher['Name']
            ))
    
    def load_publisher_data(self, event):
        selected_item = self.publisher_tree.focus()
        if not selected_item:
            return
            
        item_data = self.publisher_tree.item(selected_item)
        self.publisher_id_entry.delete(0, tk.END)
        self.publisher_name_entry.delete(0, tk.END)
        
        self.publisher_id_entry.insert(0, item_data['values'][0])
        self.publisher_name_entry.insert(0, item_data['values'][1])
    
    def add_publisher(self):
        name = self.publisher_name_entry.get()
        publisher_id = self.publisher_id_entry.get()
        
        if not name:
            messagebox.showwarning("Input Error", "Please enter publisher name")
            return
        
        try:
            query = "INSERT INTO Publisher (PublisherID, Name) VALUES (%s, %s)"
            self.cursor.execute(query, (publisher_id, name))
            self.conn.commit()
            messagebox.showinfo("Success", "Publisher added successfully")
            self.load_publishers()
            self.clear_publisher_form()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add publisher: {str(e)}")
    
    def update_publisher(self):
        selected_item = self.publisher_tree.focus()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a publisher to update")
            return
            
        publisher_id = self.publisher_id_entry.get()
        name = self.publisher_name_entry.get()
        
        if not name:
            messagebox.showwarning("Input Error", "Please enter publisher name")
            return
        
        try:
            query = "UPDATE Publisher SET Name = %s WHERE PublisherID = %s"
            self.cursor.execute(query, (name, publisher_id))
            self.conn.commit()
            messagebox.showinfo("Success", "Publisher updated successfully")
            self.load_publishers()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update publisher: {str(e)}")
    
    def delete_publisher(self):
        selected_item = self.publisher_tree.focus()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a publisher to delete")
            return
            
        if not messagebox.askyesno("Confirm", "Are you sure you want to delete this publisher?"):
            return
            
        publisher_id = self.publisher_id_entry.get()
        
        try:
            query = "DELETE FROM Publisher WHERE PublisherID = %s"
            self.cursor.execute(query, (publisher_id,))
            self.conn.commit()
            messagebox.showinfo("Success", "Publisher deleted successfully")
            self.load_publishers()
            self.clear_publisher_form()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete publisher: {str(e)}")
    
    def clear_publisher_form(self):
        self.publisher_id_entry.delete(0, tk.END)
        self.publisher_name_entry.delete(0, tk.END)
    
    def create_journal_admin_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Manage Journals")
        
        # Form frame
        form_frame = ttk.Frame(tab)
        form_frame.pack(fill=tk.X, padx=10, pady=10)
        
      
    def create_author_admin_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Manage Authors")
        
        # Form frame
        form_frame = ttk.Frame(tab)
        form_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Create all the form fields for author management
        # Similar to publisher tab but with more fields
        # Implement CRUD operations for authors
    
    def create_research_admin_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Manage Research")
        
        # Form frame
        form_frame = ttk.Frame(tab)
        form_frame.pack(fill=tk.X, padx=10, pady=10)
        
       

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = BiomedicalResearchApp(root)
    root.mainloop()


