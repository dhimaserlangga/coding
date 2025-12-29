import time
from threading import Thread, Lock
import sys

# Lock ensures that output from different threads doesn't interfere with each other,
# guaranteeing the lyrics print one line at a time.
lock = Lock()

def animate_text(text, delay=0.1):
    """
    Prints the given text character by character with a delay.
    Requires the global 'lock' to ensure thread-safe writing to stdout.
    """
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print() # Newline after the lyric is fully printed

def sing_lyric(lyric, delay, speed):
    """
    Waits for a specified delay, then starts printing the lyric at the given speed.
    """
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    """
    Defines the lyrics, timing, and speed, then starts all threads simultaneously.
    """
    # Each tuple contains (lyric text, character printing speed in seconds)
    lyrics_data = [
        ("Ceeeeeeriiitaa", 0.15),                                            # Slow start, emphasis
        ("kita tak jauh berbeda", 0.08),
        ("Got beat down by the world", 0.08),
        ("sometimes I wanna fold", 0.08),
        ("Namun suratmu kan ku ceritakan ke anak-anakku nanti", 0.08),      # Faster for the long line
        ("Bahwa aku pernah dicintaiii", 0.08),                              # Slow down, dramatic
        ("with everything you areee", 0.08),                               # Final, gentle finish
    ]

    # Delays (in seconds) before each lyric starts printing, adjusted for flow
    # [Start immediately, Wait 2.0s, Wait 4.5s, Wait 7.0s, Wait 10.5s, Wait 16.0s, Wait 20.0s]
    delays = [0.0, 3.0, 6.0, 9.0, 12.0, 17.0, 21.0]
    
    threads = []
    
    # Create and start a thread for each lyric
    for i in range(len(lyrics_data)):
        lyric, speed = lyrics_data[i]
        delay = delays[i]
        
        t = Thread(target=sing_lyric, args=(lyric, delay, speed))
        threads.append(t)
        t.start()
    
    # Wait for all threads to complete before the main program exits
    for thread in threads:
        thread.join()
        
    # Extra pause and message after the song finishes
    time.sleep(1.0)
    print("")


if __name__ == "__main__":
    sing_song()