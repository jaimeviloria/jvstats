import pytest
from jvstats import console
import os

def test_jvstats_cli(script_runner,mocker):
  ret = script_runner.run('jvstats')
  assert ret.success

def test_medians(script_runner,mocker):
  ret = script_runner.run('jvstats','delays','medians')
  assert ret.success
