from sympy import factorint
from sympy import mod_inverse

# Given values
c = 30799623142724830428134771008774390881460367194180049770617479901591091484591391500858137510867287877342653943804928164707846331839143915672730906056617147012428680844976482183492261655523056337339390942259568877248040620902843834757375278079349955880905114854509612475407520861544225725514664260341618660142
n = 66162734470397639929895334547153582871789109310109808226194873261434341609762372608106100870489807600684436835690151747789231905775061265117863474548210288394265949168753204937477698085137930480033498602383227967171466777365559934660792726075125884854414870261501376573981953429422415034945771535881963371639
e = 57325152988885502664742767926377800268684880204403088949876001165815130683844802230893826780734893952876457220211390309210307998621012616036554033222012357502159286260078575811710163042025394830810498140672344153439146493876289499594044393060927442653258971083672557141642947489014255351176540185795781515833

# Factorize n
factors = factorint(n)
if len(factors) == 2:
    p, q = factors
    print(f"Factors of n: p = {p}, q = {q}")

    # Compute φ(n)
    phi_n = (p - 1) * (q - 1)
    print(f"φ(n) = {phi_n}")

    # Compute d
    d = mod_inverse(e, phi_n)
    print(f"Private exponent d = {d}")

    # Decrypt message
    decrypted_message = pow(c, d, n)
    print(f"Decrypted message: {decrypted_message}")

else:
    print("Failed to factorize n or n does not have exactly two factors.")
