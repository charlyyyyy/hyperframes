#!/usr/bin/env python3
"""Musique originale du Reel Jean Immobilier (composée par synthèse, donc libre de droits).

Calée sur le montage de 34,93 s :
- 0 à 15,04 s : tension (la mineur, pulsation, charleston, montée) ; 28 temps exactement, le 28e tombe sur « attendu ».
- 15,04 s : arrêt net (l'impact grave est un bruitage du mix).
- 15,04 à 16,72 s : silence, queue de réverbération seulement (le pivot).
- 16,72 s : départ (do majeur, kick, claps, arpèges), le premier temps tombe quand la lumière s'ouvre.
- 32,4 à 34,93 s : fondu de fin sur la carte.
Usage : python3 compose-music.py assets/music/jean-immobilier-music.wav
"""
import sys, wave
import numpy as np

SR = 44100
TOTAL = 34.93
IMPACT = 15.04           # « attendu »
DROP = 16.72             # la lumière s'ouvre
BEAT = IMPACT / 28.0     # 0,5371 s, environ 111,7 BPM
rng = np.random.default_rng(7)
out = np.zeros((int(TOTAL * SR) + SR, 2))


def note_hz(n):          # n en demi-tons depuis la4 (440)
    return 440.0 * 2 ** (n / 12.0)


def lowpass(x, cutoff):
    a = np.exp(-2 * np.pi * cutoff / SR)
    y = np.empty_like(x)
    acc = 0.0
    for i in range(len(x)):
        acc = (1 - a) * x[i] + a * acc
        y[i] = acc
    return y


def lp_fast(x, cutoff, passes=2):
    # one-pole lowpass via FFT (cheap, zero-phase-ish): gaussian roll-off in frequency
    n = len(x)
    f = np.fft.rfftfreq(n, 1 / SR)
    X = np.fft.rfft(x)
    X *= 1 / (1 + (f / cutoff) ** (2 * passes))
    return np.fft.irfft(X, n)


def add(sig, t, pan=0.0, gain=1.0):
    i = int(t * SR)
    if i >= len(out):
        return
    sig = sig[: len(out) - i]
    l, r = np.cos((pan + 1) * np.pi / 4), np.sin((pan + 1) * np.pi / 4)
    out[i:i + len(sig), 0] += sig * gain * l * 1.414
    out[i:i + len(sig), 1] += sig * gain * r * 1.414


def env(n, a, d, s, r, sustain_len):
    total = int((sustain_len + r) * SR)
    e = np.zeros(total)
    ai, di = int(a * SR), int(d * SR)
    si = max(int(sustain_len * SR), ai + di)
    e[:ai] = np.linspace(0, 1, ai, endpoint=False)
    e[ai:ai + di] = np.linspace(1, s, di, endpoint=False)
    e[ai + di:si] = s
    e[si:] = np.linspace(s, 0, total - si) if total > si else []
    return e[:total]


def saw(freq, dur, detune=0.0):
    t = np.arange(int(dur * SR)) / SR
    f = freq * (1 + detune)
    return 2 * ((t * f) % 1.0) - 1


def kick(gain=1.0):
    n = int(0.35 * SR)
    t = np.arange(n) / SR
    f = 50 + 110 * np.exp(-t * 30)
    ph = 2 * np.pi * np.cumsum(f) / SR
    return np.sin(ph) * np.exp(-t * 9) * gain


def hat(dur=0.05, gain=1.0, cutoff=7000):
    n = int(dur * SR)
    x = rng.standard_normal(n)
    x = x - lp_fast(x, cutoff, 1)
    return x * np.exp(-np.arange(n) / SR * (60 / dur * 0.05)) * gain


def clap(gain=1.0):
    n = int(0.25 * SR)
    x = rng.standard_normal(n)
    x = lp_fast(x, 2500, 1) - lp_fast(x, 900, 1)
    t = np.arange(n) / SR
    e = np.exp(-t * 22)
    for k in (0.0, 0.012, 0.024):
        e += np.exp(-np.clip(t - k, 0, None) * 120) * (t >= k) * 0.6
    return x * e * gain


def pad(notes, dur, cutoff, gain):
    sig = np.zeros(int(dur * SR))
    for n in notes:
        for det in (-0.004, 0.0, 0.0045):
            sig += saw(note_hz(n), dur, det)
    sig = lp_fast(sig, cutoff, 2) / (len(notes) * 3)
    e = env(len(sig), min(0.6, dur / 3), 0.2, 0.85, 0.0, dur)[: len(sig)]
    fade = np.ones(len(sig))
    k = int(0.25 * SR)
    fade[-k:] = np.linspace(1, 0, k)
    return sig * e * fade * gain


def pluck(n, dur=0.3, cutoff=3000, gain=1.0):
    s = saw(note_hz(n), dur) * 0.6 + np.sign(np.sin(2 * np.pi * note_hz(n) * np.arange(int(dur * SR)) / SR)) * 0.4
    s = lp_fast(s, cutoff, 1)
    return s * np.exp(-np.arange(len(s)) / SR * 9) * gain


def bass(n, dur, cutoff=400, gain=1.0):
    t = np.arange(int(dur * SR)) / SR
    s = np.sin(2 * np.pi * note_hz(n) * t) * 0.8 + saw(note_hz(n), dur) * 0.3
    s = lp_fast(s, cutoff, 2)
    e = np.minimum(1, t / 0.01) * np.exp(-t * 2.5)
    k = int(0.02 * SR)
    e[-k:] *= np.linspace(1, 0, k)
    return s * e * gain


# ---------------- tension : la mineur, Am F Dm E, 7 mesures de 4 temps = 28 temps ----------------
A2, F2, D2, E2 = -24, -28, -31, -29          # basses (la2 = -24 depuis la4)
prog_t = [(A2, [0, 3, 7]), (F2, [-4, 0, 3]), (D2, [-7, -4, 0]), (E2, [-5, -1, 2])]
for bar in range(7):
    t0 = bar * 4 * BEAT
    root, chord = prog_t[bar % 4]
    lift = bar / 7.0                                     # la tension monte
    add(pad([c - 12 for c in chord], 4 * BEAT, 900 + 1800 * lift, 0.22), t0, 0.0)
    for b in range(4):                                   # pulsation de basse en croches
        for h in (0, 0.5):
            add(bass(root, BEAT * 0.45, 300 + 300 * lift, 0.55), t0 + (b + h) * BEAT)
    for b in range(4):
        if bar >= 1 or b >= 2:
            add(kick(0.75 if b % 2 == 0 else 0.45 + 0.3 * lift), t0 + b * BEAT)
        for s16 in range(4):                             # charleston en doubles croches
            g = (0.10 if s16 % 2 == 0 else 0.06) * (0.6 + 0.6 * lift)
            add(hat(0.04, g, 8000), t0 + (b + s16 / 4) * BEAT, 0.3 if s16 % 2 else -0.3)
    if bar >= 3:                                         # motif de pluck sombre
        for i, n in enumerate([0, 3, 7, 3, 0, 3, 7, 10]):
            add(pluck(chord[0] + n % 12 - 12 + (12 if n >= 10 else 0), 0.25, 1500 + 1500 * lift, 0.12),
                t0 + i * BEAT / 2, 0.4 if i % 2 else -0.4)
# montée de bruit filtré sur les 2 dernières mesures, coupée net sur l'impact
rise_len = 8 * BEAT
n = int(rise_len * SR)
noise = rng.standard_normal(n)
rise = (noise - lp_fast(noise, 600, 1)) * np.linspace(0, 1, n) ** 2 * 0.18
add(rise, IMPACT - rise_len, 0.0)
# coupe nette à l'impact : tout ce qui dépasse est stoppé (queue courte)
cut = int(IMPACT * SR)
tail = int(0.12 * SR)
out[cut:cut + tail] *= np.linspace(1, 0, tail)[:, None]
out[cut + tail:int(DROP * SR)] = 0.0

# ---------------- élan : do majeur, C G Am F, à partir de DROP ----------------
C3, G2, A2b, F2b = -21, -26, -24, -28
prog_e = [(C3, [3, 7, 10]), (G2, [-2, 2, 5]), (A2b, [0, 3, 7]), (F2b, [-4, 0, 3])]
arp = [0, 7, 12, 16, 12, 7, 0, 12]
bars_e = int((TOTAL - DROP) / (4 * BEAT)) + 1
for bar in range(bars_e):
    t0 = DROP + bar * 4 * BEAT
    root, chord = prog_e[bar % 4]
    add(pad(chord, 4 * BEAT, 2600, 0.20), t0, 0.0)
    add(pad([c + 12 for c in chord], 4 * BEAT, 4000, 0.07), t0, 0.2)
    for b in range(4):
        add(kick(0.85), t0 + b * BEAT)
        add(hat(0.09, 0.08, 6000), t0 + (b + 0.5) * BEAT, 0.25)          # charleston ouvert sur le contretemps
        if b in (1, 3):
            add(clap(0.32), t0 + b * BEAT, -0.1)
        for h in (0, 0.5):
            add(bass(root + 12 * 0, BEAT * 0.42, 500, 0.6), t0 + (b + h) * BEAT)
    for i, a in enumerate(arp):
        add(pluck(chord[0] + a, 0.28, 3600, 0.13), t0 + i * BEAT / 2, 0.45 if i % 2 else -0.45)
# un « crash » doux sur le départ
crash = hat(1.6, 0.25, 5000) * np.exp(-np.arange(int(1.6 * SR)) / SR * 2.0)
add(crash, DROP, 0.0)

# ---------------- réverbération (convolution FFT), fondu final, normalisation ----------------
ir_len = int(1.8 * SR)
ir = rng.standard_normal(ir_len) * np.exp(-np.arange(ir_len) / SR * 3.2)
ir = lp_fast(ir, 5000, 1)
ir /= np.sqrt(np.sum(ir ** 2))
wet = np.zeros_like(out)
nfft = 1 << int(np.ceil(np.log2(len(out) + ir_len)))
IR = np.fft.rfft(ir, nfft)
for ch in range(2):
    wet[:, ch] = np.fft.irfft(np.fft.rfft(out[:, ch], nfft) * IR, nfft)[: len(out)]
mix = out + 0.22 * wet
mix = mix[: int(TOTAL * SR)]
fade_start, fade_end = 32.4, TOTAL
a, b = int(fade_start * SR), len(mix)
mix[a:b] *= np.linspace(1, 0, b - a)[:, None] ** 1.5
mix /= np.max(np.abs(mix)) + 1e-9
mix *= 0.89
pcm = (mix * 32767).astype(np.int16)
with wave.open(sys.argv[1], "wb") as w:
    w.setnchannels(2)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes(pcm.tobytes())
print(f"{sys.argv[1]} : {len(mix) / SR:.2f} s, tempo {60 / BEAT:.1f} BPM, impact {IMPACT}, départ {DROP}")
