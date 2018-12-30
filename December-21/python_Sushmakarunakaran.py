{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the form countryIndia\n",
      "enter the to countryRussia\n",
      "enter the amount to be transferred1000\n",
      "amount in \n",
      "Russia\n",
      "is\n",
      "895.5453149001537\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "data=pd.read_excel(\"EXCHANGE RATES.xlsx\")\n",
    "a=input(\"enter the form country\")\n",
    "b=input(\"enter the to country\")\n",
    "c=int(input(\"enter the amount to be transferred\"))\n",
    "d=data[data.LOCATION==a]\n",
    "e=data[data.LOCATION==b]\n",
    "f=float(c / float (d.VALUE))*float (e.VALUE)\n",
    "print(\"amount in \")\n",
    "print(b)\n",
    "print(\"is\")\n",
    "print(f)\n",
    "    \n",
    "    "
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
   "version": "3.5.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
