
## Get flash video traffic with wireshark

Show you the request for the flash file. If the flash app traffic is available to Wireshark, it should capture it. 
Sometimes it is just a matter of finding it on the trace file. Add this to the filter:
[Source](http://ask.wireshark.org/questions/8650/capturing-http-requests-of-a-flash-application)

```
frame contains ".swf"
```