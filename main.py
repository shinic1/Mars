import yt_down
import video_down
import tiktok_down


def choice(argument):
    match argument:
        case 1:
            yt_down.catch()
        case 2:
            tiktok_down.download()
        case 3:
            return 0
        case _:
            print("Invalid choice")
            catch_error()


def catch_error():
    try:
        print(' 1. Youtube Downloader', '\n', '2. TikTok Downloader', '\n', '3. Video Downloader')
        Choice = int(input('Enter option:'))
        choice(Choice)
    except ValueError:
        print("Invalid input. Please enter a number.")
        catch_error()


catch_error()
