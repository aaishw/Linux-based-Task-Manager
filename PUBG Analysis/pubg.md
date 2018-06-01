

```python
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import itertools
import matplotlib.pyplot as plt

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory


#prep
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.preprocessing import LabelEncoder, StandardScaler, MaxAbsScaler, QuantileTransformer

#models
from sklearn.linear_model import LogisticRegression, LogisticRegressionCV, LinearRegression, Ridge, RidgeCV
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

#validation libraries
from sklearn.cross_validation import KFold, StratifiedKFold
from IPython.display import display
from sklearn import metrics
%matplotlib inline

```


```python
try:
    cs_data = pd.read_csv(' C:/Users/Aaishwary V/Desktop/test dataset/pubg project/PUBG_Player_Statistics.csv', encoding='ISO-8859-1')
    print('File load: Success')
except:
    print('File load: Failed')
    cs_data.head()
```

    File load: Failed
    


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    <ipython-input-26-5be7ed5b1f29> in <module>()
          1 try:
    ----> 2     cs_data = pd.read_csv(' C:/Users/Aaishwary V/Desktop/test dataset/pubg project/PUBG_Player_Statistics.csv', encoding='ISO-8859-1')
          3     print('File load: Success')
    

    C:\programs installed\anaconda\lib\site-packages\pandas\io\parsers.py in parser_f(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, squeeze, prefix, mangle_dupe_cols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, dayfirst, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, escapechar, comment, encoding, dialect, tupleize_cols, error_bad_lines, warn_bad_lines, skipfooter, skip_footer, doublequote, delim_whitespace, as_recarray, compact_ints, use_unsigned, low_memory, buffer_lines, memory_map, float_precision)
        708 
    --> 709         return _read(filepath_or_buffer, kwds)
        710 
    

    C:\programs installed\anaconda\lib\site-packages\pandas\io\parsers.py in _read(filepath_or_buffer, kwds)
        448     # Create the parser.
    --> 449     parser = TextFileReader(filepath_or_buffer, **kwds)
        450 
    

    C:\programs installed\anaconda\lib\site-packages\pandas\io\parsers.py in __init__(self, f, engine, **kwds)
        817 
    --> 818         self._make_engine(self.engine)
        819 
    

    C:\programs installed\anaconda\lib\site-packages\pandas\io\parsers.py in _make_engine(self, engine)
       1048         if engine == 'c':
    -> 1049             self._engine = CParserWrapper(self.f, **self.options)
       1050         else:
    

    C:\programs installed\anaconda\lib\site-packages\pandas\io\parsers.py in __init__(self, src, **kwds)
       1694 
    -> 1695         self._reader = parsers.TextReader(src, **kwds)
       1696 
    

    pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader.__cinit__()
    

    pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader._setup_parser_source()
    

    FileNotFoundError: File b' C:/Users/Aaishwary V/Desktop/test dataset/pubg project/PUBG_Player_Statistics.csv' does not exist

    
    During handling of the above exception, another exception occurred:
    

    NameError                                 Traceback (most recent call last)

    <ipython-input-26-5be7ed5b1f29> in <module>()
          4 except:
          5     print('File load: Failed')
    ----> 6     cs_data.head()
    

    NameError: name 'cs_data' is not defined



```python
cs_data[cs_data['solo_Wins'].isnull()].head(10)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-19-b27c7722b572> in <module>()
    ----> 1 cs_data[cs_data['solo_Wins'].isnull()].head(10)
    

    NameError: name 'cs_data' is not defined



```python
cs_data['total_Kills'] = cs_data['solo_Kills'] + cs_data['duo_Kills'] + cs_data['squad_Kills']
cs_data[['total_Kills', 'solo_Kills', 'duo_Kills', 'squad_Kills']].head()

```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-27-f6599824af6c> in <module>()
    ----> 1 cs_data['total_Kills'] = cs_data['solo_Kills'] + cs_data['duo_Kills'] + cs_data['squad_Kills']
          2 cs_data[['total_Kills', 'solo_Kills', 'duo_Kills', 'squad_Kills']].head()
    

    NameError: name 'cs_data' is not defined



```python
import pylab 
what=plt.scatter(
    cs_data['total_Revives'],
    cs_data['total_Kills'],
    c='b',
    marker='x') # Color = blue?
plt.xlabel("Total Revives")
plt.ylabel("Total Kills")

pubg_angels = cs_data[(cs_data['ratio_ReviveKill']>1)]
pubg_angels[['player_name','ratio_ReviveKill','total_Revives','total_Kills']]
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-28-d036712312ab> in <module>()
          1 import pylab # Not sure if I can use another library
          2 what=plt.scatter(
    ----> 3     cs_data['total_Revives'],
          4     cs_data['total_Kills'],
          5     c='b',
    

    NameError: name 'cs_data' is not defined



```python
import seaborn as sns
plt.figure(figsize=(16,8))
sns.set_style("whitegrid")
plt.title('Grouping players by Total Kills', fontsize=20, fontweight='bold', y=1.05,)
plt.xlabel('Number of players', fontsize=15)
plt.ylabel('Player Kills', fontsize=15)
sns.countplot(x="total_Kills", data=cs_data, palette(8, l=.3, s=.8));
plt.show()
```
