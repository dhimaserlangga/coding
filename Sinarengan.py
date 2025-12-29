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
        ("Ngobrol ra ono", 0.10),                      
        ("Enteke ning tengah wengi", 0.10),            
        ("Tetes embun sing ngancani", 0.14),
        ("Akuuu", 0.15),                               
        ("Sampeyan", 0.12),                           
        ("Koyo lagi kasmaran", 0.10),                  
        ("Tenaaaaan", 0.2),                            
        ("Mlaku teko tuwo bebarengan", 0.13),        
    ]

    # Delays (in seconds) before each lyric starts printing, adjusted for flow
    
    delays = [0.7, 3.0, 7.0, 14.0, 16.0, 18.5, 21.0, 25.0]
    
    # Error check to ensure data arrays match
    if len(lyrics_data) != len(delays):
        print("Error: The number of lyrics and delays must be equal.")
        return
        
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