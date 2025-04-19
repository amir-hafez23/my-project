import geoip2.database

# مسیر به پایگاه داده GeoLite2-City
geoip_db_path = 'path_to_your_GeoLite2-City.mmdb'

# ایجاد خواننده پایگاه داده
reader = geoip2.database.Reader(geoip_db_path)

def get_location_from_ip(ip_address):
    try:
        # جستجو اطلاعات جغرافیایی برای IP داده شده
        response = reader.city(ip_address)
        
        # استخراج اطلاعات
        country = response.country.name
        city = response.city.name
        latitude = response.location.latitude
        longitude = response.location.longitude
        
        return {
            'ip': ip_address,
            'country': country,
            'city': city,
            'latitude': latitude,
            'longitude': longitude
        }
    except Exception as e:
        return {
            'ip': ip_address,
            'error': str(e)
        }

# مثال استفاده
ip_address = '8.8.8.8'  # جایگزین کنید با IP مورد نظر
location_info = get_location_from_ip(ip_address)
print(location_info)