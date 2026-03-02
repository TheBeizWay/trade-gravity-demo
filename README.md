# Trade gravity – Python demo

This repo shows, in a very simple way, how a gravity-style view of trade looks using synthetic data. 

## Policy question

How do partner size and distance relate to Australia’s trade flows with key partners, and how could this framework be used to explore tariff or trade cost scenarios?

## Data

- synthetic dataset of Australia’s exports to  China, USA, Japan, India, Indonesia
- All data is made up and for demonstration only 

## Method 

- Load the toy trade data in Python using `pandas`.
- Summarise trade flows by partner.
- Calculate simple correlations between partner GDP and trade, and between distance and trade

## What this explains

- The core gravity intuition: larger economies tend to have higher trade, and distance works against trade.
- How simple, transparent Python code can be used to structure trade data and explore relationships before moving to richer models.


## Caveats

- Highly simplified and based on synthetic data.
- Not a full gravity model or policy estimate – the purpose is to demonstrate structure and thinking.

## How to run

- Run "gravity_demo.py" in a Python environment with `pandas` installed.
- It will load "tradedemo.csv", print the data, summarise simple correlations with GDP and distance.

