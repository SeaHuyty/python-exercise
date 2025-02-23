import sys
from time import sleep
import time
def print_lyrics():
    lines = [
        ("And Maybe I'm wrong", 0.13),
        ("For writing this song", 0.08),
        ("Losing my head over you.........", 0.15),
        ("And I'll be here'", 0.08),  
        ("Cause we both know how it goes", 0.07),
        ("I don't want things to change", 0.08),
        ("I pray they stay the same", 0.08),
        ("always", 0.08),
        ("And I don't care", 0.08),
        ("If you're with somebody else", 0.08),
        ("I'll give you time and space", 0.08),
        ("Just know I'm not a phase", 0.08),
        ("I'm always-ways-ways", 0.16),
        ("I'm always-ways-ways", 0.16),
        ("I'm always-ways-ways", 0.16),
    ]

    delays = [1, 1.8, 3.1, 0.65, 0.75, 0.5, 0.8, 2.96, 0.5, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)

        time.sleep(delays[i])
        print('')

print_lyrics()