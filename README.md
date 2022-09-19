#### What is this CTF?
TISC is a CTF organised by [CSIT][1]. More details on the 2022 event can be found [on their webpage][2].

#### Disclaimer:
Unfortunately, I only made it to task 3 before being unable to proceed any further.
Flags can be found in [flags.txt][3], though I doubt that will be of use.

<div style="padding:16px; border:1px solid #ced0d6; font-family:'Open Sans', sans-serif; background-color:white;">
    <div style="display:flex;">
        <div style="max-height:80px;">
            <img src="https://api.badgr.io/public/assertions/DpTkbep1S8a-3OJ3dpU0nA/image" title="Badge Image: TISC 2022 Badge of Participation" style="height:100%; max-width:80px;">
        </div>
        <div style="padding-left:16px; white-space:nowrap; text-overflow:ellipsis; overflow:hidden;">
            <a style="color:#0a1233; font-weight:600; text-decoration:underline; padding-bottom:4px;" target="_blank" href="https://badgr.com/public/assertions/DpTkbep1S8a-3OJ3dpU0nA">TISC 2022 Badge of Participation</a>
            <div style="font-size:12px; font-weight:700; color:#3b415c;  padding-bottom:8px; text-overflow:ellipsis; overflow:hidden;">TISC Issuing Team</div>
            <div style="font-size:12px; color:#3b415c; text-overflow:ellipsis; overflow:hidden;">Participants who complete at least level 1 will receive a digital badge as a little memento for your participation in TISC 2022.</div>
        </div>
    </div>
    <div style="border-top: 1px solid #ced0d6; padding-top:16px; margin-top:8px; display:flex; justify-content: space-between; color: #3b415c;">
    <div>Sep 15, 2022</div>
    <a style="color: #0a1233; font-weight:600; text-decoration:underline;" target="_blank" href="https://badgecheck.us.badgr.com/?url=https%3A%2F%2Fapi.badgr.io%2Fpublic%2Fassertions%2FDpTkbep1S8a-3OJ3dpU0nA&">Verify</a>
    </div>
</div>

#### Tasks 
##### Level 1: Slay the Dragon

For a first challenge, it certainly keeps your interest. The challenge is about beating a CLI game, which will prompt the CSIT server to send the flag to you.

Problem: The last stage features a dragon that takes you out in 1 hit.

It is impossible to circumvent beating the dragon; the flag is sent **only** when the server checks that you have defeated the dragon.

<details>
<summary style="cursor:pointer;text-decoration:underline;">Solution Steps:</summary>

1. You are meant to create a hacked client with the [client][4] folder, as the [core][5] and [server][6] folders are only meant to analyse the code for weaknesses.

2. As previously said, the dragon can defeat you in one move. As such, the client is modified to send to the server data that [never lets the dragon attack][7].

3. Normally, the client sends data on the command used to the server each turn. The server will then [validate][8] each step and make sure the client and simulated results are the same.

4. The server vulnerability is in [this line][9], where the [wrong][10] command was used; this meant [more than one command][11] can be sent at a time, without adding any previous [boss attacks][12] in the server's calculation.
</details>

##### Level 2: Leaky Matrices

A good test of your understanding of cryptography; uses many features present in actual cryptographic systems (but better).

Problem: Figure out a 8-byte symmetric key given 8 opportunities to find the identity of the data.

More info can be found in the [briefing material][13].

I did, however, find it simpler to run the [code][14] myself with NumPy's [interpreter][15].

<details>
<summary style="cursor:pointer;text-decoration:underline;">Solution Steps:</summary>

1. Let's take a look at the following key (which I used for testing). 
    ```py
    [0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 1, 1, 0, 0],
    [1, 0, 0, 1, 0, 0, 1, 0],
    [1, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [1, 1, 0, 0, 1, 0, 0, 0]
    ```

2. Looking at how the output vector was [calculated][16], we can see something interesting (for any input vector) before and after using the "&" operator
    ```py
    [2, 3, 2, 2, 1, 4, 2, 2] # Before "&"
    [0, 1, 0, 0, 1, 0, 0, 0] # After "&"
    ```
    Every time a new 1 is used in the input vector, the output vector where a digit flicks from 0 to 1 (and vice versa), **only if the key value in that position is a 1**.

3. Row n has an even number of 1s if response_n is 0, else 1.
    This means the 8 input vectors will be as follows, with a number changing to 1 every input entered.
    ```
    00000000 → 10000000 → 11000000 → 11100000 → ... → 11111111
    ```

    A change in the result produced means a 1 in that location within the secret key.

    
    Analysing the input and output vectors, we can observe the following:
    ```
    Input    → Process  → Final
    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
    10000000 → 00011101 → 00011101 → Column 1: Rows 4, 5, 6 and 8
    11000000 → 01012202 → 01010000 → Column 2: Rows 2, 5, 6 and 8
    11100000 → 12112312 → 10110110 → Column 3: Rows 1, 2, 3, 6 and 7
    11110000 → 23123422 → 01101000 → Column 4: Rows 1, 2, 4, 5, 6 and 7
    11111000 → 34223533 → 10001111 → Column 5: Rows 1, 2, 3, 6, 7 and 8
    11111100 → 35324643 → 11100001 → Column 6: Rows 2, 3, 5, 6 and 7
    11111110 → 36334743 → 10110101 → Column 7: Rows 2, 4 and 6
    11111111 → 37335743 → 11111101 → Column 8: Rows 2 and 5
    ```

    If you were to fill the specified indexes with 1s in a 8-by-8 matrix, and the rest with 0s, you will get the test key.
</details>

##### Level 3: Patient 0

> Level 3 consists of 2 parts. As previously stated, part 2 was left partially incomplete due to my inability to figure out the solutions in time.

This task provides you with a [corrupted file][17] of which you must extract clues and data out of, in order to find the flags needed.

Part 1: Find 8 corrupted bytes.
Part 2: Acquire a hash of some description (of which I was unable to decipher).

Being a CTF, the file contains many clues on the location of the bytes. A [hex editor][18] may be useful, though I used a [static version][19].

<details>
<summary style="cursor:pointer;text-decoration:underline;">Solution Steps: Part 1</summary>

1. The 1st clue is the only one needed for this part of the task. 
    Lines 343559 - 375489 hold an extractable PDF, containing the following:
    > 1. The BPB is broken, can you fix it?"

2. This refers to the BIOS Paremeter Block. If you haven't noticed, the file begins with "NTFS"; this is a NTFS file.

3. By looking at how the BPB of an NTFS file [should be formatted][20], we can locate the position of the corrupted bytes to be in the 0x20 - 0x27 range, the values of which are surprisingly obvious.

The corrupt bytes are (part of?) a key needed for part 2.

</details>

<details>
<summary style="cursor:pointer;text-decoration:underline;">Solution Steps: Part 2</summary>

1. The 2nd clue is a PNG file in lines 332039 - 332417. When extracted, a string of text is displayed, which, when base-32 decoded, provides the following:
    > 2. Thirsty for the flag? Go find the stream.
    The assumption is that this refers to a "data stream".

2. The 3rd clue can be found in lines 76040 - 76042, near a large amount of bytes that have not been deciphered. It reads:
    > 3. Are these True random bytes for Cryptology?
    This seems to imply a cryptographic algorithm employing pseudo-random bytes.

3. The 4th clue is in lines 343307 - 343318, delimited by spaces, to make finding it much harder. It reads:
    > If you need a password, the ~~original~~ reading of the BPB was actually Checked and ReChecked 32 times!
    This seems to imply the algorithm used a 32-rounds process.

Unfortunately, here the trail goes cold, and I was unable to locate the 'outer door'. It is possible brute force testing of keys was needed, but I never got that far.

More information on the hints can be found [here][21], while the NTFS file structure info can be found [here][22]. Other than what was said here, the files in the NTFS file may have been incorrectly interpreted.

</details>

[1]: https://www.csit.gov.sg
[2]: https://www.csit.gov.sg/events/tisc/tisc-2022
[3]: https://github.com/XieWren/TISC-CTF-2022/blob/main/Flags.txt
[4]: https://github.com/XieWren/TISC-CTF-2022/tree/main/slay_the_dragon/src/client
[5]: https://github.com/XieWren/TISC-CTF-2022/tree/main/slay_the_dragon/src/core
[6]: https://github.com/XieWren/TISC-CTF-2022/tree/main/slay_the_dragon/src/server
[7]: https://github.com/XieWren/TISC-CTF-2022/blob/main/slay_the_dragon/src/client/event/battleevent.py#L38
[8]: https://github.com/XieWren/TISC-CTF-2022/blob/main/slay_the_dragon/src/client/event/battleevent.py#L39
[9]: https://github.com/XieWren/TISC-CTF-2022/blob/main/slay_the_dragon/src/server/service/battleservice.py#L28
[10]: https://github.com/XieWren/TISC-CTF-2022/blob/main/slay_the_dragon/src/core/models/command.py#L31
[11]: https://github.com/XieWren/TISC-CTF-2022/blob/main/slay_the_dragon/src/client/event/battleevent.py#L38
[12]: https://github.com/XieWren/TISC-CTF-2022/blob/main/slay_the_dragon/src/server/service/battleservice.py#L32
[13]: https://github.com/XieWren/TISC-CTF-2022/blob/main/leaky_matrices/2WKV_Whitepaper.pdf
[14]: https://github.com/XieWren/TISC-CTF-2022/blob/main/leaky_matrices/main.py
[15]: https://numpy.org
[16]: https://github.com/XieWren/TISC-CTF-2022/blob/main/leaky_matrices/main.py#L95
[17]: https://github.com/XieWren/TISC-CTF-2022/blob/main/patient_0/PATIENT0
[18]: https://hexed.it
[19]: https://github.com/XieWren/TISC-CTF-2022/blob/main/patient_0/PATIENT0_hex.txt
[20]: http://jdebp.info/FGA/bios-parameter-block.html
[21]: https://github.com/XieWren/TISC-CTF-2022/blob/main/patient_0/hints.txt
[22]: https://github.com/XieWren/TISC-CTF-2022/blob/main/patient_0/conversion.py

*[many features]: e.g. XOR logic gates, matrix manipulation
*[&]: Binary AND