limit_humi = input("허용 습도:").split(" ")
print(limit_humi[0])

while True:
    now = input("현재 습도 확인 :")
    if now == "-999":
        print("끝!")
        break;
    elif now <= limit_humi[1] and limit_humi[0] <= now:
        print("Humidity OK")
    else:
        print("Warning!")
        break;
        