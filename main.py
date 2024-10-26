# main.py
import asyncio
from scraper import scrape_website
from chatbot import SimpleChatbot

async def main():
    chatbot = SimpleChatbot()
    
    # List of URLs to scrape
    urls = [
        "https://www.python.org/about/",
        "https://en.wikipedia.org/wiki/Python_(programming_language)",
        "https://en.wikipedia.org/wiki/Wikipedia",
    ]
    
    print("Select a URL to scrape:")
    for i, url in enumerate(urls):
        print(f"{i + 1}: {url}")
    
    while True:
        try:
            choice = int(input("\nEnter the number of your choice (or 0 to exit): "))
            if choice == 0:
                print("Goodbye!")
                break
                
            if 1 <= choice <= len(urls):
                url = urls[choice - 1]
                print(f"\nFetching content from {url}...")
                website_content = scrape_website(url)
                
                if not website_content:
                    print("Failed to fetch content. Please try another URL.")
                    continue
                
                print("\nContent loaded! Ask questions or type 'exit' to quit, 'back' to choose another URL.")
                
                while True:
                    question = input("\nYou: ").strip()
                    
                    if question.lower() == 'exit':
                        print("Goodbye!")
                        return
                    elif question.lower() == 'back':
                        break
                    elif question:
                        answer = await chatbot.ask_question(question, website_content)
                        print(f"Chatbot: {answer}")
                    else:
                        print("Please ask a question!")
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())