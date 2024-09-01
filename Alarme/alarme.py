import time
import playsound


def set_alarm(alarm_time):
    print(f"Alarme definido para {alarm_time}")

    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Acorda corno!")
            playsound("alarme.mp3")
            break
            time.sleep(2)


alarm_time = input("Defina a hora do alarme (HH:MM:SS): ")
set_alarm(alarm_time)
