#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

^j::
settimer, checkForCommands, 10000
return

previous_line := ""
CoordMode, Mouse, Screen

checkForCommands:
	Loop, read, Commands.txt
		last_line := A_LoopReadLine  ; When loop finishes, this will hold the last line.
		if(last_line != previous_line) {
			previous_line := last_line
			if(InStr(last_line, "_CLICK: ")) {
				clicks := SubStr(last_line, 8)
				clicks -= 1
				Loop %clicks% {
					Send, {Click 450, 1125}
					Sleep, 1500
					Send, {Click 450, 1125}
					Sleep, 3000
				}
			}
			if (InStr(last_line, "_TYPE: ")) {
				send_msg := SubStr(last_line, 7)
				Send, %send_msg%`n
			}
		}
	return