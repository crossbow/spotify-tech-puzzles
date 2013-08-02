#!/usr/bin/env python
"""
https://www.spotify.com/it/jobs/tech/zipfsong/

Say an album has ten songs. Normally, you could argue that the quality
of each song could be determined by how many times it has been played
by someone. However, it could be argued back that a person would play
the first song of an album a number of times more than the last or
second last song. This is where Zipf's law comes into play.

If you have an album of 10 songs and the first song has been played
12,000 times, Zipf's law states that the second song would be estimated
to be played 6,000 times. The equation for this is:

play count of first song / track number
12,000 / 2 = 6,000 plays

The equation to therefore determine the quality of a song is:

quality = actual play count / estimated play count

So if track 2 on the album aforementioned was indeed played 6,000 times,
it's quality would be represented by the result of '1'. However,
if it received 8,000 plays instead of 6,000, it's quality would be
represented instead by the result of '1.333...'.
The higher the figure of quality, the better.

Input

The first line of input contains two integers n and m
(1 <= n <= 50000, 1 <= m <= n), the number of songs on the album,
and the number of songs to select.
Then follow n lines. The i'th of these lines contains an integer fi
and string si, where 0 <= fi <= 10**12 is the number of times the i'th song
was listened to, and si is the name of the song.
Each song name is at most 30 characters long and consists only of
the characters 'a'-'z', '0'-'9', and underscore ('_').

Output

Output a list of the m songs with the highest quality qi,
in decreasing order of quality.
If two songs have the same quality, give precedence to
the one appearing first on the album (presumably there was
a reason for the producers to put that song before the other).

NOTE: the code is still using play_count_song_1 that turned
out to be not useful to solve the problem.
"""

from heapq import heappush, heappop
import sys

def qi(fi, play_count_song_1, album_position):
    """
    Determine the quality of a song:

    estimated play count = play count of first song / track number
    quality = actual play count / estimated play count
    """
    #zi = play_count_song_1 / float(album_position)
    #qi = fi / zi
    qi = fi * album_position
    return qi

def get_song():
    """
    Read song line
    """
    line_input = raw_input()
    fi, song_title = line_input.strip().split()
    fi = int(fi)
    song_title = song_title[:30]
    return fi, song_title

def rank_item(fi, play_count_song_1, album_position, song_title):
    """
    Return a tuple with quality, track position, song song_title
    Quality is negative in order to get the top of the heap
    """
    quality = qi(fi, play_count_song_1, album_position)
    new_item = (-quality, album_position, song_title)
    return new_item

def main():
    # 1st line of input
    line_input = raw_input()
    n, m = line_input.strip().split()
    song_number = int(n)
    song_to_select = int(m)
    if song_to_select > song_number:
        print "The number of songs to select cannot be greter than the number of songs on the album"
        sys.exit(1)
    if  song_number > 50000:
        print "The number of songs on the album cannot be greater than 50000"
        sys.exit(2)

    heap = []

    # Get quality of 1st song
    fi, song_title = get_song()
    album_position = 1
    play_count_song_1 = fi
    new_item = rank_item(fi, play_count_song_1, album_position, song_title)
    heappush(heap, new_item)

    # Get quality of the other songs
    for i in range(1, song_number):
        fi, song_title = get_song()
        album_position = i + 1
        new_item = rank_item(fi, play_count_song_1, album_position, song_title)
        heappush(heap, new_item)

    # Print result
    for i in range(song_to_select):
        print heappop(heap)[2]

if __name__ == '__main__':
    main()