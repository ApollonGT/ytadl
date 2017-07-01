# Easy YouTube Audio Downloader

```bash
usage: ytadl.py [-h] -i INPUT [-o OUTPUT] [-f FORMAT] [-q QUALITY]


optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        The FULL PATH where to output the results. (Default: current path)
  -f FORMAT, --format FORMAT
                        Audio format. Possible values: mp3, ogg, wav, aac. (Default: mp3) For details see 'youtube-dl'
  -q QUALITY, --quality QUALITY
                        Audio quality. Possible values: 0 (best) - 9 (worst). (Default: 0) For details see 'youtube-dl'

required arguments:
  -i INPUT, --input INPUT
                        Input file with one video URL (or simply video code - the part after '?v=') per line.
                        Everything after the hash character (#) is ignored.
                                              

    Example:

    play.list:
    # Some comments
    https://www.youtube.com/watch?v=<video-code> # Some comments
    <video-code> # You can use only video code or the whole url

    command:
    ./ytadl.py -i ./play.list

    Requirements: youtube-dl, ffmpeg with libmp3lame
```
