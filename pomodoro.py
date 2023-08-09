import time
import simpleaudio as sa

t0 = time.time()
lesson_time = 25
short_break_time = 5
long_break_time = 15
long_break_interval = 4
wave_obj = sa.WaveObject.from_wave_file("./alarm.wav")

while 2137:
    for i in range(long_break_interval):
        # lesson
        play_obj = wave_obj.play()
        print(f"Lesson [{lesson_time}min]")
        t1 = time.time()
        while time.time() - t1 < lesson_time * 60:
            time.sleep(1)

        # break
        play_obj = wave_obj.play()
        
        if i != long_break_interval - 1:
            print(f"Break [{short_break_time}min]")
            t1 = time.time()
            while time.time() - t1 < short_break_time * 60:
                time.sleep(1)

        else:
            print(f"Break [{long_break_time}min]")
            t1 = time.time()
            while time.time() - t1 < long_break_time * 60:
                time.sleep(1)