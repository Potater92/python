import pytest
from television import Television

def test_initialization():
    tv = Television()
    assert str(tv) == "Power = Off, Channel = [0], Volume = [0], Muted = No"

def test_power():
    tv = Television()
    tv.power()
    assert str(tv) == "Power = On, Channel = [0], Volume = [0], Muted = No"
    tv.power()
    assert str(tv) == "Power = Off, Channel = [0], Volume = [0], Muted = No"

def test_mute():
    tv = Television()
    tv.power()
    assert not tv.is_muted(), "The TV should initially not be muted."
    tv.mute()
    assert tv.is_muted(), "The TV should be muted after calling mute()."
    tv.mute()
    assert not tv.is_muted(), "The TV should not be muted after calling mute() again."

def test_channel_up():
    tv = Television()
    tv.power()
    tv.channel_up()
    assert str(tv) == "Power = On, Channel = [1], Volume = [0], Muted = No"
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()  # Should wrap around to MIN_CHANNEL
    assert str(tv) == "Power = On, Channel = [0], Volume = [0], Muted = No"

def test_channel_down():
    tv = Television()
    tv.power()
    tv.channel_down()  # Should wrap around to MAX_CHANNEL
    assert str(tv) == "Power = On, Channel = [3], Volume = [0], Muted = No"

def test_volume_up():
    tv = Television()
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = On, Channel = [0], Volume = [1], Muted = No"
    tv.volume_up()
    assert str(tv) == "Power = On, Channel = [0], Volume = [2], Muted = No"

def test_volume_down():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_down()
    assert str(tv) == "Power = On, Channel = [0], Volume = [0], Muted = No"
