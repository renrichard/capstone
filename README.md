# Important Links

## Repos
- [Pytorch Lightning](https://github.com/jasonjjl1999/capstone-vits)
- [Porting to NeMo](https://github.com/martynwei/Capstone-NeMo)

## Trained VITS Checkpoints
- [LJSpeech](https://drive.google.com/file/d/1gy5SJ_lPMrorWdneMr8_O7NQP7mZ0CkT/view?usp=sharing)
- [TEF1](https://drive.google.com/file/d/1WrO5has-siqI-wnCv5JJzOcN-tYsqNA4/view?usp=sharing)
- [TEF2](https://drive.google.com/file/d/1ND7kIXYJIvxZ66Pez_aoShHo-3ReJ-AI/view?usp=sharing)
- [TEM1](https://drive.google.com/file/d/1cBJstoA86m8OxjewPCxcGTaJGg0-crYw/view?usp=sharing)
- [TEM2](https://drive.google.com/file/d/1SpL21JxQwSWyXjsopq75L07N3TbgfWdd/view?usp=sharing)

## Inference Samples on Test Data
- [VITS](https://drive.google.com/drive/folders/172Ozoj7z-_bBtZYOxTWrQeIe0pL9P79K?usp=sharing)
- [Fastpitch (Baseline)](https://drive.google.com/drive/u/0/folders/1RrnRzpbs3iLEFxgZMQPSF6eeASg_I5B4)
- [Ground Truth](https://drive.google.com/drive/folders/1oTwy7JVCVxNyD0wZIXrbjxobWPltf8Km?usp=sharing)

## Models
| Paper | GitHub Link |
| --- | --- |
| [NeMo](https://arxiv.org/abs/1909.09577) | https://github.com/NVIDIA/NeMo |
| [Variational Inference with adversarial learning (VITS)](https://arxiv.org/abs/2106.06103) | https://github.com/jaywalnut310/vits |
| [Generative Spoken Language Modeling (GSLM)](https://arxiv.org/abs/2102.01192?fbclid=IwAR0_tSl4Y3XkQJO33DkoXdS8xyaFK5DpPwzLst8aHbuy2bhnEThnINlNHes) | https://github.com/pytorch/fairseq/tree/main/examples/textless_nlp/gslm |
| [Flowtron](https://arxiv.org/abs/2005.05957) | https://github.com/NVIDIA/flowtron |
| [VCC2020 Baseline](https://arxiv.org/abs/2010.02434) | https://github.com/espnet/espnet/tree/master/egs/vcc20 |
| [VQ-VAE](https://arxiv.org/abs/1711.00937) | https://github.com/MishaLaskin/vqvae |
| [WaveGlow](https://arxiv.org/abs/1811.00002) | https://github.com/NVIDIA/waveglow |


## Background information

### General
- [Voice Conversion Problem Overview](https://arxiv.org/abs/2008.03648)
- [Alignment In NLP](https://cse.hkust.edu.hk/~dekai/library/WU_Dekai/Wu_Alignment2010.pdf)
- [Facebook NLP Blog](https://ai.facebook.com/blog/textless-nlp-generating-expressive-speech-from-raw-audio/)

### Latent Spaces
- [Simple Introduction to Variational Autoencoders (VAE)](https://towardsdatascience.com/understanding-variational-autoencoders-vaes-f70510919f73)
- [First VAE Paper](https://arxiv.org/pdf/1812.04342.pdf)
- [Interpretation of Speech Synthesis Latent Spaces](https://arxiv.org/abs/1903.11570)
- [Acoustic Unit Discovery with VQ-VAE](https://arxiv.org/abs/2005.09409)

### Normalizing Flow
- [WaveGlow Summary](https://pytorch.org/hub/nvidia_deeplearningexamples_waveglow/)
- [Variational Inference with Normalizing Flow](https://arxiv.org/abs/1505.05770)


## Datasets

- [VCC2020](https://github.com/nii-yamagishilab/VCC2020-database)
- [LJSpeech](https://keithito.com/LJ-Speech-Dataset/)
- [ZeroSpeech](https://download.zerospeech.com/)

# How to Train VITS on LJSpeech using NeMo

1. Clone the new forked NeMo repo.

    `git clone https://github.com/jasonjjl1999/NeMo.git`

2. Once you are in the repo, make sure that you are on the `vits` branch (Note: must do this before step 4).

    `git switch vits`

3. Install Cython module in Python environment.

    `pip install cython`

4. Install NeMo dependencies (run this in root dir of NeMo).

    `./reinstall`

5. Setup LJSpeech dataset. Copy data folder (from this repo) to root, such that these files exist in your filesystem:

    `/data/speech/LJSpeech/ljspeech_train.json`

    `/data/speech/LJSpeech/ljspeech_val.json`

    `/data/speech/LJSpeech/ljspeech_test.json`

6. Download the LJSpeech dataset. Copy all `*.wav` files from the LJSpeech dataset to the following location:

    `/data/speech/LJSpeech/wavs`

7. Navigate back to NeMo root directory and run this command:

    `python vits.py train_dataset=/data/speech/LJSpeech/ljspeech_train.json validation_datasets=/data/speech/LJSpeech/ljspeech_val.json sample_rate=22050`