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
    lyrics = [
        # Stanza 1
        ("Sudahlah", 0.20),
        ("kali ini aku kalah", 0.15),
        ("Kehilangan mahkota", 0.15),
        ("Kau dan dia pemenangnya\n", 0.15),
        # Stanza 2
        ("Sudahlah", 0.20),
        ("kali ini ku berserah", 0.15),
        ("Kehilangan segalanya", 0.15),
        ("Kau dan dia pemenangnya", 0.15)
    ]
    
    delays = [1.0, 4.0, 8.5, 13.0, 21.5, 24.0, 28.5, 33.0]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
     
    for thread in threads:
        thread.join()
    
    time.sleep(1.0)
    print("")

if __name__ == "__main__":
    sing_song()