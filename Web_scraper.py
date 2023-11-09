import requests
from bs4 import BeautifulSoup

print("=" * 50)

# Function to scrape content from a website
def scrape_website_content(url):
    try:
        while True:
            # Send an HTTP GET request to the URL
            response = requests.get(url)
            response.raise_for_status()

            
            soup = BeautifulSoup(response.text, 'html.parser')

            tag = input("\nEnter the HTML tag (e.g., 'div', 'p', 'h1', etc.): ")
            

            
            elements = soup.find_all(tag)
            
            
            for element in elements:
                print(element.text)

            
            if not elements:
                print("\nNo data found !!!\n")
            choice2 = input("\nDo you want to scrape more content on this website (Y/N): ")
            if choice2.lower() == "y":
                continue
            elif choice2.lower() == "n":
                break
            else:
                print("\nInvalid choice. Please select 'Y' or 'N'.")

            

    except requests.exceptions.RequestException as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    while True:
        print("\n---Web Scraper---\n")
        print("1. Scrape content from a website")
        print("2. Exit")

        choice1 = input("\nEnter your choice (1/2): ")

        if choice1 == "1":
            # Take user input for the website URL
            url = input("\nEnter the website URL: ")

            # Call the scrape_website_content function with user input
            scrape_website_content(url)

        elif choice1 == "2":
            print("\nExiting...\n")
            break
        else:
            print("\nInvalid choice. Please select 1 or 2.")
