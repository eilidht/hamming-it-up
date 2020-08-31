# hamming-it-up

An algorithm for calculating hamming distance faster (with a small alphabet size).

 Hamming distance between two strings of equal length is the number of positions at which the corresponding symbols are 
 different. In other words, it measures the minimum number of substitutions required to change one string into the 
 other.
 
 For binary strings a and b the Hamming distance is equal to the number of ones (population count) in a XOR b.
 XOR is a very efficient computation, and counting the number of ones only needs as many steps as there ones. 
 
 The key idea in the algorithm presented here is to map strings onto binary in such a way that the hamming distance
 can then be calculated using the XOR operation. For this to work, every character must be the same hamming distance
 from every other character when converted to binary. This can be done by converting each character into a binary string 
 the length of the alphabet to be represented as follows:
 
 ### Binary to hamming mapping
 ```
 A 0001
 C 0010
 G 0100
 T 1000
```
 
 Each of these binary representations has a hamming distance of 2 when compared with any other. E.g.
 
```
 A    0001             A    0001            A    0001            A    0001
 A    0001             C    0010            G    0100            T    1000
 XOR  0000             XOR  0011            XOR  0101            XOR  1001 

                       C    0010            C    0010            C    0010
                       C    0010            G    0100            T    1000
                       XOR  0000            XOR  0110            XOR  1010

                                            G    0100            G    0100
                                            G    0100            T    1000
                                            XOR  0000            XOR  1100

                                                                 G    1000
                                                                 T    1000
                                                                 XOR  0000

 

 ```
 