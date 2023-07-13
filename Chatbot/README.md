# How to run our chatbot

**Note: this project was completed using Python 3.10.0**

1. Download and extract the Chatbot zip file [here](https://github.com/KaeCan/NLP_Portfolio/blob/main/ChatbotZip.zip).

2. In a terminal, run this command:
~~~
pip install -r requirements.txt
~~~
You may need to also install an additional spaCy dependency:
~~~
python -m spacy download en_core_web_sm
~~~
There may be other dependencies required, such as in nltk.

3. **If you do not wish to modify the chatbot's model or user models, skip to step 5**. Otherwise, you can create a new model using
[sklearn_model.py](https://github.com/KaeCan/NLP_Portfolio/blob/main/Chatbot/model/sklearn_model.py) (or our discarded [tensorflow_model.py](https://github.com/KaeCan/NLP_Portfolio/blob/main/Chatbot/model/tensorflow_model.py), but you must manually install the required dependencies)
located in the 'model' folder.

4. If you wish to ever reset or modify the starting user models, run [user_seed.py](https://github.com/KaeCan/NLP_Portfolio/blob/main/Chatbot/user_seed.py)

5. Run [chatbot.py](https://github.com/KaeCan/NLP_Portfolio/blob/main/Chatbot/chatbot.py)
