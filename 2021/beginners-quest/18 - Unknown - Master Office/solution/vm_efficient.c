#include <stdio.h>
#include <stdint.h>

uint8_t input_data[] = 
{
    66, 82, 66, 117, 75, 91, 86, 87, 31, 51, 222, 187, 112, 236, 9, 98, 34, 69, 0, 198, 150, 29,
    96, 10, 69, 26, 253, 225, 164, 8, 110, 67, 102, 108, 103, 162, 209, 1, 173, 130, 186, 5, 123,
    109, 187, 215, 86, 232, 23, 215, 184, 79, 171, 232, 128, 67, 138, 153, 251, 92, 4, 94, 93,
};


uint64_t Strlen() 
{
    return sizeof(input_data);
}

uint64_t charAt(uint64_t dummy, uint64_t index)
{
    return input_data[index];
}

void Print(uint64_t c)
{
    printf("%c", c);
}

long fibonacci(long n)
{
    int  i;
    long a;
    long b;
    long c;
    
    if (n < 2)
    {
        return 1;
    }
    
    a = 1;
    b = 1;
    for (i = 2; i < n; i++)
    {
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}

long mod(long n)
{
    return n % 0x100;
}

void decode(long index)
{
    long lVar1;
    long lVar2;
    long length;
    
    length = Strlen();
    while (index < length) 
    {
        lVar1 = charAt(0, index);
        lVar2 = fibonacci(index + 1);
        lVar1 = mod(lVar1 + index + lVar2);
        Print(lVar1);
        index += 1;
    }
}

void run_vm(void)
{
    decode(0);
    return;
}

int main(int argc, char* argv[])
{
    setbuf(stdout, NULL);
    run_vm();
    return 0;
}