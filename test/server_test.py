import requests
import time

def test_flask_app():
    print("ממתין לשרת Flask...")
    time.sleep(20)  # זמן סביר יותר
    
    try:
        # בדיקה 1: דף הבית
        print("בודק דף הבית...")
        home_response = requests.get("http://flask_app:5000/")
        print(f"דף הבית: {home_response.status_code}")
        
        # בדיקה 2: הוספת משימה
        print("מוסיף משימה...")
        url = "http://flask_app:5000/add"
        data = {"title": "new task"}
        response = requests.post(url, data=data)
        print(f" new task: {response.status_code}")
        
        # בדיקה 3: משימה שנייה
        data2 = {"title": "new task"}
        response2 = requests.post(url, data=data2)
        print(f"second task: {response2.status_code}")
        
        print("✅ the tests are done!")
        
    except Exception as e:
        print(f"❌ error in test: {e}")

if __name__ == "__main__":
    test_flask_app()