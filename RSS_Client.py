#!/usr/bin/env python3

import urllib.request as request
import xml.etree.ElementTree as ET
import tkinter as tk

from pytube import YouTube
from pytube import Channel

RSS_Simple = "https://www.youtube.com/feeds/videos.xml?channel_id="
RSS_URL = "https://www.youtube.com/feeds/videos.xml?channel_id=UCR-DXc1voovS8nhAvccRZhg"
YouTube_URL = "https://www.youtube.com/watch?v=FBz7MX2bLcM"

def parsujRSS(rss_url):
    raw_page = request.urlopen(rss_url)
    rss = raw_page.read()

    vystup = list()

    root = ET.fromstring(rss)
    for potomok in root:
        if potomok.tag == "{http://www.w3.org/2005/Atom}entry":
            retazec = ""
            for obsahPolozky in potomok:
                if obsahPolozky.tag == "{http://www.w3.org/2005/Atom}title":
                    retazec += obsahPolozky.text + " | "
                if obsahPolozky.tag == "{http://www.w3.org/2005/Atom}link":
                    retazec += obsahPolozky.attrib["href"]
            vystup.append(retazec)

    return vystup

def vytvorGUI():
    okno = tk.Tk()
    nastavOkno(okno)
    okno.mainloop()

def open():
    okno2 = tk.Toplevel()
    nastavOkno2(okno2)

def nastavOkno(okno):
    okno.title("Youtube RSS parser novy")

    okno.geometry("800x600+800+600")
    okno.resizable(True, False)

    labelUrl = tk.Label(okno, text="Url:")
    labelUrl.grid(row=0, column=0, sticky="w", padx=5)

    entryUrl = tk.Entry(okno)
    entryUrl.grid(row=0, column=1, sticky="w", ipadx=250)
    entryUrl.insert(0, RSS_URL)

    ButtonUrl = tk.Button(okno, text="Parsuj", command=lambda: akciaButton(entryUrl.get(), textRSS))
    ButtonUrl.grid(row=0, column=2, padx=5)

    ButtonOpen = tk.Button(okno, text="Hladanie", command=open)
    ButtonOpen.grid(row=0, column=3, padx=5)

    textRSS = tk.Text(okno)
    textRSS.grid(row=1, column=0, columnspan=3, padx=5, ipadx=30)
    textRSS.place(x=5, y=30, width=770, height=600)

def akciaButton(url, textRSS):
    vystup = parsujRSS(url)
    textRSS.delete("1.0", tk.END)
    for i in vystup:
        textRSS.insert(tk.END, i + "\n")


def akciaHladanie(url, textChannel):
    x = YouTube(url)
    Cid = x.channel_id
    Curl = x.channel_url

    c = Channel(Curl)
    Cname = c.channel_name
    rssUrl = RSS_Simple+Cid

    textChannel.delete("1.0", tk.END)
    info = (""" Channel Name= {0}\n Channel ID= {1}\n Channel Url= {2}\n Channel RSS= {3}\n """.format(Cname, Cid, Curl, rssUrl))

    textChannel.insert(tk.END, info)

    print("\n")
    print(" Channel Name= ", Cname)
    print(" Channel ID= ", Cid)
    print(" Channel URL= ", Curl)
    print(" Channel RSS= ", rssUrl)



def nastavOkno2(okno):
    okno.title("Hladanie")

    okno.geometry("800x600+800+600")
    okno.resizable(True, False)

    labelUrl = tk.Label(okno, text="Url:")
    labelUrl.grid(row=0, column=0, sticky="w", padx=5)

    entryUrl = tk.Entry(okno)
    entryUrl.grid(row=0, column=1, sticky="w", ipadx=250)
    entryUrl.insert(0, YouTube_URL)

    ButtonUrl = tk.Button(okno, text="Hladaj", command=lambda: akciaHladanie(entryUrl.get(), textChannel))
    ButtonUrl.grid(row=0, column=2, padx=5)

    ButtonOpen = tk.Button(okno, text="Zavriet", command=okno.destroy)
    ButtonOpen.grid(row=0, column=3, padx=5)

    textChannel = tk.Text(okno)
    textChannel.grid(row=1, column=0, columnspan=3, padx=5, ipadx=30)
    textChannel.place(x=5, y=30, width=760, height=600)


if __name__ == "__main__":
    vytvorGUI()



































































