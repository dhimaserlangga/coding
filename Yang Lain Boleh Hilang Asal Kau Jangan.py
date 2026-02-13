import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.08):
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
        ("Yang lain boleh hilang, asal kau jangan", 0.15),
        ("Dunia boleh sepi, asal kau di sini", 0.14),
        ("Melihatmu tersenyum, hangat hatiku", 0.14),
        ("Semoga begitu pun kau padaku", 0.15)
    ]    
    
    delays = [
        0.5,   
        8.5,    
        16.5,  
        24.5    
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