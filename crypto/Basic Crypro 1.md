# Classical Caesar cipher
 
```python
a = 'MablBlGhmVetllbvteVtxltkVbiaxk'
import string
def rotn(n):
   from string import ascii_lowercase as lc, ascii_uppercase as uc
   mapping = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
   return mapping
   
 for x in range(26):
         print("CTF_FLAG{"+f"{a.translate(rotn(x))}"+"}")
    
CTF_FLAG{MablBlGhmVetllbvteVtxltkVbiaxk}
CTF_FLAG{NbcmCmHinWfummcwufWuymulWcjbyl}
CTF_FLAG{OcdnDnIjoXgvnndxvgXvznvmXdkczm}
CTF_FLAG{PdeoEoJkpYhwooeywhYwaownYeldan}
CTF_FLAG{QefpFpKlqZixppfzxiZxbpxoZfmebo}
CTF_FLAG{RfgqGqLmrAjyqqgayjAycqypAgnfcp}
CTF_FLAG{SghrHrMnsBkzrrhbzkBzdrzqBhogdq}
CTF_FLAG{ThisIsNotClassicalCaesarCipher}
CTF_FLAG{UijtJtOpuDmbttjdbmDbftbsDjqifs}
CTF_FLAG{VjkuKuPqvEncuukecnEcguctEkrjgt}
CTF_FLAG{WklvLvQrwFodvvlfdoFdhvduFlskhu}
CTF_FLAG{XlmwMwRsxGpewwmgepGeiwevGmtliv}
CTF_FLAG{YmnxNxStyHqfxxnhfqHfjxfwHnumjw}
CTF_FLAG{ZnoyOyTuzIrgyyoigrIgkygxIovnkx}
CTF_FLAG{AopzPzUvaJshzzpjhsJhlzhyJpwoly}
CTF_FLAG{BpqaQaVwbKtiaaqkitKimaizKqxpmz}
CTF_FLAG{CqrbRbWxcLujbbrljuLjnbjaLryqna}
CTF_FLAG{DrscScXydMvkccsmkvMkockbMszrob}
CTF_FLAG{EstdTdYzeNwlddtnlwNlpdlcNtaspc}
CTF_FLAG{FtueUeZafOxmeeuomxOmqemdOubtqd}
CTF_FLAG{GuvfVfAbgPynffvpnyPnrfnePvcure}
CTF_FLAG{HvwgWgBchQzoggwqozQosgofQwdvsf}
CTF_FLAG{IwxhXhCdiRaphhxrpaRpthpgRxewtg}
CTF_FLAG{JxyiYiDejSbqiiysqbSquiqhSyfxuh}
CTF_FLAG{KyzjZjEfkTcrjjztrcTrvjriTzgyvi}
CTF_FLAG{LzakAkFglUdskkausdUswksjUahzwj}
```

flag: CTF_FLAG{ThisIsNotClassicalCaesarCipher}