import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fft import fft, fftfreq
from scipy.signal import find_peaks, butter, lfilter

fs, data = wavfile.read('corrupted.wav')
N = data.shape[0]
print(fs, N)
duration = N/fs
t = np.linspace(0, duration, N)
plt.plot(t, data)
# plt.xlim(1.0, 1.005)
plt.show()

y = fft(data)
freqs = fftfreq(N, 1/fs)
amplitudes = abs(y)[:N//2]
frequencies = freqs[:N//2]
plt.plot(frequencies, amplitudes)
plt.show()
# for i in range(1,5):
#     plt.figure(i)
#     plt.plot(frequencies, amplitudes)
#     plt.xlim((i-1)*5000, i*5000)
#     plt.show()
peaks_arr = find_peaks(amplitudes, height=1e8)
peak_indices = peaks_arr[0]
peak_frequencies = peak_indices*fs/N
# heights = peaks_arr[1]['peak_heights']
print(peak_frequencies)
fc = peak_frequencies[2]
print(fc)
carrier = 2*np.pi*fc*t
demodulated = data*np.cos(carrier)
plt.plot(t, demodulated)
stage_2 = fft(demodulated)
plt.plot(freqs[:N//2], abs(stage_2[:N//2]))
plt.show()

#butterworth low pass filter
fc = 4000
fnyq = fs/2
normal_cutoff = fc/fnyq
order = 5
b, a = butter(order, normal_cutoff, btype="low", analog=False)
low_pass_filtered = lfilter(b,a,demodulated)
plt.plot(t, low_pass_filtered)
plt.show()
stage_3 = fft(low_pass_filtered)
plt.plot(freqs[:N//2], abs(stage_3[:N//2]))
plt.show()

peaks = find_peaks(abs(stage_3[:N//2]), height=0.25e8)
peak_indices = peaks[0]
peak_frequencies = peak_indices*fs/N
print(peak_frequencies)
# stage_3[0:10] = 0
stage_3[0:500] = 0
for p in peak_indices:
    stage_3[int(p-10):int(p+10)] = 0
    stage_3[N-int(p+10):N-int(p-10)] = 0
plt.plot(freqs[:N//2], abs(stage_3)[:N//2])
plt.show()

peaks = peaks = find_peaks(abs(stage_3[:N//2]), height=7e6)
peak_indices = peaks[0]
peak_frequencies = peak_indices*fs/N
print(peak_frequencies)
# stage_3[0:10] = 0
# stage_3[0:50] = 0
for p in peak_indices:
    stage_3[int(p-10):int(p+10)] = 0
    stage_3[N-int(p+10):N-int(p-10)] = 0
plt.plot(freqs[:N//2], abs(stage_3)[:N//2])
plt.show()

stage_4 = np.fft.ifft(stage_3)
plt.plot(t, stage_4)
plt.show()

peak = max(np.abs(stage_4))
if (peak>0):
    recovered = stage_4/peak
else:
    recovered = stage_4
plt.plot(t, recovered)
plt.show()
wavfile.write('recovered.wav', int(fs), stage_4.astype(np.float32))
# # plt.xlim(5000,10000)
# plt.show()
# peaks_2 = find_peaks(abs(y_filtered[:N//2]), height=0.75e7)
# peak_indices = peaks_2[0]
# filtered_2 = y_filtered.copy()
# for p in peak_indices:
#     filtered_2[int(p-10):int(p+10)] = 0
#     filtered_2[N-int(p+10):N-int(p-10)] = 0
    # plt.plot(freqs[:N//2], abs(filtered_2))
# plt.plot(freqs[:N//2], abs(filtered_2[:N//2]))
# plt.show()
# clean_signal_f = np.fft.ifft(y_filtered).real
# plt.plot(t, clean_signal_f)
# plt.show()
# # plt.xlim(0, 1000)
# wavfile.write('recovered.wav', int(fs), recovered.astype(np.float32))