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
        ("Selaluuuu", 0.10),
        ("Ada pelangi", 0.14),
        ("Pada setiap mendungnya", 0.10),
        ("Setiap derita", 0.10),
        ("Ku kan ada", 0.10),
        ("Slalu untukmuuuu", 0.10),
        ("Temani setiap derita", 0.10),
        ("Jadi pelukan ternyaman untukmu", 0.12)
    ]    
    
    delays = [
        0.5,   
        4.0,   
        8.5,   
        13.0,  
        15.5,  
        19.5,
        24.0,
        28.0   
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