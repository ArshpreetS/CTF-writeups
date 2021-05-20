## Resources and Libraries
- Crypto --> I had use the command `pip install pycryptodome==3.4.3` to install this module
- factordb.com

To find the prime factors p and q. 
I used the site called **factordb.com**

After getting the factors, I could simply find the totient using the formula *(p-1)(q-1)*

I used the function *inverse* and *long_to_bytes* from the module Crypto.Util.number

inverse -->
long_to_bytes -->

The decryption key *d* could be found: `inverse(e,phi)`
The message then could easily be found using long_to_bytes(pow(c,d,n))