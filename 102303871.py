import sys
import os
import time

def main():
    
    # check 1: no of params
    if len(sys.argv) != 5:
        print("ERROR! Correct format is: \npython <program.py> <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>")
        sys.exit(1)

    singer_name = sys.argv[1]
    
    # check 2: datatype error
    try:
        num_videos = int(sys.argv[2])
        duration = int(sys.argv[3])
    except:
        print("ERROR! Datatype Error: integers only for count and duration")
        sys.exit(1)

    output_file = sys.argv[4]

    # check 3: no of vids
    if num_videos < 10:
        print("ERROR!: Need more than 10 videos")
        sys.exit(1)
        
    # check 4: no of secs 
    if duration < 20:
        print("Error: Duration must be > 20")
        sys.exit(1)


    print(f"Mashup for {singer_name}...")
    
    if not os.path.exists('temp_downloads'):
        os.makedirs('temp_downloads')


    existing_files = [f for f in os.listdir('temp_downloads') if f.endswith('.mp3')]
    
    # if there are enough files, then stop further downlaod
    if len(existing_files) >= num_videos:
        print(f"Found {len(existing_files)} existing files. Skipping download.")
        
    else:
        print(f"Downloading {num_videos} videos...")
        search_query = f"ytsearch{num_videos}:{singer_name}"
        
        # automatic max-download 
        cmd_download = (
            f'python3 -m yt_dlp '
            f'"{search_query}" '
            f'-x --audio-format mp3 '
            f'--remote-components ejs:github '
            f'--max-downloads {num_videos} '
            f'-o "temp_downloads/%(title)s.%(ext)s" '
        )
        
        os.system(cmd_download)


    print("Processing audio...  ")
    
    files = [f for f in os.listdir('temp_downloads') if f.endswith('.mp3')]
    files = files[:num_videos]
    
    # check : no files found
    if len(files) == 0:
        print("ERROR! : No files found to process.")
        sys.exit(1)
    
    concat_list = open("concat_list.txt", "w")
    
    for i, f in enumerate(files):
        input_path = os.path.join('temp_downloads', f)
        
        safe_name = f"video_{i}.mp3"
        safe_path = os.path.join('temp_downloads', safe_name)
        
        # renaming to avoid special character errors
        if os.path.exists(input_path) and input_path != safe_path:
             os.rename(input_path, safe_path)
        
        cut_path = os.path.join('temp_downloads', f"cut_{i}.mp3")
        
        
        cmd_cut = f'ffmpeg -y -i "{safe_path}" -ss 0 -t {duration} -c:a libmp3lame -q:a 4 "{cut_path}" -loglevel quiet'
        os.system(cmd_cut)
        
        concat_list.write(f"file 'temp_downloads/cut_{i}.mp3'\n")
        
    concat_list.close()

    print("Merging...")
    
    cmd_merge = f'ffmpeg -y -f concat -safe 0 -i concat_list.txt -c copy "{output_file}" -loglevel quiet'
    os.system(cmd_merge)

    print(f"Done! Saved {output_file}")
    
    
    # clean temp folders
    for f in os.listdir('temp_downloads'):
        os.remove(os.path.join('temp_downloads', f))
    os.rmdir('temp_downloads')
    os.remove("concat_list.txt")

if __name__ == "__main__":
    main()