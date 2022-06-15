# recipes
Provide some packages's recipe for android development with python-for-android

## portaudio
portaudio used by pyaudio, libpthread library miss.
## pyaudio
fix bug

## ujson
fix bug
## BugFix
### crypt.h not found
add following in your Recipe class
```
	call_hostpython_via_targetpython = False
```
