import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import re
from datetime import datetime
import mysql.connector

# Database connection information
db_config = {
    'host': 'host',
    'user': 'user',
    'password': 'password',
    'database': 'database',
}

# Function to establish a connection to the database
def connect_to_database():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    return connection, cursor

# Function to create the necessary table if it doesn't exist
def create_table_if_not_exists():
    create_table_query = """
    CREATE TABLE IF NOT EXISTS scraped_data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        url VARCHAR(255),
        tag VARCHAR(50),
        date VARCHAR(20),
        time VARCHAR(20),
        content TEXT,
        UNIQUE KEY unique_content (content)
    )
    """
    db_cursor.execute(create_table_query)

# Establish a connection to the database
db_connection, db_cursor = connect_to_database()

# Create the 'scraped_data' table if it doesn't exist
create_table_if_not_exists()
db_connection.commit()

print("\nWeb Scraper\n")

printed_content = set()

def is_scraping_allowed(url):
    try:
        parsed_url = urlparse(url)
        robots_txt_url = urljoin(url, '/robots.txt')
        response = requests.get(robots_txt_url)

        if response.status_code == 200:
            robots_content = response.text
            return 'User-agent:' not in robots_content or re.search(r'User-agent: \*', robots_content) is not None
        else:
            return True

    except requests.exceptions.RequestException:
        return True

def scrape_website_content(url, filename):
    try:
        if not is_scraping_allowed(url):
            print("\nWeb scraping is not allowed on this website.")
            return
        else:
            print("\nWeb scraping is allowed on this website.")
        
        with open(filename, 'a', encoding='utf-8') as file:
            # Send an HTTP GET request to the URL
            response = requests.get(url)
            response.raise_for_status()
        
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')
            
            while True:
                tag = input("\nEnter the HTML tag ('div', 'p', 'h1', 'ul', 'li', 'ol', 'table', etc.): ")
                
                if not tag:
                    print("\nInvalid tag. Please enter a valid HTML tag.\n")
                    continue
                
                # Find elements with the specified tag and class
                data = soup.find_all(tag)

                if not data:
                    print("\nNo data found !!!\n")
                    continue

                # Establish a connection to the database
                db_connection, db_cursor = connect_to_database()

                try:
                    print("\nScraping data...")
                    for element in data:
                        content = element.text.strip()
                        if content in printed_content:
                            continue

                        if content:
                            file.write(f"{content}\n")
                            printed_content.add(content)

                        insert_query = "INSERT INTO scraped_data (url, tag, date, time, content) VALUES (%s, %s, %s, %s, %s)"
                        values = (url, tag, datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%H:%M'), content)
                        db_cursor.execute(insert_query, values)

                        for child in element.find_all(tag, recursive=False):
                            child_content = child.text.strip()
                            if child_content and child_content not in printed_content:
                                file.write(f"    {child_content}\n")
                                printed_content.add(child_content)

                    db_connection.commit()
                    print(f"\nScraped data has been stored in the file: {filename}\n")

                except mysql.connector.Error as err:
                    print(f"Error inserting data into the database: {err}")

                finally:
                    if db_connection.is_connected():
                        db_cursor.close()
                        db_connection.close()
                        print("\nDatabase connection closed.")

                while True:
                    choice2 = input("\nDo you want to scrape more content on this website (Y/N): ").lower()
                    if choice2 == "y":
                        break
                    elif choice2 == "n":
                        return
                    else:
                        print("\nInvalid choice. Please select 'Y' or 'N'.")
                        
    except KeyboardInterrupt:
        print("\nExiting...\n")
        exit()
        
    except requests.exceptions.RequestException as e:
        print(f"\nAn error occurred: {e}")
        return

if __name__ == "__main__":
    while True:
        print("\n1. Scrape content from a website")
        print("2. Exit")

        choice1 = input("\nEnter your choice : ")

        if choice1 == "1":
            url = input("\nEnter the website URL: ")
            filename = input("\nEnter the filename to save the scraped data: ")
            scrape_website_content(url, filename)

        elif choice1 == "2":
            print("\nExiting...\n")
            break
        else:
            print("\nInvalid choice !!!")
