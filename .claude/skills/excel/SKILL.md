---
name: excel
description: Work with Excel files (.xlsx, .xls). Use when reading, writing, creating, or manipulating spreadsheets. Handles data extraction, formatting, formulas, and conversions.
allowed-tools: Read, Write, Bash, Edit
argument-hint: [file.xlsx] [operation]
---

# Excel File Operations

When working with Excel files, use Python with `openpyxl` (for .xlsx) or `pandas` (for data analysis).

## Setup

First, ensure required packages are installed:
```bash
pip install openpyxl pandas xlrd
```

## Common Operations

### Reading Excel Files

```python
import pandas as pd

# Read entire file
df = pd.read_excel('file.xlsx')

# Read specific sheet
df = pd.read_excel('file.xlsx', sheet_name='Sheet1')

# Read all sheets
all_sheets = pd.read_excel('file.xlsx', sheet_name=None)
```

### Writing Excel Files

```python
import pandas as pd

# Write DataFrame to Excel
df.to_excel('output.xlsx', index=False)

# Write multiple sheets
with pd.ExcelWriter('output.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Sheet1', index=False)
    df2.to_excel(writer, sheet_name='Sheet2', index=False)
```

### Using openpyxl for More Control

```python
from openpyxl import Workbook, load_workbook

# Create new workbook
wb = Workbook()
ws = wb.active
ws['A1'] = 'Hello'
ws['B1'] = 'World'
wb.save('new_file.xlsx')

# Load existing workbook
wb = load_workbook('existing.xlsx')
ws = wb.active

# Iterate through rows
for row in ws.iter_rows(min_row=1, max_row=10, values_only=True):
    print(row)
```

### Data Manipulation

```python
import pandas as pd

df = pd.read_excel('data.xlsx')

# Filter rows
filtered = df[df['column'] > 100]

# Sort data
sorted_df = df.sort_values('column', ascending=False)

# Group and aggregate
summary = df.groupby('category').agg({'value': 'sum'})

# Add calculated columns
df['new_col'] = df['col1'] + df['col2']
```

### Converting Formats

```python
import pandas as pd

# Excel to CSV
df = pd.read_excel('input.xlsx')
df.to_csv('output.csv', index=False)

# CSV to Excel
df = pd.read_csv('input.csv')
df.to_excel('output.xlsx', index=False)

# Excel to JSON
df = pd.read_excel('input.xlsx')
df.to_json('output.json', orient='records', indent=2)
```

### Formatting with openpyxl

```python
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, Border, Side, PatternFill

wb = Workbook()
ws = wb.active

# Bold header
ws['A1'].font = Font(bold=True, size=12)

# Center alignment
ws['A1'].alignment = Alignment(horizontal='center')

# Background color
ws['A1'].fill = PatternFill(start_color='FFFF00', fill_type='solid')

# Column width
ws.column_dimensions['A'].width = 20

wb.save('formatted.xlsx')
```

## Best Practices

1. **Always close files**: Use context managers (`with` statements)
2. **Handle large files**: Use `chunksize` parameter for big datasets
3. **Validate data**: Check for missing values with `df.isnull().sum()`
4. **Backup originals**: Before modifying, create a copy of the original file
5. **Use appropriate dtypes**: Specify column types to avoid memory issues

## Error Handling

```python
import pandas as pd

try:
    df = pd.read_excel('file.xlsx')
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Cannot access file - it may be open in another program")
except Exception as e:
    print(f"Error reading file: {e}")
```
