#!/usr/bin/env python3
"""Mix du Reel court (34,93 s) : voix d'origine coupée en 4 morceaux (dans les silences), bruitages recalés,
musique originale (compose-music.py) baissée sous la voix (sidechain), loudnorm -16 LUFS.
Usage : python3 build-reel-audio.py   (depuis jean-immobilier-reel/)"""
import json, subprocess
TOTAL = 34.93
VOICE = "assets/audio/voix-montage.wav"          # ancien montage 49,80 s
# (début, fin) dans l'ancien montage, gardés bout à bout ; chaque coupe tombe dans un silence de la voix
KEEP = [(0.00, 4.46), (12.89, 16.91), (19.96, 34.67), (37.26, 44.70)]
END_OLD = 44.70                                   # début de l'ancienne carte de fin
def remap(t):
    acc = 0.0
    for a, b in KEEP:
        if a <= t < b:
            return acc + t - a
        acc += b - a
    if t >= END_OLD:
        return acc + t - END_OLD
    return None                                   # bruitage d'une séquence coupée
# 1. voix
parts, labels = [], []
for i, (a, b) in enumerate(KEEP):
    parts.append(f"[0]atrim={a}:{b},asetpts=PTS-STARTPTS,afade=t=in:d=0.005,afade=t=out:st={b - a - 0.005:.3f}:d=0.005[v{i}]")
    labels.append(f"[v{i}]")
graph = ";".join(parts) + ";" + "".join(labels) + f"concat=n={len(KEEP)}:v=0:a=1,apad=whole_dur={TOTAL}[out]"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", VOICE, "-filter_complex", graph, "-map", "[out]", "-ar", "44100", "-ac", "1",
                "assets/audio/voix-reel35.wav"], check=True)
# 2. bruitages recalés (ceux des séquences coupées disparaissent ; la fin est raccourcie à 4,30 s)
old = json.load(open("../jean-immobilier/assets/audio/sfx-events.json"))
new = []
for name, t, vol in old:
    nt = remap(t)
    if nt is not None and nt < TOTAL - 0.3:
        new.append([name, round(nt, 3), vol])
json.dump(new, open("assets/audio/sfx-events-reel35.json", "w"), indent=1)
# 3. mix : voix + bruitages + musique baissée sous la voix
SFX = "../.claude/skills/media-use/audio/assets/sfx/"
args = ["ffmpeg", "-v", "error", "-y", "-i", "assets/audio/voix-reel35.wav", "-i", "assets/music/jean-immobilier-music.wav"]
g = ["[0]aformat=sample_rates=44100:channel_layouts=stereo,asplit=2[v][key]",
     "[1]aformat=sample_rates=44100:channel_layouts=stereo,volume=0.42[m]",
     "[m][key]sidechaincompress=threshold=0.03:ratio=6:attack=15:release=320:makeup=1[md]"]
lab = ["[v]", "[md]"]
for k, (name, t, vol) in enumerate(new):
    args += ["-i", SFX + name + ".mp3"]
    d = int(t * 1000)
    g.append(f"[{k + 2}]aformat=sample_rates=44100:channel_layouts=stereo,volume={vol},adelay={d}|{d}[e{k}]")
    lab.append(f"[e{k}]")
g.append("".join(lab) + f"amix=inputs={len(lab)}:normalize=0:duration=first,loudnorm=I=-16:TP=-1.5:LRA=11,atrim=0:{TOTAL}[out]")
subprocess.run(args + ["-filter_complex", ";".join(g), "-map", "[out]", "-ar", "48000", "assets/audio/mix-reel35.wav"], check=True)
print(f"voix + {len(new)} bruitages + musique -> assets/audio/mix-reel35.wav ({TOTAL} s)")
