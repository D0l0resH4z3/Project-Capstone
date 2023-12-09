import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import re
from datetime import datetime
from firebase_admin import credentials, firestore, initialize_app

# Firebase credentials
cred = credentials.Certificate({
    "type": "",
            "project_id": "",
            "private_key_id": "",
            "private_key": "",
            "client_email": "",
            "client_id": "",
            "auth_uri": "",
            "token_uri": "",
            "auth_provider_x509_cert_url": "",
            "client_x509_cert_url": "",
            "universe_domain": ""
})

initialize_app(cred)

# Function to create the necessary collection if it doesn't exist
def create_collection_if_not_exists(db):
    try:
        db.collection(u'scraped_data')
    except Exception as e:
        print(f"Error creating collection: {e}")

# Function to check if scraping is allowed on a website
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

# Function to scrape website content
def scrape_website_content(url, db):
    try:
        if not is_scraping_allowed(url):
            print("\nWeb scraping is not allowed on this website.")
            return
        else:
            print("\nWeb scraping is allowed on this website.")

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

            try:
                print("\nScraping data...")
                for element in data:
                    content = element.text.strip()
                    if content:
                        # Add data to Firebase
                        db.collection(u'scraped_data').add({
                            'url': url,
                            'tag': tag,
                            'date': datetime.now().strftime('%Y-%m-%d'),
                            'time': datetime.now().strftime('%H:%M'),
                            'content': content
                        })

                print(f"\nScraped data has been stored in Firebase.\n")

            except Exception as e:
                print(f"Error processing data: {e}")

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
    # Establish a connection to the Firebase database
    db = firestore.client()

    # Create the 'scraped_data' collection if it doesn't exist
    create_collection_if_not_exists(db)

    while True:
        print("\n1. Scrape content from a website")
        print("2. Exit")

        choice1 = input("\nEnter your choice : ")

        if choice1 == "1":
            url = input("\nEnter the website URL: ")
            scrape_website_content(url, db)

        elif choice1 == "2":
            print("\nExiting...\n")
            break
        else:
            print("\nInvalid choice !!!")
