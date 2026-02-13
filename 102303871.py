import sys
import os
import yt_dlp
from moviepy.editor import AudioFileClip, concatenate_audioclips

def main():
    # check 1: no of args
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>")
        sys.exit(1)

    singer = sys.argv[1]
    
    # check 2: datatype 
    try:
        n = int(sys.argv[2])
        y = int(sys.argv[3])
    except:
        print("Error: integers only for count and duration")
        sys.exit(1)

    outfile = sys.argv[4]

    # check 3: no of songs
    if n < 10:
        print("Error: Need more than 10 videos")
        sys.exit(1)
        
    # check 4: no of secs
    if y < 20:
        print("Error: Duration must be > 20")
        sys.exit(1)

    print(f"Processing {singer}...")
    
    if not os.path.exists('temp_downloads'):
        os.makedirs('temp_downloads')


    search_query = f"ytsearch{n}:{singer}"
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'temp_downloads/%(title)s.%(ext)s',
        'quiet': True,
        'noplaylist': True,
        'overwrites': {'remote_components': 'ejs:github'} 
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([search_query])
    except Exception as e:
        print(e)


    print("Converting and cutting audio...")
    
    all_files = [f for f in os.listdir('temp_downloads')]
    
    clips = []
    count = 0
    
    for filename in all_files:
        if count == n:
            break
            
        file_path = os.path.join('temp_downloads', filename)
        
        try:
            audio = AudioFileClip(file_path)
            
            # cutting the first Y seconds
            cut_audio = audio.subclip(0, y)
            clips.append(cut_audio)
            count += 1
            
        except Exception as e:
            print(f"Skipping {filename} due to error")
            continue


    print("Merging audios...")
    
    # check : if no files found
    if len(clips) > 0:
        final_clip = concatenate_audioclips(clips)
        final_clip.write_audiofile(outfile)
        print(f"Done! Saved {outfile}")
    else:
        print("No audio clips processed")
        
    
    # cleanup
    for c in clips:
        c.close()
        
    for f in os.listdir('temp_downloads'):
        try:
            os.remove(os.path.join('temp_downloads', f))
        except:
            pass
    os.rmdir('temp_downloads')

if __name__ == "__main__":
    main()