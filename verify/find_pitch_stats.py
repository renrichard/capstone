from glob import glob
from os.path import join

import numpy as np
from librosa import yin, note_to_hz
from librosa.core import load

from preprocess.json.vcc_2020_constants import vcc_2020_target_sr
from preprocess.json.vcc_2020_paths import synth_dir


def find_pitch_stats(speaker):
	synth_speaker_path = join(synth_dir, speaker)
	synth_speaker_filepaths = sorted(glob(synth_speaker_path + '/*.wav'))

	means = []
	stdevs = []
	fmins = []
	fmaxs = []

	fmin = note_to_hz('C2') # recommended by librosa
	fmax = note_to_hz('C7') # recommended by librosa

	fmin = 30 # in colab notebook
	fmax = 512 # in colab notebook


	for fpath in synth_speaker_filepaths:
		target_data, _ = load(fpath, vcc_2020_target_sr)
		f0 = yin(target_data, fmin, fmax, sr=vcc_2020_target_sr)
		means.append(f0.mean())
		stdevs.append(f0.std())
		fmins.append(f0.min())
		fmaxs.append(f0.max())

	means = np.array(means)
	stdevs = np.array(stdevs)
	fmins = np.array(fmins)
	fmaxs = np.array(fmaxs)


	print('id:', speaker)
	print('pitch mean: %.2f' % means.mean())
	print('pitch stdev: %.2f' % stdevs.mean())
	print('fmins mean: %.2f' % fmins.mean())
	print('fmaxs mean: %.2f' % fmaxs.mean())
	print()



if __name__ == "__main__":
	find_pitch_stats('TEM1')
