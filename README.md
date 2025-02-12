# Mogi Table Bot
## Tutorial
I strongly advise to follow and read the whole instructions, to prevent confusion. (It won't take long)
## First Time Setup:
Download MogiTableBotv2.1.exe from https://github.com/9tarek/8DX-Mogi-Table-Bot/releases.

If you're planning to use the OBS Overlay, download the 2 fonts aswell, and install them.

Fonts needed for OBS Overlay:

[DS-Digital Bold](https://github.com/lisophorm/dreamteam/raw/master/src/assets/fonts/Digital/DS-DIGIB.TTF)

[New Rodin Pro](https://archive.org/download/Fontworks/Fonts/FOT-NewRodin%20Pro%20B.otf)

Run both, and press Install on the top left.

Go to the Settings tab and check the "Using OBS Virtual Camera" if you're using it for your own game, leave it disabled if you're watching a Stream. (Leaving it disabled will take a Screenshot from your PC, rather than your Capture Card).

Check the OBS Overlay checkbox if you want to use the Overlay.

<p align="center">
  <img src="https://github.com/user-attachments/assets/c8b2650e-b389-4917-883d-5c77162b6751" alt="Bild 1" width="400"/>
  <img src="https://github.com/user-attachments/assets/9897ee2b-1a23-4cdd-86de-cc59656104d0" alt="Bild 2" width="397"/>
</p> 


If you activated OBS Overlay this window should pop up.

![image](https://github.com/user-attachments/assets/2f78c3f0-f9c8-478e-87b9-9a230976188e)

Don't minimize this window, you can click a window behind it, to make it disappear. (Windows doesn't render it, if you minimize it)

Go to OBS and press on the gear icon next to "Start Virtual Camera", under Controls.

<p align="center">
  <img src="https://github.com/user-attachments/assets/fc9d8faf-8f0d-42c3-95f0-9d01f4c61921" alt="Bild 1" width="200"/>
  <img src="https://github.com/user-attachments/assets/81dc61b4-5332-4cec-b878-564431b2c116" alt="Bild 2" width="800"/>
</p> 

Set it to Source, and then select your Capture Card Source.

Under Sources, add a new Window Capture, name it whatever you want, and set the Window to the Scores Overlay. Under Window Match Priority, apply Window title must match, and disable Capture Cursor.

![image](https://github.com/user-attachments/assets/cdcb41a4-996f-445e-916a-e15ac3e2adc3)

Move the Overlay, to where you want it. (pressing Ctrl while dragging, unlocks it)

Right-click the Window Capture, press on Filters, and add a Chroma Key. Set the Opacity to 0.5 and Contrast to 2.5

![image](https://github.com/user-attachments/assets/0c333730-2e1e-41b4-b153-c8e48c15f5a7)

This finished the Setup.

## How to Use:

Every time you use the Bot you have to Start your Virtual Camera in OBS, so the Bot can get the Image from the Switch.

![image](https://github.com/user-attachments/assets/1e760b1c-4856-4200-aec3-71aedb1b4a55)

Whenever you're at the end of a race, wait until the Points finished adding up and press the Hotkey, you can alternatively wait until the scoreboard sorts itself and press it then. 

<p align="center">
  <img src="https://github.com/user-attachments/assets/f74d7f0a-ba37-44e2-a58f-e8b0902985ba" alt="Bild 2" width="400"/>
  <img src="https://github.com/user-attachments/assets/18587502-2051-46c5-a535-f1c989fbc050" alt="Bild 1" width="400"/>
  Left = Good, Right = Bad
</p> 

In case of a Disconnect, enter the first Letter of the Tag, and the amount the Person disconnected with, (shows in Overlay and next to Table). If more than one person disconnected in a single race, you can check on the Screenshots Tab, to see how much each one disconnected with.

![image](https://github.com/user-attachments/assets/3ce4b612-a5a1-4eb6-b2e7-37d9b21af3d1)

If it's a Japanese Tag or a Symbol, press the Insert Tags button, so you can get the Tag.

If the room crashes, press the Room Crash button, and it will add the Points to the following Tables/Scores. 

Press Clear after a mogi with DC Points/Room Crash finished.

Bind a Key to ESC to unbind it.

## Disclaimer:

It does not work if somebody has the tag at the end of the name.

If the Table / Scores don't update, check the Screenshots tab.

![image](https://github.com/user-attachments/assets/c2b88cb4-3824-46d3-a246-267b5061774e)

If this image shows up, you forgot to start the Virtual Camera






