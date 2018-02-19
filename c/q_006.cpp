/**
 * Note: The returned array must be malloced, assume caller calls free().
 
zigzag pattern:
n=numRows
Δ=2n-2    1                           2n-1                         4n-3
Δ=        2                     2n-2  2n                    4n-4   4n-2
Δ=        3               2n-3        2n+1              4n-5       .
Δ=        .           .               .               .            .
Δ=        .       n+2                 .           3n               .
Δ=        n-1 n+1                     3n-3    3n-1                 5n-5
Δ=2n-2    n                           3n-2                         5n-4
*/

char* convert(char* s, int numRows) {
    int n = strlen(s);
    int idx_row = 0, maxInt = 2*(numRows - 1);
    int int1, int2, index = 0;
    
    if (numRows <= 1 || n <= numRows) return s;
    char* res = (char*) malloc(n + 1);
    
    while (idx_row < numRows) {
        int idx = idx_row, count = 0;
        if (idx_row == 0 || idx_row == numRows - 1) {
            int1 = maxInt;
            int2 = maxInt;
        }
        else {
            int1 = maxInt - idx_row*2;
            int2 = maxInt - int1;
        }
        
        while (idx < n) {
            res[index] = *(s + idx);
            if (count%2 == 0) idx += int1;
            else idx += int2;

            count++;
            index++;
        }
        idx_row++;
    }
    res[index] = 0;
    return res;
}