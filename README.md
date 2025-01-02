# hamming-it-up

An algorithm for calculating hamming distance faster (with a small alphabet size).

 Hamming distance between two strings of equal length is the number of positions at which the corresponding symbols are 
 different. In other words, it measures the minimum number of substitutions required to change one string into the 
 other. For example, it requires one substitution to turn CAT into TAT.
 
 For binary strings a and b the Hamming distance is equal to the number of ones (population count) in a XOR b.
 XOR is a very efficient computation, and counting the number of ones only needs as many steps as there ones [Wegner]. 
 
 The key idea in the algorithm presented here is to map strings onto binary in such a way that the hamming distance
 can then be calculated using the efficient binary XOR operation, which can compare many characters simultaneously in 
 one operation. A 64-bit machine could compare 16 characters (in the 4 letter alphabet described below) in one operation,
 plus one operation for every point of mismatch. 
 This algorithm will be most effective when:
 * the same string is searched many times, and so the overhead of pre-processing to binary doesn't matter.
 * the alphabet size is small (the binary representation of each char is equal to the length of the alphabet)
 * we are only interested in results with few mismatches (then the algorithm can terminate early without 
    counting all mismatches)
    
 
 For this to work, every character must be the same hamming distance
 from every other character when converted to binary. This can be done by converting each character into a binary string 
 the length of the alphabet to be represented as follows:
 
 ### Binary to hamming mapping
 ```
 A 0001
 C 0010
 G 0100
 T 1000
```
I later discovered that this is known as one-hot encoding. I haven't found any references to it being used in 
DNA hamming distance comparisons.
 
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

                                                                 T    1000
                                                                 T    1000
                                                                 XOR  0000
 ```

### Example 

For example compare CAT to TAT:

1. Convert to binary representation
    ```
    CAT -> 001000011000
    TAT -> 100000011000
    ```
2. XOR the binary representations
    ```
    001000011000
    100000011000
    ------------
    101000000000
    ```
3. Count the number of ones in the result 
    ```
    101000000000  -> 2
    ```
4. Divide by 2 to get number of differences between the strings
    ```
    2/2 = 1 The strings differ by one character.
    ```

## Extension to larger alphabet size
The same pattern can be used for any alphabet size. The binary representation of each character will have as many digits
as there are characters in the alphabet. For example:
 ```
 A 000001
 B 000010
 C 000100
 D 001000
 E 010000
 F 100000
```
Any of these two binary representations will mismatch at two positions when XOR'ed.

## Extension to handle simple wildcard matches
It is possible to represent the wildcard operator (\*) with zeros. This will mismatch any character at only one position.
The number of wildcard operators in the search just need to be removed from the final mismatch count. 
Note that the number of wildcards must be known

For example, searching for the pattern T\*T in TTT and CAT:

1. Convert to binary representation
    ```
    *   -> 0000
    T*T -> 100000001000
    TTT -> 100010001000
    CAT -> 001000011000
    ```
2. XOR the binary representations
    ```
    T*T  100000001000       T*T  100000001000
    TTT  100010001000       CAT  001000011000
    -----------------       -----------------
    XOR  000010000000       XOR  101000010000
    ```
3. Count the number of ones in the result 
    ```
    T*T:TTT 000010000000 -> 1
    T*T:CAT 101000010000 -> 3
    ```
   
4. Subtract the number of wildcards in the pattern
    ```
    T*T:TTT  1-1 = 0
    T*T:CAT  3-1 = 2
   
4. Divide by 2 to get number of differences between the strings
    ```
    T*T:TTT  0/2 = 0 The strings differ by no characters.
    T*T:CAT  2/2 = 1 The strings differ by one character.
    ```

## References
[Wegner]A technique for counting ones in a binary computer by Peter Wegner, CACM 3 (1960)

Faster binary hamming dist implementations in python
This stackoverflow thread has a useful discussion https://stackoverflow.com/questions/32730202/fast-hamming-distance-computation-between-binary-numpy-arrays/32731794

https://github.com/ilanschnell/bitarray in C efficient arrays of booleans as bits. 
Has a count_xor() method - sounds perfect!


An algorithm that maps the 4 DNA bases onto just 2 binary digits and then uses a somewhat similar algorithm to get the 
hamming dist is described in this paper. Uses XOR, then some binary transformations to account for differing at one or
two positions for mismatches, then counts the ones at the end (cardinality).
IJFCC 2015 Vol.4(3): 165-169 ISSN: 2010-3751
DOI: 10.7763/IJFCC.2015.V4.377
Efficient Sequence Comparison Using Binary Codes
Hossein Kamel Rahimi
http://www.ijfcc.org/show-57-684-1.html
Also https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.hamming.html worth a shot

modern microprocessors have a specific instruction (POPCNT, “population count”) for counting the number of bits set to 1.
https://en.wikipedia.org/wiki/SSE4#POPCNT_and_LZCNT

This paper uses the same DNA encoding https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2735968/
Casilli R, Marongiu A, Melchionna S, Palazzari P, Paparcone R, Rosato V. IMAGE: a new tool for the prediction of transcription factor binding sites. Bioinform Biol Insights. 2008;2:357-367. Published 2008 Oct 3.

Note to self 
CMake projects should use: "-DCMAKE_TOOLCHAIN_FILE=C:/src/win64/vcpkg/scripts/buildsystems/vcpkg.cmake"
