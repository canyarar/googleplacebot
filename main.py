import requests
import json
 
# Google Places API Key
api_key = "YOUR_API_KEY"
 
# İşletme adı
place_name = "business_name"
 
# İşletmenin bulunduğu yer
location = "business_location"
 
# API isteği URL'si
url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={place_name}+in+{location}&key={api_key}"
 
# API isteği
response = requests.get(url)
 
# JSON verisi
data = response.json()
 
# İşletme detayları
place_id = data["results"][0]["place_id"]
 
# İşletme detayı API isteği URL'si
details_url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&key={api_key}"
 
# İşletme detayı API isteği
details_response = requests.get(details_url)
 
# İşletme detayı JSON verisi
details_data = details_response.json()
 
# İşletme adı
business_name = details_data["result"]["name"]
 
# İşletme adresi
business_address = details_data["result"]["formatted_address"]
 
# İşletme telefon numarası
business_phone = details_data["result"]["formatted_phone_number"]
 
# İşletme kategorisi
business_category = details_data["result"]["types"][0]
 
# İşletme fotoğraf URL'leri
business_photos = [photo["photo_reference"] for photo in details_data["result"]["photos"]]
 
# İşletme bilgileri
business_info = {
    "name": business_name,
    "address": business_address,
    "phone": business_phone,
    "category": business_category,
    "photos": business_photos
}
 
print(business_info)
