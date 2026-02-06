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
        ("Maka terimalah diriku", 0.15),
        ("Kita akan bahagia selamanya", 0.15),
        ("Ku berjanji jadi suamimu", 0.15),
        ("Dan ku akan memberikan yang terbaik untukmu", 0.15)
    ]    
    
    delays = [
        0.5,  
        7.5,   
        15.5,   
        21.0  
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