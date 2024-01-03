from os.path import isfile,join

import os

from subprocess import call,STDOUT

import subprocess



input_video = './ibuck.mp4'





def extract(val,vid):

	print("extracting in progress....")

	global input_video
	
	# frames extraction

	global count,height,width,fps

	

	ffmpeg_cmd = [

		'ffmpeg',

		'-i', input_video,

		'-q:v', "0",

		"./temp/%01d.png"

        ]

	try:

		subprocess.run(ffmpeg_cmd, check=True)

		print("Frames extracted successfully.")

	except subprocess.CalledProcessError as e:

		print(f"An error occurred: {e}")



def stego():

	print("---- Welcome to frame extractor ----")

	extract(True,input_video)

stego()