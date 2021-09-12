This package will create the json files that will be used to train the models. Currently,
it creates the json files for the VCC2020 dataset.

It contains the following files:

Scripts:

create_vcc_2020_json: This script is responsible for creating the json files and resampling the dataset.
Here is the order of operation:
1. Create a resample file path (`target_speaker/resample/E10051.wav`)
2. Resample the original audio file (`target_speaker/E10051.wav`) and save to above file path
3. Calculate the duration of the audio file.
4. Get the transcription corresponding to audio file.
5. Write the resample path, duration, and transcription to the json.
6. All the jsons are saved in a folder `~/data/VCC2020-database/extract/target_task1/json`

Example from hi_fi_tts_v0 used in tts_finetune:

`{"audio_filepath": "audio/6670_other/8322/                                    internationalshortstories1_02_patten_0006.flac", "text": "this name           was given it", "duration": 1.18, "text_no_preprocessing": "This name          was given it,", "text_normalized": "This name was given it,"}`

Example created from script:

`{"audio_filepath": "/Users/richardren/data/VCC2020-database/extract/           target_task1/TEF1/resample/E10051.wav", "duration": 3.298639455782313,         "text": "Moroccan agriculture enjoys special treatment when exporting to Europe."},`

**NOTE**: To run the script, I assume you:
 1. Download the dataset to a directory called `~/data` that is under your home directory.
 2. Unzip all files like target_task1 or vcc2020_database_transcriptions zips to a folder called `~/data/VCC2020-database/extract`


Resource files:

vcc_2020_constants: This file contains numerical constants to help with preprocessing the wav files.

vcc_2020_paths: This file contains the relevant file and directory paths to create the json files.
E.g. the path where the dataset resides.
