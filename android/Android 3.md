---
aliases: []
Tags: []
---
``````ad-success
title: # #h/lime ==Android 3==
#h/lime ==date: 2022-02-04==
#h/lime ==time: 17:34==
----
Status:
Key concepts:
answ:
rsa implementation
```java
public final void onClick(View var1) {
      BigInteger var3 = new BigInteger(this.c.getResources().getString(2131099674));
      BigInteger var2 = new BigInteger("10001", 16);
      if ((new BigInteger(this.a.getText().toString().getBytes())).modPow(var2, var3).toString().equals("4541193573047010079622862634544566667638995016075815652287123393675051074423")) {
         this.b.setText("Congrats!");
      } else {
         this.b.setText("Fail!");
```
pubic exp = 65537
lets find resourse 2131099674=0x7f06001a

```bash
┌──(kali㉿kali)-[~/Downloads]
└─$ grep -r "0x7f06001a" ./android 
./android/res/values/public.xml:    <public type="string" name="nnn" id="0x7f06001a" />
./android/smali/com/application/test/e.smali:    const v2, 0x7f06001a
┌──(kali㉿kali)-[~/Downloads]
└─$ grep -r "nnn" ./android
grep: ./android/res/drawable-hdpi-v4/abc_popup_background_mtrl_mult.9.png: binary file matches
./android/res/values/strings.xml:    <string name="nnn">85715674500858120010215671295511591797438474555497398310962747973700011956693</string>
./android/res/values/public.xml:    <public type="string" name="nnn" id="0x7f06001a" />
```
N = 85715674500858120010215671295511591797438474555497398310962747973700011956693

lets find primes:
p = 256128251579833588962640669288236343457 (39 digits) 
q = 334659195040579408284360462422195488949 (39 digits)

flag: CTF_FLAG{rsa_is_totally_broken}
---
``````

---
```ad-example
title: ## #h/white _References_
color: 200,200,200
collapse: open
```
- 
