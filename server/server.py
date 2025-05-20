import os
import socket
import requests

api_key = os.getenv("OPEN_WEATHER_API")

def get_weather(city):
    if not api_key:
        return "APIキーの設定ミス"

    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric", "lang": "ja"}
    try:
        res = requests.get(url, params=params, timeout=5)
        if res.status_code == 200:
            data = res.json()
            weather = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            return f"{city}の天気: {weather}、気温：{temp}℃"
        else:
            return f"エラー: {city}の天気情報の取得失敗 ({res.status_code})"
    except requests.exceptions.RequestException as e:
        return f"取得失敗: {str(e)}"

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 5000))
    server.listen(1)
    print("待機")

    while True:
        conn, addr = server.accept()
        print(f"接続: {addr}")
        city = conn.recv(1024).decode("utf-8")
        print(f"受け取った地名: {city}")
        result = get_weather(city)
        conn.send(result.encode("utf-8"))
        conn.close()

if __name__ == "__main__":
    main()