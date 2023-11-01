---
title: UWB reflected wave simulation experiment by VNA
tags:
  - research-about
  - VNA
  - UWB
---
# Experiment Equipment


# UWB Signal Decomposition and Reconstruction by Different Frequencies

Considering our experiment equipment E5063A ENA Series Network analyzer has 100KHz - 6.5GHz signal range, we design a code experiment to divide a gauss-pulse UWB signal, whose center frequency is about 3.25GHz and bandwidth is about 6.5GHz.

 First, generate the UWB gauss-pulse signal, here we using `scipy.signal.gausspulse`, it generates the gauss pulse signal modulated by sinusoidal function. The formula:
 
 $$
 x(t) = e^{j 2\pi f t} e^{-\frac{1}{2 \sigma^2} \cdot t^2}
 $$

 
```python
# Generate UWB signal parameters
sampling_rate = 10e13 # Sampling rate in Hz
duration = 1e-8 # Duration of the signal in seconds
amplitude = 1.0  # Amplitude of the UWB signal
start_frequency = 100e3
end_frequency = 6.5e9
center_frequency = (start_frequency + end_frequency) / 2  # Center frequency of the UWB signal
bandwidth =  (end_frequency - start_frequency) / center_frequency # Bandwidth of the UWB signal

# Generate time vector
t = np.linspace(-duration/2, duration/2, int(sampling_rate * duration))

# Generate UWB signal
uwb_signal = signal.gausspulse(t, fc=center_frequency, bw=bandwidth)
```

Then, we apply FFT (Fast Fourier Transform) method to analyze this UWB signal spectrum, the code is like:

```python
# Perform Fourier transform on the UWB signal
spectrum = np.fft.fft(uwb_signal)
frequencies = np.fft.fftfreq(len(uwb_signal), d=1/sampling_rate)
# spectrum = np.fft.fftshift(spectrum)
# frequencies = np.fft.fftshift(frequencies)


# Get amplitude and phase from the spectrum
amplitude_spectrum = np.abs(spectrum)
phase_spectrum = np.angle(spectrum)

# Reconstruct UWB signal from amplitude and phase spectra
reconstructed_signal = np.fft.ifft(amplitude_spectrum * np.exp(1j * phase_spectrum))

```


Plot this data,

```python
sorted_indices = np.argsort(frequencies)

frequencies_sorted = frequencies[sorted_indices]
amplitude_spectrum_sorted = amplitude_spectrum[sorted_indices]
phase_spectrum_sorted = phase_spectrum[sorted_indices]

# Plotting the results
plt.figure(figsize=(10, 6))

# Plot time-domain UWB signal
plt.subplot(2, 2, 1)
plt.plot(t, uwb_signal)
plt.title('UWB Signal (Time Domain)')
plt.xlabel('Time')
plt.ylabel('Amplitude')

# Plot frequency spectrum
plt.subplot(2, 2, 2)
plt.plot(frequencies_sorted[10:-10], amplitude_spectrum_sorted[10:-10])
plt.title('Frequency Spectrum')
plt.xlabel('Frequency')
plt.ylabel('Amplitude')

# Plot phase spectrum
plt.subplot(2, 2, 3)
plt.plot(frequencies_sorted[10:-10], phase_spectrum_sorted[10:-10])
plt.title('Phase Spectrum')
plt.xlabel('Frequency')
plt.ylabel('Phase')

# Plot reconstructed UWB signal
plt.subplot(2, 2, 4)
plt.plot(t, reconstructed_signal)
plt.title('Reconstructed UWB Signal (Time Domain)')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
```


Here's result:

![](research_career/attachments/Figure_1%204.png)


Cause we only have 100KHz - 6.5GHz signal range, we want to focus on this range's data:

```python
mask = abs(frequencies) < 10e9
frequencies_mask = frequencies[mask]
amplitude_spectrum_mask = amplitude_spectrum[mask]
phase_spectrum_mask = phase_spectrum[mask]

reconstructed_signal = np.fft.ifft(amplitude_spectrum_mask * np.exp(1j * phase_spectrum_mask))

sorted_indices = np.argsort(frequencies_mask)
frequencies_sorted = frequencies_mask[sorted_indices]
amplitude_spectrum_sorted = amplitude_spectrum_mask[sorted_indices]
phase_spectrum_sorted = phase_spectrum_mask[sorted_indices]

plt.figure(figsize=(10, 6))

# Plot time-domain UWB signal
plt.subplot(2, 2, 1)
plt.plot(t, uwb_signal)
plt.title('UWB Signal (Time Domain)')
plt.xlabel('Time')
plt.ylabel('Amplitude')

# Plot frequency spectrum
plt.subplot(2, 2, 2)
plt.plot(frequencies_sorted, amplitude_spectrum_sorted)
plt.axvline(x=3.25e9, color='r', linestyle='--')
plt.axvline(x=6.5e9, color='r', linestyle='--')
plt.title('Frequency Spectrum')
plt.xlabel('Frequency')
plt.ylabel('Amplitude')

# Plot phase spectrum
plt.subplot(2, 2, 3)
plt.plot(frequencies_sorted, phase_spectrum_sorted)
plt.title('Phase Spectrum')
plt.xlabel('Frequency')
plt.ylabel('Phase')

# Plot reconstructed UWB signal
plt.subplot(2, 2, 4)
plt.plot(np.linspace(-duration/2, duration/2, len(reconstructed_signal)), reconstructed_signal)
plt.title('Reconstructed UWB Signal (Time Domain)')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()

```

The result:

![](research_career/attachments/Figure_2.png)

Here we can see that, in `scipy.signal.gausspulse` function, the signal's bandwidth controlled by fractional bandwidth parameter, which means,

$$
\text{fractional bandwidth} = \frac{\text{upper frequency of the signal} - \text{lower frequency of the signal}}{\text{center frequency}}
$$

Meanwhile, the bandwidth definition of gauss pulse means the energy has fallen to 50%

We can focus more on our signal range, like that:

![](research_career/attachments/Figure_3.png)

By this gauss pulse spectrum, we have chance to reconstruct UWB signal from the VNA frequency sweeping signal.
## Conclusion From this experiment

From this experiment, we can yield that we can use different frequencies signal to reconstruct gaussian pulse to generate UWB signal, the parameters will be based on the gauss pulse spectrum.

$$
\text{UWB Signal} = \sum_{i}^N \alpha_i \sin{(\omega_i t + \phi_i)}
$$

* $\alpha_i$ represents different frequencies signals' power intensity to reconstruct UWB signal
* $\omega_i$ represents different frequencies
* $\phi_i$ represents different frequencies' signals' phase



# Data Analysis


