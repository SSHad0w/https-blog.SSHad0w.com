---
title: "HTB Emdee Five For Life"
date: 2022-06-26
categories: ['htb', 'writeups']
---

Hello hackers! Today we'll cover a quick and fun scripting challenge python. This is the first Challenge on the Intro to Dante track on Hack The Box which is described as:
"Practice machines and challenges to help you prepare for the Dante Pro Lab."

# Introduction

For this challenge, we're met with a website that presents us with a prompt and field. The field says "MD5" in it, suggesting that we're expected to submit the MD5 hash version of the text.

![7e8ffdf4cd21b8d8e520a7de76212fb2.png](/assets/img/emdee-five-for-life/6b5ffa159ff34547a89604173deec78c.png)

# Methodology:

I looked up an [MD5 hash generator website](https://www.md5hashgenerator.com/) to complete the challenge. I inputted the string, copied the hash, and I was met with an unfavorable response:

![070ba9ff9b030207b243f0a632c19fa4.png](/assets/img/emdee-five-for-life/c7e303d689914f8ba57089583b5f9313.png)

The site changed the text provided and told me I was "Too slow!". Since I didn't appreciate it's teasing, I decided to boost my speed with a bespoke solution to this challenge.

# Identifying the template

First, I need to see what a normal raw response looks like from this server, so I'm able to parse out the relevant data, hash it, and submit a response *programmatically*. For that reason, I don't think burp suite will help me here, as it won't give me a view of how it needs to be parsed. I think python will get the job done well.

## Grabbing the response

I opened up the greatest editor of all time and wrote:

```py3
import requests
response = requests.get('http://134.209.176.83:30536') # change this for your instance!
print(response.content)
```

It's extremely simple, but it did the trick. Running this code gave me a response like the following:

```html
b'<html>\n<head>\n<title>emdee five for life</title>\n</head>\n<body style="background-color:powderblue;">\n<h1 align=\'center\'>MD5 encrypt this string</h1><h3 align=\'center\'>c3WOTbjAmW4hFDHQpCjZ</h3><center><form action="" method="post">\n<input type="text" name="hash" placeholder="MD5" align=\'center\'></input>\n</br>\n<input type="submit" value="Submit"></input>\n</form></center>\n</body>\n</html>\n'
```

I ran it a few more times to make sure I had a good understanding of the format.

Great! Now all I need to do is pluck out the relevant information in the response.

## Parsing the output

I tried parsing the output using classic python methods like `.split()`, but I ran into the following.

```py3
TypeError: byte indices must be integers or slices, not str
```

Turns out this was still raw bytes, instead of a proper string type.

The following update to my code fixed this issue:

```py3
import requests
response = requests.get('http://134.209.176.83:30536')
res = response.content

res = res.decode('utf-8')

print(res)
```

Now our output is a properly formatted string:

```html
<html>
<head>
<title>emdee five for life</title>
</head>
<body style="background-color:powderblue;">
<h1 align='center'>MD5 encrypt this string</h1><h3 align='center'>pV0iSaxkboFU0E07UayP</h3><center><form action="" method="post">
<input type="text" name="hash" placeholder="MD5" align='center'></input>
</br>
<input type="submit" value="Submit"></input>
</form></center>
</body>
</html>


```

## Grabbing specific output

Now it's time to shave our output down to only the text we need. We can use any parsing method, but I found [This stack overflow answer](https://stackoverflow.com/a/24053323) to be most helpful.

```py
import requests
response = requests.get('http://104.248.160.75:31480')
res = response.content

res = res.decode('utf-8')

mystr = res
search = "3 align='center'>"
start = mystr.index(search)+len(search)
stop = mystr.index("</h3>", start)
res = (mystr [ start : stop ])

print(res)
```

Now we have the raw "word."

Now let's hash it!

## Hashing the word

[According to stack overflow](https://stackoverflow.com/a/5297483), we can use the following lines to make an MD5 hash of the word:

```py3
import hashlib
print(hashlib.md5(res.encode('utf-8')).hexdigest())
```

Using the following code should yelid a valid MD5 hash:

```py3
import requests
import hashlib
response = requests.get('http://178.128.167.10:31790')
res = response.content

res = res.decode('utf-8')

mystr = res
search = "3 align='center'>"
start = mystr.index(search)+len(search)
stop = mystr.index("</h3>", start)
res = (mystr [ start : stop ])

print(res)

print("MD5 version:")

print(hashlib.md5(res.encode('utf-8')).hexdigest())
```

Output should look something like this:

```
fJHiQK1isKuPYxbEulUH
MD5 version:
80ed60f85b4fbbc982b5816912b1ba6a
```

Don't forget! We can always verify the validity with [an online tool:](https://www.md5hashgenerator.com/)

![21e983c747f84524a318b84af239b953.png](/assets/img/emdee-five-for-life/b06943e9cb2b40f699d5f886736a8dbe.png)

That looks correct! now, we can focus on sending the hashed message back to the server!

## Sending the hash

In the original response, we saw that the HTML field name was called "hash" so we'll use that field name to submit our response. [After a bit of reading](https://www.geeksforgeeks.org/get-post-requests-using-python/), the syntax became extremely straightforward for the `requests` library. We just need a dictionary to hold our data and submit our response. With that added, our code now looks like the following:

```py3
import requests
import hashlib
# Grabbing and decoding
url = 'http://178.128.167.10:31790'
response = requests.get(url) 
res = response.content
res = res.decode('utf-8')
# Parsing out the word
mystr = res
search = "3 align='center'>"
start = mystr.index(search)+len(search)
stop = mystr.index("</h3>", start)
res = (mystr [ start : stop ])
print(res)

# Hashing as MD5
print("MD5 version:")
hash = (hashlib.md5(res.encode('utf-8')).hexdigest())
print(hash)

# Sending the hash
payload = {"hash":hash}
response = requests.post(url, data=payload)
res = response.content
flag = res.decode('utf-8')
print("\n\n" + flag)
```

Everything looks ready to use, so let's run it!

Output:

## Our flag... Or not?

```html
LSByV3cfj4CH7ufR5G2a
MD5 version:
46b323c4923e460759346454210adb8f


<html>
<head>
<title>emdee five for life</title>
</head>
<body style="background-color:powderblue;">
<h1 align='center'>MD5 encrypt this string</h1><h3 align='center'>OLWB7P9EqGd03jHmmXRN</h3><p align='center'>Too slow!</p><center><form action="" method="post">
<input type="text" name="hash" placeholder="MD5" align='center'></input>
</br>
<input type="submit" value="Submit"></input>
</form></center>
</body>
</html>
```

It seems we're too slow.

I thought we'd be fast enough, but maybe our code was too inefficient. We'll have to find a way to speed it up, but first we'll need to find out how fast we currently are!

## Clocking our code

Let's see how fast our code is running.

We can use the `time` command to clock it

`time python3 payload.py` yields us:

```
real	0m0.690s
user	0m0.173s
sys	0m0.017s
```

## Why it didn't work:

After reading a [blog post](https://www.soeren.codes/posts/hackthebox-emdee-five-for-life-writeup/) about this challenge, I found out why this wouldn't work properly:

![Credit to Soren_codes ](/assets/img/emdee-five-for-life/f59fe0ebbb2f4a779538177fb2affa12.png)

Knowing this, I rewrote my code to use a single coherent `session` rather than sending random disjointed requests.

Our code now looks like this:

```
import requests
import hashlib
# Grabbing and decoding
url = 'http://161.35.166.224:32511'
session = requests.session()
response = session.get(url) 
res = response.content
res = res.decode('utf-8')
# Parsing out the word
mystr = res
search = "3 align='center'>"
start = mystr.index(search)+len(search)
stop = mystr.index("</h3>", start)
res = (mystr [ start : stop ])
print(res)

# Hashing as MD5
print("MD5 version:")
hash = (hashlib.md5(res.encode('utf-8')).hexdigest())
print(hash)


# Sending the hash
payload = {"hash":hash}
response = session.post(url, data=payload)
res = response.content
flag = res.decode('utf-8')
print("\n\n" + flag)
```

Only a few small changes, but it made a huge difference!

Output:

```
C7RrJ4GN4f2tMK51Z8JZ
MD5 version:
d185f72466f92c697b6c9ed3ca496ebe


<html>
<head>
<title>emdee five for life</title>
</head>
<body style="background-color:powderblue;">
<h1 align='center'>MD5 encrypt this string</h1><h3 align='center'>C7RrJ4GN4f2tMK51Z8JZ</h3><p align='center'>HTB{N1c3_ScrIpt1nG_B0i!}</p><center><form action="" method="post">
<input type="text" name="hash" placeholder="MD5" align='center'></input>
</br>
<input type="submit" value="Submit"></input>
</form></center>
</body>
</html>
```

## Lessons learned
It's times like this that remind me that [it's okay to use writeups](https://www.hackthebox.com/blog/It-is-Okay-to-Use-Writeups), even [the best people in the field do it to learn!](https://www.linkedin.com/posts/ippsec_it-is-okay-to-use-writeups-activity-7072539730092941312-VNtm?utm_source=share&utm_medium=member_desktop). If I hadn't have stopped and read a writeup, I wouldn't have understood why I needed to use `requests.session()`, and I wouldn't have been able to progress. It's easy to get frustrated while learning new things, but there's no point in staying frustrated if you're stuck.

Thanks for reading! Be sure to come back to read my writeup on "Heist"!


Thanks for reading! Be sure to come back to read my writeup on "Heist"!

![148d5c56eb68815bb589c42a3b9da574.png](/assets/img/emdee-five-for-life/6421a9e3bea0497e914951adb3f79a2d.png)
