import numpy as np
import matplotlib.pyplot as plt

Ac = float(input("Enter carrier amplitude (Ac): "))
Fc = float(input("Enter carrier frequency (Fc in Hz): "))
fs = float(input("Enter sampling frequency (fs in Hz): "))
bit_dur = float(input("Enter bit duration (in seconds): "))
bits_input = input("Enter bit sequence (e.g. 1 0 1 1 0): ")

bits = [int(b) for b in bits_input.split()]

t = np.linspace(0, len(bits) * bit_dur, int(fs * len(bits) * bit_dur), endpoint=False)

message = np.repeat(bits, int(fs * bit_dur))

carrier = Ac * np.sin(2 * np.pi * Fc * t)

ASK_signal = message * carrier

plt.figure()

plt.subplot(3,1,1)
plt.step(t, message, where='post')
plt.title("Message Signal")

plt.subplot(3,1,2)
plt.plot(t, carrier)
plt.title("Carrier Signal")

plt.subplot(3,1,3)
plt.plot(t, ASK_signal)
plt.title("ASK Signal")

plt.tight_layout()
plt.show()