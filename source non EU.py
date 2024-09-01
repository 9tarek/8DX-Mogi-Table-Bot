from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import customtkinter
import keyboard
from PIL import Image, ImageGrab, ImageTk
from io import BytesIO
import time
import base64
import os
from datetime import datetime
import win32clipboard
import re
import pyperclip
import json
import pywinstyles
import cv2
from pygrabber.dshow_graph import FilterGraph

def extract_theme():

    home_dir = os.path.expanduser("~")
    theme_path = os.path.join(home_dir, ".mogi_table_bot_theme.json")
    
    if not os.path.exists(theme_path):
        theme = """
            {
        "CTk": {
            "fg_color": ["gray92", "gray14"]
        },
        "CTkToplevel": {
            "fg_color": ["gray92", "gray14"]
        },
        "CTkFrame": {
            "corner_radius": 6,
            "border_width": 0,
            "fg_color": ["gray86", "gray17"],
            "top_fg_color": ["gray81", "gray20"],
            "border_color": ["gray65", "gray28"]
        },
        "CTkButton": {
            "corner_radius": 6,
            "border_width": 0,
            "fg_color": ["#B288DA", "#9F7DB7"],
            "hover_color": ["#7E4B9C", "#693D82"],
            "border_color": ["#3E454A", "#949A9F"],
            "text_color": ["gray98", "#DCE4EE"],
            "text_color_disabled": ["gray78", "gray68"]
        },
        "CTkLabel": {
            "corner_radius": 0,
            "fg_color": "transparent",
            "text_color": ["gray10", "#DCE4EE"]
        },
        "CTkEntry": {
            "corner_radius": 6,
            "border_width": 2,
            "fg_color": ["#F9F9FA", "#343638"],
            "border_color": ["#979DA2", "#565B5E"],
            "text_color":["gray10", "#DCE4EE"],
            "placeholder_text_color": ["gray52", "gray62"]
        },
        "CTkCheckBox": {
            "corner_radius": 6,
            "border_width": 3,
            "fg_color": ["#B288DA", "#9F7DB7"],
            "border_color": ["#3E454A", "#949A9F"],
            "hover_color": ["#7E4B9C", "#693D82"],
            "checkmark_color": ["#DCE4EE", "gray90"],
            "text_color": ["gray10", "#DCE4EE"],
            "text_color_disabled": ["gray60", "gray45"]
        },
        "CTkSwitch": {
            "corner_radius": 1000,
            "border_width": 3,
            "button_length": 0,
            "fg_color": ["#939BA2", "#4A4D50"],
            "progress_color": ["#B288DA", "#9F7DB7"],
            "button_color": ["gray36", "#D5D9DE"],
            "button_hover_color": ["gray20", "gray100"],
            "text_color": ["gray10", "#DCE4EE"],
            "text_color_disabled": ["gray60", "gray45"]
        },
        "CTkRadioButton": {
            "corner_radius": 1000,
            "border_width_checked": 6,
            "border_width_unchecked": 3,
            "fg_color": ["#B288DA", "#9F7DB7"],
            "border_color": ["#3E454A", "#949A9F"],
            "hover_color":["#7E4B9C", "#693D82"],
            "text_color": ["gray10", "#DCE4EE"],
            "text_color_disabled": ["gray60", "gray45"]
        },
        "CTkProgressBar": {
            "corner_radius": 1000,
            "border_width": 0,
            "fg_color": ["#939BA2", "#4A4D50"],
            "progress_color": ["#B288DA", "#9F7DB7"],
            "border_color": ["gray", "gray"]
        },
        "CTkSlider": {
            "corner_radius": 1000,
            "button_corner_radius": 1000,
            "border_width": 6,
            "button_length": 0,
            "fg_color": ["#939BA2", "#4A4D50"],
            "progress_color": ["gray40", "#AAB0B5"],
            "button_color": ["#B288DA", "#9F7DB7"],
            "button_hover_color": ["#7E4B9C", "#693D82"]
        },
        "CTkOptionMenu": {
            "corner_radius": 6,
            "fg_color": ["#B288DA", "#9F7DB7"],
            "button_color": ["#9B75C1", "#8C6DA7"],
            "button_hover_color": ["#7E4B9C", "#693D82"],
            "text_color": ["gray98", "#DCE4EE"],
            "text_color_disabled": ["gray78", "gray68"]
        },
        "CTkComboBox": {
            "corner_radius": 6,
            "border_width": 2,
            "fg_color": ["#F9F9FA", "#343638"],
            "border_color": ["#979DA2", "#565B5E"],
            "button_color": ["#979DA2", "#565B5E"],
            "button_hover_color": ["#6E7174", "#7A848D"],
            "text_color": ["gray10", "#DCE4EE"],
            "text_color_disabled": ["gray50", "gray45"]
        },
        "CTkScrollbar": {
            "corner_radius": 1000,
            "border_spacing": 4,
            "fg_color": "transparent",
            "button_color": ["gray55", "gray41"],
            "button_hover_color": ["gray40", "gray53"]
        },
        "CTkSegmentedButton": {
            "corner_radius": 6,
            "border_width": 2,
            "fg_color": ["#979DA2", "gray29"],
            "selected_color": ["#B288DA", "#9F7DB7"],
            "selected_hover_color": ["#7E4B9C", "#693D82"],
            "unselected_color": ["#979DA2", "gray29"],
            "unselected_hover_color": ["gray70", "gray41"],
            "text_color": ["gray98", "#DCE4EE"],
            "text_color_disabled": ["gray78", "gray68"]
        },
        "CTkTextbox": {
            "corner_radius": 6,
            "border_width": 0,
            "fg_color": ["#F9F9FA", "gray23"],
            "border_color": ["#979DA2", "#565B5E"],
            "text_color":["gray10", "#DCE4EE"],
            "scrollbar_button_color": ["gray55", "gray41"],
            "scrollbar_button_hover_color": ["gray40", "gray53"]
        },
        "CTkScrollableFrame": {
            "label_fg_color": ["gray78", "gray23"]
        },
        "DropdownMenu": {
            "fg_color": ["gray90", "gray20"],
            "hover_color": ["gray75", "gray28"],
            "text_color": ["gray10", "gray90"]
        },
        "CTkFont": {
            "macOS": {
            "family": "SF Display",
            "size": 13,
            "weight": "normal"
            },
            "Windows": {
            "family": "Roboto",
            "size": 13,
            "weight": "normal"
            },
            "Linux": {
            "family": "Roboto",
            "size": 13,
            "weight": "normal"
            }
        }
        }"""
        with open(theme_path, "w") as theme_file:
            theme_file.write(theme)
    return theme_path
    


hotkey = "Down"
twitchhotkey = None
autocopy = "Disabled"
using_obs_virtual_cam = False
obs_overlay_active = False
cap = None


def get_config_path():
    home_dir = os.path.expanduser("~")
    config_file = ".mogi_table_bot_v2_config.json"
    return os.path.join(home_dir, config_file)

def load_settings():
    global hotkey, twitchhotkey, autocopy, using_obs_virtual_cam, obs_overlay_active
    config_path = get_config_path()
    try:
        if os.path.exists(config_path):
            with open(config_path, "r") as file:
                settings = json.load(file)
                hotkey = settings.get("hotkey", hotkey)
                twitchhotkey = settings.get("twitchhotkey", twitchhotkey)
                autocopy = settings.get("autocopy", autocopy)
                using_obs_virtual_cam = settings.get("using_obs_virtual_cam", using_obs_virtual_cam)
                obs_overlay_active = settings.get("obs_overlay_active", obs_overlay_active)
        else:
            save_settings()
    except Exception:
        save_settings()

def save_settings():
    config_path = get_config_path()
    settings = {
        "hotkey": hotkey,
        "twitchhotkey": twitchhotkey,
        "autocopy": autocopy,
        "using_obs_virtual_cam": using_obs_virtual_cam,
        "obs_overlay_active": obs_overlay_active
    }
    with open(config_path, "w") as file:
        json.dump(settings, file)

load_settings()

left = 0
top = 132
right = 1579
bottom = 1020

currentimg = 0
currentss = 0
recentss = 0
dc_points = ""
dc_score = 0

customtkinter.set_appearance_mode("dark")
theme_path = extract_theme()
customtkinter.set_default_color_theme(theme_path)

root = customtkinter.CTk()
root.geometry("700x520")
root.title("Mogi Table Bot")
root.resizable(False, False)
icon_data = b"""AAABAAEAICAAAAEAIACoEAAAFgAAACgAAAAgAAAAQAAAAAEAIAAAAAAAABAAAMMOAADDDgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJgoUACRFkwAliJPIpMYTICEFlDKdC9n0l9hnXNFkNULTn/BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAlBBHAJMQRRSXEkmuqA5P/LwDUv++BE3/myxu8GxxsmcA//8BWJDTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKYACwCUAj0AkgI5PaIBP+7DAEz/1wBV/+AAV//YBFf/lkCG00p4tSReb64AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWQAAAJcANACPADAxpQA45cIARv/RAE3/2QBS/+EAVv+5FV/8W0uEeADV/wE4X5gAQ2mfAEFnnQdFbKAeRWygGUFlngRDaJ8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAjQAsAI8AJAmMADSPigA6+4kAPP+KADr/lAA5/54COP9mJ1TcOFCFOFdMXgByDTwMSl+Re0t0o9hMdaPQSG+hdD9imQxCZ5wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAogAAALsAAAC8EwsArJwZAJ72GACm/xkAqv8iAJ7/OAB7/00KUf8xJWnFAgSQZGIIRn5JS3n0TXek/1F8pv9MdKLzRWmeaDBGjwFBY5sAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADgAAAAsAAAALIXAAC9uwAA0f8AAOD/AADr/wAA9f8AAPX/CQHZ/w0Ikf8HAVP5TQE09kgoTf9DZ5j/T3ml/1B5pf9JcKDhQmebSd///wA7XpQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACvAAAA/wAAAL8oAADGwQAA1f8AAOj/AAD2/wAA/v8AAP//AADz/wQAk/8/ACb/VQkk/z9Kd/9KcqL/UHqk/012of9FapzPPmGVLEFkmQAlXHoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB/AAAAjgMBAHKKAACi/wAA1f8AAOj/AAD1/wAA/v8AAP7/AADu/x8Aev9TABv/RypP/0FlmP9Lc6H/S3Of/0Rqmv89Y5d/haz/ADZbiwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA3AAAAJQAAAC2TgEAbeQBAEf/AQCH/wAA0v8AAPb/AAD//wAA/v8AAPT/AwDb/z0ATv9nDC7/TUx9/0duo/9FbqD/Rmea/1RUiJDJAAABZTVkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuwAAAMBoAACu/AAAi/8CAF3/BABj/wQAlf8DAMf/AQ3o/wAd9f8AC/X/IACy/4kAPP+OE0X/eEN7/21Ujv+CPXf/pBdSenVYmQCyADgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA3gAAAP8AAADXHQAAxJwAALv9AADT/wAA2/8BALf/AwCH/wYAbf8DUJr/CMr3/weg8/8IGdH/ZQB5/8AATP/KAlH/ygZV/9UCUtPfAFAw3gBOAMsAdAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAM0AAADOCAAAy1QAAMjFAADA+wAAvP8AANH/AADi/wAA3v8CAtf/CAfM/wsrzf8Kaef/A2/Z/wMSnP8RAKD/ZQWm89sUgLr5EHaZ+wZzPP8AbQH/AHIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADIAAAAyhIAAMWGAADC7gAAwv8AAMD/AAC//wAAvv8EBLP/JiWi/1VUo/91dLn/fnvN/2Vi2P8tK+P/BAPy/wAA+f8CAf3XPRTgKf99ewT///8A/7X3AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAxgAAAMYQAADGlgAAy/kAAN3/AADi/wAAyf8AAMD/Bgav/0hHn/+NjKP/q6u1/7y8xP+5ucH/vr7J/7Ox1f9WVen/BQX+/wAA/vYAAPpiAAD/AAAA8QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADLAAAAxjsAANroAADy/wAA/PkAAOLxAAC++QEBsv9CQqD/lpeg/7GytP/Fxsj/09PW/5eXmv+qqa3/393i/8nG3/9BQPL/AAD//wAA/L8AAPYVAAD4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOEAAADXEAAA9V0AAP5yAAD5XgUTumYFFJjkHB6a/4aHnv+sraz/x8jI/9nZ2f/j4uP/2tnb/+Hg4v/u7O7/7+3t/5uZ7f8JCf3/AAD/9AAA/VIAAP0AAAD/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFWpsAAVSQAIhfY0/InmenxNKi/lNXYr/oaGi/7+/v//c3N3/6urq/+7u7v/y8vL/9/b3//r5+v/7+vr/1dPy/yEh9/8AAP//AAD+mwAA/wYAAP8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARX3wAAAAAAiqKppA5pL7/HXGU/16Im/+trq3/0dHR/6ysrf+cnJz/5OTk//n5+f/7+vv/7e3t//v7+v/08/r0R0ftwQAA/fEAAP+1AAD/DgAA/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAxbeAAAAAAAGnGORRx6mc0cmLX/ZJuk/7y7u/+qqqr/Hx8f/wgICP+NjY3//f39/7Ozs/9BQUH/rq6u/////uvKyvREAAD9SQAA/0AAAP8DAAD/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGmmEABFeexdBmK1fMpizzRunzP9slaL/wsHA/25ubv8AAAD/AAAA/1tbW//k5OT/Q0ND/wAAAP9qamr/9/f33fv7+yP5+fkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD01PABYbEAAAcGgEFYmtWEfE3O8xst3/E6Hd/1SsyP+9xMT/aGdn/wAAAP8AAAD/a2tr/8XGxv8WFhb/AAAA/1tna//Y4uaq////Cvb39wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIjLwACI6/EQaFsY0LiLnOIq7i/SGp4/8kndL/HbHh/27N5f+PoKP/HRsZ/x8eHf+4uLf/wcHB/xIQEP8SHR7/MICO9V6ZrFgJaYQA6e/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAia1AAHoNoUCInAlhJ5pqsRfrL4QrbZ/1Cy0f8SktP/F7Ds/0vD6v9rq7v/n77C/+/5+//j6ur/gYiI/1aPlf8ho7rZEnmXIhSEoQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABYm/AAWPxAEAh8gGFGmVcAt4q/0pnsn/KKDT/w2k6f8Nr/T/FKPj/zC87v9Iz/j/Xdb4/2fb9/9f2fX/L7jc/xyQrc0phpUYJ5WlAA4bUQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD5C8ABaUvQcLh7OGCo7F/Aue1/8PmND/Dafe/xir5f9PwM//NafO/xSk7P8PqvD/Fq7q/xe07f8Pksv/QZqn5mG5uS5cu7wAWoB/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB/nwASms4AE5PEIQ+azcodjrnyD1mm/wEWeP8GZqX/GqTc/1zH3/82pM3/DaXt/w2v9P9Bwef/TM3r/w6W0v8jia/rNJCtNDKPrgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA2VzAAMlMoGDpPHNCeOtlYNSp7aAAeO/wQvpv8MnOL/FZ7d/w6T1f8Mf7v/EZ7e/zW+5f87v+H/CoXH/QaDveQKfqVAA4XPAA91gQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGbZwAComiAgRemEwCQJq9CVqy/RCWzv8Rhs3/BDOa/wMSbv8NXKX/Dajk/w6Z0P8feKnZDn60ugmLuqAPhaYKDYetAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWepoAGXGIBg+Aq2oUotfwEKfc/xBxuf8EHZL9ARSL/w9Yov8PjML/EpfJ40ObsV0WkcdWEJnSXQp2pQYNg7YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAx+rQALd6UOC4CzURSWzqgNoN3kDo/Hvw1ppnoGY6WUH4e6hRSVx9wMndGhBnmcCBM+YQAAyvoAAMr6AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABijAAAAAABB3uvXgd+tVIMhLNqEYqvERqLnAQEdKYEDp/aQwyd2DT1//8AAILFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/8D///+Af///gH///4Aw//+AIH//gAA//4AAP//AAB//wAAf/8AAD//AAB//gAAf/gAAH/wAAH/4AAD/+AAAf/gAAH/+AAA//gAAP/8AAD/+AAH//AAB//gAA//4AAP/+AAD//wAA//8AAP//AAD//8AAf//gAH//4AP///AH/8="""
icon_image = Image.open(BytesIO(base64.b64decode(icon_data)))
icon = ImageTk.PhotoImage(icon_image)
root.wm_iconbitmap()
root.iconphoto(True, icon)

tabview = customtkinter.CTkTabview(root,height = 490, width=660)
tabview.grid(row=0, column=2, padx=(20, 0), pady=(10, 0), sticky="nsew")
tabview.add("Table Bot")
tabview.add("Settings")
tabview.add("Screenshots")
tabview.add("Info")
tabview.tab("Settings").grid_columnconfigure(0, weight=1)
tabview.tab("Settings").grid_columnconfigure(1, weight=0)
tabview.tab("Settings").grid_columnconfigure(2, weight=1)

tagsfont = customtkinter.CTkFont(family="FOT-NewRodin Pro B", size=32)
scoresfont = customtkinter.CTkFont(family="DS-Digital", size=42, weight="bold")
smallerfont = customtkinter.CTkFont(family="DS-Digital", size=30, weight="bold")

infotext = customtkinter.CTkTextbox(tabview.tab("Info"), width=620, height=250)
infotext.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
infotext.insert("0.0", "Press Hotkey once you're on the sorted race results screen or the points finished adding up\nOnly enter the first Letter of Tag for DC Points (in this format: A10 B10 C10 D10 E10 F10)\nUse the normal Hotkey if youre using OBS method or watching Fullscreen (recommended)\nUse the Twitch Hotkey if youre watching twitch with chat opened (highly experimental)\nTwitch Mode might not work if youre not on Chrome and dont have something in your bookmarks \n(might not even work then)\n\nMade by tarek\nusing https://gb.hlorenzi.com/table\n\nDiscord: 9tarek\nin case of questions\nv2")
infotext.configure(state="disabled")




auto_copy_label = customtkinter.CTkLabel(tabview.tab("Settings"), text="Auto Copy to Clipboard", anchor="center")
auto_copy_label.grid(row=0, column=1, padx=0, pady=(5, 0))

def auto_copy_menu_callback(choice):
    global autocopy
    autocopy = choice

auto_copy_menu = customtkinter.CTkOptionMenu(tabview.tab("Settings"), values=["Disabled", "Table", "Scores"], command=auto_copy_menu_callback, anchor="center")
auto_copy_menu.grid(row=1, column=1, pady=(0, 0))
auto_copy_menu.set(autocopy)



def set_dc_points(driver):
    global dc_points
    global currentimg
    global tableimg
    dc_points = dc_points_field.get()
    if currentimg != 0:
        pywinstyles.set_opacity(image_label, value=0.2)
        add_dc_points(driver)
        images = driver.find_elements(By.TAG_NAME, "img")
        image_element = images[7]
        image_url = image_element.get_attribute("src")

        if image_url.startswith("data:image/png;base64,"):
            base64_data = image_url.split(",")[1]
            image_data = base64.b64decode(base64_data)
            img = Image.open(BytesIO(image_data))
            currentimg = img

            max_size = (600, 363)
            img.thumbnail(max_size)

            tableimg.configure(dark_image=img)
            image_label.configure(image=tableimg)
            image_label.image = tableimg
            pywinstyles.set_opacity(image_label, value=1)
        
        if autocopy == "Table":
            send_to_clipboard()
        elif autocopy == "Scores":
            copy_scores_to_clipboard(driver)
        check_for_dc_points(driver)
        if obs_overlay_active:
            update_obs_overlay(driver)

def clear_dc_points(driver):
    dc_points_field.delete(0, "end")
    set_dc_points(driver)

def roomcrash(driver):
    scores = driver.find_element(By.TAG_NAME, "textarea")
    scoresvalue = scores.get_attribute("value")
    scoresfr = {}
    pattern = re.compile(r"^(.*?) (?:\[\w{2}\] )?(\d+(\+\d+)*)$")
    for line in scoresvalue.split("\n"):
        match = pattern.match(line)
        if match:
            name = match.group(1)
            name = name.lstrip()
            score_str = match.group(2)
            score = sum(int(x) for x in score_str.split("+"))

            initial = name[0].upper()
            if initial in scoresfr:
                scoresfr[initial] += score
            else:
                scoresfr[initial] = score
    sortedscores = sorted(scoresfr.items(), key=lambda x: x[1], reverse=True)

    out = " ".join([f"{key}{value}" for key, value in sortedscores])
    dc_points_field.delete(0, "end") 
    dc_points_field.insert(0, out)
    global dc_points
    dc_points = out

def fill_in_tags(driver):
    scores = driver.find_element(By.TAG_NAME, "textarea")
    scoresvalue = scores.get_attribute("value")
    tags = set()
    pattern = re.compile(r"^(.*?) (?:\[\w{2}\] )?(\d+(\+\d+)*)$")
    for line in scoresvalue.split("\n"):
        match = pattern.match(line)
        if match:
            name = match.group(1)
            name = name.lstrip()
            initial = name[0].upper()
            tags.add(initial)

    out = "".join([f"{key}" for key in tags])
    dc_points_field.insert("end", out)


dc_points_label = customtkinter.CTkLabel(tabview.tab("Settings"), text="DC Points")
dc_points_label.grid(row=2, column=1, pady=(10, 0))

dc_points_field = customtkinter.CTkEntry(tabview.tab("Settings"), placeholder_text="e.g. A6 B10 C2")
dc_points_field.grid(row=3, column=1, pady=(0, 0))



button_frame_settings = customtkinter.CTkFrame(tabview.tab("Settings"))
button_frame_settings.grid(row=4, column=1, pady=(10, 0))

fill_in_tags_button = customtkinter.CTkButton(button_frame_settings, text="Insert Tags", command=lambda: fill_in_tags(driver))
fill_in_tags_button.grid(row=1, column=1, pady=(10, 0))

dc_points_clear = customtkinter.CTkButton(button_frame_settings, text="Clear", command=lambda: clear_dc_points(driver))
dc_points_clear.grid(row=0, column=0, padx=(5, 5))

roomcrash_button = customtkinter.CTkButton(button_frame_settings, text="Room Crash", command=lambda: roomcrash(driver))
roomcrash_button.grid(row=0, column=2, padx=(5, 5))

dc_points_submit = customtkinter.CTkButton(button_frame_settings, text="Submit", command=lambda: set_dc_points(driver))
dc_points_submit.grid(row=0, column=1, padx=(5, 5))


def change_hotkey():
    status_label.configure(text="Listening...")
    root.bind("<Key>", set_hotkey)
    
def set_hotkey(event):
    global hotkey
    if event.keysym == "Escape":
        if hotkey:
            keyboard.remove_hotkey(hotkey)
        hotkey = None
        status_label.configure(text=f"Current: None")
    else:
        if hotkey:
            keyboard.remove_hotkey(hotkey)
        hotkey = event.keysym
        keyboard.add_hotkey(hotkey, lambda: upload_screenshot(driver))
        status_label.configure(text=f"Current: {hotkey}")
    root.unbind("<Key>")

def change_twitch_hotkey():
    twitch_status_label.configure(text="Listening...")
    root.bind("<Key>", set_twitch_hotkey)
    
def set_twitch_hotkey(event):
    global twitchhotkey
    if event.keysym == "Escape":
        if twitchhotkey:
            keyboard.remove_hotkey(twitchhotkey)
        twitchhotkey = None
        twitch_status_label.configure(text=f"Current: None")
    else:
        if twitchhotkey:
            keyboard.remove_hotkey(hotkey)
        twitchhotkey = event.keysym
        keyboard.add_hotkey(twitchhotkey, lambda: upload_screenshot_twitch(driver))
        twitch_status_label.configure(text=f"Current: {twitchhotkey}")
    root.unbind("<Key>")

    
hotkeys_label = customtkinter.CTkLabel(tabview.tab("Settings"), text="Hotkeys")
hotkeys_label.grid(row=5, column=1, pady=(10, 0))    
button_frame_hotkeys = customtkinter.CTkFrame(tabview.tab("Settings"))
button_frame_hotkeys.grid(row=6, column=1, pady=(0, 0))    

change_hotkey_button = customtkinter.CTkButton(button_frame_hotkeys, text="Change Hotkey", command=change_hotkey)
change_hotkey_button.grid(row=0, column=0, padx=(5, 5))

if hotkey:
    status_label = customtkinter.CTkLabel(button_frame_hotkeys, text="Current: " + hotkey, anchor="w")
else:
    status_label = customtkinter.CTkLabel(button_frame_hotkeys, text="Current: None", anchor="w")
status_label.grid(row=1, column=0, padx=0, pady=(0, 0))

change_twitch_hotkey_button = customtkinter.CTkButton(button_frame_hotkeys, text="Change Twitch Hotkey", command=change_twitch_hotkey)
change_twitch_hotkey_button.grid(row=0, column=1, padx=(5, 5))

if twitchhotkey:
    twitch_status_label = customtkinter.CTkLabel(button_frame_hotkeys, text="Current: " + twitchhotkey, anchor="w")
else:
    twitch_status_label = customtkinter.CTkLabel(button_frame_hotkeys, text="Current: None", anchor="w")
twitch_status_label.grid(row=1, column=1, padx=0, pady=(0, 0))


image_label = customtkinter.CTkLabel(tabview.tab("Table Bot"), text="")
image_label.grid(row=0, column=0, padx=(25,0), pady=10)

black_img = Image.new("RGB", (600, 363), color="black")
tableimg = customtkinter.CTkImage(dark_image=black_img, size=(600, 363))
image_label.configure(image=tableimg)
image_label.image = tableimg

currentss_label = customtkinter.CTkLabel(tabview.tab("Screenshots"), text="Current Screenshot", anchor="center")
recentss_label = customtkinter.CTkLabel(tabview.tab("Screenshots"), text="Recent Screenshot", anchor="center")
currentss_label.grid(row=0, column=0, padx=(0,0), pady=(25, 0))
recentss_label.grid(row=0, column=1, padx=(0,0), pady=(25, 0))

currentss_image_label = customtkinter.CTkLabel(tabview.tab("Screenshots"), text="", anchor="nw")
recentss_image_label = customtkinter.CTkLabel(tabview.tab("Screenshots"), text="", anchor="nw")
currentss_image_label.grid(row=1, column=0, padx=(14,20), pady=10)
recentss_image_label.grid(row=1, column=1, padx=(0,0), pady=10)

currentss = customtkinter.CTkImage(dark_image=black_img, size=(300, 300))
recentss = customtkinter.CTkImage(dark_image=black_img, size=(300, 300))
currentss_image_label.configure(image=currentss)
recentss_image_label.configure(image=recentss)




def send_to_clipboard():
    output = BytesIO()
    currentimg.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()

def copy_scores_to_clipboard(driver):
    scores = driver.find_element(By.TAG_NAME, "textarea")
    scoresvalue = scores.get_attribute("value")
    scoresfr = {}
    pattern = re.compile(r"^(.*?) (?:\[\w{2}\] )?(\d+(\+\d+)*)$")
    for line in scoresvalue.split("\n"):
        match = pattern.match(line)
        if match:
            name = match.group(1)
            name = name.lstrip()
            score_str = match.group(2)
            score = sum(int(x) for x in score_str.split("+"))

            initial = name[0].upper()
            if initial == "8" and not using_obs_virtual_cam:
                initial = "B"
            if initial in scoresfr:
                scoresfr[initial] += score
            else:
                scoresfr[initial] = score
    sortedscores = sorted(scoresfr.items(), key=lambda x: x[1], reverse=True)
    total_score = sum(scoresfr.values())

    out = " || ".join([f"{key} {value}" for key, value in sortedscores])
    if ((total_score % 82) == 0):
        out += f" || @{12 - int(total_score / 82)}"
    else:
        out += f" || @{12 - (int(total_score / 82) + 1)} (missing {82 - (total_score % 82)} pts)"
    pyperclip.copy(out)

def check_for_dc_points(driver):
    global dc_score
    scores = driver.find_element(By.TAG_NAME, "textarea")
    scoresvalue = scores.get_attribute("value")
    total = 0
    pattern = re.compile(r"^(.*?) (?:\[\w{2}\] )?(\d+(\+\d+)*)$")
    for line in scoresvalue.split("\n"):
        match = pattern.match(line)
        if match:
            score_str = match.group(2)
            score = sum(int(x) for x in score_str.split("+"))
            total += score
    if total % 82 == 0:
        dc_score = 0
        missing_points_label.configure(text="")
    else:
        dc_score = 82 - (total % 82)
        missing_points_label.configure(text=f"Missing: {dc_score}pts")

button_frame = customtkinter.CTkFrame(tabview.tab("Table Bot"))
button_frame.grid(row=1, column=0, padx=(0, 0), pady=10)

copy_button = customtkinter.CTkButton(button_frame, text="Copy Table", command=send_to_clipboard)
copy_button.grid(row=0, column=0, padx=20, pady=0)

copy_scores_button = customtkinter.CTkButton(button_frame, text="Copy Scores", command=lambda: copy_scores_to_clipboard(driver))
copy_scores_button.grid(row=0, column=1, pady=0)

missing_points_label = customtkinter.CTkLabel(tabview.tab("Table Bot"), text="")
missing_points_label.grid(row=1, padx=(500,0), pady=(0,0))

def add_dc_points(driver):
    dc_scores = dc_points.split()
    scores = driver.find_element(By.TAG_NAME, "textarea")
    scoresvalue = scores.get_attribute("value")
    lines = scoresvalue.splitlines()[::-1]
    dc_helper = {}
    for team in dc_scores:
        tag = team[0].upper()
        points = team[1:]
        dc_helper[tag] = points
    new_html = []
    added_tags = set()
    if dc_points != "":
        for line in lines:
            line = line.lstrip()
            if line != "":
                for tag, points in dc_helper.items():
                    if "+" in line[-5:]:
                        line = re.sub(r'\+\d+$', '', line)
                    if line[0].upper() == tag and tag not in added_tags:
                        line += "+" + points
                        added_tags.add(tag)
                        break
                new_html.append(line)
    else: 
        for line in lines:
            if line != "":
                if "+" in line[-5:]:
                    line = re.sub(r'\+\d+$', '', line)
                new_html.append(line)         

    new_html = new_html[::-1]
    new_html = "\n".join(new_html)
    scores.clear()  
    scores.send_keys(new_html)
    images = driver.find_elements(By.TAG_NAME, "img")
    image_element = images[7]
    while True:
        if image_element.get_attribute("style").split(";")[3].split(":")[1] == " 1":
            break

obs_overlay_not_active_scores = """ÍÍÍ''Ý!|¡¡įįį [au] 0"""

def upload_screenshot(driver):
    broke = False
    global tableimg
    global recentss, currentss
    if not using_obs_virtual_cam:
        screenshot = ImageGrab.grab()
        screenshot_data = BytesIO()
        screenshot.save(screenshot_data, format="PNG")
        screenshot_data.seek(0)

        temp_screenshot_path = os.path.join(os.getcwd(), datetime.now().strftime("%Y-%m-%d %H-%M-%S.png"))
        with open(temp_screenshot_path, "wb") as temp_screenshot_file:
            temp_screenshot_file.write(screenshot_data.read())
    else:
        temp_screenshot_path = capture_image_from_obs_virtual_camera()

    try:
        upload_element = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        upload_element.send_keys(temp_screenshot_path)

        pywinstyles.set_opacity(image_label, value=0.2)

        images = driver.find_elements(By.TAG_NAME, "img")
        image_element = images[7]
        time.sleep(0.5)
        while True:
            if image_element.get_attribute("style").split(";")[3].split(":")[1] == " 1":
                break
        scores = driver.find_element(By.TAG_NAME, "textarea")
        scoresvalue = scores.get_attribute("value")
        if "¹■" in scoresvalue:
            scoresvalue = scoresvalue.replace("¹■", "VA")
            scores.clear()
            scores.send_keys(scoresvalue)
        if obs_overlay_not_active_scores in scoresvalue.replace("\n", ""):
            broke = True
            pywinstyles.set_opacity(image_label, value=1)
        else:
            if dc_points != "":
                add_dc_points(driver)
            else: 
                scores.send_keys(" ")
                while True:
                    if image_element.get_attribute("style").split(";")[3].split(":")[1] == " 1":
                        break
                
            image_url = image_element.get_attribute("src")

            if image_url.startswith("data:image/png;base64,"):
                base64_data = image_url.split(",")[1]
                image_data = base64.b64decode(base64_data)
                img = Image.open(BytesIO(image_data))
                global currentimg
                currentimg = img
                
                max_size = (600, 363)
                img.thumbnail(max_size)

                tableimg.configure(dark_image=img)
                image_label.configure(image=tableimg)
                image_label.image = tableimg
                pywinstyles.set_opacity(image_label, value=1)

        screenshot_image = Image.open(temp_screenshot_path)
        cropped_image = screenshot_image.crop((795, 0, 1875, 1080))
        cropped_image.save(temp_screenshot_path, format="PNG")

        ss_ctk_image = customtkinter.CTkImage(dark_image=cropped_image, size=(300, 300))
        recentss = currentss
        currentss = ss_ctk_image
        currentss_image_label.configure(image=currentss)
        recentss_image_label.configure(image=recentss)
        screenshot_image.close()
        

    finally:
        os.remove(temp_screenshot_path)
        if not broke:
            if obs_overlay_active:
                update_obs_overlay(driver)
            check_for_dc_points(driver)
            if autocopy == "Table":
                send_to_clipboard()
            elif autocopy == "Scores":
                copy_scores_to_clipboard(driver)


def upload_screenshot_twitch(driver):
    global tableimg
    global recentss, currentss
    screenshot = ImageGrab.grab()
    cropped_image = screenshot.crop((left, top, right, bottom))
    new_size = (1920, 1080)
    screenshot = cropped_image.resize(new_size, Image.LANCZOS)
    screenshot_data = BytesIO()
    screenshot.save(screenshot_data, format="PNG")
    screenshot_data.seek(0)


    temp_screenshot_path = os.path.join(os.getcwd(), datetime.now().strftime("%Y-%m-%d %H-%M-%S"))
    with open(temp_screenshot_path, "wb") as temp_screenshot_file:
        temp_screenshot_file.write(screenshot_data.read())

    try:
        upload_element = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        upload_element.send_keys(temp_screenshot_path)
        pywinstyles.set_opacity(image_label, value=0.2)
        images = driver.find_elements(By.TAG_NAME, "img")
        image_element = images[7]
        time.sleep(0.5)
        while True:
            if image_element.get_attribute("style").split(";")[3].split(":")[1] == " 1":
                break
        scores = driver.find_element(By.TAG_NAME, "textarea")
        scoresvalue = scores.get_attribute("value")
        if "¹■" in scoresvalue or "¹ı■" in scoresvalue:
            scoresvalue = scoresvalue.replace("¹■", "VA")
            scoresvalue = scoresvalue.replace("¹ı■", "VA")
            scores.clear()
            scores.send_keys(scoresvalue)
        if dc_points != "":
            add_dc_points(driver)
        else: 
            scores.send_keys(" ")
            while True:
                if image_element.get_attribute("style").split(";")[3].split(":")[1] == " 1":
                    break
        
        image_url = image_element.get_attribute("src")

        if image_url.startswith("data:image/png;base64,"):
            base64_data = image_url.split(",")[1]
            image_data = base64.b64decode(base64_data)
            img = Image.open(BytesIO(image_data))
            global currentimg
            currentimg = img

            max_size = (600, 363)
            img.thumbnail(max_size)

            tableimg.configure(dark_image=img)
            image_label.configure(image=tableimg)
            image_label.image = tableimg
            pywinstyles.set_opacity(image_label, value=1)
        
        screenshot_image = Image.open(temp_screenshot_path)
        cropped_image = screenshot_image.crop((795, 0, 1875, 1080))
        cropped_image.save(temp_screenshot_path, format="PNG")

        ss_ctk_image = customtkinter.CTkImage(dark_image=cropped_image, size=(300, 300))
        recentss = currentss
        currentss = ss_ctk_image
        currentss_image_label.configure(image=currentss)
        recentss_image_label.configure(image=recentss)
        screenshot_image.close()
        

    finally:
        os.remove(temp_screenshot_path)
        if obs_overlay_active:
            update_obs_overlay(driver)
        check_for_dc_points(driver)
        if autocopy == "Table":
            send_to_clipboard()
        elif autocopy == "Scores":
            copy_scores_to_clipboard(driver)


obs_overlay_window = None

def close_obs():
    global obs_overlay_window
    global obs_overlay_active
    
    obs_overlay_active = False
    obs_overlay_window.destroy()
    obs_overlay_checkbox.deselect()
def toggle_obs(driver):
    global obs_overlay_active
    global obs_overlay_window
    global icon

    if not obs_overlay_active:
        obs_overlay_window = customtkinter.CTkToplevel()
        obs_overlay_window.geometry("780x125")
        obs_overlay_window.title("Scores Overlay")
        obs_overlay_window.resizable(False, False)
        obs_overlay_window.configure(fg_color="green")
        obs_overlay_window.iconphoto(True, icon)
        
        obs_overlay_active = True
        obs_overlay_window.protocol("WM_DELETE_WINDOW", close_obs)
        if currentimg != 0:
            update_obs_overlay(driver)
        else: 
            resetoverlay(driver)
            
    else:
        close_obs()

obs_overlay_checkbox = customtkinter.CTkCheckBox(tabview.tab("Settings"), command=lambda: toggle_obs(driver), text="OBS Overlay")
obs_overlay_checkbox.grid(row=8, column=1, pady=(15, 0))

def capture_image_from_obs_virtual_camera():
    for _ in range(3):
        cap.read()

    ret, frame = cap.read()
    if not ret:
        raise ValueError("Couldnt capture Screenshot")

    # Check the actual resolution of the captured frame
    height, width, _ = frame.shape

    temp_screenshot_path = os.path.join(os.getcwd(), datetime.now().strftime("%Y-%m-%d %H-%M-%S.png"))

    # Save the captured frame as a PNG file in full resolution
    if width == 1920 and height == 1080:
        cv2.imwrite(temp_screenshot_path, frame)
        return temp_screenshot_path
    else:
        raise ValueError("Screnshot not 1920x1080 (Maybe selected wrong Capture Device)")
    

def get_obs_virtual_cam_index():
    graph = FilterGraph()
    devices = graph.get_input_devices()
    for index, name in enumerate(devices):
        if "OBS Virtual Camera" in name:
            return index
    # Return None or raise an error if the OBS Virtual Camera is not found
    raise ValueError("OBS Virtual Camera not found (make sure OBS is installed)")

def toggle_using_obs_virtual_cam():
    global using_obs_virtual_cam
    global cap
    if not using_obs_virtual_cam:
        obs_virtual_cam_index = get_obs_virtual_cam_index()
        cap = cv2.VideoCapture(obs_virtual_cam_index)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
        using_obs_virtual_cam = True
    else:
        cap.release()
        cap = None
        using_obs_virtual_cam = False

using_obs_virtual_cam_checkbox = customtkinter.CTkCheckBox(tabview.tab("Settings"), command=toggle_using_obs_virtual_cam, text="Using OBS Virtual Camera")
using_obs_virtual_cam_checkbox.grid(row=9, column=1, pady=(15, 0))



placeholder_2v2_data = b"""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"""
placeholder_2v2_imagetk = ImageTk.PhotoImage(Image.open(BytesIO(base64.b64decode(placeholder_2v2_data))))

placeholder_3v3_data = b"""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"""
placeholder_3v3_imagetk = ImageTk.PhotoImage(Image.open(BytesIO(base64.b64decode(placeholder_3v3_data))))

placeholder_4v4_data = b"""iVBORw0KGgoAAAANSUhEUgAAAYYAAAB9CAYAAACmosSLAAAAAXNSR0IArs4c6QAACi9JREFUeF7tnX9PU2kYRN+3pVDaolBFP9z6t5/M/XAuBlDbUn60d3O7SmQFAQP3jMkha7JxkRnPPJnZFltr+c2Pwzdvm6urq7Jarcp63f5oSinN5h8//jwC7979VT58+PvPM67jJyXgHTwpzu6+WG2laun12h/90u/3y9bWVjn65+Pmvzz249G/aH86bS4vLkuzXj9Wy88PJmAhBIfToTXvoEPYHUjVXq8Mtgfl9Pj4UV3/4E/ePzhoLs4vOvitKEEQsBAI6nma3kFeJk/laHtnu5yenDyo8+/9pOnrw2Z5dlZK43NETxVQ4texEBJT6d6Td9A9804Vay3D3d1y/Onol93/y//oo4ROI0PFLAQUf4y4dxATxbMaue/Rw53D8OLlfnN1efms5vziOQQshJwsSCfeAUm/W+2twaB8+Xx66wbc+pOOQrcBJahZCAkp8B68Az6DLh3cNQ4/DYNPH3UZS46WhZCTBenEOyDpM9q3Pa10Yxg232heLBh3qqIELAQUf4y4dxATRadGhqPRjW9I3xiG0XjS+KePOs0jRsxCiIkCNeIdoPg58VrLYj673oPrf/EpJC6TBGULISEF3oN3wGdAOfjxKaXrYRiNxr5QgUokQNdCCAghwIJ3EBACaGGxmH97c41SSvs2FxfLc9CO0jQBC4FOIEPfO8jIgXKxPdzZvH3GZh3Gk73G9z6iosjQtRAycqBdeAd0Aqx++95K89nXWtt3SZ3PZqwb1XECFgIeQYQB7yAiBtTEeDIp9WD6qjlfLlEjivMELAQ+gwQH3kFCCqyHneGwVF/lzIaQom4hpCTB+vAOWP4J6u2roetkb69Zr/y7FRICIT1YCCT9HG3vICcLykmv3yvVF7VR+LN0LYSsPCg33gFFPki31nYYxo1/HWdQKJAVCwECHybrHYQFQtippVRf2EaQz9O0EPIyIRx5BwT1PE2HIS8TxJGFgGCPE/UO4iJBDDkMCPY8UQshLxPCkXdAUM/TdBjyMkEcWQgI9jhR7yAuEsSQw4BgzxO1EPIyIRx5BwT1PE2HIS8TxJGFgGCPE/UO4iJBDDkMCPY8UQshLxPCkXdAUM/TdBjyMkEcWQgI9jhR7yAuEsSQw4BgzxO1EPIyIRx5BwT1PE2HIS8TxJGFgGCPE/UO4iJBDDkMCPY8UQshLxPCkXdAUM/TdBjyMkEcWQgI9jhR7yAuEsSQw4BgzxO1EPIyIRx5BwT1PE2HIS8TxJGFgGCPE/UO4iJBDDkMCPY8UQshLxPCkXdAUM/TdBjyMkEcWQgI9jhR7yAuEsSQw4BgzxO1EPIyIRx5BwT1PE2HIS8TxJGFgGCPE/UO4iJBDDkMCPY8UQshLxPCkXdAUM/TdBjyMkEcWQgI9jhR7yAuEsSQw4BgzxO1EPIyIRx5BwT1PE2HIS8TxJGFgGCPE/UO4iJBDDkMCPY8UQshLxPCkXdAUM/TdBjyMkEcWQgI9jhR7yAuEsSQw4BgzxO1EPIyIRx5BwT1PM36/v37Js+WjiQgAQlIgCLgIwaKfJiu/6cYFghkxzuAwIfJOgxhgVB2LASKfJaud5CVB+XGYaDIh+laCGGBQHa8Awh8mKzDEBYIZcdCoMhn6XoHWXlQbhwGinyYroUQFghkxzuAwIfJOgxhgVB2LASKfJaud5CVB+XGYaDIh+laCGGBQHa8Awh8mKzDEBYIZcdCoMhn6XoHWXlQbhwGinyYroUQFghkxzuAwIfJOgxhgVB2LASKfJaud5CVB+XGYaDIh+laCGGBQHa8Awh8mKzDEBYIZcdCoMhn6XoHWXlQbhwGinyYroUQFghkxzuAwIfJOgxhgVB2LASKfJaud5CVB+XGYaDIh+laCGGBQHa8Awh8mKzDEBYIZcdCoMhn6XoHWXlQbhwGinyYroUQFghkxzuAwIfJOgxhgVB2LASKfJaud5CVB+XGYaDIh+laCGGBQHa8Awh8mKzDEBYIZcdCoMhn6XoHWXlQbhwGinyYroUQFghkxzuAwIfJOgxhgVB2LASKfJaud5CVB+XGYaDIh+laCGGBQHa8Awh8mKzDEBYIZcdCoMhn6XoHWXlQbhwGinyYroUQFghkxzuAwIfJOgxhgVB2LASKfJaud5CVB+XGYaDIh+laCGGBQHa8Awh8mKzDEBYIZcdCoMhn6XoHWXlQbhwGinyYroUQFghkxzuAwIfJOgxhgVB2LASKfJaud5CVB+XGYaDIh+laCGGBQHa8Awh8mKzDEBYIZcdCoMhn6XoHWXlQbhwGinyYroUQFghkxzuAwIfJOgxhgVB2LASKfJaud5CVB+XGYaDIh+laCGGBQHa8Awh8mKzDEBYIZcdCoMhn6XoHWXlQbhwGinyYroUQFghkxzuAwIfJOgxhgVB2LASKfJaud5CVB+XGYaDIh+laCGGBQHa8Awh8mKzDEBYIZcdCoMhn6XoHWXlQbhwGinyYroUQFghkxzuAwIfJOgxhgVB2LASKfJaud5CVB+XGYaDIh+laCGGBQHa8Awh8mKzDEBYIZcdCoMhn6XoHWXlQbhwGiry6EpCABEIJOAyhwWhLAhKQAEXAYaDIqysBCUgglIDDEBqMtiQgAQlQBBwGiry6EpCABEIJOAyhwWhLAhKQAEXAYaDIqysBCUgglIDDEBqMtiQgAQlQBBwGiry6EpCABEIJOAyhwWhLAhKQAEXAYaDIqysBCUgglIDDEBqMtiQgAQlQBBwGiry6EpCABEIJOAyhwWhLAhKQAEXAYaDIqysBCUgglEAdjcdNaULdaUsCEpCABLolUEupo/GkKY3L0C151SQgAQmEEqi11MneXrNerUMdaksCEpCABLok0Ov3Sn3xcr+5urzsUlctCUhAAhIIJbA1GJR6MH3VnC+XoRa1JQEJSEACXRLYGQ5LPXzztpnPZl3qqiUBCUhAAqEExpNJqa238WSvadZ+nyE0J21JQAIS6IRA7fXKfPa1boZhfzptLpbnnQgrIgEJSEACmQS2hzvl9Pj4v2FoP0ajsX9mNTMrXUlAAhLohMBiMd9swvUw7B8cNBfnF52IKyIBCUhAAlkEtne2y+nJyc1h2Dxq8MVuWUnpRgISkEAXBGoti/ns+oHC9b+02tPXh81ysejChhoSkIAEJBBCYDgaleNPR7cPQ+vRp5RCktKGBCQggQ4I/PgU0ne5G48Yvv+kr4buIA0lJCABCcAE2lc5f/l8+tMO3DoMrVfHAU5MeQlIQALPSOCuUWgl7xwGn1Z6xkT80hKQgARAArc9ffSjnV8OQ/uJm29In50V35obTFFpCUhAAk9BoNYy3N298Y3m277svcPw/Rf5TemnSMWvIQEJSIAhcN+jhEc9Yvj/b6F9+4zLi8vieysx4aoqAQlI4KEE2vc+GmwPNm9z8dBf037eoz75xy/cvivr1dVVWa1WZb1uf7TvqNFs/vFDAhKQgAQ6JPDt9cq9Xi29Xr/0+/2ytbVVjv75+Fsd/y9ewX7AuL0ntAAAAABJRU5ErkJggg=="""
placeholder_4v4_imagetk = ImageTk.PhotoImage(Image.open(BytesIO(base64.b64decode(placeholder_4v4_data))))


def update_obs_overlay(driver):
    global obs_overlay_window
    scores = driver.find_element(By.TAG_NAME, "textarea")
    scoresvalue = scores.get_attribute("value")
    scoresfr = {}
    pattern = re.compile(r"^(.*?) (?:\[\w{2}\] )?(\d+(\+\d+)*)$")
    for line in scoresvalue.split("\n"):
        match = pattern.match(line)
        if match:
            name = match.group(1)
            name = name.lstrip()
            score_str = match.group(2)
            score = sum(int(x) for x in score_str.split("+"))

            initial = name[0].upper()
            if initial == "8" and not using_obs_virtual_cam:
                initial = "B"
            if initial in scoresfr:
                scoresfr[initial] += score
            else:
                scoresfr[initial] = score
    sortedscores = sorted(scoresfr.items(), key=lambda x: x[1], reverse=True)
    total_score = sum(scoresfr.values())
    if ((total_score % 82) == 0):
        races_left = f"@{12 - int(total_score / 82)}"
        missingpoints = 0
    else:
        races_left = f"@{12 - (int(total_score / 82) + 1)}"
        missingpoints = 82 - (total_score % 82)


    tags = [key for key, _ in sortedscores]
    teamscores = [value for key, value in sortedscores]
    if len(tags) > 6:
        tags = tags[:6]
        teamscores = teamscores[:6]
    elif len(tags) == 5:
        tags = tags[:4]
        teamscores = teamscores[:4]

    if len(tags) == 6: #2v2
        clear_imagetk = customtkinter.CTkImage(dark_image=(Image.new("RGB", (780, 125), "#008000")))
        clear_label = customtkinter.CTkLabel(master=obs_overlay_window, width=780, height=125, image=clear_imagetk)
        clear_label.place(x=0, y=0)
        imageholder_canvas = customtkinter.CTkCanvas(master=obs_overlay_window, width=780, height=125, bg="green", highlightthickness = 0)
        imageholder_canvas.place(x=0, y=0)
        imageholder_canvas.create_image((0, 0), image=placeholder_2v2_imagetk, anchor="nw")
        for i in range(6): 
            x_position = (i * 130) + 65  
            imageholder_canvas.create_text((x_position, 22), text=f"{tags[i]}", font=tagsfont, anchor="center", fill="white")
            imageholder_canvas.create_text((x_position, 67), text=f"{teamscores[i]}", font=scoresfont, anchor="center", fill="white")

        for i in range(5): 
            x_position_1 = (i * 130) + 65 
            x_position_2 = ((i + 1) * 130) + 65  

            score_diff = abs(teamscores[i] - teamscores[i + 1])

            diff_x_position = (x_position_1 + x_position_2) / 2  
            diff_y_position =  90 + (35 // 2)

            imageholder_canvas.create_text((diff_x_position, diff_y_position), text=f"+{score_diff}", font=smallerfont, anchor="center", fill="white")
        imageholder_canvas.create_text((720,(90 + 35 // 2)), text=f"{races_left}", font=smallerfont, anchor="center", fill="medium purple")
        if missingpoints != 0:
            imageholder_canvas.create_text((40,(90 + 35 // 2)), text=f"-{missingpoints}", font=smallerfont, anchor="center", fill="red")
    elif len(tags) == 4: #3v3
        clear_imagetk = customtkinter.CTkImage(dark_image=(Image.new("RGB", (780, 125), "#008000")))
        clear_label = customtkinter.CTkLabel(master=obs_overlay_window, width=780, height=125, image=clear_imagetk)
        clear_label.place(x=0, y=0)

        imageholder_canvas = customtkinter.CTkCanvas(master=obs_overlay_window, width=520, height=125, bg="green", highlightthickness=0)
        imageholder_canvas.place(x=((780 - 520) // 2), y=0)  
        imageholder_canvas.create_image((0, 0), image=placeholder_3v3_imagetk, anchor="nw")
        
        for i in range(4):
            x_position = (i * 130) + 65  
            imageholder_canvas.create_text((x_position, 22), text=f"{tags[i]}", font=tagsfont, anchor="center", fill="white")
            imageholder_canvas.create_text((x_position, 67), text=f"{teamscores[i]}", font=scoresfont, anchor="center", fill="white")
        
        for i in range(3): 
            x_position_1 = (i * 130) + 65 
            x_position_2 = ((i + 1) * 130) + 65  

            score_diff = abs(teamscores[i] - teamscores[i + 1])

            diff_x_position = (x_position_1 + x_position_2) / 2  
            diff_y_position =  90 + (35 // 2)

            imageholder_canvas.create_text((diff_x_position, diff_y_position), text=f"+{score_diff}", font=smallerfont, anchor="center", fill="white")
        
        imageholder_canvas.create_text((460,(90 + 35 // 2)), text=f"{races_left}", font=smallerfont, anchor="center", fill="medium purple")
        if missingpoints != 0:
            imageholder_canvas.create_text((40,(90 + 35 // 2)), text=f"-{missingpoints}", font=smallerfont, anchor="center", fill="red")
    elif len(tags) == 3: #4v4
        clear_imagetk = customtkinter.CTkImage(dark_image=(Image.new("RGB", (780, 125), "#008000")))
        clear_label = customtkinter.CTkLabel(master=obs_overlay_window, width=780, height=125, image=clear_imagetk)
        clear_label.place(x=0, y=0)
        imageholder_canvas = customtkinter.CTkCanvas(master=obs_overlay_window, width=390, height=125, bg="green", highlightthickness=0)
        imageholder_canvas.place(x=((780 - 390) // 2), y=0)
        imageholder_canvas.create_image((0, 0), image=placeholder_4v4_imagetk, anchor="nw")


        positions = [65, 195, 325]  

        for i in range(3): 
            x_position = positions[i]
            imageholder_canvas.create_text((x_position, 22), text=f"{tags[i]}", font=tagsfont, anchor="center", fill="white")
            imageholder_canvas.create_text((x_position, 67), text=f"{teamscores[i]}", font=scoresfont, anchor="center", fill="white")

        for i in range(2): 
            x_position_1 = positions[i]
            x_position_2 = positions[i + 1]
            score_diff = abs(teamscores[i] - teamscores[i + 1])

            diff_x_position = (x_position_1 + x_position_2) / 2
            diff_y_position = 90 + (35 // 2)

            imageholder_canvas.create_text((diff_x_position, diff_y_position), text=f"+{score_diff}", font=smallerfont, anchor="center", fill="white")

        imageholder_canvas.create_text((360, (90 + 35 // 2)), text=f"{races_left}", font=smallerfont, anchor="center", fill="medium purple")

        if missingpoints != 0:
            imageholder_canvas.create_text((30, (90 + 35 // 2)), text=f"-{missingpoints}", font=smallerfont, anchor="center", fill="red")
    elif len(tags) == 2: #6v6
        clear_imagetk = customtkinter.CTkImage(dark_image=(Image.new("RGB", (780, 125), "#008000")))
        clear_label = customtkinter.CTkLabel(master=obs_overlay_window, width=780, height=125, image=clear_imagetk)
        clear_label.place(x=0, y=0)

        imageholder_canvas = customtkinter.CTkCanvas(master=obs_overlay_window, width=390, height=125, bg="green", highlightthickness=0)
        imageholder_canvas.place(x=((780 - 390) // 2), y=0)
        imageholder_canvas.create_image((0, 0), image=placeholder_4v4_imagetk, anchor="nw")

        positions = [65, 195, 325]
        imageholder_canvas.create_text((65, 22), text=f"{tags[0]}", font=tagsfont, anchor="center", fill="white")
        imageholder_canvas.create_text((65, 67), text=f"{teamscores[0]}", font=scoresfont, anchor="center", fill="white")
        imageholder_canvas.create_text((325, 22), text=f"{tags[1]}", font=tagsfont, anchor="center", fill="white")
        imageholder_canvas.create_text((325, 67), text=f"{teamscores[1]}", font=scoresfont, anchor="center", fill="white")

        score_diff = abs(teamscores[0] - teamscores[1])


        imageholder_canvas.create_text((195, 22), text=f"+{score_diff}", font=smallerfont, anchor="center", fill="white")
        imageholder_canvas.create_text((195, 67), text="-", font=smallerfont, anchor="center", fill="white")

        imageholder_canvas.create_text((340, (90 + 35 // 2)), text=f"{races_left}", font=smallerfont, anchor="center", fill="medium purple")

        if missingpoints != 0:
            imageholder_canvas.create_text((50, (90 + 35 // 2)), text=f"-{missingpoints}", font=smallerfont, anchor="center", fill="red")

def resetoverlay(driver):
    scores = driver.find_element(By.TAG_NAME, "textarea")
    scores.clear()
    scores.send_keys(" ")

    images = driver.find_elements(By.TAG_NAME, "img")
    image_element = images[7]
    time.sleep(0.1)
    while True:
        if image_element.get_attribute("style").split(";")[3].split(":")[1] == " 1":
            break
    image_url = image_element.get_attribute("src") 
    if image_url.startswith("data:image/png;base64,"):
        base64_data = image_url.split(",")[1]
        image_data = base64.b64decode(base64_data)
        img = Image.open(BytesIO(image_data))
        max_size = (600, 363)
        img.thumbnail(max_size) 
        tableimg.configure(dark_image=img)
        image_label.configure(image=tableimg)
        image_label.image = tableimg
        if obs_overlay_active:
            imageholder_canvas = customtkinter.CTkCanvas(master=obs_overlay_window, width=780, height=125, bg="green", highlightthickness = 0)
            imageholder_canvas.place(x=0, y=0)
            imageholder_canvas.create_image((0, 0), image=placeholder_2v2_imagetk, anchor="nw")
            for i in range(6): #2v2
                x_position = (i * 130) + 65  
                imageholder_canvas.create_text((x_position, 22), text="-", font=tagsfont, anchor="center", fill="white")
                imageholder_canvas.create_text((x_position, 67), text="0", font=scoresfont, anchor="center", fill="white")

            for i in range(5): 
                x_position_1 = (i * 130) + 65 
                x_position_2 = ((i + 1) * 130) + 65  

                diff_x_position = (x_position_1 + x_position_2) / 2  
                diff_y_position =  90 + (35 // 2)

                imageholder_canvas.create_text((diff_x_position, diff_y_position), text="+0", font=smallerfont, anchor="center", fill="white")
                imageholder_canvas.create_text((720,(90 + 35 // 2)), text=f"@12", font=smallerfont, anchor="center", fill="medium purple")
        global currentimg
        currentimg = 0
        check_for_dc_points(driver)

reset_button = customtkinter.CTkButton(tabview.tab("Settings"), command=lambda: resetoverlay(driver), text="Reset Scores") 
reset_button.grid(row=7, column=1, pady=(10,0))
        


if __name__ == "__main__":

    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get("https://gb.hlorenzi.com/table")
    if hotkey:
        keyboard.add_hotkey(hotkey, lambda: upload_screenshot(driver))
    if twitchhotkey:
        keyboard.add_hotkey(twitchhotkey, lambda: upload_screenshot_twitch(driver))

    select_element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "selectTableGame")))
    select_element.click()

    select = Select(select_element)
    select.select_by_visible_text("MK8DX")
    select_element.click()
    

    images = driver.find_elements(By.TAG_NAME, "img")
    image_element = images[7]
    image_url = image_element.get_attribute("src")
    if image_url.startswith("data:image/png;base64,"):
        base64_data = image_url.split(",")[1]
        image_data = base64.b64decode(base64_data)
        img = Image.open(BytesIO(image_data))
        max_size = (600, 363)
        img.thumbnail(max_size) 
        tableimg.configure(dark_image=img)
        image_label.configure(image=tableimg)
        image_label.image = tableimg
    
    if obs_overlay_active:
        obs_overlay_active = not obs_overlay_active
        toggle_obs(driver)
        obs_overlay_checkbox.select()
    
    if using_obs_virtual_cam:
        using_obs_virtual_cam = not using_obs_virtual_cam
        toggle_using_obs_virtual_cam()
        using_obs_virtual_cam_checkbox.select()

    def on_closing():
        if hotkey != "Multi_key" and twitchhotkey !="Multi_key":
            save_settings()
        driver.quit()
        root.destroy()
        if using_obs_virtual_cam:
            cap.release() 

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()