# AllowListShell

A very little shell to only allow specific commands, defined in the config.ini


example config.ini:
```ini
[global]
command_timeout=60
[commands]
shutdown=shutdown -h now
shutdownkde=qdbus org.kde.ksmserver /KSMServer logout 1 2 0
shutdowngnome=gnome-session-quit --power-off --no-prompt
notify=notify-send
ls=ls
```
