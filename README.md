# voice-printer
voice recognition and print by thermal printer

![demo](https://user-images.githubusercontent.com/319850/81499823-2dc38b00-9309-11ea-9465-19f0f2a2a8d5.gif)

## Features
Check my [blog](https://idis.dev/blog/voice-printer/)

## Getting Started

### Prerequire

* [Julius](https://julius.osdn.jp/en_index.php) - For Voice Recognition. Use ver4.5

You can install this command
```bash
sh install.sh
```

### Set the pin where the printer is connected
[Circuit](https://easyeda.com/minmax/voice-printer)


## Uses

### Run main
```bash
python main.py
```

### make own dictation
you need dictation to increase voice recognition rate.
1. Edit mydictation/word.yomi
2. Convert to dictation 'word.dic'
```bash
sh makedict.sh
```

### test mike and speaker
```bash
python record_voice.py
```

## What to expect in next updates

- [ ] make interface curcuit boad between raspberry pi and printer.
- [ ] make case to fix position of printer
