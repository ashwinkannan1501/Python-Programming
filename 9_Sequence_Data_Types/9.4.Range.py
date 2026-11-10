"""
Range : 
A range is a type which is mostly used in for loops 
A range represents an immutable arithmetic progression of integers 
It consume O(1) space complexity - because it computes teh values on-demand and consumes constant memory space
It stores , only 'start' , 'stop' & 'step' values

Syntax & Declaration : 
-----------------------
range(stop)
range(start, stop[, step])

where start -> Defaults to 0 if ommitted
stop -> Exclusive boundary : the generated values do not reach it's limits 
step -> Difference between each consecutive integer. Can be negative for descending sequence. Defualts to 1 if omitted
"""
ranges = range(10,500,50)
print(f'Ranges Value : {ranges} , Type : {type(ranges)}')
for count in ranges: # Counting in for loop
    print(count)
# Fast O(1) membership checks via arithmetic formulas
print(35 in ranges)
print(460 in ranges)
# Direct indexing and slicing
print(ranges[8])
print(ranges[-8])
# Slicing a range produces another range
print(ranges[3:6]) # range(160, 310, 50)
print(list(ranges[3:6])) # [160, 210, 260]

# Attributes
print(f'Starting Position : {ranges.start}')
print(f'Stopping Position : {ranges.stop}')
print(f'Stepping Position : {ranges.step}')