{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3fa162f6-f4bd-4179-a140-9aab858d935b",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Çalışan():\n",
    "    personel = []\n",
    "\n",
    "    def __init__(self,isim):\n",
    "        self.isim = isim\n",
    "        self.kabiliyetleri = []\n",
    "        self.personele_ekle()\n",
    "\n",
    "    @classmethod\n",
    "    def personel_sayısını_görüntüle(cls):\n",
    "        print(len(cls.personel))\n",
    "\n",
    "    def personele_ekle(self):\n",
    "        self.personel.append(self.isim)\n",
    "        print(\"{} adlı kişi personele eklendi\".format(self.isim))\n",
    "\n",
    "    @classmethod\n",
    "    def personeli_görüntüle(cls):\n",
    "        print(\"Personel listesi:\")\n",
    "        for kişi in cls.personel:\n",
    "            print(kişi)\n",
    "\n",
    "    def kabiliyet_ekle(self, kabiliyet):\n",
    "        self.kabiliyetleri.append(kabiliyet)\n",
    "\n",
    "    def kabiliyetleri_görüntüle(self):\n",
    "        print(\"{} adlı kişinin kabiliyetleri: \".format(self.isim))\n",
    "        for kabiliyet in self.kabiliyetleri:\n",
    "            print(kabiliyet)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "25add0c5-638c-4835-8b9f-5cc4f59696af",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
