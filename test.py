import ctypes
import requests
from io import BytesIO
from PIL import Image

def change_wallpaper_from_url(image_url):
    try:
        response = requests.get(image_url)
        response.raise_for_status()

        image = Image.open(BytesIO(response.content))
        bmp_path = "temp_wallpaper.bmp"
        image.save(bmp_path, "BMP")

        ctypes.windll.user32.SystemParametersInfoW(20, 0, bmp_path, 0)
        return "Hình nền đã được thay đổi!"
    except Exception as e:
        return f"Đã xảy ra lỗi: {str(e)}"
