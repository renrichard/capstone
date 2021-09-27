from glob import glob
from json import dumps
from os.path import join
from re import sub

from librosa.core import load

from preprocess.json.create_vcc_2020_json import get_num_to_transcription, get_duration
from preprocess.json.vcc_2020_constants import vcc_2020_target_sr, speakers
from preprocess.json.vcc_2020_paths import synth_dir


def find_speaker_rate(speaker):
	num_to_transcription = get_num_to_transcription()

	synth_speaker_path = join(synth_dir, speaker)
	synth_speaker_filepaths = sorted(glob(synth_speaker_path + '/*.wav'))
	synth_speaker_filenums = [f.rsplit('/', 1)[1].split('.')[0][1:] for f in synth_speaker_filepaths]
	synth_speaker_transcriptions = [num_to_transcription[n] for n in synth_speaker_filenums]

	synth_speaker_filenums_to_transcriptions = dict(zip(synth_speaker_filepaths, synth_speaker_transcriptions))

	metadata = []

	for fpath, t in synth_speaker_filenums_to_transcriptions.items():

		file_metadata = dict()

		num_words = len(t.split())
		num_chars = len(t) - t.count(' ') - t.count('.')
		target_data, _ = load(fpath, vcc_2020_target_sr)
		duration = get_duration(target_data, vcc_2020_target_sr)

		file_metadata['fpath'] = fpath
		file_metadata['num_words'] = num_words
		file_metadata['num_chars'] = num_chars
		file_metadata['duration'] = duration
		file_metadata['word_rate'] = num_words / duration
		file_metadata['char_rate'] = num_chars / duration

		metadata.append(file_metadata)

	fp = join(synth_speaker_path, '{}_duration.json'.format(speaker))
	with open(fp, 'w') as f:
		contents = dumps(metadata).strip('[]')
		contents = sub('}, {', '}\n{', contents)
		f.write(contents)

if __name__ == "__main__":
	find_speaker_rate(speakers[0])
