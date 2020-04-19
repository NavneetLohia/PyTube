from pytube import YouTube

link = input("Enter link of Youtube video: ")
utube = YouTube(link)

videos = utube.streams.all()

i = 1
for stream in videos:
  print(str(i) + " " + str(stream))
  i += 1

stream_no = int(input("Enter Number: "))

vid = videos[stream_no - 1]
vid.download(r"D:")

print("Downloaded")