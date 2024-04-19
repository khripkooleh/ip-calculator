# IP Address Calculator | ip-calculator
This Python project offers several tools for working with IP addresses, including format conversions and the computation of network information like broadcast addresses and network addresses, among other things.

# Features:
- **IPCals Class:** Provides several methods for manipulating IP addresses, such as creating network masks, converting between integer, dotted-decimal, and binary string formats, determing network class, and extracting network information.
- **IPHelper Class:** Provides an easy-to-use interface for getting detailed information about an IP address based on prefix length, which includes the address's class, network, broadcast, and host addresses.
- **Easy to read:** Project if fully commented, so it will be easy for new users to manage and navigate the code.

# Usage:
1. Import the '**IPCals**' and '**IPHelper**' classes into your Python project.
2. Create an instance of '**IPHelper**' and call the '**GetIPBriefInfo**' method with the IP address and prefix length as arguments to obtain detailed information about the IP address.

# Example №1: 
```python
# Importing classes into our Python project
from ip_calculator import IPCalc, IPHelper 

# Creating several variables to work with

# Define an IP address as a string
ip_address = "192.0.0.1"
# Define the prefix length
prefix_length = 24 

# Convert the string representation of the IP address to its integer form
ip_integer = IPCalc.ConvertStringToIP(ip_address)
# Get detailed information about the IP address using the IPHelper class
IPHelper.GetIPBriefInfo(ip_integer, prefix_length) 

```

# Example №2: 
```python
# Importing classes into our Python project
from ip_calculator import IPCalc, IPHelper 

# Creating a list of IP addresses as strings
rawip = ["10.0.0.1","10.0.0.2","192.168.0.0","11.22.33.240","131.122.224.230"]
# Defining a list of prefix lengths
prefix = [8, 17, 24, 10, 14] 

# Converting the list of IP addresses from strings to integers using list comprehension
ip_list = [IPCalc.ConvertStringToIP(ip) for ip in raw_ip]

# Iterating through the lists of IP addresses and prefix lengths
for i in range(len(prefix)):
# Getting detailed information about each IP address 
    IPHelper.GetIPBriefInfo(ip_list[i], prefix[i])

```

## Contributors:
- [Khripko Oleh](https://github.com/khripkooleh)

Feel free to contribute, report issues, or suggest improvements as I'm only getting into Python!
