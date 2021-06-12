from os import sys
from pytube import YouTube
from pafy import new
from pytube import Playlist
import humanize

print("|----------------------------|")
print("|Welcome in Y.D.M cmd version|")
print("|----------------------------|")

def main(): #main function
    print("------------------------\nif you want to download:")
    print("------------------------\nVideo Enter [1]|\n----------------")
    print("Audio Enter [2]|\n----------------")
    vd_aud = int(input("i want to download: "))
    if vd_aud == 1:
        print(
            "-------------------------------------\nto download a single video write [1]| "
            "\n-------------------------------------")
        print("download a playlist write [2]| \n------------------------------")
        violist = int(input("download: "))

        if violist == 1:
            url = input("Enter the url: ") #Enter video url
            video = new(url)
            stream = video.streams

            for i in stream:
                print('resolution: %s, ext: %s, size: %0.2fMb' % (i.resolution, i.extension, i.get_filesize() / 1024 / 1024))
            filepath = input("Enter file path: ") #here entering the file path
            print("---------------------------\nfor high quality Enter [1]|"
                  "\n---------------------------")
            print("for low quality Enter [2]|\n---------------------------")
            quality = int(input("Enter quality: "))
            if quality == 1: # means high quality
                video.getbest().download(filepath=filepath)
                print("Download Completed") #Download completion message
                choice_1 = input("press [q] to exit or [enter] to restart: ")
                if choice_1 == "q":
                    sys.exit(0)
                else:
                    main()
            elif quality == 2: #means low qualiy
                stream[0].download(filepath=filepath)
                print("Download Completed")#Download completion message
                choice_1 = input("press [q] to exit or [enter] to restart: ")
                if choice_1 == "q":
                    sys.exit(0)
                else:
                    main()
        elif violist == 2:
            playlist_link = input("Please enter the playlist url: ")#playlist url
            playlist = Playlist(playlist_link)
            filepath2 = input("Enter the file path: ") #here entering the file path
            print("----------------------------------\nfor the highest quality enter [1]| "
                  "\n----------------------------------")
            print("for the lowest quality enter [2]| \n---------------------------------")
            quality2 = int(input("choose the quality: "))
            if quality2 == 1:
                print("download in progress...")# Download progress message
                for video in playlist.videos:
                    video.streams.get_highest_resolution().download(output_path=filepath2)
                print("Download Completed")#Download completion message
            elif quality2 == 2:
                print("download in progress...")# Download progress message
                for video in playlist.videos:
                    video.streams.get_lowest_resolution().download(output_path=filepath2)
                print("Download Completed")#Download completion message
            choice_1 = input("press [q] to exit or [enter] to restart: ")
            if choice_1 == "q":
                sys.exit(0)
            else:
                main()
    elif vd_aud == 2: # audio download 
        url_1 = input("Enter the url: ") #video url
        video_1 = new(url_1)
        audiometry = video_1.audiostreams
        for i in audiometry:
            print('Bitrate: %s, ext: %s, size: %0.2fMb' % (i.bitrate, i.extension, i.get_filesize() / 1024 / 1024))
        filepath_2 = input("Enter the file path: ") #here entering the file path
        video_1.getbestaudio(preftype='m4a').download(filepath=filepath_2)
        print("Download Completed")#Download completion message
        choice_1 = input("press [q] to exit or [enter] to restart: ")
        if choice_1 == "q":
            sys.exit(0)
        else:
            main()


main()
