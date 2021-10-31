import librosa
import librosa.display

import numpy as np
import matplotlib.pyplot as plt

from preprocess.json.vcc_2020_constants import vcc_2020_orig_sr, vcc_2020_target_sr


def visualize_waves(filenames, sample_rates, alphas, labels, title):
	for i in range(len(filenames)):
		data, _ = librosa.load(filenames[i], sample_rates[i])
		plt.plot(data, alpha=alphas[i], label=labels[i])

	plt.title(title)
	plt.legend()
	plt.show()

def visualize_mel(filename, title):
	y, _ = librosa.load(filename, vcc_2020_target_sr)
	S = librosa.feature.melspectrogram(y=y, sr=vcc_2020_target_sr, n_mels=128)
	S_dB = librosa.power_to_db(S, ref=np.max)
	fig, ax = plt.subplots()
	img = librosa.display.specshow(S_dB, x_axis='time',
	                               y_axis='mel', sr=vcc_2020_target_sr, ax=ax)
	fig.colorbar(img, ax=ax, format='%+2.0f dB')
	ax.set(title=title)
	plt.show()




if __name__ == '__main__':
	# visualize_waves(['/Users/richardren/data/VCC2020-database/extract/target_task1/TEF1/E20021.wav',
	#                  '/Users/richardren/data/VCC2020-database/extract/target_task1/TEF1/resample/E20021.wav'],
	#                 [vcc_2020_orig_sr, vcc_2020_target_sr],
	#                 [0.5,0.5],
	#                 ['Original', 'Resampled'],
	#                 'Comparison of Original and Resampled Audio')
	#
	# visualize_waves(['/Users/richardren/Downloads/FP_TEF2_1k.wav', '/Users/richardren/Downloads/FP_TEM1_1k.wav'],
	#                 [vcc_2020_target_sr, vcc_2020_target_sr],
	#                 [0.5,0.5],
	#                 ['Female', 'Male'],
	#                 'Noise comparison of Generated Female vs Male Speakers')
	visualize_mel('/Users/richardren/Downloads/FP_TEF2_1k.wav', 'Female Melspectrogram')
	visualize_mel('/Users/richardren/Downloads/FP_TEM1_1k.wav', 'Male Melspectrogram')
