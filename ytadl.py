#!/usr/bin/python3

import os
import os.path

import argparse
from argparse import RawTextHelpFormatter

app_name = "Easy YouTube Audio Downloader"

parser = argparse.ArgumentParser(
    description=app_name,
    formatter_class=RawTextHelpFormatter,
    epilog='''
    Example:

    play.list:
    # Some comments
    https://www.youtube.com/watch?v=<video-code> # Some comments
    <video-code> # You can use only video code or the whole url

    command:
    ./ytadl.py -i ./play.list

    Requirements: youtube-dl, ffmpeg with libmp3lame
    ''')

# Required
required = parser.add_argument_group("required arguments")

required.add_argument("-i", "--input",
                      help = '''Input file with one video URL (or simply video code - the part after '?v=') per line.
Everything after the hash character (#) is ignored.
                      ''', required=True)

# Optional
parser.add_argument("-o", "--output", help="The FULL PATH where to output the results. (Default: current path)")
parser.add_argument("-f", "--format", help="Audio format. Possible values: mp3, ogg, wav, aac. (Default: mp3) For details see 'youtube-dl'")
parser.add_argument("-q", "--quality", help="Audio quality. Possible values: 0 (best) - 9 (worst). (Default: 0) For details see 'youtube-dl'")

args = parser.parse_args()

print("***   "+app_name+": START   ***")

if (os.path.exists(args.input)):
    listfile = args.input
    print("Setting input file to: "+listfile)
else:
    print("Error: File "+args.input+" not found.")
    exit()

if (args.output and os.path.isdir(args.output)):
    outdir = os.path.abspath(args.output)+'/'
else:
    outdir = os.getcwd()+'/'
    if (args.output):
        print("Warning: '"+args.output+"' is not a directory.")

print("Setting output path to: "+outdir)

supported_formats = ['mp3', 'ogg', 'wav', 'aac']
if (args.format and args.format in supported_formats):
    aformat = args.format
else:
    if (args.format):
        print("Warning: '"+args.format+"' not supported.")
    aformat = 'mp3'
print("Setting audio format to: "+aformat)

if (args.quality and args.quality in range(0,10)):
    quality = args.quality
else:
    if (args.quality):
        print("Warning: '"+args.quality+"' invalid quality. Accepted values 0 - 9.")
    quality = '0'
print("Setting audio quality to: "+quality)

unread = 0

with open(listfile) as f:
    for line in f:
        vurl = line.strip()
        if '#' in vurl:
            vurl, comment = vurl.split("#", 1)
            vurl = vurl.strip()
        if (len(vurl) > 0 and vurl[0] != '#'):
            cmd = 'youtube-dl -x --restrict-filenames --audio-format '+aformat+' --audio-quality '+quality+' -o "'+outdir+'%(title)s.%(ext)s" "' + vurl + '"'
            os.system(cmd)
        else:
            unread += 1

if (unread > 0):
    print(str(unread)+" unread lines")

print("***   "+app_name+": END     ***")
