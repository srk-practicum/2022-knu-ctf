---
aliases: []
Tags: []
---
``````ad-success
title: # #h/lime ==Basic Thing 3==
#h/lime ==date: 2022-01-28==
#h/lime ==time: 10:23==
----
Status:
Key concepts:
answ: 
```python
data = '82 64 112 85 95 89 114 103 103 114 69 95 85 64 70 95 48 74 97 95 65 104 122 79 51 69'
data = [int(x) for x in data.split(' ')]
data
for x in data:
    print(chr(x), end = '')
a = 'R@pU_YrggrE_U@F_0Ja_AhzO3E'
import string
def rotn(n):
   from string import ascii_lowercase as lc, ascii_uppercase as uc
   mapping = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
   return mapping

for x in range(26):
    print("CTF_FLAG{"+f"{a.translate(rotn(x))}"+"}")
	
CTF_FLAG{R@pU_YrggrE_U@F_0Ja_AhzO3E}
CTF_FLAG{S@qV_ZshhsF_V@G_0Kb_BiaP3F}
CTF_FLAG{T@rW_AtiitG_W@H_0Lc_CjbQ3G}
CTF_FLAG{U@sX_BujjuH_X@I_0Md_DkcR3H}
CTF_FLAG{V@tY_CvkkvI_Y@J_0Ne_EldS3I}
CTF_FLAG{W@uZ_DwllwJ_Z@K_0Of_FmeT3J}
CTF_FLAG{X@vA_ExmmxK_A@L_0Pg_GnfU3K}
CTF_FLAG{Y@wB_FynnyL_B@M_0Qh_HogV3L}
CTF_FLAG{Z@xC_GzoozM_C@N_0Ri_IphW3M}
CTF_FLAG{A@yD_HappaN_D@O_0Sj_JqiX3N}
CTF_FLAG{B@zE_IbqqbO_E@P_0Tk_KrjY3O}
CTF_FLAG{C@aF_JcrrcP_F@Q_0Ul_LskZ3P}
CTF_FLAG{D@bG_KdssdQ_G@R_0Vm_MtlA3Q}
CTF_FLAG{E@cH_LetteR_H@S_0Wn_NumB3R}
CTF_FLAG{F@dI_MfuufS_I@T_0Xo_OvnC3S}
CTF_FLAG{G@eJ_NgvvgT_J@U_0Yp_PwoD3T}
CTF_FLAG{H@fK_OhwwhU_K@V_0Zq_QxpE3U}
CTF_FLAG{I@gL_PixxiV_L@W_0Ar_RyqF3V}
CTF_FLAG{J@hM_QjyyjW_M@X_0Bs_SzrG3W}
CTF_FLAG{K@iN_RkzzkX_N@Y_0Ct_TasH3X}
CTF_FLAG{L@jO_SlaalY_O@Z_0Du_UbtI3Y}
CTF_FLAG{M@kP_TmbbmZ_P@A_0Ev_VcuJ3Z}
CTF_FLAG{N@lQ_UnccnA_Q@B_0Fw_WdvK3A}
CTF_FLAG{O@mR_VoddoB_R@C_0Gx_XewL3B}
CTF_FLAG{P@nS_WpeepC_S@D_0Hy_YfxM3C}
CTF_FLAG{Q@oT_XqffqD_T@E_0Iz_ZgyN3D}
```
flag: CTF_FLAG{E@cH_LetteR_H@S_0Wn_NumB3R}
---
``````

---
```ad-example
title: ## #h/white _References_
color: 200,200,200
collapse: open
```
- 
