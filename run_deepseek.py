import os

def run():
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        print("Missing API key. Exiting.")
        return

    print("✅ DeepSeek script started with API key.")
    # Continue your logic here...

if __name__ == "__main__":
    run()
