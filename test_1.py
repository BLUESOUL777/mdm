import numpy as np
import matplotlib.pyplot as plt

Ac = float(input("Enter carrier amplitude (Ac): "))
f0 = float(input("Enter frequency for bit 0 (f0 in Hz): "))
f1 = float(input("Enter frequency for bit 1 (f1 in Hz): "))
fs = float(input("Enter sampling frequency (fs in Hz): "))
bit_dur = float(input("Enter bit duration (in seconds): "))
bits_input = input("Enter bit sequence (e.g. 1 0 1 0): ")

bits = [int(b) for b in bits_input.split()]

t = np.linspace(0, len(bits) * bit_dur, int(fs * len(bits) * bit_dur), endpoint=False)

message = np.repeat(bits, int(fs * bit_dur))

FSK_signal = []
for b in bits:
    tb = np.linspace(0, bit_dur, int(fs * bit_dur), endpoint=False)
    if b == 1:
        FSK_signal.extend(Ac * np.sin(2 * np.pi * f1 * tb))
    else:
        FSK_signal.extend(Ac * np.sin(2 * np.pi * f0 * tb))

FSK_signal = np.array(FSK_signal)

plt.figure()

plt.subplot(2,1,1)
plt.step(t, message, where='post')
plt.title("Message Signal")

plt.subplot(2,1,2)
plt.plot(t, FSK_signal)
plt.title("FSK Signal")

plt.tight_layout()
plt.show()