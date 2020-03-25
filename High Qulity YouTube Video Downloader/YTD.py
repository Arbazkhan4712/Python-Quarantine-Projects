import  youtube_dl


arg = sys.argv[1]
ytd={}
with youtube_dl.YoutubeDL(ytd)as yt:
    yt.download([arg])