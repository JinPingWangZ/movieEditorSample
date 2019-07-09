import time
import ffmpeg
from moviepy.editor import VideoFileClip

video = str(input("Vídeo: ") + ".mp4")
tempos = []
c = 1

tempos_ini = list(input("Tempos: ").replace(".", ":").split(" "))

for i in tempos_ini:

    if len(i) <= 5:
        tempos.append("00:" + i)

    else:
        tempos.append(i)

print(tempos)

#print("Tempo inicial: " + time.strftime("%H:%M:%S", time.gmtime(sum(x * int(t) for x, t in zip([3600, 60, 1], tempos[0].split(":"))) - 3)))
#print("Tempo final: " + time.strftime("%H:%M:%S", time.gmtime(sum(x * int(t) for x, t in zip([3600, 60, 1], tempos[0].split(":"))) + 12)))

for i in tempos:

    temp_ini = time.strftime("%H:%M:%S", time.gmtime(sum(x * int(t) for x, t in zip([3600, 60, 1], i.split(":"))) - 2))
    temp_end = time.strftime("%H:%M:%S", time.gmtime(sum(x * int(t) for x, t in zip([3600, 60, 1], i.split(":"))) + 2))

    print( "---", temp_ini, temp_end )

    clip_ini = 0
    clip_ini = VideoFileClip(video).subclip(temp_ini, temp_end)

    print( "+++", clip_ini )
    #clip = CompositeVideoClip([clip_ini])
    #time.sleep(2)
    try:
        clip_ini.write_videofile(str(c) + ".mp4", fps = 25)
        clip_ini.close()
    except:
        print ("error!")
    c = c + 1




#print(tempos_ini)
#print(len(tempos_ini))
#print(tempos)

#clip = VideoFileClip(video).subclip("00:01:20", "00:01:30")
#clipfinal = CompositeVideoClip([clip])
#clipfinal.write_videofile("deu3!.mp4")

