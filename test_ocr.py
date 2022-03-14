import pytest
import ocr
import asyncio


def test_ocr1():
  r = asyncio.run(ocr.read_image("./sample.png"))
  assert(bool(r))