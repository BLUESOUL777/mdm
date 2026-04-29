import numpy as np
import matplotlib.pyplot as plt

Ac = float(input("Enter carrier amplitude (Ac): "))
Fc = float(input("Enter carrier frequency (Fc in Hz): "))
fs = float(input("Enter sampling frequency (fs in Hz): "))
bit_dur = float(input("Enter bit duration (in seconds): "))
bits_input = input("Enter bit sequence (e.g. 1 0 1 1): ")

bits = [int(b) for b in bits_input.split()]

t = np.linspace(0, len(bits) * bit_dur, int(fs * len(bits) * bit_dur), endpoint=False)

message = np.repeat(bits, int(fs * bit_dur))

PSK_signal = []
for b in bits:
    tb = np.linspace(0, bit_dur, int(fs * bit_dur), endpoint=False)
    if b == 1:
        PSK_signal.extend(Ac * np.sin(2 * np.pi * Fc * tb))
    else:
        PSK_signal.extend(Ac * np.sin(2 * np.pi * Fc * tb + np.pi))

PSK_signal = np.array(PSK_signal)

plt.figure()

plt.subplot(2,1,1)
plt.step(t, message, where='post')
plt.title("Message Signal")

plt.subplot(2,1,2)
plt.plot(t, PSK_signal)
plt.title("PSK Signal")

plt.tight_layout()
plt.show()