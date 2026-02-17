class Solution(object):
    def readBinaryWatch(self, turnedOn):
        result = []
        
        # hours: 0–11, minutes: 0–59
        for h in range(12):
            for m in range(60):
                # count number of ON LEDs (1 bits)
                if (bin(h).count('1') + bin(m).count('1')) == turnedOn:
                    # hour no leading zero, minute 2 digits
                      result.append("{}:{:02d}".format(h, m))

        
        
        return result

        