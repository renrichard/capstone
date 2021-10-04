from glob import glob
from os.path import join

from librosa.core import load

from preprocess.json.create_vcc_2020_json import get_num_to_transcription, get_duration
from preprocess.json.vcc_2020_constants import vcc_2020_target_sr, speakers
from preprocess.json.vcc_2020_paths import synth_dir

import numpy as np

def find_speaker_rate(speaker):
	num_to_transcription = get_num_to_transcription()

	synth_speaker_path = join(synth_dir, speaker)
	synth_speaker_filepaths = sorted(glob(synth_speaker_path + '/*.wav'))
	synth_speaker_filenums = [f.rsplit('/', 1)[1].split('.')[0][1:] for f in synth_speaker_filepaths]
	synth_speaker_transcriptions = [num_to_transcription[n] for n in synth_speaker_filenums]

	synth_speaker_filenums_to_transcriptions = dict(zip(synth_speaker_filepaths, synth_speaker_transcriptions))

	word_rates = []
	char_rates = []

	for fpath, t in synth_speaker_filenums_to_transcriptions.items():

		num_words = len(t.split())
		num_chars = len(t) - t.count(' ') - t.count('.')
		target_data, _ = load(fpath, vcc_2020_target_sr)
		duration = get_duration(target_data, vcc_2020_target_sr)

		word_rates.append(num_words / duration)
		char_rates.append(num_chars / duration)

	word_rates = np.array(word_rates)
	char_rates = np.array(char_rates)

	print('id:', speaker)
	print('word/s mean: %.2f' % word_rates.mean())
	print('word/s stdev: %.2f' % word_rates.std())
	print('char/s mean: %.2f' % char_rates.mean())
	print('char/s stdev: %.2f' % np.std(char_rates))
	print()



if __name__ == "__main__":
	for speaker in speakers:
		find_speaker_rate(speaker)
