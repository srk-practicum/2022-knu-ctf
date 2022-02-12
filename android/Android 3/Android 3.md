# Android 3

## This task is about RSA implementation
```java
public final void onClick(View var1) {
      BigInteger var3 = new BigInteger(this.c.getResources().getString(2131099674));
      BigInteger var2 = new BigInteger("10001", 16);
      if ((new BigInteger(this.a.getText().toString().getBytes())).modPow(var2, var3).toString().equals("4541193573047010079622862634544566667638995016075815652287123393675051074423")) {
         this.b.setText("Congrats!");
      } else {
         this.b.setText("Fail!");
```

## From upper code we can get the public exponent,
```
pubic exp = 65537
```
## message,
```
4541193573047010079622862634544566667638995016075815652287123393675051074423
```
## and the id of the resouce (2131099674=0x7f06001a). Lets find the data behind that id. APK is an archive, so we can extract everything from it using [apktool](https://ibotpeaches.github.io/Apktool/). 

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
## So, N = 85715674500858120010215671295511591797438474555497398310962747973700011956693. It's len is just 77 bytes, so it can be factored in nearly 5 minutes
```
p = 256128251579833588962640669288236343457 (39 digits) 
q = 334659195040579408284360462422195488949 (39 digits)
```
## After primes are found and knowing public exponent decoding the message is a trivial thing. 
flag: CTF_FLAG{rsa_is_totally_broken}