# Original soundtrack for the Jean Immobilier review story.
# 120 BPM, D major, I-V-vi-IV. Synthesized from scratch (no samples), then the
# bundled Pixabay SFX are laid on the same grid as the GSAP timeline in index.html.
# Usage: python3 assets/music.py <project_dir> <out.wav> [music_gain, 0.62 = with music]
import subprocess
import sys
import wave

import numpy as np

SR = 48000
DUR = 33.0
BEAT = 0.5
N = int(SR * DUR)
rng = np.random.default_rng(42)
PROJECT = sys.argv[1]
OUT = sys.argv[2]
# music bed level; 0 = sound effects only (current cut)
MUSIC_GAIN = float(sys.argv[3]) if len(sys.argv) > 3 else 0.0

# ---- schedule (mirrors index.html) ----
E = [8.0, 14.0, 18.0, 25.0]
X = [13.95, 17.95, 24.95, 28.9]
O = 29.0
DROP = 4.0  # drums in, with the counter
FULL = 8.0  # claps in, with the first review
FINAL = 31.0  # final chord, on the website tap


def mtof(m):
    return 440.0 * 2 ** ((m - 69) / 12)


def t_(d):
    return np.arange(int(d * SR)) / SR


def place(buf, sig, t, gain=1.0):
    i = int(round(t * SR))
    if i >= buf.shape[-1]:
        return
    n = min(sig.shape[-1], buf.shape[-1] - i)
    buf[..., i : i + n] += sig[..., :n] * gain


def fft_filter(x, lo=None, hi=None, order=2):
    X_ = np.fft.rfft(x)
    f = np.fft.rfftfreq(len(x), 1 / SR)
    h = np.ones_like(f)
    if hi:
        h /= np.sqrt(1 + (f / hi) ** (2 * order))
    if lo:
        h /= np.sqrt(1 + (lo / np.maximum(f, 1e-3)) ** (2 * order))
    return np.fft.irfft(X_ * h, len(x))


def reverb(x, seconds=1.8, decay=0.55, seed=1):
    r = np.random.default_rng(seed)
    ir = r.standard_normal(int(seconds * SR)) * np.exp(-t_(seconds) / decay)
    ir = fft_filter(ir, lo=200, hi=6000)
    ir /= np.sqrt(np.sum(ir**2))
    L = len(x) + len(ir)
    y = np.fft.irfft(np.fft.rfft(x, L) * np.fft.rfft(ir, L), L)[: len(x)]
    return y


# ---- harmony ----
CH = {
    "D": ([62, 66, 69, 74], 38),
    "A": ([61, 64, 69, 73], 45),
    "Bm": ([62, 66, 71, 74], 47),
    "G": ([62, 67, 71, 74], 43),
}
PROG = ["D", "A", "Bm", "G"]
# (start, length, chord)
bars = [(b * 2.0, 2.0, PROG[b % 4]) for b in range(15)]
bars.append((30.0, 1.0, "A"))
bars.append((FINAL, 2.0, "D"))


def saw(f, d, detune_cents=0.0, phase=0.0):
    ff = f * 2 ** (detune_cents / 1200)
    ph = (phase + ff * t_(d)) % 1.0
    return 2 * ph - 1


# sidechain envelope (house pump) from the drop to the final hit
side = np.ones(N)
for k in np.arange(DROP, FINAL + 0.01, BEAT):
    i = int(k * SR)
    seg = t_(0.45)
    n = min(len(seg), N - i)
    side[i : i + n] = np.minimum(side[i : i + n], 1 - 0.55 * np.exp(-seg[:n] / 0.11))

padL = np.zeros(N)
padR = np.zeros(N)
bass = np.zeros(N)
arpL = np.zeros(N)
arpR = np.zeros(N)

for start, length, name in bars:
    notes, root = CH[name]
    d = length + 0.6
    tt = t_(d)
    env = np.minimum(1, tt / 0.25) * np.clip((d - tt) / 0.6, 0, 1)
    if start == FINAL:
        env = np.minimum(1, tt / 0.01) * np.exp(-tt / 1.4)
    for m in notes:
        f = mtof(m)
        place(padL, (saw(f, d, -7) + saw(f, d, 5, 0.3)) * env * 0.5, start)
        place(padR, (saw(f, d, 7, 0.6) + saw(f, d, -4, 0.1)) * env * 0.5, start)
    # bass: 8th notes from the drop, root note
    if start >= DROP - 0.01:
        fb = mtof(root)
        steps = int(length / 0.25) if start != FINAL else 1
        for k in range(steps):
            nd = 0.24 if start != FINAL else 1.8
            tb = t_(nd)
            tone = np.sin(2 * np.pi * fb * tb) + 0.35 * np.sin(4 * np.pi * fb * tb)
            tone = np.tanh(1.6 * tone) * np.minimum(1, tb / 0.004) * np.exp(-tb / (0.16 if start != FINAL else 0.9))
            place(bass, tone, start + k * 0.25, 0.9 if k % 2 else 0.6)
    # arpeggio: 8ths over chord tones, two octaves up
    pattern = [0, 1, 2, 3, 2, 1, 2, 3]
    if start != FINAL:
        for k in range(int(length / 0.25)):
            m = notes[pattern[k % 8]] + 12
            f = mtof(m)
            ta = t_(0.6)
            pl = (
                np.sin(2 * np.pi * f * ta)
                + 0.45 * np.sin(4 * np.pi * f * ta) * np.exp(-ta / 0.08)
                + 0.2 * np.sin(6 * np.pi * f * ta) * np.exp(-ta / 0.04)
            )
            pl *= np.minimum(1, ta / 0.003) * np.exp(-ta / 0.22)
            g = 0.55 if start < DROP else 0.8
            pan = 0.3 if k % 2 else -0.3
            place(arpL, pl * np.sqrt((1 - pan) / 2), start + k * 0.25, g)
            place(arpR, pl * np.sqrt((1 + pan) / 2), start + k * 0.25, g)
    else:
        for j, m in enumerate([74, 78, 81, 86]):
            f = mtof(m + 12)
            ta = t_(2.0)
            pl = np.sin(2 * np.pi * f * ta) * np.exp(-ta / 0.9) * np.minimum(1, ta / 0.003)
            place(arpL, pl, FINAL + j * 0.06, 0.5)
            place(arpR, pl, FINAL + j * 0.06, 0.5)

# intro: pad filter opens up into the drop
open_curve = np.clip(np.arange(N) / SR / DROP, 0, 1)
padL_lo = fft_filter(padL, hi=600)
padR_lo = fft_filter(padR, hi=600)
padL_hi = fft_filter(padL, hi=1800)
padR_hi = fft_filter(padR, hi=1800)
padL = padL_lo * (1 - open_curve) + padL_hi * open_curve
padR = padR_lo * (1 - open_curve) + padR_hi * open_curve

# delay on the arp (dotted 8th)
for buf in (arpL, arpR):
    dl = int(0.375 * SR)
    echo = np.zeros_like(buf)
    echo[dl:] = buf[:-dl] * 0.32
    echo[2 * dl :] += buf[: -2 * dl] * 0.12
    buf += fft_filter(echo, hi=3500)

# ---- drums ----
kick = np.zeros(N)
hats = np.zeros(N)
clap = np.zeros(N)


def kick_hit():
    tt = t_(0.45)
    f = 48 + 120 * np.exp(-tt / 0.035)
    ph = 2 * np.pi * np.cumsum(f) / SR
    body = np.sin(ph) * np.exp(-tt / 0.22)
    click = rng.standard_normal(len(tt)) * np.exp(-tt / 0.003) * 0.25
    return np.tanh(1.5 * (body + click))


def hat_hit(open_=False):
    d = 0.25 if open_ else 0.08
    tt = t_(d)
    n = fft_filter(rng.standard_normal(len(tt)), lo=7000, order=3)
    return n * np.exp(-tt / (0.07 if open_ else 0.022))


def clap_hit():
    tt = t_(0.35)
    n = fft_filter(rng.standard_normal(len(tt)), lo=900, hi=3500)
    env = np.zeros_like(tt)
    for o in (0.0, 0.011, 0.022):
        env += (tt >= o) * np.exp(-np.maximum(tt - o, 0) / (0.012 if o < 0.02 else 0.11))
    return n * env


for k in np.arange(DROP, 30.5, BEAT):
    place(kick, kick_hit(), k)
place(kick, kick_hit(), FINAL, 1.1)
for k in np.arange(DROP + 0.25, 30.5, BEAT):
    place(hats, hat_hit(open_=(round(k / BEAT) % 4 == 3)), k, 1.0)
for k in np.arange(DROP, 30.5, 0.125):
    if abs((k / 0.25) - round(k / 0.25)) > 0.1 and k >= FULL:
        place(hats, hat_hit(), k, 0.35)
for k in np.arange(FULL + 0.5, 30.5, 1.0):
    place(clap, clap_hit(), k)
# little snare fill into the final chord
for j, k in enumerate(np.arange(30.5, 31.0, 0.125)):
    place(clap, clap_hit(), k, 0.4 + 0.15 * j)

# risers: into the drop and into the final chord; crash on the final chord
def riser(d, f0=400, f1=6000):
    tt = t_(d)
    u = tt / d
    n = rng.standard_normal(len(tt))
    lo = fft_filter(n, hi=f0)
    hi_ = fft_filter(n, lo=f1 * 0.3)
    return (lo * (1 - u) + hi_ * u) * u**2


fx = np.zeros(N)
place(fx, riser(2.0), DROP - 2.0, 0.5)
place(fx, riser(1.0), FINAL - 1.0, 0.45)
tt = t_(2.2)
crash = fft_filter(rng.standard_normal(len(tt)), lo=4000) * np.exp(-tt / 0.6)
place(fx, crash, FINAL, 0.5)

# ---- mix ----
pad_wetL = reverb(padL + arpL * 0.6 + clap * 0.5, seed=2)
pad_wetR = reverb(padR + arpR * 0.6 + clap * 0.5, seed=3)
L = (padL * 0.12 + arpL * 0.16 + bass * 0.32) * side + kick * 0.5 + hats * 0.14 + clap * 0.16 + fx * 0.12 + pad_wetL * 0.07
R = (padR * 0.12 + arpR * 0.16 + bass * 0.32) * side + kick * 0.5 + hats * 0.14 + clap * 0.16 + fx * 0.12 + pad_wetR * 0.07
music = np.stack([L, R])
music = np.tanh(music * 1.4) / 1.4
music /= np.abs(music).max()
fade = np.clip((DUR - np.arange(N) / SR) / 0.8, 0, 1)
music *= fade


# ---- SFX on the same grid (bundled Pixabay library) ----
def load(name):
    raw = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", f"{PROJECT}/assets/sfx/{name}.mp3", "-f", "f32le", "-ac", "2", "-ar", str(SR), "-"],
        capture_output=True,
        check=True,
    ).stdout
    return np.frombuffer(raw, np.float32).reshape(-1, 2).T.astype(np.float64)


whoosh, click, pop, chime = (load(n) for n in ("whoosh-short", "click-soft", "pop", "chime"))
sfx = np.zeros((2, N))
place(sfx, whoosh, 3.05, 0.35)
place(sfx, pop, 4.5, 0.3)
for t in [7.6] + [x - 0.3 for x in X[:3]] + [X[3] - 0.5]:
    place(sfx, whoosh, t - 0.05, 0.32)
for e in E:
    place(sfx, click, e + 1.5, 0.55)
    place(sfx, pop, e + 1.55, 0.18)
place(sfx, click, O + 2.0, 0.55)
place(sfx, chime, O + 2.0, 0.4)

mix = music * MUSIC_GAIN + sfx
mix /= max(1.0, np.abs(mix).max() / 0.7)
pcm = (mix.T * 32767).astype(np.int16)
with wave.open(OUT, "wb") as w:
    w.setnchannels(2)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes(pcm.tobytes())
print("ok", OUT)
