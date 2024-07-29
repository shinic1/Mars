from moviepy.editor import VideoFileClip, AudioFileClip
from pytubefix import YouTube
from pytubefix.cli import on_progress


# For mp4 downloads above 720p YouTube's codec requires the download of video and audio files separately
def download_video(res, yt):
    print('downloading video...')
    yt.streams.filter(res=f"{res}").first().download(filename=yt.title + "_video.mp4")
    yt.streams.get_by_itag(140).download(filename=yt.title + "_audio.mp4")
    convert(yt)


# Only downloads audio with the menu function
def download_audio():
    yt = yt_link()
    print('downloading audio...')
    yt.streams.get_by_itag(140).download(filename=yt.title + "_audio.mp4")
    print('Done')


# After both files are downloaded, convert will merge them together
def convert(yt):
    video_clip = VideoFileClip(yt.title + "_video.mp4")
    audio_clip = AudioFileClip(yt.title + "_audio.mp4")
    print('converting...')
    final_clip = video_clip.set_audio(audio_clip)
    final_title = yt.title + "_video_final.mp4"
    final_clip.write_videofile(final_title, threads=8, preset='ultrafast')
    print('done, your video has been downloaded')


def yt_link():
    link = input('Enter a youtube link:')
    yt = YouTube(link, on_progress_callback=on_progress)
    return yt


# Simple switch case to set a resolution
def resolution():
    yt = yt_link()
    print(' 1. 360p', '\n', '2. 480p', '\n', '3. 720p', '\n', '4. 1080p')
    res = int(input("Enter 1-4 for a resolution: "))
    match res:
        case 1:
            download_video("360p", yt)
        case 2:
            download_video("480p", yt)
        case 3:
            download_video("720p", yt)
        case 4:
            download_video("1080p", yt)
        case _:
            print("Invalid choice")
            resolution()


def selector(argument):
    match argument:
        case 1:
            resolution()
        case 2:
            download_audio()
        case _:
            print("Invalid choice")
            catch()


def catch():
    try:
        print(' 1. Download video', '\n', '2. Download audio')
        head = int(input('Enter your choice: '))
        selector(head)
    except ValueError:
        print("Invalid input. Please enter a number.")
        catch()
