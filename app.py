# import required libraries

import sys
import streamlit as st
import numpy as np
import subprocess

# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'librosa'])

import librosa

# Basic page setup

st.set_page_config(layout='centered')

st.markdown("<p style='color:black;font-size:32px;text-align:center'><b>11755/18797 Machine Learning For Signal Processing: Final Project</b></p>", unsafe_allow_html=True)
st.image("app_files/front_page.PNG")

# create the singer to song dictionary

singer_to_song = {'ADIZ':['01']}

# create the selection boxes

singer = st.sidebar.selectbox('Select a singer', ('ADIZ','JLEE','JTAN','KENN','MCUR','MPOL','MPUR','NJAT','PMAR','SAMF','VKOW','ZHIY'))
song = st.sidebar.selectbox('Select a song', singer_to_song[singer])

# display the original song

st.markdown("Let's listen to the original song first")
aud1 = open("outputs/original/"+str(song)+"_"+str(singer)+".wav",'rb')
aud1 = aud1.read()
st.audio(aud1)

# display the lyrics

st.markdown("Let's listen to the lyrics now")
aud2 = open("outputs/read/"+str(song)+"_"+str(singer)+".wav",'rb')
aud2 = aud2.read()
st.audio(aud2)

# display the reconstructed song

st.markdown("Let's listen to the reconstructed audio")
aud3 = open("outputs/reconstructed/"+str(song)+"_"+str(singer)+".wav",'rb')
aud3 = aud3.read()
st.audio(aud3)

# display the similarity metric

y1, sr1 = librosa.load("outputs/original/"+str(song)+"_"+str(singer)+".wav")
spectrogram1 = librosa.stft(y1, n_fft=1024, hop_length=512, center=False, win_length=1024)
M1 = abs(spectrogram1)

y2, sr2 = librosa.load("outputs/reconstructed/"+str(song)+"_"+str(singer)+".wav")
spectrogram2 = librosa.stft(y2, n_fft=1024, hop_length=512, center=False, win_length=1024)
M2 = abs(spectrogram2)

sim_metric = (np.linalg.norm(np.dot(M2.T,M1))/np.linalg.norm(M2)/np.linalg.norm(M1))/(np.linalg.norm(np.dot(M2.T,M2))/np.linalg.norm(M2)/np.linalg.norm(M2))

st.metric('Similarity', str(round(sim_metric,2)), str(round(sim_metric-0.74,2)))