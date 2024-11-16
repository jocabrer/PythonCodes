from pytube import YouTube

def run():
    video_url = input("please enter youtube video url:")
    yt = YouTube(video_url)
    ys = yt.streams.filter(only_audio=True).first()

    print("Downloading...")
    ys.download(output_path="D:\\Dev\\PythonCodes\\Musica")

    print("Download complete... {}".format(yt.title))

if __name__=='__main__':
    run()