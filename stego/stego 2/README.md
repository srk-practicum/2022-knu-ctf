```bash
┌──(kali㉿kali)-[~/Downloads]
└─$ zsteg embed.png                           
b1,r,lsb,xy         .. file: PDF document, version 1.4
b1,g,lsb,xy         .. text: ")?fS__R_"
b1,rgba,lsb,xy      .. text: "QQ?qy7}s"
b1,abgr,msb,xy      .. text: "[_US{wuS"
b3,abgr,msb,xy      .. file: PGP Secret Sub-key -
b4,g,lsb,xy         .. text: "ve2TFR7F"


┌──(kali㉿kali)-[~/Downloads]
└─$ zsteg embed.png -E b1,r,lsb,xy > embed.pdf
```

that pdf contains our flag

flag CTF_FLAG{r0_crew_is_only_significant_thing}