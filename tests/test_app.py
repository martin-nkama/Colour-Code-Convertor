import pytest
import os
import sys

# Add the parent directory of 'hex_rgb' to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import (
    hex_to_rgb, rgb_to_hex, rgba_to_hex, hex_to_rgba, rgb_to_hsl,
    hsl_to_rgb, rgb_to_rgba, rgba_to_rgb, hsl_to_hex, hsl_to_rgba,
    rgba_to_hsl, hex_to_hsl
)

def test_hex_to_rgb():
    assert hex_to_rgb('#ffffff') == (255, 255, 255)
    assert hex_to_rgb('#000000') == (0, 0, 0)

def test_rgb_to_hex():
    assert rgb_to_hex(255, 255, 255) == '#ffffff'
    assert rgb_to_hex(0, 0, 0) == '#000000'

def test_rgba_to_hex():
    assert rgba_to_hex(255, 255, 255, 1) == '#ffffffff'
    assert rgba_to_hex(0, 0, 0, 0) == '#00000000'

def test_hex_to_rgba():
    assert hex_to_rgba('#ffffffff') == (255, 255, 255, 255)
    assert hex_to_rgba('#00000000') == (0, 0, 0, 0)
    assert hex_to_rgba('#ff0000') == (255, 0, 0, 255)  # Ensure it handles hex without alpha

def test_rgb_to_hsl():
    assert rgb_to_hsl(255, 0, 0) == (0, 100, 50)
    assert rgb_to_hsl(0, 255, 0) == (120, 100, 50)

def test_hsl_to_rgb():
    assert hsl_to_rgb(0, 100, 50) == (255, 0, 0)
    assert hsl_to_rgb(120, 100, 50) == (0, 255, 0)

def test_rgb_to_rgba():
    assert rgb_to_rgba(255, 0, 0) == (255, 0, 0, 255)
    assert rgb_to_rgba(0, 255, 0, 0.5) == (0, 255, 0, 128)

def test_rgba_to_rgb():
    assert rgba_to_rgb(255, 0, 0, 255) == (255, 0, 0)
    assert rgba_to_rgb(0, 255, 0, 128) == (0, 255, 0)

def test_hsl_to_hex():
    assert hsl_to_hex(0, 100, 50) == '#ff0000'
    assert hsl_to_hex(120, 100, 50) == '#00ff00'

def test_hsl_to_rgba():
    assert hsl_to_rgba(0, 100, 50, 1) == '#ff0000ff'
    assert hsl_to_rgba(120, 100, 50, 0.5) == '#00ff0080'

def test_hex_to_hsl():
    assert hex_to_hsl('#ff0000') == (0, 100, 50)
    assert hex_to_hsl('#00ff00') == (120, 100, 50)

def test_rgba_to_hsl():
    assert rgba_to_hsl(255, 0, 0, 255) == (0, 100, 50, 255)
    assert rgba_to_hsl(0, 255, 0, 128) == (120, 100, 50, 128)
