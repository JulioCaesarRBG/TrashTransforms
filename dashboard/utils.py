from firebase_admin import db
from .models import SensorData
from datetime import datetime

def fetch_firebase_data():
    ref = db.reference('/sensors')
    data = ref.get()

    if data:
        for key, value in data.items():
            timestamp = datetime.utcfromtimestamp(value.get('timestamp', 0))
            distance = value.get('distance', 0)
            mq4 = value.get('mq4', 0)
            mq135 = value.get('mq135', 0)
            temperature = value.get('temperature', 0)
            humidity = value.get('humidity', 0)

            if not SensorData.objects.filter(timestamp=timestamp).exists():
                SensorData.objects.create(
                    timestamp=timestamp,
                    distance=distance,
                    mq4=mq4,
                    mq135=mq135,
                    temperature=temperature,
                    humidity=humidity,
                )
