---
title: "Visualization Pandas"
author: "Juan Carlos Rubio Polania"
date: "2024-05-06"
---

# Data Visualization with Pandas and Matplotlib 📊🐍📈

## Overview

This workflow demonstrates how to create multiple types of scientific visualizations in Python using `pandas` and `matplotlib`.

The script includes:
- Creation of abundance datasets
- Data sorting
- Bar plots
- Horizontal bar plots
- Histograms
- Boxplots
- Area plots
- Kernel density estimation (KDE)
- Pie charts
- Figure customization

Although this example uses abundance values from marine genera, the workflow can be adapted to many applications involving:
- Ecology
- Biodiversity studies
- Environmental analyses
- Species abundance
- Community structure
- Exploratory data analysis
- Statistical visualization

The workflow also demonstrates how to customize figures using:
- Font styles
- Font sizes
- Axis labels
- Rotations
- Publication-style formatting

---

# Required Packages

```python
import pandas as pd
import matplotlib.pyplot as plt
```

---

# Workflow

## 1. Import Libraries

```python
import pandas as pd
import matplotlib.pyplot as plt
```

The script imports libraries for:
- Data manipulation
- Statistical graphics
- Scientific visualization

---

## 2. Create Abundance Datasets

```python
G1 = pd.Series(...)
G2 = pd.Series(...)
```

Two abundance datasets are created using pandas Series objects.

Each Series contains:
- Abundance values
- Taxonomic names as labels

---

## 3. Sort Data

```python
G1 = G1.sort_values(ascending=False)
```

The abundance values are sorted in descending order.

---

## 4. Generate Multiple Plot Types

The workflow demonstrates several plot types available in pandas and matplotlib.

### Vertical Bar Plot

```python
G2.plot(kind='bar')
```

### Horizontal Bar Plot

```python
G2.plot(kind='barh')
```

### Histogram

```python
G2.plot(kind='hist')
```

### Boxplot

```python
G2.plot(kind='box')
```

### Area Plot

```python
G2.plot(kind='area')
```

### Kernel Density Estimation (KDE)

```python
G2.plot(kind='kde')
```

### Pie Chart

```python
G2.plot(kind='pie')
```

---

## 5. Customized Scientific Figure

```python
G3.plot(kind='bar', color='firebrick')
```

The workflow demonstrates figure customization including:
- Figure titles
- Font sizes
- Font styles
- Italic labels
- Axis formatting
- Tick rotation

Times New Roman is used for publication-style formatting.

---

## 6. Customized Pie Chart

```python
fig, ax = plt.subplots()
```

The pie chart includes:
- Percentage labels
- Italicized taxa names
- Custom font sizes
- Improved readability

---

# Applications

This workflow can be useful for:
- Marine sciences
- Ecology
- Environmental sciences
- Biodiversity studies
- Species abundance analyses
- Scientific figure preparation
- Educational purposes
- Exploratory data analysis

---

# Requirements

- Python 3.x
- pandas
- matplotlib

Install packages with:

```bash
pip install pandas matplotlib
```

---

# License

This project is licensed under the MIT License.

---

# Author

Juan Carlos Rubio Polania, PhD
