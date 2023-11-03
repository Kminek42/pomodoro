import time
import simpleaudio as sa
import datetime

file = open("config.txt", "r")
data = file.read()
file.close()

lesson_time = int(data.split()[1])
short_break_time = int(data.split()[3])
long_break_time = int(data.split()[5])
long_break_interval = int(data.split()[7])

wave_obj = sa.WaveObject.from_wave_file("./alarm.wav")

t0 = time.time()

def save_stat(filename, description):
    formatted_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file = open(".stats.txt", "a")
    file.write(f"{formatted_datetime} {description}\n")
    file.close()


def block(block_name, duration):
    t0 = time.time()

    wave_obj.play()
    print(f"{block_name} [{duration}min]")

    while time.time() - t0 < duration * 60:
        time.sleep(1)
        if int(time.time()) % 10 == 0:
            save_stat("stats.txt", block_name)

break_n = 0

while 2137:
    # lesson
    block("lesson", lesson_time)

    # break
    break_n += 1
    if break_n % long_break_interval:
        block("break", short_break_time)

    else:
        block("break", long_break_time)
