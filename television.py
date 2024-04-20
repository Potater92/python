class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False  # TV initially off
        self.__muted = False   # TV initially not muted
        self.__volume = Television.MIN_VOLUME  # Start at min volume
        self.__channel = Television.MIN_CHANNEL  # Start at min channel

    def power(self):
        self.__status = not self.__status

    def mute(self):
        if self.__status:  # Can only mute if the TV is on
            self.__muted = not self.__muted

    def channel_up(self):
        if self.__status:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        if self.__status:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        if self.__status and not self.__muted:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        if self.__status and not self.__muted:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def is_muted(self):
        return self.__muted

    def __str__(self):
        return f"Power = {'On' if self.__status else 'Off'}, Channel = [{self.__channel}], Volume = [{self.__volume}], Muted = {'Yes' if self.__muted else 'No'}"
