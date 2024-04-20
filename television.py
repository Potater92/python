class Television:
    """A simple model of a television, which can control volume, channel, and power state, and can be muted."""

    MIN_VOLUME: int = 0  # Minimum volume level
    MAX_VOLUME: int = 2  # Maximum volume level
    MIN_CHANNEL: int = 0  # Minimum channel number
    MAX_CHANNEL: int = 3  # Maximum channel number

    def __init__(self) -> None:
        """Initializes the television with power off, not muted, minimum volume, and set to the minimum channel."""
        self.__status: bool = False  # TV initially off
        self.__muted: bool = False   # TV initially not muted
        self.__volume: int = Television.MIN_VOLUME  # Start at min volume
        self.__channel: int = Television.MIN_CHANNEL  # Start at min channel

    def power(self) -> None:
        """Toggles the power state of the television."""
        self.__status = not self.__status

    def mute(self) -> None:
        """Toggles the mute status of the television. Can only mute if the TV is on."""
        if self.__status:  # Muting is only possible when the TV is on
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """Increases the channel number. Wraps around to the minimum channel if currently at the maximum channel."""
        if self.__status:  # Can only change channel if the TV is on
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """Decreases the channel number. Wraps around to the maximum channel if currently at the minimum channel."""
        if self.__status:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """Increases the volume by one level, up to the maximum volume. Does not affect volume when muted."""
        if self.__status and not self.__muted:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """Decreases the volume by one level, down to the minimum volume. Unmutes the TV if muted."""
        if self.__status and not self.__muted:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def is_muted(self) -> bool:
        """Returns True if the television is currently muted, otherwise False."""
        return self.__muted

    def __str__(self) -> str:
        """Returns a string representation of the television's current status, including power, channel, volume, and mute status."""
        return (f"Power = {'On' if self.__status else 'Off'}, "
                f"Channel = [{self.__channel}], "
                f"Volume = [{self.__volume}], "
                f"Muted = {'Yes' if self.__muted else 'No'}")
