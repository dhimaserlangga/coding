import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.075):
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
        ("Meski hatiku untuk kamu", 0.12),
        ("Dan hatimu tetap aku", 0.12),
        ("Jangan coba kita tuk bertemu", 0.17),
        ("Takkan sanggup aku bertahan diam", 0.15),
        ("Ingin berlari memelukmu", 0.16),                    
        ("Yang pernah kumiliki", 0.16)
    ]

    delays = [
        0.5, 
        4.5,    
        8.5,    
        15.5,   
        21.0,   
        27.0    
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