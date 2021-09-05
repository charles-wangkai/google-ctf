/* This is a first-pass (call it version 0.2) of an interpreter
 * for the evil programing language. More specifically this is
 * the base language, without the standard library.
 *
 * There should be detailed descriptions of the evil programming
 * language elsewhere. Here, I will just say that it will take
 * any text file as a valid program. All lowercase letters are
 * evil language commands. Uppercase letters are standard library
 * calls (not implemented in this version). Note that there is no
 * such thing as a syntax error in evil.
 *
 * Usage:
 *     java evil mySourceFile.evl
 *
 * ------------------------
 * version: 0.21
 * release date: 10/31/2002
 * Author: Tom Wrensch
 * ------------------------
 *
 * Release History:
 *   0.20 10/25/2002 TeW  First public version released.
 *   0.21 10/31/2002 TeW  bug fix release
 */
import java.io.IOException;
import java.io.FileInputStream;

public class evil implements Runnable {

    byte[] wheel, source, pental;
    int wheelPos, sourcePos, pentalPos;
    int wheelSize, sourceSize, pentalSize;
	byte A;
    boolean standardMark = true;
    
    static public void main(String[] args) {
        StringBuffer buf = new StringBuffer();
        if (args.length < 1) return;
        try {
            FileInputStream fin =
                new FileInputStream(args[0]);
            int b;
            do {
                b = fin.read();
                if (b > 0) 
                    buf.append((char)b);
            } while (b > 0);
        } catch (IOException e) {
        }
        buf.append("");
        evil e = new evil(buf.toString());
        e.execute();
    }
    
    public evil(String pgm) {
        pentalSize = 5;
        reset();
        source = pgm.getBytes();
        sourceSize = source.length;
    }
    
    public void execute() {
        reset();
        while (sourcePos >= 0 && sourcePos < sourceSize)
            doOne(source[sourcePos]);
    }
    
        
    public void run() {
        execute();
    }
    
    public byte[] getWheel() {
        if (wheel.length == wheelSize)
            return wheel;
        byte[] temp = wheel;
        wheel = new byte[wheelSize];
        for (int i=0; i<wheelSize; i++)
            wheel[i] = temp[i];
        return temp;
    }
    
    public byte[] getPental() {
        return pental;
    }
    
    public byte getA() {
        return A;
    }
    
    
    void reset() {
        A = 0;
        wheelPos = 0;
        wheel = new byte[100];
        wheelSize = 1;
        pental = new byte[pentalSize];
        sourcePos = 0;
        wheelPos = 0;
        pentalPos = 0;
    }
    
    
    void doOne(byte cmd) {
        byte mark = (byte) 'm';
        byte altmark = (byte) 'j';
        byte b;
        
        switch ((char) cmd) {
            
            case 'a':
                A++;
                break;
            
            case 'b': 
                jump(false);
                break;
            
            case 'c':
                wopen();
                break;
            
            case 'd':
                for (int i=wheelPos;i<wheelSize-1;i++)
                    wheel[i]=wheel[i+1];
                wheelSize--;
                if (wheelSize <= 0) {
                    wheelSize = 1;
                    wheelPos = 0;
                    wheel[wheelPos] = 0;
                }
                break;
                
            case 'e':
                A = weave(A);
                break;
            
            case 'f':
                jump(true);
                break;
            
            case 'g':
                A = pental[pentalPos];
                break;
            
            case 'h':
                pentalPos = (pentalPos + 1) % pentalSize;
                break;
            
            case 'i':
                wheelPos = (wheelPos + 1) % wheelSize;
                break;
            
            case 'j':
                break;
            
            case 'k':
                pental[pentalPos] = A;
                break;
            
            case 'l':
                b = wheel[wheelPos];
                wheel[wheelPos] = A;
                A = b;
                break;
            
            case 'm':
                break;
            
            case 'n':
                pentalPos = (pentalPos - 1);
                if (pentalPos<0) pentalPos = pentalSize-1;
                break;
            
            case 'o':
                wheelPos = (wheelPos - 1) ;
                if (wheelPos < 0) wheelPos = wheelSize - 1;
                break;
            
            case 'p':
                A = wheel[wheelPos];
                break;
            
            case 'q':
                swap();
                break;
            
            case 'r':
                A = read();
                break;
            
            case 's':
                if (A == 0) sourcePos++;
                break;
            
            case 't':
                if (A != 0) sourcePos++;
                break;
                
            case 'u':
                A--;
                break;
            
            case 'v':
                b=pental[pentalPos];
                pental[pentalPos] = A;
                A = b;
                break;
            
            case 'w':
                write(A);
                break;
            
            case 'x':
                standardMark = !standardMark;
                break;
            
            case 'y':
                wheel[wheelPos] = A;
                break;
            
            case 'z':
                A = 0;
        }
        sourcePos++;
    }
    
    void jump(boolean forward) {
        byte mark = (byte) (standardMark?'m':'j');
        if (forward) {
            while (sourcePos < sourceSize
                    && source[sourcePos] != mark)
                sourcePos++;
        }
        else {
            while (sourcePos >= 0
                    && source[sourcePos] != mark)
                sourcePos--;
        }
    }
    
    void wopen() {
        if (wheelSize >= wheel.length) {
            byte[] temp = wheel;
            wheel = new byte[temp.length + 100];
            for (int i=0; i<wheelSize; i++)
                wheel[i] = temp[i];
        }
        for (int i=wheelSize; i>wheelPos; i--)
            wheel[i] = wheel[i-1];
        wheel[wheelPos] = 0;
    }
    
    
    static int[] weaveMap = {4, 1, 16, 2, 64, 8, 128, 32};

    byte weave(byte x) {
        int mask = 1;
        int answer = 0;
        for (int i=0; i<8; i++) {
            if ((x&mask)!=0)
                answer = answer|(byte)weaveMap[i];
            mask = mask<<1;
        }
        return (byte)answer;
    }
    
    void swap() {
        byte[] temp = wheel;
        wheel = source;
        source = temp;
        int t = wheelPos;
        wheelPos = sourcePos;
        sourcePos = t;
        t = wheelSize;
        wheelSize = sourceSize;
        sourceSize = t;
    }
    
    byte read() {
        byte answer = 0;
        try {
            answer = (byte) System.in.read();
        } 
        catch (IOException e) {
        }
        return answer;
    }
    
    void write(byte b) {
        System.out.print((char)b);
    }
}

