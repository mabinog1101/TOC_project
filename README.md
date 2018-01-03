# TOC Project 2017

A telegram bot based on a finite state machine

## Setup

### Prerequisite
* Python 3

#### Run the sever

```sh
python3 app.py
```

## Finite State Machine
![fsm](https://i.imgur.com/GrnQCQD.png)

## Usage
The initial state is set to `user`.

`user` state可以用指定的指令觸發到指定的三個state，並且回傳訊息後回到`user` state

* user
	* Input: "早安"
		* Reply: "快遲到了 還不去上課"

	* Input: "午安"
		* Reply: "肚子餓了 快幫我買東西吃"
	* Input: "晚安"
		* Reply: "那麼早就睡 你是豬嗎"
	* Else Input
		*Reply:"fk u <3"


