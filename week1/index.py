# CryptoBuddy: A rule-based cryptocurrency advisor bot

# 1. Define the crypto database
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8
    }
}

# 2. Define naimacrypyo's tone and responses
def greet_user():
    print("👋 Hey there! I’m naimacrypto. Let’s find you a green and growing crypto! 🚀")

def get_user_input():
    return input("💬 Ask me about crypto advice (e.g., most sustainable, best long-term): ").lower()

# 3. Analyze user queries
def analyze_query(query):
    if "sustainable" in query:
        best = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print(f"🌱 Invest in {best}! It’s eco-friendly and has long-term potential!")
    
    elif "trending" in query or "rising" in query:
        rising_coins = [k for k in crypto_db if crypto_db[k]["price_trend"] == "rising"]
        print("📈 Trending Up:")
        for coin in rising_coins:
            print(f" - {coin}")
    
    elif "long-term" in query or "growth" in query:
        for name, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] >= 7:
                print(f"💡 {name} is trending up and has a top-tier sustainability score!")
                return
        print("⚠️ No perfect match found, but consider coins with rising trends.")
    
    else:
        print("❓ I’m not sure what you mean. Try asking about ‘sustainable’, ‘trending’, or ‘long-term’.")

# 4. Run chatbot
def run_chatbot():
    greet_user()
    while True:
        user_query = get_user_input()
        if user_query in ["exit", "quit"]:
            print("👋 Goodbye! Remember: crypto is risky—always do your own research!")
            break
        analyze_query(user_query)

run_chatbot()
