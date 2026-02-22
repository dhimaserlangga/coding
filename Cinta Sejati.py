import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.07):
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
        ("Cinta kita melukiskan sejarah", 0.14),
        ("Menggelarkan cerita penuh sukacita", 0.13),
        ("Sehingga siapa pun insan Tuhan pasti tahu", 0.12),
        ("Cinta kita sejati", 0.14)
    ]    
    
    delays = [
        0.5,  
        6.0, 
        12.0,   
        21.5   
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