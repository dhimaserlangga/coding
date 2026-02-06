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
        ("Banyak waktu racun", 0.12),
        ("Tapi diterima", 0.12),
        ("Siapapun aku kau", 0.15),
        ("Tangan yang terbuka", 0.12),
        ("Seeeeembuhkuuuuu", 0.18),
        ("Untukku untukmu untuk kitaaa", 0.17)
    ]   
    
    delays = [
        0.5,  
        4.0,  
        7.5,   
        11.5,   
        17.0,   
        23.5   
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