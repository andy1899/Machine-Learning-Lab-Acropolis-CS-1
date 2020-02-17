{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      "List Trainer: [##                  ] 10%"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package stopwords to /home/andy/nltk_data...\n",
      "[nltk_data]   Package stopwords is already up-to-date!\n",
      "[nltk_data] Downloading package averaged_perceptron_tagger to\n",
      "[nltk_data]     /home/andy/nltk_data...\n",
      "[nltk_data]   Package averaged_perceptron_tagger is already up-to-\n",
      "[nltk_data]       date!\n",
      "/home/andy/.local/lib/python3.7/site-packages/chatterbot/corpus.py:38: YAMLLoadWarning: calling yaml.load() without Loader=... is deprecated, as the default Loader is unsafe. Please read https://msg.pyyaml.org/load for full details.\n",
      "  return yaml.load(data_file)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "List Trainer: [####################] 100%\n",
      "Thank you.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Exception in Tkinter callback\n",
      "Traceback (most recent call last):\n",
      "  File \"/usr/lib/python3.7/tkinter/__init__.py\", line 1705, in __call__\n",
      "    return self.func(*args)\n",
      "  File \"<ipython-input-1-29a3ebb89e4d>\", line 53, in ask\n",
      "    textF.delete(1.0, END)\n",
      "  File \"/usr/lib/python3.7/tkinter/__init__.py\", line 2679, in delete\n",
      "    self.tk.call(self._w, 'delete', first, last)\n",
      "_tkinter.TclError: bad entry index \"1.0\"\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I'm doing great.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Exception in Tkinter callback\n",
      "Traceback (most recent call last):\n",
      "  File \"/usr/lib/python3.7/tkinter/__init__.py\", line 1705, in __call__\n",
      "    return self.func(*args)\n",
      "  File \"<ipython-input-1-29a3ebb89e4d>\", line 53, in ask\n",
      "    textF.delete(1.0, END)\n",
      "  File \"/usr/lib/python3.7/tkinter/__init__.py\", line 2679, in delete\n",
      "    self.tk.call(self._w, 'delete', first, last)\n",
      "_tkinter.TclError: bad entry index \"1.0\"\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "My name is Andy\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Exception in Tkinter callback\n",
      "Traceback (most recent call last):\n",
      "  File \"/usr/lib/python3.7/tkinter/__init__.py\", line 1705, in __call__\n",
      "    return self.func(*args)\n",
      "  File \"<ipython-input-1-29a3ebb89e4d>\", line 53, in ask\n",
      "    textF.delete(1.0, END)\n",
      "  File \"/usr/lib/python3.7/tkinter/__init__.py\", line 2679, in delete\n",
      "    self.tk.call(self._w, 'delete', first, last)\n",
      "_tkinter.TclError: bad entry index \"1.0\"\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "My name is Andy\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Exception in Tkinter callback\n",
      "Traceback (most recent call last):\n",
      "  File \"/usr/lib/python3.7/tkinter/__init__.py\", line 1705, in __call__\n",
      "    return self.func(*args)\n",
      "  File \"<ipython-input-1-29a3ebb89e4d>\", line 53, in ask\n",
      "    textF.delete(1.0, END)\n",
      "  File \"/usr/lib/python3.7/tkinter/__init__.py\", line 2679, in delete\n",
      "    self.tk.call(self._w, 'delete', first, last)\n",
      "_tkinter.TclError: bad entry index \"1.0\"\n"
     ]
    }
   ],
   "source": [
    "from tkinter import *\n",
    "# import PhotoImage\n",
    "\n",
    "# create main window\n",
    "\n",
    "from chatterbot import ChatBot\n",
    "from chatterbot.trainers import ListTrainer\n",
    "\n",
    "chatbot = ChatBot(\"Andy's Bot\")\n",
    "\n",
    "conversation = [\n",
    "    \"Good morning\",\n",
    "    \"Hi there!\",\n",
    "    \"How are you doing?\",\n",
    "    \"I'm doing great.\",\n",
    "    \"That is good to hear\",\n",
    "    \"Thank you.\",\n",
    "    \"You're welcome.\",\n",
    "    \"What is your name\",\n",
    "    \"My name is Andy\",\n",
    "    \"Created by Anand on 17/02\"\n",
    "]\n",
    "\n",
    "trainer = ListTrainer(chatbot)\n",
    "trainer.train(conversation)\n",
    "\n",
    "master = Tk()\n",
    "master.title(\"ChatBot\")\n",
    "master.geometry(\"500x650\")\n",
    "img = PhotoImage(file=\"download.png\")\n",
    "photo = Label(master, image=img)\n",
    "photo.pack(pady=5)\n",
    "frame = Frame(master)\n",
    "sc = Scrollbar(frame)\n",
    "msg = Listbox(frame, width=80, height=20)\n",
    "sc.pack(side=RIGHT, fill=Y)\n",
    "msg.pack(side=LEFT, fill=BOTH, pady=10)\n",
    "frame.pack()\n",
    "textF = Entry(master, font=(\"Verdana\", 20))\n",
    "textF.pack(pady=10)\n",
    "\n",
    "\n",
    "def ask():\n",
    "    while True:\n",
    "        query = textF.get()\n",
    "        if query == 'exit':\n",
    "            break\n",
    "        response = chatbot.get_response(query)\n",
    "        print(response)\n",
    "        msg.insert(END, \"you :\" + query)\n",
    "        msg.insert(END, \"bot:\")\n",
    "        msg.insert(END, response)\n",
    "        textF.delete(1.0, END)\n",
    "\n",
    "\n",
    "button = Button(master,\n",
    "                text=\"ASK\",\n",
    "                fg=\"red\",\n",
    "                command=ask)\n",
    "button.pack()\n",
    "# Run forever!\n",
    "master.mainloop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
