a='SO YJBMGNLJEMTB  E IHXIGSGHGSNO YSMTUJ SI E PUGTNW NV UOYJBMGSOL XB DTSYT HOSGI NV \
MZESOGUCG EJU JUMZEYUW DSGT YSMTUJGUCG  EYYNJWSOL GN E VSCUW IBIGUP  GTU  HOSGI  \
PEB XU ISOLZU ZUGGUJI  GTU PNIG YNPPNO   MESJI NV ZUGGUJI  GJSMZUGI NV ZUGGUJI  \
PSCGHJUI NV GTU EXNFU  EOW IN VNJGT  GTU JUYUSFUJ WUYSMTUJI GTU GUCG XB MUJVNJPSOL \
GTU SOFUJIU IHXIGSGHGSNO YGV_VZEL{GTSI_MHAAZU_YEOONG_XU_INZFUW}'
b={'Y':'C', 'G':'T', 'V':'F', 'Z':'L', 'E':'A', 'L':'G', 'N':'O', 'T':'H',\
   'U':'E', 'C':'X', 'J':'R', 'I':'S', 'S':'I', 'M':'P', 'O':'N', 'W':'D',\
   'P':'M', 'D':'W', 'F':'V', 'B':'Y', 'X':'B', 'H':'U', 'A':'Z'}
c=''
for i in a:
    if i==' ' or i=='_' or i=='{' or i=='}':
        c+=i
    elif i in b:
        c+=b[i]
    else:
        c+='*'
print(c)

##With substitution letter begin from YGV_VZEL - CTF_FLAG
