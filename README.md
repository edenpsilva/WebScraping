# Web Scraper
Several Python scripts to web scraper

This is a small project to scrapping a toy webpages. These pags works like a bookstore.
The aim in this project is to capture
1. The book's name
2. The book's category
3. The rate of the books
4. The book's price
5. If the book is available or not in the store

And finally. ingest this informatoin into a database.
This project is base on: https://medium.com/@meigarom/o-projeto-de-data-engineering-para-o-seu-portf%C3%B3lio-c186c7191823

## My implementation

On the first cycle, I implemented a solution using two main files: 
- util.py - that contains several functions to get information from the page
- Web Scraping.py  - that contais the functions to navegate into the webpages and the code to save the collected data into a database

db_creation - the tird file in this project is responsable to the database creation. Considering a SQLite database.

The project is implemented using Pyhton and SQL. 
1. Selenium for Python was used to navegate between the pages
2. BeautifulSoup was used to collect the information in the page
3. sqlite3 - was used to connect with the database
4. SQL  was used to insert the data into the database

Future imporvments

1. To change the SQLite by a more deployment database as SQLPostgre os MySQL
2. To create a script or apply Airflow to automatize the ingestion process
