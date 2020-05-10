# voice-printer
voice recognition and print by thermal printer

## Features
Check this blog
https://idis.dev/blog/voice-printer/


## Getting Started

### Prerequire

I use Open Source Library
* [Julius](https://julius.osdn.jp/en_index.php) - Voice Recognition

### Set the pin where the printer is connected
[Circuit] https://easyeda.com/minmax/voice-printer


#### Include the library in the sketch
Install 

```c++
int pin = 2;
void setup() {
  EasyBuzzer.setPin(pin);
};  

## Uses

### Regular Beep

## What to expect in next updates

- [ ] Support for multiple instances of `EasyBuzzer` Class, making possible to have more than one Buzzer.
- [ ] Shortcut functions to predefined sounds like; success, error and warning.


