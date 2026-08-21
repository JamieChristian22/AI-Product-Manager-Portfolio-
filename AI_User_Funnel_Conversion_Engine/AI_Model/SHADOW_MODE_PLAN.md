# Shadow Mode Plan

## Purpose
Validate scoring behavior before model outputs influence users.

## Duration
7 days minimum.

## Traffic
100% eligible users scored in shadow mode.
0% decisions served from model.

## Compare
- score distributions
- latency
- feature missingness
- calibration
- segment performance
- expected intervention volume
- frequency-cap impact
- fallback behavior

## Exit Criteria
- no consent violations
- p95 latency <200 ms
- missing key features <2%
- no cohort quality gap >10pp
- model metrics above warning thresholds
