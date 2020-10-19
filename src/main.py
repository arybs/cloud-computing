import pyspark

sc = pyspark.SparkContext('local[*]')

txt = sc.textFile('file:////usr/share/doc/python3.8/copyright')
print(txt.count())

python_lines = txt.filter(lambda line: 'python' in line.lower())
print(python_lines.count())