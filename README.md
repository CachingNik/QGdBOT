# Quaratined Gamers Discord Bot

## Command Prefix
Use '>' before text to interact with the bot.

Example:\
`>Yo`\
`>Hi`\
`>Bye`

## Memes
The Bot can display memes on different topics using simple command.\
`>meme (Topic name)`

Screenshot:\
![image1](Screenshots/s1.jpg "1")

## Animated Emojis
The Bot replies with animated emojis when the user message contains some specific words.

Example:\
`Lol`
`sed`

Screenshot:\
![image2](Screenshots/s2.jpg "2")

## Audio Playback
The Bot plays the audio of any Youtube video url provided to it.

In order to make the bot play an audio, the bot needs to join a voice channel involving the user who invokes it using `>join` command.

To play an audio, `>play` command must be typed in the discord server followed by the `url` of the Youtube video whose audio you want to listen.\
Example:
`>play http://www.youtube.com/watch?v={video.id}` 

Other Commands in this category:\
`>leave`\
`>pause`\
`>resume`\
`>stop`

*PS: Currently not supported in phones (on speakers).*

Screenshots:\
![image3](Screenshots/s3.jpg "3")

![image4](Screenshots/s4.jpg "4")

![image5](Screenshots/s5.jpg "5")

## Filter Words

The bot has various reactions for some words. each word falls into a category for which
the bot has same reaction/output. These words can now be
managed by the users using few commands.

This is done using Mongodb Database System. Storing all the the different words in
a collection. 

Commands:
1. To add word to a category: `>add [category] [word]`
2. To remove word from a category: `>rem [category] [word]`
3. To view the list of Filtered words: `>filist`

*PS: Only one word can be added or removed at a time. Currently there are predefined categories and each category has a 
certain word limit.*

Categories: `LAUGH` `BAD` `OK`

Screenshots:\
![image6](Screenshots/s6.jpg "6")
