import os
from os import system, name 

# Clean terminal 
def clear(): 
    # for windows os
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux os
    else: 
        _ = system('clear')     
   
clear()

try:
    import PySimpleGUI as sg
    from pytube import YouTube
except ImportError:
    os.system("pip install pysimplegui")
    os.system("pip install pytube")

def main():

    sg.theme('LightBlue3')

    layout = [  [sg.Text("URL  "), sg.InputText()],
                [sg.Text("PATH"), sg.InputText()],
                [sg.Button("OK"), sg.Button("CANCEL")] ]

    window = sg.Window("YouTube to MP3", layout)

    while True:
        event, values  = window.read()

        if event == "OK":
           window.close()
           break

        if event == sg.WIN_CLOSED or event == "CANCEL":
           exit()

    window.close()
    yt = YouTube(str(values[0]))
    video = yt.streams.filter(only_audio=True).first()
    destination = str((values[1]))
    out_file = video.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    newLayout = [ [sg.Text(f"The .mp3 is downloaded in {destination}")],
    [sg.Button("EXIT")], [sg.Button("DOWNLOAD")] ]

    newWindow = sg.Window("SUCCESSFULLY!", newLayout)

    while True:
        event, values  = newWindow.read()

        if event == "EXIT":
           window.close()
           break

        if event == "DOWNLOAD":
           newWindow.close()
           main()

        if event == sg.WIN_CLOSED or event == "CANCEL":
           exit()

    newWindow.close()

main()
