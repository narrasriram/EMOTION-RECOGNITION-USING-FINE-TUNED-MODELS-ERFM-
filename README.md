# Setup Guide



Step 1: Clone the repository to your Local Machine
	For MAC users, open the terminal/ For Windows users, open the Gitbash terminal
	Type the following command:
git clone https://github.com/narrasriram/EMOTION-RECOGNITION-USING-FINE-TUNED-MODELS-ERFM-.git

Step 2: Download the Models
	Download the models from the below publicly accessbile Google Drive Links -
For Distilbert Model:
https://drive.google.com/folderview?id=18K2g5mPgVkCbp-ioeW89Pjc1Zh0eSlWY

For ALBERT Model:
https://drive.google.com/drive/folders/1vVfeSXd0xXZSpxY83fy4Xc0_D7kSoBM8?usp=sharing

Step 3: Organize the Project Files in a Folder
	Create a folder for the project “ReplicatingEmotionRecognizer”
	Paste a copy of “emotionrecognizer.py” file from the cloned github repository folder to the “ReplicatingEmotionRecognizer”
	Store the downloaded Distilbert and ALBERT in the “ReplicatingEmotionRecognizer” folder

Step 4: Update the Model Accessible Paths
	Open the “emotionrecognizer.py” file
	Update the path of Distibert Model specified in the file to your system path where the Distilbert Model is present.
	Update the path of ALBERT Model specified in the file to your system path where the ALBERT Model is present.
	
Step 5: Install Dependencies
	Install k-train library using the following command in terminal
pip install ktrain
	Install transformers library using the following command in terminal
pip install transformers

Step 6: Run the File
	In the command prompt, navigate to the “ReplicatingEmotionRecognizer” folder.
	Type the following command to run the File:
python3 emotionrecognizer.py

Step 7: Test with an Example
	When the user runs the python file, the system prompts to give an input sentence.
	Once the user enters the Input Sentence and click on Enter button, the system generates the output for the user.



