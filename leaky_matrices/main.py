import sys
import numpy as np




# Banner String
banner = """
 ::::::::        :::       :::     :::     :::   :::
:+:    :+:       :+:       :+:   :+: :+:   :+:   :+:
      +:+        +:+       +:+  +:+   +:+   +:+ +:+
    +#+          +#+  +:+  +#+ +#++:++#++:   +#++:
  +#+            +#+ +#+#+ +#+ +#+     +#+    +#+
 #+#              #+#+# #+#+#  #+#     #+#    #+#
##########         ###   ###   ###     ###    ###

:::    ::: :::::::::: :::   :::          :::               :::
:+:   :+:  :+:        :+:   :+:         :+:                 :+:
+:+  +:+   +:+         +:+ +:+         +:+                   +:+
+#++:++    +#++:++#     +#++:         +#+    +#++:++#++:++    +#+
+#+  +#+   +#+           +#+           +#+                   +#+
#+#   #+#  #+#           #+#            #+#                 #+#
###    ### ##########    ###             ###              ###

:::     ::: :::::::::: :::::::::  ::::::::::: :::::::::: :::   :::
:+:     :+: :+:        :+:    :+:     :+:     :+:        :+:   :+:
+:+     +:+ +:+        +:+    +:+     +:+     +:+         +:+ +:+
+#+     +:+ +#++:++#   +#++:++#:      +#+     :#::+::#     +#++:
 +#+   +#+  +#+        +#+    +#+     +#+     +#+           +#+
  #+#+#+#   #+#        #+#    #+#     #+#     #+#           #+#
    ###     ########## ###    ### ########### ###           ###
"""




# Helper & Win Functions
def sysout(fstr):
    sys.stdout.write(fstr)
    sys.stdout.flush()

def prompt(fstr):
    guards = "=" * len(fstr)
    sysout(f"{guards}\n{fstr}\n{guards}\n")

def vectostr(v):
    return "".join(map(str, v.reshape(-1)))

def strtovec(s, rows=8, cols=1):
    return np.fromiter(list(s), dtype="int").reshape(rows, cols)
"""
array([[1],
    [0],
    [1],
    [0],
    [1],
    [0],
    [1],
    [0]])
"""

def win():
    flag = open("/flag.txt").read().strip()
    prompt(f"Here is your flag: {flag}")




# SECRET KEY (Symmetric)
SECRET_KEY = np.round(np.random.rand(8, 8)).astype("int")
"""
array([[0, 0, 1, 1, 1, 0, 0, 0],
       [0, 1, 1, 1, 1, 1, 1, 1],
       [0, 0, 1, 0, 1, 1, 0, 0],
       [1, 0, 0, 1, 0, 0, 1, 0],
       [1, 1, 0, 1, 0, 1, 0, 1],
       [1, 1, 1, 1, 1, 1, 1, 0],
       [0, 0, 1, 1, 1, 1, 0, 0],
       [1, 1, 0, 0, 1, 0, 0, 0]])
"""

if __name__ == "__main__":
    sysout(banner)




    # Client --> Server Challenges
    prompt("Challenge Me!")
    for i in range(8):
        input_vec = input(f"Challenge Me #{i+1:02} <-- ")
        assert len(input_vec) == 8
        assert input_vec.count("1") + input_vec.count("0") == 8
        input_vec = strtovec(input_vec)
        output_vec = (SECRET_KEY @ input_vec) & 1
        """
        Before "& 1"            After "& 1"     <--     even = 0, odd = 1
        array([[2],             array([[0],
               [3],                    [1],
               [2],                    [0],
               [2],                    [0],
               [1],                    [1],
               [4],                    [0],
               [2],                    [0],
               [2]])                   [0]], dtype=int32)
        """
        sysout(f"My Response --> {vectostr(output_vec)}\n")




    # Server --> Client Challenges
    prompt("Challenge You!")
    for i in range(8):
        input_vec = np.round(np.random.rand(8, 1)).astype("int")
        sysout(f"Challenge You #{i+1:02} --> {vectostr(input_vec)}\n")
        test_vec = input(f"Your Response <-- ")
        assert len(test_vec) == 8
        assert test_vec.count("1") + test_vec.count("0") == 8
        test_vec = strtovec(test_vec)
        answer_vec = (SECRET_KEY @ input_vec) & 1
        assert (answer_vec == test_vec).all()




    # Authenticated!
    prompt("All challenges passed :)")
    win()