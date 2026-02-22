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
        ("Mengapa takut", 0.11),
        ("Pada lara", 0.11),
        ("Sementara semua rasa", 0.09),
        ("Bisa kita cipta", 0.12),
        ("Akan selalu ada tenang", 0.10),
        ("Disela sela gelisah yang menunggu reda", 0.14)
    ]    
    
    delays = [
        0.5,    
        2.5,     
        6.3,     
        9.3,    
        12.5,    
        15.5     
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