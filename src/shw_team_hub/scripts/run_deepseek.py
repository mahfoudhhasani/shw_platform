import os
import requests

def run():
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        print("❌ Missing API key. Exiting.")
        return

    print("✅ DeepSeek script started with API key.")

    # Example request – replace with real DeepSeek API endpoint
    url = "https://api.deepseek.com/endpoint"  # Replace with actual
    headers = {"Authorization": f"Bearer {api_key}"}

    try:
        response = requests.get(url, headers=headers)
        if response.ok:
            print("🎉 Success:", response.json())
        else:
            print("❌ API call failed:", response.status_code, response.text)
    except Exception as e:
        print("❌ Error while calling DeepSeek API:", str(e))

if __name__ == "__main__":
    run()
