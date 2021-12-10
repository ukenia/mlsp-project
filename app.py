import sys

# # implement pip as a subprocess:
# subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
# 'matplotlib'])
#import imageio
import streamlit as st

st.set_page_config(layout='centered')

st.markdown("# MLSP Project")



st.markdown("Lets listen to the reconstructed audio")
file1='sample//'
file2='out//'

singer_to_song = {'ADIZ':['01']}

singer = st.sidebar.selectbox('Select a singer', ('ADIZ','VKOW'))
select_dept = st.sidebar.selectbox('Select a song', singer_to_song[singer])

aud1 = open(select_dept+"_recon.wav",'rb')
aud1 = aud1.read()
st.audio(aud1)