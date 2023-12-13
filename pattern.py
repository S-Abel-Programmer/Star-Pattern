''' Create a triange star pattern 1 star to 5 stars at the point then back to 1 star'''

# n = 5   # pre entered max star number

# for i in range(n):
#     for j in range(i+1):   # set loop to (i+1) so in first line 1 * then second line 2 stars
#         print("* ", end=" ")
#     print()

# n = 4
# for i in range(n):
#     for j in range(i,n):    # add a start condition so it stars at 4 (i,n)
#         print("* ", end=" ")
#     print()

# The above code works perfectly fine, although I have just seen it needs to be a IF / Else / FOR!!!! :-( 



row_count = 5
start = 1
end = (2 * row_count) + 1
for row_number in range(start, end):
    star_count = row_number if row_number <= row_count else end - row_number - 1   # the minus 1 at the end stumped me for ages as it was 2 5 star lines
    for i in range(star_count):
        print("* ", end=" ")
    print()
    

    
        



    




