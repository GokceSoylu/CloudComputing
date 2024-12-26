import requests
import json
from datetime import datetime, timedelta

# USGS API endpoint
USGS_API_URL = "https://earthquake.usgs.gov/fdsnws/event/1/query"

def fetch_earthquake_data(start_time, end_time, min_magnitude, max_magnitude, output_file):
    """
    USGS API'den deprem verilerini çeker ve JSON dosyasına kaydeder.
    """
    params = {
        "format": "geojson",
        "starttime": start_time,
        "endtime": end_time,
        "minmagnitude": min_magnitude,
        "maxmagnitude": max_magnitude
    }

    try:
        # API isteği gönder
        response = requests.get(USGS_API_URL, params=params)
        response.raise_for_status()  # Hata kontrolü

        # Yanıtı JSON formatında işleme
        data = response.json()

        # JSON dosyasına kaydet
        with open(output_file, "w") as file:
            json.dump(data, file, indent=4)

        print(f"Veriler '{output_file}' dosyasına kaydedildi.")
    except requests.exceptions.RequestException as e:
        print(f"API isteği başarısız oldu: {e}")

# Örnek kullanım
if __name__ == "__main__":
    # Geçtiğimiz bir haftalık depremleri çek
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=7)

    fetch_earthquake_data(
        start_time=start_date.strftime("%Y-%m-%d"),
        end_time=end_date.strftime("%Y-%m-%d"),
        min_magnitude=4.0,  # Minimum büyüklük
        max_magnitude=10.0, # Maksimum büyüklük
        output_file="earthquake_data.json"
    )
