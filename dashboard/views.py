from django.shortcuts import render
from django.http import JsonResponse
from dashboard.firebase_config import get_database

def dashboard(request):
    """
    Render the dashboard page.
    """
    return render(request, 'dashboard/index.html')


def get_sensor_data(request):
    """
    Fetch data from Firebase and return it as JSON.
    """
    try:
        print("Fetching data from Firebase...")
        
        # Get Firebase database reference
        ref = get_database().child('sensors')
        data = ref.get()
        print("Data received from Firebase:", data)

        if not data:
            return JsonResponse({"message": "No data found"}, status=404)

        formatted_data = [
            {
                "timestamp": value.get("timestamp"),
                "distance": value.get("distance"),
                "mq4": value.get("mq4"),
                "mq135": value.get("mq135"),
                "temperature": value.get("temperature"),
                "humidity": value.get("humidity"),
            }
            for key, value in data.items()
        ]

        return JsonResponse(formatted_data, safe=False)

    except Exception as e:
        print("Error occurred:", e)
        return JsonResponse({"error": str(e)}, status=500)
