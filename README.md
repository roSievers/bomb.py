# Bomb.by

While playing "Boom", by bomb broke. So I made my own.

## Licensing

Sound File:
 * Tick Sound - DeepFrozenApps - http://soundbible.com/2044-Tick.html
 * Boom Sound - Jim Rogers - http://soundbible.com/1919-Shotgun-Blast.html

## Settings

You can adjust the constants in the python script for most things. If the
boom sound is to loud for your taste, adjust it with ffmpeg:

    ffmpeg -i boom-scr.mp3 -filter:a "volume=0.5" boom.mp3