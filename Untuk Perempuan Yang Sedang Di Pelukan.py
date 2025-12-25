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
        ("Tak terasa gelap pun jatuh", 0.12),
        ("Di ujung malam", 0.09),
        ("Menuju pagi yang dingin", 0.09),
        ("Hanya ada sedikit bintang malam ini", 0.1),
        ("Mungkin karena kau", 0.12),
        ("Sedang cantik-cantiknya", 0.15)
    ]
    delays = [0.5, 7.3, 10.5, 14.0, 19.5, 22.0]
    
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