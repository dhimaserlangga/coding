import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    print("")
    
    lyrics = [
        ("Terbawa lagi langkahku ke sana", 0.10),
        ("Mantra apa entah yang istimewa", 0.10),
        ("Ku percaya selalu ada", 0.10),
        ("Sesuatu di Jogja\n", 0.10),
        ("Dengar lagu lama, ini katanya", 0.10),
        ("Izinkan aku pulang ke kotamu", 0.10),
        ("Ku percaya selalu ada", 0.12),
        ("Sesuatu di Jogja", 0.10)
    ]    
    delays = [
        0.5,  
        4.5,  
        9.5,   
        14.0,
        19.5,  
        24.5,  
        28.0,  
        32.5
    ]

    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()
    print("")