import requests
import time
import sys

def test_flask_app():
    time.sleep(20)
    
    try:
        # בדיקה 1: דף הבית
        home_response = requests.get("http://flask_app:5000/")
        print(home_response.status_code)
        
        if home_response.status_code != 200:
            return False
        
        # בדיקה 2: הוספת משימה
        url = "http://flask_app:5000/add"
        data = {"title": "new task"}
        response = requests.post(url, data=data)
        print(response.status_code)
        
        # בדיקה 3: משימה שנייה
        data2 = {"title": "second task"}
        response2 = requests.post(url, data=data2)
        print(response2.status_code)
        
        return True
        
    except Exception as e:
        print(f"ERROR: {e}")
        return False

if __name__ == "__main__":
    success = test_flask_app()
    if success:
        sys.exit(0)
    else:
        sys.exit(1)