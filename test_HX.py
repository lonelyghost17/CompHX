#!/usr/bin/env python3

#import numpy as np
import pytest
from . import HX_analyze as hx

def test_lmtd_counter():
    assert hx.log_mean_temp_diff_counter(100,85,30,55) == pytest.approx(49.83,.005)

def test_lmtd_counter2():
    with pytest.raises(ValueError):
        hx.log_mean_temp_diff_counter(10,10,10,10)

def test_lmtd_counter3():
    with pytest.raises(ValueError):
        hx.log_mean_temp_diff_counter(10,100,10,100)
        
def test_lmtd_counter4():
    with pytest.raises(ValueError):
        hx.log_mean_temp_diff_counter(10,100,100,10)
            
def test_lmtd_parallel():
    assert hx.log_mean_temp_diff_parallel(100,85,30,55) == pytest.approx(47.21,.005)

def test_lmtd_parallel2():
    with pytest.raises(ValueError):
        hx.log_mean_temp_diff_parallel(10,10,10,10)
        
def test_lmtd_parallel3():
    with pytest.raises(ValueError):
        hx.log_mean_temp_diff_parallel(10,100,100,10)
        
def test_lmtd_parallel4():
    with pytest.raises(ValueError):
        hx.log_mean_temp_diff_parallel(100,10,100,10)

def test_q_lmtd_counter():
    assert hx.q_lmtd_counter(1,1,100,85,30,55) == pytest.approx(49.83,.005)
    
def test_q_lmtd_counter2():
    with pytest.raises(ValueError):
        hx.q_lmtd_counter(-11,1,100,-85,30,-55)
    
def test_q_lmtd_parallel():
    assert hx.q_lmtd_parallel(1,1,100,85,30,55) == pytest.approx(47.21,.005)
    
def test_q_lmtd_parralel2():
    with pytest.raises(ValueError):
        hx.q_lmtd_parallel(-11,1,100,-85,30,-55)

def test_c_min_cold():
    assert hx.c_min(10,10,1,1) == 1
    
def test_c_min_hot():
    assert hx.c_min(1,1,10,10) == 1
    
def test_c_min_equal():
    assert hx.c_min(2,2,2,2) == 4
    
def test_c_min_zero():
    with pytest.raises(ValueError):
        hx.c_min(0,1,0,2)