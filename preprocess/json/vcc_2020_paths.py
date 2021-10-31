from os.path import expanduser

home = expanduser('~')

data_path = home + '/data/VCC2020-database'

extract_path = home + '/data/VCC2020-database/extract'

transcription_path = home + '/data/VCC2020-database/extract/vcc2020_database_transcriptions'

train_transcription_path = home + '/data/VCC2020-database/extract/vcc2020_database_transcriptions/transcriptions_training'
train_transcription_filename = home + '/data/VCC2020-database/extract/vcc2020_database_transcriptions/transcriptions_training/vcc2020_database_training_Eng_transcriptions.txt'

eval_transcription_path = home + '/data/VCC2020-database/extract/vcc2020_database_transcriptions/transcriptions_evaluation'
eval_transcription_filename = eval_transcription_path + '/vcc2020_database_evaluation_transcriptions.txt'


task_path = home + '/data/VCC2020-database/extract/target_task1'
task_json_dir = task_path + 'json'

groundtruth_path = home + '/data/VCC2020-database/extract/vcc2020_database_groundtruth'
groundtruth_json_dir = groundtruth_path + '/json'


synth_dir = task_path
