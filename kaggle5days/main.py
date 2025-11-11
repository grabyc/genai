from dotenv import load_dotenv
import os

# load .env from project root
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def main():
    print("Hello from kaggle5days!")
    print("key:", GOOGLE_API_KEY)


if __name__ == "__main__":
    main()
