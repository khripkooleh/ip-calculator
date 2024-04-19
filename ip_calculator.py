class IPCalc:
    """
    Class that calculates all needed information about an IP address.

    """

    # ---------- Class level constants for IP address class masks ---------- #
    classBMask = 0b1000 << 28
    classCMask = 0b1100 << 28
    classDMask = 0b1110 << 28
    classEMask = 0b1111 << 28
    # ---------------------------------------------------------------------- #

    @staticmethod
    def CreateMaskFromPrefix(prefix: int) -> int:
        """
        Create a network mask from a given prefix length.

        :param prefix: The prefix length (1-32)
        :return: The network mask as an integer
    
        """
        NetMask = 0

        for i in range(1, prefix + 1):
            NetMask <<= 1
            NetMask += 1

        NetMask <<= 32 - prefix
        return NetMask
    
    @staticmethod
    def ConverIPToDecString(ip: int) -> str:
        """
        Convert an IP address from integer format to dotted-decimal string format.

        :param ip: The IP address as an integer
        :return: The IP address as a string
    
        """
        a = []

        for i in range(4):
            a.insert(0, str(ip % 256))
            ip //= 256
        
        return ".".join(a)
    
    @staticmethod
    def ConvertIPToBinString(ip: int) -> str:
        """
        Convert an IP address from integer format to binary string format.

        :param ip: The IP address as an integer
        :return: The IP address as a binary string

        """
        res = ""
        key = 1 << 31
        for i in range(1, 33):
            val = key & ip
            res += "1" if val != 0 else "0"
            ip <<= 1
            if i % 8 == 0 and i != 32:
                res += "."

        return res
    
    @staticmethod
    def ConvertStringToIP(ipString: str) -> int:
        """
        Convert an IP address from dotted-decimal string format to integer format.

        :param ipString: The IP address as a dotted-decimal string
        :return: The IP address as an integer
        """
        ResolvedIP = 0
        Dlist = ipString.split('.')
        for i in range(4):
            ResolvedIP += int(Dlist[i]) << (8 * (3 - i))
        
        return ResolvedIP
    
    @staticmethod
    def GetNetworkAddressFromIP(ip: int, netmask: int) -> int:
        """
        Get the network address from an IP address and a network mask.

        :param ip: The IP address as an integer
        :param netmask: The network mask as an integer
        :return: The network address as an integer
        """
        return ip & netmask
    
    @staticmethod
    def GetFirstHostAddress(networkIP: int) -> int:
        """
        Get the first host address in a network.

        :param networkIP: The network address as an integer
        :return: The first host address as an integer
        """
        return networkIP+1
    
    @staticmethod
    def GetBroadcastAddress(networkIP: int, netmask: int) -> int:
        """
        Get the broadcast address for a network.

        :param networkIP: The network address as an integer
        :param netmask: The network mask as an integer
        :return: The broadcast address as an integer
        """
        return (networkIP & netmask) | (~netmask)
    
    @staticmethod
    def GetLastHostAddress(networkIP: int, netMask: int) -> int:
        """
        Get the last host address in a network.

        :param networkIP: The network address as an integer
        :param netMask: The network mask as an integer
        :return: The last host address as an integer
        """
        return (networkIP & netMask) | ((~netMask)-1)
    
    @staticmethod
    def GetNetworkClass(ip: int) -> str:
        """
        Get the network class of an IP address.

        :param ip: The IP address as an integer
        :return: The network class as a string ('A', 'B', 'C', 'D', or 'E')
        """
        if (ip & IPCalc.classEMask) == IPCalc.classEMask:
            return "E"
        if (ip & IPCalc.classDMask) == IPCalc.classDMask:
            return "D"
        if (ip & IPCalc.classCMask) == IPCalc.classCMask:
            return "C"
        if (ip & IPCalc.classBMask) == IPCalc.classBMask:
            return "B"
        return "A"

class IPHelper:

    """

    Class that prints out all information about an IP address after calculations.

    """

    @staticmethod
    def GetIPBriefInfo(ip: int, prefix: int):
        print("====================< IP >==================")
        print(f"str IP: {IPCalc.ConverIPToDecString(ip)}")
        print(f"bin IP: {IPCalc.ConvertIPToBinString(ip)}")
        print(f"int IP: {ip}")
        print(f"Detected class: {IPCalc.GetNetworkClass(ip)}")
        print(f"Resolved IP: {IPCalc.ConverIPToDecString(ip)}")
        net_mask = IPCalc.CreateMaskFromPrefix(prefix)
        print(f"Network Mask: {IPCalc.ConverIPToDecString(net_mask)}")
        net_ip = IPCalc.GetNetworkAddressFromIP(ip, net_mask)
        print(f"Network IP: {IPCalc.ConverIPToDecString(net_ip)}")
        print(f"Broadcast IP: {IPCalc.ConverIPToDecString(IPCalc.GetBroadcastAddress(net_ip, net_mask))}")
        print(f"First Host IP: {IPCalc.ConverIPToDecString(IPCalc.GetFirstHostAddress(net_ip))}")
        print(f"Last Host IP: {IPCalc.ConverIPToDecString(IPCalc.GetLastHostAddress(net_ip, net_mask))}")

if __name__ == "__main__":
    
    rawip = ["10.0.0.1","10.0.0.2","192.168.0.0","11.22.33.240","131.122.224.230"]
    prefix = [8, 17, 24, 10, 14]
    ipList = [IPCalc.ConvertStringToIP(ip) for ip in rawip]

    for i in range(len(prefix)):
        IPHelper.GetIPBriefInfo(ipList[i], prefix[i])